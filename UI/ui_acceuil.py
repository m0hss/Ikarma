# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acceuilJIsamq.ui'
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
import resources_rc

class Ui_AcceuilWidget(object):
    def setupUi(self, AcceuilWidget):
        if AcceuilWidget.objectName():
            AcceuilWidget.setObjectName(u"AcceuilWidget")
        AcceuilWidget.resize(441, 715)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AcceuilWidget.sizePolicy().hasHeightForWidth())
        AcceuilWidget.setSizePolicy(sizePolicy)
        AcceuilWidget.setMinimumSize(QSize(441, 715))
        AcceuilWidget.setMaximumSize(QSize(441, 715))
        AcceuilWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(AcceuilWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_58 = QWidget(AcceuilWidget)
        self.widget_58.setObjectName(u"widget_58")
        sizePolicy.setHeightForWidth(self.widget_58.sizePolicy().hasHeightForWidth())
        self.widget_58.setSizePolicy(sizePolicy)
        self.widget_58.setMaximumSize(QSize(413, 85))
        self.horizontalLayout_28 = QHBoxLayout(self.widget_58)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_84 = QFrame(self.widget_58)
        self.frame_84.setObjectName(u"frame_84")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_84.sizePolicy().hasHeightForWidth())
        self.frame_84.setSizePolicy(sizePolicy1)
        self.frame_84.setMinimumSize(QSize(0, 59))
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.frame_84)
        self.verticalLayout_123.setSpacing(0)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.label_135 = QLabel(self.frame_84)
        self.label_135.setObjectName(u"label_135")
        sizePolicy.setHeightForWidth(self.label_135.sizePolicy().hasHeightForWidth())
        self.label_135.setSizePolicy(sizePolicy)
        self.label_135.setMinimumSize(QSize(40, 40))
        self.label_135.setMaximumSize(QSize(40, 40))
        self.label_135.setPixmap(QPixmap(u":/images/images/profile/circled3.png"))
        self.label_135.setScaledContents(True)
        self.label_135.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.label_135.setWordWrap(True)

        self.verticalLayout_123.addWidget(self.label_135, 0, Qt.AlignLeft|Qt.AlignTop)

        self.verticalSpacer_10 = QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_123.addItem(self.verticalSpacer_10)


        self.horizontalLayout_28.addWidget(self.frame_84)

        self.frame_85 = QFrame(self.widget_58)
        self.frame_85.setObjectName(u"frame_85")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_85.sizePolicy().hasHeightForWidth())
        self.frame_85.setSizePolicy(sizePolicy2)
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_124 = QVBoxLayout(self.frame_85)
        self.verticalLayout_124.setSpacing(0)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.label_136 = QLabel(self.frame_85)
        self.label_136.setObjectName(u"label_136")
        sizePolicy2.setHeightForWidth(self.label_136.sizePolicy().hasHeightForWidth())
        self.label_136.setSizePolicy(sizePolicy2)
        self.label_136.setWordWrap(True)

        self.verticalLayout_124.addWidget(self.label_136)


        self.horizontalLayout_28.addWidget(self.frame_85)

        self.frame_86 = QFrame(self.widget_58)
        self.frame_86.setObjectName(u"frame_86")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_86.sizePolicy().hasHeightForWidth())
        self.frame_86.setSizePolicy(sizePolicy3)
        self.frame_86.setMinimumSize(QSize(100, 0))
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_127 = QVBoxLayout(self.frame_86)
        self.verticalLayout_127.setSpacing(0)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.pushButton_102 = QPushButton(self.frame_86)
        self.pushButton_102.setObjectName(u"pushButton_102")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_102.sizePolicy().hasHeightForWidth())
        self.pushButton_102.setSizePolicy(sizePolicy4)
        self.pushButton_102.setStyleSheet(u"border: 1px solid #555;\n"
"padding: 3px 5px;\n"
"font-weight: bold;\n"
"border-radius: 5px;\n"
"background-color: #2C2828")

        self.verticalLayout_127.addWidget(self.pushButton_102, 0, Qt.AlignTop)


        self.horizontalLayout_28.addWidget(self.frame_86)


        self.verticalLayout.addWidget(self.widget_58)

        self.postPlayWidget = QWidget(AcceuilWidget)
        self.postPlayWidget.setObjectName(u"postPlayWidget")
        sizePolicy1.setHeightForWidth(self.postPlayWidget.sizePolicy().hasHeightForWidth())
        self.postPlayWidget.setSizePolicy(sizePolicy1)
        self.postPlayWidget.setMinimumSize(QSize(397, 553))
        self.postPlayWidget.setMaximumSize(QSize(397, 16777215))
        self.postPlayWidget.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayoutWidget = QWidget(self.postPlayWidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 19, 341, 561))
        self.acceuilLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.acceuilLayout.setSpacing(0)
        self.acceuilLayout.setObjectName(u"acceuilLayout")
        self.acceuilLayout.setContentsMargins(9, 0, 0, 0)
        self.SCLWidget = QWidget(self.horizontalLayoutWidget)
        self.SCLWidget.setObjectName(u"SCLWidget")
        self.SCLWidget.setMinimumSize(QSize(43, 532))
        self.SCLWidget.setMaximumSize(QSize(56, 532))
        self.SCLWidget.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout_23 = QVBoxLayout(self.SCLWidget)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, -1, 0, 0)
        self.verticalSpacer_11 = QSpacerItem(20, 390, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_23.addItem(self.verticalSpacer_11)

        self.frame_87 = QFrame(self.SCLWidget)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(37, 180))
        self.frame_87.setMaximumSize(QSize(37, 16777215))
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.verticalLayout_126 = QVBoxLayout(self.frame_87)
        self.verticalLayout_126.setSpacing(6)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(0, 0, 6, 0)
        self.pushButton_99 = QPushButton(self.frame_87)
        self.pushButton_99.setObjectName(u"pushButton_99")
        self.pushButton_99.setMinimumSize(QSize(0, 0))
        self.pushButton_99.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_99.setLayoutDirection(Qt.RightToLeft)
        icon = QIcon()
        icon.addFile(u":/icons/icons/feather/heart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_99.setIcon(icon)
        self.pushButton_99.setIconSize(QSize(24, 24))

        self.verticalLayout_126.addWidget(self.pushButton_99)

        self.label_137 = QLabel(self.frame_87)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setAlignment(Qt.AlignCenter)

        self.verticalLayout_126.addWidget(self.label_137)

        self.pushButton_100 = QPushButton(self.frame_87)
        self.pushButton_100.setObjectName(u"pushButton_100")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/feather/message-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_100.setIcon(icon1)
        self.pushButton_100.setIconSize(QSize(24, 24))

        self.verticalLayout_126.addWidget(self.pushButton_100)

        self.label_138 = QLabel(self.frame_87)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setAlignment(Qt.AlignCenter)

        self.verticalLayout_126.addWidget(self.label_138)

        self.pushButton_101 = QPushButton(self.frame_87)
        self.pushButton_101.setObjectName(u"pushButton_101")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/feather/share-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_101.setIcon(icon2)
        self.pushButton_101.setIconSize(QSize(24, 24))

        self.verticalLayout_126.addWidget(self.pushButton_101)

        self.label_139 = QLabel(self.frame_87)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setAlignment(Qt.AlignCenter)

        self.verticalLayout_126.addWidget(self.label_139)


        self.verticalLayout_23.addWidget(self.frame_87)


        self.acceuilLayout.addWidget(self.SCLWidget)


        self.verticalLayout.addWidget(self.postPlayWidget)


        self.retranslateUi(AcceuilWidget)

        QMetaObject.connectSlotsByName(AcceuilWidget)
    # setupUi

    def retranslateUi(self, AcceuilWidget):
        AcceuilWidget.setWindowTitle(QCoreApplication.translate("AcceuilWidget", u"Form", None))
        self.label_135.setText("")
        self.label_136.setText(QCoreApplication.translate("AcceuilWidget", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Jr.ney</span><img src=\":/images/images/app/twitter-verified-png-original.png\" width=\"10\"/><span style=\" font-size:10pt;\"> Big up Profile<br/>Never!!! <br/>#foot #challenge #ytags #bestfriends #goal sankara!!</span><span style=\" font-size:9pt;\"><br/></span></p></body></html>", None))
        self.pushButton_102.setText(QCoreApplication.translate("AcceuilWidget", u"Following", None))
        self.pushButton_99.setText("")
        self.label_137.setText(QCoreApplication.translate("AcceuilWidget", u"13.6K", None))
        self.pushButton_100.setText("")
        self.label_138.setText(QCoreApplication.translate("AcceuilWidget", u"143", None))
        self.pushButton_101.setText("")
        self.label_139.setText(QCoreApplication.translate("AcceuilWidget", u"582", None))
    # retranslateUi

