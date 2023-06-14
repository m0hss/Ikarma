import cv2
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QSize, QTimer, QRect, QEvent
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QSizePolicy, QSlider, QMainWindow
from PySide2.QtGui import QPixmap, QImage, QIcon, QMovie, QMouseEvent
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent

from UI.ui_acceuil import *
import os
import sys
import requests
from pathlib import Path
import time
from VideoPlayer import VideoWidget
from client import APIClient
import vlc
import random
from vlc import EventType

class AcceuilWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        
        self.ui= Ui_AcceuilWidget()
        self.ui.setupUi(self)
   

        self.client= APIClient()
        
        posts = self.client.get_all_posts()
        # dico = dict(posts) 
        titles = [post['title'] for post in posts]    
        print(titles)
        self.random_post = random.choice(posts)
        print(self.random_post['title'])
        print(self.random_post['description']) 
        print(self.random_post['user']['username'])
        print(self.random_post['user']['first_name'])
        print(self.random_post['user']['last_name'])
        print(self.random_post['user']['id'])
        
        user_id = self.random_post['user']['id']
        avatar = self.client.get_user_avatar(user_id)
        pixmap = QPixmap()
        pixmap.loadFromData(avatar)
        self.ui.label_135.setPixmap(pixmap)
        self.ui.label_136.setText(QCoreApplication.translate("AcceuilWidget", 
                                                             f"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">{self.random_post['user']['username']}</span><img src=\":/images/images/app/twitter-verified-png-original.png\" width=\"10\"/>\n"
                                                             f"<span style=\" font-size:10pt;\"> {self.random_post['user']['first_name']} {self.random_post['user']['last_name']}<br/>{self.random_post['description']}<br/></span><span style=\" font-size:9pt;\"><br/></span></p></body></html>", None))
        

        
        
        video_path = f"videos/{ self.random_post['title'] }.mp4"
        # print(video_path)
        title = self.random_post['title']
        self.video_player = VideoWidget(video_path, title , 322, 570)
        self.ui.acceuilLayout.addWidget(self.video_player)
        self.ui.acceuilLayout.addWidget(self.ui.SCLWidget)
        self.ui.postPlayWidget.setLayout(self.ui.acceuilLayout)
    