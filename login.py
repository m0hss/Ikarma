
import requests as req
from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal, QTimer
import keyring
import time
from client import APIClient


class LoginWorker(QThread):
    
    login_successful = pyqtSignal()
    login_failed = pyqtSignal(str)
    progress_updated = pyqtSignal(int)
    
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.client = APIClient()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        # self.timer.start(10)
    
    def run(self):
        self.progress = 0
        self.timer.start(10) # start timer with 10ms interval
        try:
            self.progress_updated.emit(self.progress)
            self.client.login(self.username, self.password)
            self.login_successful.emit()
        except req.exceptions.HTTPError as e:
            self.login_failed.emit("Wrong email or password")
        # finally:
        #     i = 0
        #     while not self.isInterruptionRequested():
        #         self.progress_updated.emit(i % 101)
        #         i += 1
        #         time.sleep(0.01)
        #         # if not self.isRunning():
        #         #     break
    def update_progress(self):
        self.progress += 1
        # emit progress signal
        self.progress_updated.emit(self.progress % 101)
