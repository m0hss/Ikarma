# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tikplayerympBse.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import resources_rc

class Ui_VideoWidget(object):
    def setupUi(self, VideoWidget, width, height):
        if VideoWidget.objectName():
            VideoWidget.setObjectName(u"VideoWidget")
        VideoWidget.resize(width, height)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VideoWidget.sizePolicy().hasHeightForWidth())
        VideoWidget.setSizePolicy(sizePolicy)
        VideoWidget.setMinimumSize(QSize(width, height))
        VideoWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(VideoWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(VideoWidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(width, height))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setMouseTracking(True)
        self.label.setStyleSheet(u"background-color: transparent;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.controlWidget = QWidget(VideoWidget)
        self.controlWidget.setObjectName(u"controlWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.controlWidget.sizePolicy().hasHeightForWidth())
        self.controlWidget.setSizePolicy(sizePolicy2)
        self.controlWidget.setMinimumSize(QSize(width, 20))
        self.controlWidget.setMaximumSize(QSize(16777215, 20))
        self.controlWidget.setStyleSheet(u"background-color:  rgba(75, 75, 75, 200)")
        self.horizontalLayout = QHBoxLayout(self.controlWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 2, 0)
        self.playButton = QToolButton(self.controlWidget)
        self.playButton.setObjectName(u"playButton")
        sizePolicy.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy)
        self.playButton.setMaximumSize(QSize(30, 20))
        self.playButton.setLayoutDirection(Qt.LeftToRight)
        self.playButton.setAutoFillBackground(False)
        self.playButton.setStyleSheet(u"background-color: transparent;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/feather/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.playButton.setIcon(icon)
        self.playButton.setIconSize(QSize(20, 20))
        self.playButton.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.playButton)

        self.QSlider = QSlider(self.controlWidget)
        self.QSlider.setObjectName(u"QSlider")
        self.QSlider.setMinimumSize(QSize(77, 13))
        self.QSlider.setMaximumSize(QSize(16777215, 18))
        self.QSlider.setAutoFillBackground(False)
        self.QSlider.setStyleSheet(u"#QSlider::groove:horizontal{\n"
"border: 1px solid #FFFFFF;  background: #C0C0C0;  height: 1px;  border-radius: 1px;  padding-left:-1px;  padding-right:-1px;\n"
"}\n"
"\n"
"#QSlider::handle:horizontal{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,   stop:0.6 #000, stop:0.778409 rgba(255, 255, 255, 255));  width: 11px;  margin-top: -5px;  margin-bottom: -5px;  border-radius: 5px;\n"
"}\n"
"*{\n"
"background-color: transparent;\n"
"margin-right: 1.5px;\n"
"}")
        self.QSlider.setMaximum(100)
        self.QSlider.setValue(0)
        self.QSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.QSlider)

        self.timeLabel = QLabel(self.controlWidget)
        self.timeLabel.setObjectName(u"timeLabel")
        sizePolicy.setHeightForWidth(self.timeLabel.sizePolicy().hasHeightForWidth())
        self.timeLabel.setSizePolicy(sizePolicy)
        self.timeLabel.setMinimumSize(QSize(76, 20))
        self.timeLabel.setMaximumSize(QSize(76, 20))
        self.timeLabel.setStyleSheet(u"background-color: transparent; margin-left: 2px;")
        self.timeLabel.setFrameShape(QFrame.StyledPanel)
        self.timeLabel.setFrameShadow(QFrame.Sunken)
        self.timeLabel.setScaledContents(True)
        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.timeLabel.setWordWrap(False)
        self.timeLabel.setMargin(0)
        self.timeLabel.setIndent(0)

        self.horizontalLayout.addWidget(self.timeLabel, 0, Qt.AlignHCenter)

        self.soundButton = QToolButton(self.controlWidget)
        self.soundButton.setObjectName(u"soundButton")
        sizePolicy.setHeightForWidth(self.soundButton.sizePolicy().hasHeightForWidth())
        self.soundButton.setSizePolicy(sizePolicy)
        self.soundButton.setMinimumSize(QSize(24, 20))
        self.soundButton.setMaximumSize(QSize(27, 20))
        self.soundButton.setLayoutDirection(Qt.RightToLeft)
        self.soundButton.setStyleSheet(u"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/feather/volume-x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.soundButton.setIcon(icon1)
        self.soundButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.soundButton)


        self.verticalLayout.addWidget(self.controlWidget)


        self.retranslateUi(VideoWidget)

        QMetaObject.connectSlotsByName(VideoWidget)
    # setupUi

    def retranslateUi(self, VideoWidget):
        VideoWidget.setWindowTitle(QCoreApplication.translate("VideoWidget", u"Form", None))
        self.label.setText("")
        self.playButton.setText("")
        self.timeLabel.setText(QCoreApplication.translate("VideoWidget", u"00:16/00:30", None))
        self.soundButton.setText("")
    # retranslateUi

