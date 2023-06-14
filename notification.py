from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *
from PySide2.QtCore import QSize, QTimer, QRect, QEvent, Signal, QThread

class TrayNotification(QThread):
    
    logout = Signal()
    
    def __init__(self, app):
        super().__init__()
        # Create system tray
        self.tray = QSystemTrayIcon(QIcon(u":/icons/icons/ikarma.png"), app)
        self.menu = QMenu()
        self.create_actions()
        self.add_actions_to_menu()
        self.tray.setContextMenu(self.menu)
        # set the window title here
        # self.tray.setWindowTitle("IKarma")
        self.tray.setToolTip("IKarma")

    def create_actions(self):
        self.action_tray_message = QAction("Logout")
        self.action_hide = QAction("Hide Window")
        self.action_show = QAction("Show Window")
        self.action_exit = QAction("Exit")
        self.action_tray_message.triggered.connect(self.logout.emit)
        self.action_exit.triggered.connect(QApplication.instance().exit)

    def add_actions_to_menu(self):
        self.menu.addAction(self.action_tray_message)
        self.menu.addAction(self.action_hide)
        self.menu.addAction(self.action_show)
        self.menu.addAction(self.action_exit)
        

    def show_tray_message(self, icon, title, message=None):
        qicon = QIcon(f':icons/icons/feather/{icon}')
        duration = 3 * 1000 #3 seconds
        self.tray.showMessage(title, message, qicon, duration)

    def show(self):
        self.tray.show()