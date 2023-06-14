import cv2
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QSize, QTimer, QRect, QEvent, Signal
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QSizePolicy, QSlider, QMessageBox
from PySide2.QtGui import QPixmap, QImage, QIcon, QMovie, QMouseEvent
from pathlib import Path
from UI.ui_post import *
from client import APIClient
from notification import TrayNotification


class PostEditWidget(QWidget):
    
    backBtnSignal = Signal()
    delete = Signal()
    prevBtnSignal = Signal()
    
    def __init__(self, post, parent=None):
        super().__init__()
        
        self.ui= Ui_PostEdit()
        self.ui.setupUi(self)
        
        self.post = post
        self.client = APIClient()
        self.notif = TrayNotification(self)
        self.notif.show()
        
        title = self.post['title']
        self.ui.title.setText(title)
        self.ui.description.setHtml(self.post['description'])
        try:
            pixmap = QPixmap(f'images/thumbnail/{title}212x380.png')
            print('from existing png')
        except Exception as e:
            print(f'Error loading image file: {e}')
            app.exit(1)
            
        self.ui.thumbnailLabel.setPixmap(pixmap)
        
        self.ui.confirmBtn.clicked.connect(self.save)
        self.ui.backBtn.clicked.connect(self.backBtnSignal.emit)
        self.ui.deletePostBtn.clicked.connect(self.deletePost)
        
        
        
        
    def save(self):
        data ={ 
            "title": self.ui.title.text(),
            "description": self.ui.description.toPlainText(),
        }
        print('id = ',self.post['id'])
        print("data = ", data)
        id = self.post['id']
        self.client.patch_post(id, data)
        self.notif.show_tray_message("check-circle-green.svg", "Info", "Saved Successflly")
        
    def deletePost(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setText("Are you sure you want to delete this post?")
        msg_box.setWindowTitle("Confirm Deletion")
        # msg_box.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        msg_box.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        msg_box.setIconPixmap(QIcon(u":/icons/icons/feather/alert-octagon.svg").pixmap(40, 40))
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg_box.setStyleSheet("QMessageBox { background-color: #2C2828; }"
                            "QMessageBox QLabel { color: white; }"
                            "QMessageBox QPushButton { background-color: #555; color: #000; }")
        response = msg_box.exec_()
        if response == QtWidgets.QMessageBox.Yes:
            self.client.delete_post(self.post['id'])
            self.delete.emit()
            self.notif.show_tray_message("check-circle-green.svg", "Info",f'{self.post["title"]} deleted Successflly!')
    
        
        
        
# os.environ["QT_SCALE_FACTOR"] = "1"
# if __name__ == '__main__':
#     app = QApplication(sys.argv) 
#     window = PostEditWidget()
#     window.show()
#     sys.exit(app.exec_())   