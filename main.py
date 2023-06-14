import sys
import os
# IMPORT GUI FILE
from UI.ui_mainInterface import *


# IMPORT Custom widgets
from Custom_Widgets.Widgets import *

from login import LoginWorker
from acceuil import AcceuilWidget
from post import PostEditWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QMovie, QWheelEvent
from PIL import Image
import keyring
from passlib.context import CryptContext
from passlib.hash import bcrypt
from VideoPlayer import VideoWidget
from client import APIClient
from acceuil import AcceuilWidget
from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QToolTip
from notification import TrayNotification
import time
import secrets



os.environ["QT_SCALE_FACTOR"] = "1"
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    
    SERVICE_NAME = "ikarma"
    USERNAME = "access-token"
    
    
    #####################################################################
    ## New User
    #####################################################################
    def add_user(self):
        # Get the data from the input fields
        first_name = self.ui.lineEdit_Fname.text()
        last_name = self.ui.lineEdit_Lname.text()
        email = self.ui.lineEdit_Email.text()
        password = self.ui.lineEdit_pass.text()

        print(email)
        
        # Create the data payload
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
        }
        
        # Send the POST requestsuest and get the response
        response = self.client.add_user(data)
        # Notifiate response message 
        self.notif.show_tray_message("check-circle-green.svg", "Account Created 🎉", f"Welcome {email}")
      
        self.client.login(data['email'], data['password'])
        # Redirect to Edit Profil Page 
        self.set_edit_profil()
        self.ui.CancelBtn.setVisible(False)
        self.ui.emailQline.setEnabled(False)
     
    #####################################################################
    ## Login User Worker signals n slots
    #####################################################################
    def login(self, username=None, password=None):
        
       
        
        username = self.ui.usernameLine.text()
        password = self.ui.passwordLine.text()
        if not username:
            self.notif.show_tray_message("alert-circle.svg", "Username Or Email !")
        elif  not password:
            self.notif.show_tray_message("alert-circle.svg", "Password Missing ..")
        if username and password: 
            self.worker = LoginWorker(username, password)
            # self.worker.progress_updated.connect(self.ui.loadingBar.setValue)
            self.worker.login_successful.connect(self.on_login_successful)
            self.worker.login_failed.connect(self.on_login_failed)
            
            
            self.worker.run()
     
    def on_login_successful(self):
        self.set_profilHeader()
        self.set_posts()
        self.ui.mainPages.setCurrentWidget(self.ui.profilPage)
        # self.ui.label_notification.setPixmap(QPixmap(u":/icons/icons/feather/check-circle-green.svg"))
        # self.ui.notificationText.setText(f' Welcome {self.worker.username}')
        # self.ui.notification.expandMenu()
        self.notif.show_tray_message("check-circle-green.svg", "Login Successfully", f"Welcome back {self.worker.username}")

    def on_login_failed(self, message):
        self.notif.show_tray_message("x-circle-red.svg",message)

    def on_progress_updated(self, value):
        time.sleep(0.01)
        self.ui.loadingBar.setValue(value)
    
    # Delete User
    #######################################################################
    def delete_user(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setText("Are you sure you want to delete your account ?")
        # msg_box.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        msg_box.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        msg_box.setIconPixmap(QIcon(u":/icons/icons/feather/alert-triangle.svg").pixmap(40, 40))
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg_box.setStyleSheet("QMessageBox { background-color: #2C2828; }"
                            "QMessageBox QLabel { color: white; }"
                            "QMessageBox QPushButton { background-color: #555; color: #000; }")
        response = msg_box.exec_()
        if response == QtWidgets.QMessageBox.Yes:
            self.client.delete_user()
            self.notif.show_tray_message("info.svg", "See You Soon .. 👋👋")
            self.logout()
    
    
    ############################################################   
    ## Set the Edit Profile Fields Page with Current User Data
    ############################################################
    
    def set_edit_profil(self):
    
        user_data = self.client.get_current_user()
        print(user_data)
        avatar = self.client.get_user_avatar(user_data['id'])

    
        pixmap = QPixmap()
        pixmap.loadFromData(self.client.get_user_avatar(user_data['id']))
        print("PIXMAP HEREEEEEEE",pixmap)
        self.ui.avatarLabel.setPixmap(pixmap)
            
            
                
        ## Set Form Fields
        if user_data['gender'] == 'male':
            self.ui.maleBox.setChecked(True)
        else:
            self.ui.femaleBox.setChecked(True)
        self.ui.CancelBtn.setVisible(True)
        self.ui.emailQline.setText(user_data['email'])
        self.ui.firstnameQline.setText(user_data['first_name']if user_data['first_name'] else "First Name")
        self.ui.lastnameQline.setText(user_data['last_name']if user_data['last_name'] else "Last Name")
        self.ui.biotextEdit.setText(user_data['bio']if user_data['country'] else "Bio...")
        self.ui.usernameQline.setText(user_data['username'] if user_data['username'] else "Username")
        self.ui.countryQline.setText(user_data['country'] if user_data['country'] else "Country")
        self.ui.stateQline.setText(user_data['state'] if user_data['state'] else "State")
        self.ui.phoneQline.setText(str(user_data['phone']) if user_data['phone'] else "Phone")
    
        
        
        self.ui.mainPages.setCurrentWidget(self.ui.profilEditPage)
        self.ui.profilEdit.collapseMenu()
     
    ##################################################################
    ## Patch user data
    ##################################################################    
    def edit_profil(self):
        
        data ={
            "gender": "male" if self.ui.maleBox.isChecked() else "female",
            "first_name": self.ui.firstnameQline.text(),
            "last_name": self.ui.lastnameQline.text(),
            "bio": self.ui.biotextEdit.toPlainText(),
            "username": self.ui.usernameQline.text(),
            "country": self.ui.countryQline.text(),
            "state": self.ui.stateQline.text(),
            "phone": self.ui.phoneQline.text(),
        }
        # print('hereeeee:',data)
        self.client.patch_user_data(data)
        print('**********************************')
        

        # Notification response message
        self.set_profilHeader()
        self.notif.show_tray_message("check-circle-green.svg", "Info", "Saved Successflly")
        self.ui.emailQline.setEnabled(True)
        self.ui.mainPages.setCurrentWidget(self.ui.profilPage)
        
    
    ###########################################
    ## Edit Avatar
    ###########################################
    def upload_avatar(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Avatar", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_path:
            files = {"avatar": open(file_path, "rb")}
            pixmap = QPixmap()
            
            data = self.client.update_avatar(files)
        
            
            if data:
             
                pixmap.loadFromData(data)
                self.ui.avatarLabel.setPixmap(pixmap)
                self.notif.show_tray_message("check-circle-green.svg", "Info", "Avatar uploaded successfully")
                self.set_profilHeader()

            else:
                self.notif.show_tray_message("x-circle-red.svg", "Error", "Error ! Try Again ..")
           
    

    
    ####### Base Settings ########
       
    ## Set Profil Header
    #####################################################################
    def set_profilHeader(self):
     
        
        user_data = self.client.get_current_user()

        print("###########################")
        
        avatar = self.client.get_user_avatar(user_data['id'])
            
            
        pixmap = QPixmap()
        pixmap.loadFromData(avatar)
        pix = pixmap
        
        
        self.ui.profilPixLabel.setPixmap(pix)
        self.ui.profileBtn.setIcon(QIcon(pix))
        self.ui.profileBtn.setStyleSheet(u"border: 1px solid  rgb(254, 44, 85);""border-radius: 14px;")
        self.ui.label_74.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">{user_data['username']}</span>\n"
                                                                f"<span style=\" font-weight:600;\"/><img src=\":/images/images/app/twitter-verified-png-original.png\" width=\"20\"/><br/>\n"
                                                                f"<span style=\" font-size:12pt;\">{ user_data['first_name'] } {user_data['last_name']}</span></p></body></html>", None))
        self.ui.bioLabel.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:10pt;\">{user_data['bio']}</span></p></body></html>", None)) 
        
        print("####################################################")
       
    
    ## Set Profil Posts
    #####################################################################
    
    def set_posts(self):
        for i in reversed(range(self.ui.gridLayout_4.count())): 
            widget = self.ui.gridLayout_4.itemAt(i).widget()
            self.ui.gridLayout_4.removeWidget(widget)
            widget.deleteLater()
            
        user_data = self.client.get_current_user()
        post_title = []
        # self.GLayout = QGridLayout()
        for post in user_data['posts']:
            post_title.append(post['title'])
            print('#####TITLE HERE :',post_title)
           

        
        for i, title in enumerate(post_title):
            video_path = f'videos/{title}.mp4'
            print(title)
            print(video_path)
    
            self.video_player = VideoWidget(video_path, title, 212, 380)
            self.ui.gridLayout_4.addWidget(self.video_player, i//2, i%2)
        self.ui.tab_3.setLayout(self.ui.gridLayout_4)
         
            # self.ui.gridLayout_4.setRowStretch(0, 4)
            # # self.GLayout.setColumnStretch(0, 4)      
            # self.ui.gridLayout_4.setContentsMargins(9, 9, 9, 9)     
            # self.ui.gridLayout_4.setSpacing(6)    
        
    
    ## Set Acceuil Section
    ############################################################################
    def set_acceuil(self):
        
        for i in range(5):
            self.acceuil = AcceuilWidget()
            print('##############POST HERRE ///',self.acceuil.random_post['title'])
            self.ui.acceuilSection.addWidget(self.acceuil)
        

    ###########################################################################
    ## Upload Post
    ###########################################################################
    
    def add_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Video File", "", "Video Files (*.mp4 *.avi *.mov)")
        if file_path:
            self.ui.pathLabel.setText(file_path)

    ############################################################   
    # Upload Posts
    ############################################################  
    
    def upload_video(self):
   
        
        title = self.ui.titleQline.text()
        description = self.ui.legendTextEdit.toPlainText()
        path = self.ui.pathLabel.text()
        
        if path and title and description:   
            video_path = f'videos/{title}.mp4'
            ext = path.rsplit(".", 1)[1].lower()
            with open(path, 'rb') as f:
                files = {'file':(f'{secrets.token_hex(5)}.{ext}', f.read())}
                
            self.client.upload_video_file(title, description, files)
            self.notif.show_tray_message("check-circle-green.svg", "Info", "Uploded Successflly")
          
            
            self.video_player = VideoWidget(video_path, title, 212, 380)
           
            
            row_max = self.ui.gridLayout_4.rowCount()
            column = self.ui.gridLayout_4.columnCount()
            nbw = self.ui.gridLayout_4.count()
        
            print("row layout::",nbw//2)
            print('column', nbw%2)
            self.ui.gridLayout_4.addWidget(self.video_player, nbw//2, nbw%2)
            
            self.ui.mainPages.setCurrentWidget(self.ui.profilPage)
            self.ui.titleQline.setText('title here ..')
            self.ui.legendTextEdit.setHtml('Description ..')
            self.ui.pathLabel.setText('')
          
          
        elif not path:
            self.notif.show_tray_message("alert-circle.svg", "Info", " File Not Found")
        
        elif not title:
            self.notif.show_tray_message("alert-circle.svg", "Info", "Title not found")
        
        
        elif not description:
            self.notif.show_tray_message("alert-circle.svg", "Info", "Description not found ")
        
          
    ############################################################
    # Edit Posts
    ############################################################

    def clear_stacked_widget(self, widget):
        while widget.count() > 0:
            widget.removeWidget(widget.widget(0))
        
    def post_edit(self):
        print("*****************begin:")
        self.clear_stacked_widget(self.ui.editPostWidget)
        posts = self.client.get_user_posts()
        print(posts)
        if posts:
            for p in posts:
                print(p)
                self.post = PostEditWidget(p)
                # self.ui.postLayout.addWidget(self.post)
                self.ui.editPostWidget.addWidget(self.post)
                self.post.backBtnSignal.connect(lambda: self.ui.mainPages.setCurrentWidget(self.ui.profilPage))
                
                self.post.delete.connect(self.delete_post)
            self.ui.mainPages.setCurrentWidget(self.ui.editPostPage)
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText("You Have No Post.      ")
           
            # msg_box.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            msg_box.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            msg_box.setIconPixmap(QIcon(u":/icons/icons/feather/info.svg").pixmap(40, 40))
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg_box.setStyleSheet("QMessageBox { background-color: #2C2828; }"
                                "QMessageBox QLabel { color: white; }"
                                "QMessageBox QPushButton { background-color: #555; color: #000; }")
            response = msg_box.exec_()
        
    def delete_post(self):
        widget =  self.ui.editPostWidget.widget(self.ui.editPostWidget.currentIndex())
        self.ui.editPostWidget.removeWidget(widget)
        self.set_posts()
        if self.ui.editPostWidget.count() == 0:
            self.ui.mainPages.setCurrentWidget(self.ui.profilPage)
        else:
            self.ui.editPostWidget.setCurrentIndex(0)
       
           
    def show_tooltip(self):
        self.ui.label.show()
        self.ui.label.move(self.ui.notifBtn.mapToGlobal(self.ui.notifBtn.rect().topLeft()))
        
        # QToolTip.showText( self.ui.notifBtn.mapToGlobal(self.ui.notifBtn.rect().bottomLeft()), "This is a tooltip")     
                # self.ui.notifBtn.setToolTip(self.ui.widget_2)
        # self.tooltip.show()
    
    def eventFilter(self, obj, event):
        if obj == self.ui.scrollArea_2 and event.type() == QWheelEvent.Wheel:
            # Handle wheel events only when the cursor is inside the scroll widget
            if self.ui.scrollArea_2.rect().contains(event.pos()):
                if event.angleDelta().y() < 0:  # scroll down
                    if self.ui.acceuilSection.currentIndex() == self.ui.acceuilSection.count() - 1:
                        self.ui.acceuilSection.slideToPreviousWidget()
                else:
                    self.ui.acceuilSection.slideToNextWidget()
        
                event.accept()  
            return True
        return super().eventFilter(obj, event)
        
    ################################################################
    ## PROGRESS BAR FUNCTION
    ################################################################ 
    def progress(self):
       count = 24
       for i in range(100):
           count += 1
           time.sleep(0.01)
           self.ui.loadingBar.setValue(count)
        
    def check_key(self):
        if keyring.get_password(self.SERVICE_NAME, self.USERNAME) is None:
            self.ui.mainPages.setCurrentWidget(self.ui.loginPage)
        else:
            self.ui.mainPages.setCurrentWidget(self.ui.profilPage)
    
    def delete_key(self):
        if keyring.get_password(self.SERVICE_NAME, self.USERNAME):
            keyring.delete_password(self.SERVICE_NAME, self.USERNAME)
        else:
            pass
    
    def logged_in(self):
        if keyring.get_password(self.SERVICE_NAME, self.USERNAME):
            print('TRUE')
            return True
        else:
            print('FALSE')
            return False
        
    def check_password(self):
        user = self.client.get_current_user()
        print(user['password'])
        decode = self.pwd_context.verify(self.ui.ancienpass.text(), user['password'])
        return decode
       
    def update_password(self):
        
        new_pass = self.ui.newpass.text()
        
        if (self.check_password()) and (new_pass):
            data = {
                "password": self.ui.newpass.text()
            }
            self.client.patch_user_data(data)
            self.notif.show_tray_message("check-circle-green.svg", "Info", "Password Updated")
        elif not self.check_password():
            self.notif.show_tray_message("alert-circle.svg", "Error !!", "Wrong Password")
        elif not self.ui.newpass.text():
            self.notif.show_tray_message("alert-circle.svg", "Info", "Password Must Be .. !!")
            
            
    def logout(self):
        self.delete_key()
        self.ui.profileBtn.setIcon(QIcon(u":/icons/icons/feather/log-in.svg"))
        self.ui.mainPages.setCurrentWidget(self.ui.loginPage) 
    
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        # APPLY JSON STYLESHEET
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        self.show()
        
        self.client = APIClient()
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        self.set_acceuil()
        
        ##################################################################
        ## Mock Setup Override
        ##################################################################
        self.ui.mainPages.setCurrentWidget(self.ui.loginPage)
        self.ui.themeBtn.clicked.connect(lambda: self.ui.themeBtn.setIcon(QIcon("icons/feather/sun.svg")))
        # self.ui.profileBtn.setVisible(False)
        # Remove window tlttle bar
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        # # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # # Apply shadow effect
        # self.shadow = QGraphicsDropShadowEffect(self)
        # self.shadow.setBlurRadius(20)
        # self.shadow.setXOffset(0)
        # self.shadow.setYOffset(0)
        # self.shadow.setColor(QColor(0, 92, 157, 150))
        # # Appy shadow to central widget
        # self.ui.centralwidget.setGraphicsEffect(self.shadow)
        # self.ui.notification.setVisible(False)
        
        #######################################################################
        # SHARE CLICK EVENTS
        #######################################################################
        self.ui.homeBtn.clicked.connect(lambda: self.ui.mainPages.setCurrentWidget(self.ui.profilPage) if self.logged_in() else self.ui.mainPages.setCurrentWidget(self.ui.loginPage))
        self.ui.homeBtn1.clicked.connect(lambda: self.ui.mainPages.setCurrentWidget(self.ui.profilPage) if self.logged_in() else self.ui.mainPages.setCurrentWidget(self.ui.loginPage))
        self.ui.followingBtn.clicked.connect(self.progress)
        self.ui.followingBtn1.clicked.connect(self.progress)
        self.ui.liveBtn.clicked.connect(lambda: self.ui.liveBtn1.click())
        
        
        ## Login n Register Pages
        self.ui.loginLabel.linkActivated.connect(lambda: self.ui.mainPages.setCurrentWidget(self.ui.registerPage))
        self.ui.registerLabel.linkActivated.connect(lambda: self.ui.mainPages.setCurrentWidget(self.ui.loginPage))
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.registerBtn.clicked.connect(self.add_user)
        
        ## Profil Edit Page
        self.ui.saveBtn.clicked.connect(self.edit_profil)
        self.ui.editBtn.clicked.connect(self.set_edit_profil)
        self.ui.edithumbnailBtn.clicked.connect(self.upload_avatar)
        self.ui.CancelBtn.clicked.connect(lambda: self.ui.mainPages.setCurrentWidget(self.ui.profilPage))
        
        ## Security Page
        self.ui.securityBtn.clicked.connect(lambda: self.ui.mainPages.setCurrentWidget(self.ui.securityPage))
        self.ui.deleteAccountBtn.clicked.connect(self.delete_user)
        self.ui.savePassBtn.clicked.connect(self.update_password)
        self.ui.backBtn2.clicked.connect(lambda: self.ui.mainPages.setCurrentWidget(self.ui.profilPage))
        
        ## Edit Post Events
        self.ui.editPostBtn.clicked.connect(self.post_edit)
        self.ui.nextBtn.clicked.connect(lambda: self.ui.editPostWidget.slideToNextWidget())
        self.ui.prevBtn.clicked.connect(lambda: self.ui.editPostWidget.slideToPreviousWidget())
        
        
        # Upload Post
        self.ui.uploadBtn.clicked.connect(lambda: self.ui.mainPages.setCurrentWidget(self.ui.uploadPage) if self.logged_in() else self.ui.mainPages.setCurrentWidget(self.ui.loginPage))
        self.ui.addFileBtn.clicked.connect(self.add_file)
        self.ui.uploadFileBtn.clicked.connect(self.upload_video)
        
        # Scroll Event
        self.ui.scrollArea_2.installEventFilter(self)
        self.ui.notifBtn.clicked.connect(self.show_tooltip)
        
        # self.ui.closeNotification.clicked.connect(self.ui.notification.collapseMenu())
        self.ui.profileBtn.clicked.connect(self.check_key)
        self.ui.closeWindow.clicked.connect(self.delete_key)
        
        
        ## Notifaction Tary Windows 
        self.notif = TrayNotification(self)
        self.notif.show()
        self.notif.logout.connect(lambda: self.logout())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("IKarma") # set the name of your app here

    # Create main window
    window = MainWindow()
    # Show main window
    window.show()
    # Run the event loop
    sys.exit(app.exec_())
