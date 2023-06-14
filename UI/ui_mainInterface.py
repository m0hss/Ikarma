# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainInterfaceAyhGaa.ui'
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

from Custom_Widgets.Widgets import QCustomQPushButton
from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1294, 891)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(91, 0))
        icon = QIcon()
        icon.addFile(u":/icons/icons/ikarma.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"border: nine;\n"
"padding: 0;\n"
"margin: 0;\n"
"background-color: transparent;\n"
"background: #121212;\n"
"border-color: transparent;\n"
"}\n"
"\n"
"#centralwidget * {\n"
"background-color:#121212;\n"
"color : rgba(255, 255, 255, 200);\n"
"}\n"
"\n"
"#searchInput{\n"
"	background-color: rgba(138, 138, 138, 100);\n"
"    border-radius: 10px;\n"
"	color : rgb(248, 248, 248)\n"
"}\n"
"\n"
"#searchButton, #searchLine{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#loadingBarCont {\n"
"background-color:  rgba(0, 0, 0, 200);\n"
"}\n"
"\n"
"#profilPixFrame {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#header{\n"
"	border-bottom: 1px solid #555;\n"
"}\n"
"\n"
"#sideMenu  *{\n"
"text-align: left;\n"
"border-color: rgba(188, 188, 23, 100);\n"
"}\n"
"\n"
"#sideMenuCont, #commentsSectionCont{\n"
" border-right: 1px solid lightgray;\n"
" border-color: rgba(188, 188, 23, 100);\n"
"}\n"
"\n"
"#footer{\n"
"	border-top: 1px solid lightgray;\n"
"}\n"
"\n"
"#sideMenuCont  QPushButton{\n"
"	font-weight: bold;\n"
""
                        "	color: rgba(188, 188, 23, 200);\n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"\n"
"#scrollArea_acceuilSection, #acceuilSection {\n"
"border-right: 1px solid lightgrey;\n"
"padding-right : 5px;\n"
"}\n"
"\n"
"QScrollArea{\n"
"	background: rgba(0, 0, 0, 150);\n"
"}\n"
"QScrollBar{\n"
"	background: transparent;\n"
"}\n"
"QScrollBar:horizontal {\n"
"  height: 16px;\n"
"  margin: 2px 16px 2px 16px;\n"
"  border: 1px solid rgba(254, 44, 85, 100);\n"
"  border-radius: 4px;\n"
"  background-color: rgb(185, 185, 185); }\n"
"\n"
"QScrollBar:vertical {\n"
"  background-color: rgb(185, 185, 185);\n"
"  width: 16px;\n"
"  margin: 16px 2px 16px 2px;\n"
"  border: 1px solid rgba(254, 44, 85, 100);\n"
"  border-radius: 4px; }\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgba(254, 44, 85, 100);\n"
"  border: 1px solid rgba(254, 44, 85, 100);\n"
"  border-radius: 4px;\n"
"  min-width: 8px; }\n"
"  QScrollBar::handle:horizontal:hover {\n"
"    background-color:rgba(254, 44, 85, 1.0);\n"
"    border: rgba(2"
                        "54, 44, 85, 1.0);\n"
"    border-radius: 4px;\n"
"    min-width: 8px; }\n"
"  QScrollBar::handle:horizontal:focus {\n"
"    border: 1px solid rgba(254, 44, 85, 1.0); }\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgba(254, 44, 85, 100);\n"
"  border: 1px solid rgba(254, 44, 85, 100);\n"
"  min-height: 8px;\n"
"  border-radius: 4px; }\n"
"  QScrollBar::handle:vertical:hover {\n"
"    background-color: rgba(254, 44, 85, 1.0);\n"
"    border: rgba(254, 44, 85, 1.0);\n"
"    border-radius: 4px;\n"
"    min-height: 8px; }\n"
"  QScrollBar::handle:vertical:focus {\n"
"    border: 1px solid rgba(254, 44, 85, 1.0); }\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  margin: 0px 0px 0px 0px;\n"
"  border-image: url(\":/icons/icons/feather/chevron-right.svg\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin; }\n"
"  QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on {\n"
"    border-image: url(\":/icons/icons/feather/chevro"
                        "n-right.svg\");\n"
"    height: 12px;\n"
"    width: 12px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin; }\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/icons/icons/feather/chevron-down.svg\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin; }\n"
"  QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
"    border-image: url(\":/icons/icons/feather/chevron-down.svg\");\n"
"    height: 12px;\n"
"    width: 12px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin; }\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  margin: 0px 3px 0px 3px;\n"
"  border-image: url(\":/icons/icons/feather/chevron-left.svg\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin; }\n"
"  QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on {\n"
"    border-image: url(\":/icons/icons/fea"
                        "ther/chevron-left.svg\");\n"
"    height: 12px;\n"
"    width: 12px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin; }\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/icons/icons/feather/chevron-up.svg\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin; }\n"
"  QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
"    border-image: url(\":/icons/icons/feather/chevron-up.svg\");\n"
"    height: 12px;\n"
"    width: 12px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin; }\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"  background: none; }\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"  background: none; }\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"  background: none; }\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
""
                        "  background: none; }\n"
"\n"
"QTabWidget{\n"
"background-color: rgba(255,255,255,255);\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"  border: 1px solid lightgray;\n"
"  top:-1px; \n"
"  background: rgb(245, 245, 245);; \n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"  background: rgb(255, 255, 255); \n"
"  border: none; \n"
"  padding: 10px;\n"
"  font-weight: bold;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"  background:rgba(254, 44, 85, 100);\n"
"  margin-bottom: -1px; \n"
"  border-bottom: 2px solid #000;\n"
"  padding: 10px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"  background-color: #121212;\n"
"  margin-bottom: -1px; \n"
"  border-bottom: 2px solid #000;\n"
"  padding: 10px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    background:  rgba(188, 188, 23, 1.0);\n"
"    text-align: center;\n"
"    height: 2px;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"   background-color:  rgba(188, 188, 23, 1.0);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_24 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 1)
        self.widget = QWidget(self.header)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(64, 64))

        self.horizontalLayout_8.addWidget(self.pushButton)


        self.horizontalLayout_4.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.searchInput = QFrame(self.frame_2)
        self.searchInput.setObjectName(u"searchInput")
        self.searchInput.setStyleSheet(u"")
        self.searchInput.setFrameShape(QFrame.StyledPanel)
        self.searchInput.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.searchInput)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.searchLine = QLineEdit(self.searchInput)
        self.searchLine.setObjectName(u"searchLine")
        self.searchLine.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.searchLine)

        self.searchButton = QPushButton(self.searchInput)
        self.searchButton.setObjectName(u"searchButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/feather/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon1)
        self.searchButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.searchButton)


        self.horizontalLayout_2.addWidget(self.searchInput, 0, Qt.AlignVCenter)


        self.horizontalLayout_4.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.uploadBtn = QPushButton(self.frame_3)
        self.uploadBtn.setObjectName(u"uploadBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(28)
        sizePolicy2.setVerticalStretch(28)
        sizePolicy2.setHeightForWidth(self.uploadBtn.sizePolicy().hasHeightForWidth())
        self.uploadBtn.setSizePolicy(sizePolicy2)
        self.uploadBtn.setMinimumSize(QSize(28, 28))
        self.uploadBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/feather/upload-cloud.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.uploadBtn.setIcon(icon2)
        self.uploadBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.uploadBtn)

        self.notifBtn = QToolButton(self.frame_3)
        self.notifBtn.setObjectName(u"notifBtn")
        sizePolicy2.setHeightForWidth(self.notifBtn.sizePolicy().hasHeightForWidth())
        self.notifBtn.setSizePolicy(sizePolicy2)
        self.notifBtn.setMinimumSize(QSize(28, 28))
        self.notifBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/feather/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notifBtn.setIcon(icon3)
        self.notifBtn.setIconSize(QSize(24, 24))
        self.notifBtn.setPopupMode(QToolButton.DelayedPopup)
        self.notifBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.notifBtn.setAutoRaise(True)

        self.horizontalLayout_7.addWidget(self.notifBtn)

        self.msgBtn = QPushButton(self.frame_3)
        self.msgBtn.setObjectName(u"msgBtn")
        sizePolicy2.setHeightForWidth(self.msgBtn.sizePolicy().hasHeightForWidth())
        self.msgBtn.setSizePolicy(sizePolicy2)
        self.msgBtn.setMinimumSize(QSize(28, 28))
        self.msgBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/feather/message-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.msgBtn.setIcon(icon4)
        self.msgBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.msgBtn)

        self.profileBtn = QPushButton(self.frame_3)
        self.profileBtn.setObjectName(u"profileBtn")
        sizePolicy2.setHeightForWidth(self.profileBtn.sizePolicy().hasHeightForWidth())
        self.profileBtn.setSizePolicy(sizePolicy2)
        self.profileBtn.setMinimumSize(QSize(28, 28))
        self.profileBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.profileBtn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/feather/log-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn.setIcon(icon5)
        self.profileBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.profileBtn)


        self.horizontalLayout_4.addWidget(self.frame_3, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.header)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, 4, -1)
        self.themeBtn = QPushButton(self.frame_5)
        self.themeBtn.setObjectName(u"themeBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/feather/moon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.themeBtn.setIcon(icon6)

        self.horizontalLayout_6.addWidget(self.themeBtn)

        self.minimizeWindow = QPushButton(self.frame_5)
        self.minimizeWindow.setObjectName(u"minimizeWindow")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/feather/minus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeWindow.setIcon(icon7)

        self.horizontalLayout_6.addWidget(self.minimizeWindow)

        self.restoreWindow = QPushButton(self.frame_5)
        self.restoreWindow.setObjectName(u"restoreWindow")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/feather/stop-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreWindow.setIcon(icon8)

        self.horizontalLayout_6.addWidget(self.restoreWindow)

        self.closeWindow = QPushButton(self.frame_5)
        self.closeWindow.setObjectName(u"closeWindow")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/feather/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeWindow.setIcon(icon9)

        self.horizontalLayout_6.addWidget(self.closeWindow)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.widget_2, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_24.addWidget(self.header)

        self.loadingBarCont = QWidget(self.centralwidget)
        self.loadingBarCont.setObjectName(u"loadingBarCont")
        sizePolicy1.setHeightForWidth(self.loadingBarCont.sizePolicy().hasHeightForWidth())
        self.loadingBarCont.setSizePolicy(sizePolicy1)
        self.verticalLayout_16 = QVBoxLayout(self.loadingBarCont)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.loadingBar = QProgressBar(self.loadingBarCont)
        self.loadingBar.setObjectName(u"loadingBar")
        self.loadingBar.setMinimumSize(QSize(0, 2))
        self.loadingBar.setMaximumSize(QSize(16777215, 2))
        self.loadingBar.setMaximum(100)
        self.loadingBar.setValue(20)
        self.loadingBar.setTextVisible(False)
        self.loadingBar.setInvertedAppearance(False)

        self.verticalLayout_16.addWidget(self.loadingBar)


        self.verticalLayout_24.addWidget(self.loadingBarCont)

        self.mainbody = QWidget(self.centralwidget)
        self.mainbody.setObjectName(u"mainbody")
        sizePolicy1.setHeightForWidth(self.mainbody.sizePolicy().hasHeightForWidth())
        self.mainbody.setSizePolicy(sizePolicy1)
        self.horizontalLayout_13 = QHBoxLayout(self.mainbody)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.sideMenu = QWidget(self.mainbody)
        self.sideMenu.setObjectName(u"sideMenu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sideMenu.sizePolicy().hasHeightForWidth())
        self.sideMenu.setSizePolicy(sizePolicy3)
        self.sideMenu.setMinimumSize(QSize(160, 0))
        self.sideMenu.setMaximumSize(QSize(160, 16777215))
        self.sideMenu.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.sideMenu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 9, 0, 0)
        self.scrollArea = QScrollArea(self.sideMenu)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy4)
        self.scrollArea.setMinimumSize(QSize(157, 651))
        self.scrollArea.setMaximumSize(QSize(180, 16777215))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.sideMenuCont = QWidget()
        self.sideMenuCont.setObjectName(u"sideMenuCont")
        self.sideMenuCont.setGeometry(QRect(0, 0, 160, 709))
        sizePolicy4.setHeightForWidth(self.sideMenuCont.sizePolicy().hasHeightForWidth())
        self.sideMenuCont.setSizePolicy(sizePolicy4)
        self.sideMenuCont.setMaximumSize(QSize(180, 16777215))
        self.sideMenuCont.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.sideMenuCont)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.nav1_2 = QWidget(self.sideMenuCont)
        self.nav1_2.setObjectName(u"nav1_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.nav1_2.sizePolicy().hasHeightForWidth())
        self.nav1_2.setSizePolicy(sizePolicy5)
        self.nav1 = QGridLayout(self.nav1_2)
        self.nav1.setObjectName(u"nav1")
        self.nav1.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.nav1.setHorizontalSpacing(3)
        self.nav1.setContentsMargins(12, 9, 0, 0)
        self.followingBtn1 = QPushButton(self.nav1_2)
        self.followingBtn1.setObjectName(u"followingBtn1")
        sizePolicy5.setHeightForWidth(self.followingBtn1.sizePolicy().hasHeightForWidth())
        self.followingBtn1.setSizePolicy(sizePolicy5)
        font = QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.followingBtn1.setFont(font)
        self.followingBtn1.setCursor(QCursor(Qt.PointingHandCursor))

        self.nav1.addWidget(self.followingBtn1, 1, 1, 1, 1)

        self.homeBtn1 = QPushButton(self.nav1_2)
        self.homeBtn1.setObjectName(u"homeBtn1")
        self.homeBtn1.setFont(font)
        self.homeBtn1.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeBtn1.setStyleSheet(u"")

        self.nav1.addWidget(self.homeBtn1, 0, 1, 1, 1)

        self.liveBtn1 = QPushButton(self.nav1_2)
        self.liveBtn1.setObjectName(u"liveBtn1")
        sizePolicy5.setHeightForWidth(self.liveBtn1.sizePolicy().hasHeightForWidth())
        self.liveBtn1.setSizePolicy(sizePolicy5)
        self.liveBtn1.setCursor(QCursor(Qt.PointingHandCursor))

        self.nav1.addWidget(self.liveBtn1, 2, 1, 1, 1)

        self.homeBtn = QCustomQPushButton(self.nav1_2)
        self.homeBtn.setObjectName(u"homeBtn")
        sizePolicy5.setHeightForWidth(self.homeBtn.sizePolicy().hasHeightForWidth())
        self.homeBtn.setSizePolicy(sizePolicy5)
        self.homeBtn.setMaximumSize(QSize(28, 24))
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/feather/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon10)
        self.homeBtn.setIconSize(QSize(24, 24))
        self.homeBtn.setAutoDefault(False)
        self.homeBtn.setFlat(False)

        self.nav1.addWidget(self.homeBtn, 0, 0, 1, 1)

        self.liveBtn = QPushButton(self.nav1_2)
        self.liveBtn.setObjectName(u"liveBtn")
        sizePolicy5.setHeightForWidth(self.liveBtn.sizePolicy().hasHeightForWidth())
        self.liveBtn.setSizePolicy(sizePolicy5)
        self.liveBtn.setMaximumSize(QSize(28, 24))
        self.liveBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/feather/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.liveBtn.setIcon(icon11)
        self.liveBtn.setIconSize(QSize(24, 24))

        self.nav1.addWidget(self.liveBtn, 2, 0, 1, 1)

        self.followingBtn = QPushButton(self.nav1_2)
        self.followingBtn.setObjectName(u"followingBtn")
        sizePolicy5.setHeightForWidth(self.followingBtn.sizePolicy().hasHeightForWidth())
        self.followingBtn.setSizePolicy(sizePolicy5)
        self.followingBtn.setMaximumSize(QSize(28, 24))
        self.followingBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/feather/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.followingBtn.setIcon(icon12)
        self.followingBtn.setIconSize(QSize(24, 24))

        self.nav1.addWidget(self.followingBtn, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.nav1_2)

        self.nav2_3 = QWidget(self.sideMenuCont)
        self.nav2_3.setObjectName(u"nav2_3")
        sizePolicy5.setHeightForWidth(self.nav2_3.sizePolicy().hasHeightForWidth())
        self.nav2_3.setSizePolicy(sizePolicy5)
        self.verticalLayout_56 = QVBoxLayout(self.nav2_3)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label2 = QLabel(self.nav2_3)
        self.label2.setObjectName(u"label2")
        sizePolicy5.setHeightForWidth(self.label2.sizePolicy().hasHeightForWidth())
        self.label2.setSizePolicy(sizePolicy5)
        self.label2.setStyleSheet(u"color: rgb(81, 81, 81);")

        self.verticalLayout_56.addWidget(self.label2)

        self.nav2 = QFrame(self.nav2_3)
        self.nav2.setObjectName(u"nav2")
        sizePolicy5.setHeightForWidth(self.nav2.sizePolicy().hasHeightForWidth())
        self.nav2.setSizePolicy(sizePolicy5)
        self.nav2.setFrameShape(QFrame.StyledPanel)
        self.nav2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.nav2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.nav2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)

        self.pushButton_17 = QPushButton(self.nav2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy5.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.pushButton_17, 5, 0, 1, 1)

        self.label_7 = QLabel(self.nav2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(30, 30))
        self.label_7.setPixmap(QPixmap(u":/images/images/profile/profile-pic.png"))
        self.label_7.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_5 = QLabel(self.nav2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(30, 30))
        self.label_5.setStyleSheet(u"border-radius: 15px;")
        self.label_5.setPixmap(QPixmap(u":/images/images/profile/profile-pic (1).png"))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_3 = QLabel(self.nav2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_6 = QLabel(self.nav2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(30, 30))
        self.label_6.setPixmap(QPixmap(u":/images/images/profile/profile-pic (5).png"))
        self.label_6.setScaledContents(True)
        self.label_6.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_4 = QLabel(self.nav2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 4, 2, 1, 1)


        self.verticalLayout_56.addWidget(self.nav2)


        self.verticalLayout.addWidget(self.nav2_3)

        self.nav3_3 = QWidget(self.sideMenuCont)
        self.nav3_3.setObjectName(u"nav3_3")
        sizePolicy5.setHeightForWidth(self.nav3_3.sizePolicy().hasHeightForWidth())
        self.nav3_3.setSizePolicy(sizePolicy5)
        self.verticalLayout_30 = QVBoxLayout(self.nav3_3)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label2_3 = QLabel(self.nav3_3)
        self.label2_3.setObjectName(u"label2_3")
        sizePolicy5.setHeightForWidth(self.label2_3.sizePolicy().hasHeightForWidth())
        self.label2_3.setSizePolicy(sizePolicy5)
        self.label2_3.setStyleSheet(u"color: rgb(81, 81, 81);")

        self.verticalLayout_30.addWidget(self.label2_3)

        self.nav2_6 = QFrame(self.nav3_3)
        self.nav2_6.setObjectName(u"nav2_6")
        sizePolicy5.setHeightForWidth(self.nav2_6.sizePolicy().hasHeightForWidth())
        self.nav2_6.setSizePolicy(sizePolicy5)
        self.nav2_6.setFrameShape(QFrame.StyledPanel)
        self.nav2_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.nav2_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_9 = QLabel(self.nav2_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(30, 30))
        self.label_9.setStyleSheet(u"border-radius: 15px;")
        self.label_9.setPixmap(QPixmap(u":/images/images/profile/profile-pic (2).png"))
        self.label_9.setScaledContents(True)
        self.label_9.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_12 = QLabel(self.nav2_6)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 0, 2, 1, 1)

        self.label_11 = QLabel(self.nav2_6)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 1, 2, 1, 1)

        self.label_13 = QLabel(self.nav2_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(30, 30))
        self.label_13.setPixmap(QPixmap(u":/images/images/profile/profile-pic (10).png"))
        self.label_13.setScaledContents(True)
        self.label_13.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_10 = QLabel(self.nav2_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(30, 30))
        self.label_10.setPixmap(QPixmap(u":/images/images/profile/circled2.png"))
        self.label_10.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_10, 4, 0, 1, 1)

        self.label_14 = QLabel(self.nav2_6)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 4, 2, 1, 1)

        self.pushButton_24 = QPushButton(self.nav2_6)
        self.pushButton_24.setObjectName(u"pushButton_24")
        sizePolicy5.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy5)

        self.gridLayout_3.addWidget(self.pushButton_24, 5, 0, 1, 1)


        self.verticalLayout_30.addWidget(self.nav2_6)


        self.verticalLayout.addWidget(self.nav3_3)

        self.nav4_3 = QWidget(self.sideMenuCont)
        self.nav4_3.setObjectName(u"nav4_3")
        sizePolicy5.setHeightForWidth(self.nav4_3.sizePolicy().hasHeightForWidth())
        self.nav4_3.setSizePolicy(sizePolicy5)
        self.verticalLayout_15 = QVBoxLayout(self.nav4_3)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label4 = QLabel(self.nav4_3)
        self.label4.setObjectName(u"label4")
        sizePolicy5.setHeightForWidth(self.label4.sizePolicy().hasHeightForWidth())
        self.label4.setSizePolicy(sizePolicy5)
        self.label4.setStyleSheet(u"color: rgb(81, 81, 81);")

        self.verticalLayout_15.addWidget(self.label4)

        self.nav4 = QFrame(self.nav4_3)
        self.nav4.setObjectName(u"nav4")
        sizePolicy5.setHeightForWidth(self.nav4.sizePolicy().hasHeightForWidth())
        self.nav4.setSizePolicy(sizePolicy5)
        self.nav4.setFrameShape(QFrame.StyledPanel)
        self.nav4.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.nav4)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(9, -1, -1, -1)
        self.pushButton_18 = QPushButton(self.nav4)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.pushButton_18)

        self.pushButton_19 = QPushButton(self.nav4)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.pushButton_19)

        self.pushButton_20 = QPushButton(self.nav4)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pushButton_20)

        self.pushButton_21 = QPushButton(self.nav4)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.pushButton_21)


        self.verticalLayout_15.addWidget(self.nav4)


        self.verticalLayout.addWidget(self.nav4_3)

        self.verticalSpacer = QSpacerItem(20, 107, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.sideMenuCont)

        self.verticalLayout_5.addWidget(self.scrollArea)


        self.horizontalLayout_13.addWidget(self.sideMenu)

        self.scrollArea_2 = QScrollArea(self.mainbody)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy5.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy5)
        self.scrollArea_2.setMinimumSize(QSize(454, 711))
        self.scrollArea_2.setMaximumSize(QSize(445, 16777215))
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollArea_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 447, 712))
        sizePolicy5.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy5)
        self.scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 715))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(6, 0, 6, 0)
        self.acceuilSection = QCustomStackedWidget(self.scrollAreaWidgetContents)
        self.acceuilSection.setObjectName(u"acceuilSection")
        sizePolicy5.setHeightForWidth(self.acceuilSection.sizePolicy().hasHeightForWidth())
        self.acceuilSection.setSizePolicy(sizePolicy5)
        self.acceuilSection.setMinimumSize(QSize(438, 710))
        self.acceuilSection.setMaximumSize(QSize(438, 710))
        self.acceuilSection.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.acceuilSection)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_13.addWidget(self.scrollArea_2)

        self.homeSection = QWidget(self.mainbody)
        self.homeSection.setObjectName(u"homeSection")
        sizePolicy1.setHeightForWidth(self.homeSection.sizePolicy().hasHeightForWidth())
        self.homeSection.setSizePolicy(sizePolicy1)
        self.homeSection.setMinimumSize(QSize(628, 671))
        self.homeSection.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_21 = QVBoxLayout(self.homeSection)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QCustomStackedWidget(self.homeSection)
        self.mainPages.setObjectName(u"mainPages")
        sizePolicy1.setHeightForWidth(self.mainPages.sizePolicy().hasHeightForWidth())
        self.mainPages.setSizePolicy(sizePolicy1)
        self.mainPages.setMinimumSize(QSize(628, 0))
        self.mainPages.setMaximumSize(QSize(16777215, 16777215))
        self.mainPages.setStyleSheet(u"")
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.horizontalLayout_14 = QHBoxLayout(self.loginPage)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.loginFormCont = QFrame(self.loginPage)
        self.loginFormCont.setObjectName(u"loginFormCont")
        sizePolicy5.setHeightForWidth(self.loginFormCont.sizePolicy().hasHeightForWidth())
        self.loginFormCont.setSizePolicy(sizePolicy5)
        self.loginFormCont.setMinimumSize(QSize(361, 481))
        self.loginFormCont.setMaximumSize(QSize(361, 481))
        self.loginFormCont.setStyleSheet(u"QPushButton#loginButton{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#loginButton:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#loginButton:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QPushButton#fbButton, #linkedinButton, #ytButton, #twitterButton, #signupButton{	\n"
"	background-color:  transparent;\n"
"	color:rgba(85, 98, 112, 255);\n"
"}\n"
"QPushButton#fbButton:hover, #linkedinButton:hover, #ytButton:hover, #twitterButton:hover, #signupButton::hover{	\n"
"	color:rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#fbButton:pressed, #linkedinButton:pressed, #ytButton:pressed, #twitterButton:pressed {	\n"
"	padding-left:3px;"
                        "\n"
"	padding-top:5px;\n"
"	color:rgba(115, 128, 142, 255);\n"
"}\n"
"#socialFrame, #frame_10, #widget_5, #widget_6 {\n"
"background-color:  transparent;\n"
"\n"
"}\n"
"#usernameLine, #passwordLine{\n"
"background-color:  transparent;\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;\n"
"}\n"
"\n"
"#iconeLabel{\n"
"background-color: transparent;\n"
"}\n"
"#signupFrame {\n"
"background-color: transparent;\n"
"}\n"
"#RegisterButton {\n"
"color:rgba(255, 255, 255, 140);\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#forgetpassLabel, #loginLabel {\n"
"color:rgba(255, 255, 255, 140);\n"
"background-color: transparent;\n"
"}")
        self.label_19 = QLabel(self.loginFormCont)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(30, 30, 300, 420))
        self.label_19.setStyleSheet(u"border-image: url(:/images/images/app/background.png);\n"
"border-radius:20px;")
        self.label_20 = QLabel(self.loginFormCont)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(30, 30, 300, 420))
        self.label_20.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
"border-radius:20px;")
        self.label_21 = QLabel(self.loginFormCont)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(40, 60, 280, 390))
        self.label_21.setStyleSheet(u"background-color:rgba(0, 0, 0, 100);\n"
"border-radius:15px;")
        self.frame_10 = QFrame(self.loginFormCont)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(50, 50, 250, 405))
        self.frame_10.setMinimumSize(QSize(250, 405))
        self.frame_10.setMaximumSize(QSize(16777215, 405))
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_10)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.widget_5 = QWidget(self.frame_10)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy5.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy5)
        self.widget_5.setMinimumSize(QSize(231, 238))
        self.widget_5.setMaximumSize(QSize(231, 238))
        self.verticalLayout_29 = QVBoxLayout(self.widget_5)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.iconeLabel = QLabel(self.widget_5)
        self.iconeLabel.setObjectName(u"iconeLabel")
        self.iconeLabel.setMinimumSize(QSize(60, 60))
        self.iconeLabel.setMaximumSize(QSize(60, 60))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.iconeLabel.setFont(font1)
        self.iconeLabel.setStyleSheet(u"")
        self.iconeLabel.setPixmap(QPixmap(u":/icons/icons/feather/user-circle.svg"))
        self.iconeLabel.setScaledContents(True)
        self.iconeLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.iconeLabel, 0, Qt.AlignHCenter)

        self.usernameLine = QLineEdit(self.widget_5)
        self.usernameLine.setObjectName(u"usernameLine")
        self.usernameLine.setMinimumSize(QSize(200, 40))
        self.usernameLine.setMaximumSize(QSize(200, 40))
        font2 = QFont()
        font2.setPointSize(10)
        self.usernameLine.setFont(font2)
        self.usernameLine.setStyleSheet(u"")

        self.verticalLayout_29.addWidget(self.usernameLine, 0, Qt.AlignHCenter)

        self.passwordLine = QLineEdit(self.widget_5)
        self.passwordLine.setObjectName(u"passwordLine")
        self.passwordLine.setMinimumSize(QSize(200, 40))
        self.passwordLine.setMaximumSize(QSize(200, 40))
        self.passwordLine.setFont(font2)
        self.passwordLine.setEchoMode(QLineEdit.Password)

        self.verticalLayout_29.addWidget(self.passwordLine, 0, Qt.AlignHCenter)


        self.verticalLayout_28.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.frame_10)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(231, 141))
        self.widget_6.setMaximumSize(QSize(231, 141))
        self.verticalLayout_31 = QVBoxLayout(self.widget_6)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.loginButton = QPushButton(self.widget_6)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(200, 40))
        self.loginButton.setMaximumSize(QSize(200, 40))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.loginButton.setFont(font3)

        self.verticalLayout_31.addWidget(self.loginButton, 0, Qt.AlignHCenter)

        self.loginLabel = QLabel(self.widget_6)
        self.loginLabel.setObjectName(u"loginLabel")
        self.loginLabel.setMinimumSize(QSize(162, 25))
        self.loginLabel.setMaximumSize(QSize(162, 25))
        self.loginLabel.setAlignment(Qt.AlignCenter)
        self.loginLabel.setOpenExternalLinks(False)

        self.verticalLayout_31.addWidget(self.loginLabel, 0, Qt.AlignHCenter)

        self.socialFrame = QFrame(self.widget_6)
        self.socialFrame.setObjectName(u"socialFrame")
        self.socialFrame.setMinimumSize(QSize(141, 51))
        self.socialFrame.setMaximumSize(QSize(141, 51))
        self.socialFrame.setFrameShape(QFrame.StyledPanel)
        self.socialFrame.setFrameShadow(QFrame.Raised)
        self.SocialConnectLayout_2 = QHBoxLayout(self.socialFrame)
        self.SocialConnectLayout_2.setSpacing(5)
        self.SocialConnectLayout_2.setObjectName(u"SocialConnectLayout_2")
        self.fbButton = QPushButton(self.socialFrame)
        self.fbButton.setObjectName(u"fbButton")
        self.fbButton.setMaximumSize(QSize(30, 30))
        font4 = QFont()
        font4.setFamily(u"Social Media Circled")
        font4.setPointSize(15)
        self.fbButton.setFont(font4)

        self.SocialConnectLayout_2.addWidget(self.fbButton)

        self.twitterButton = QPushButton(self.socialFrame)
        self.twitterButton.setObjectName(u"twitterButton")
        self.twitterButton.setMaximumSize(QSize(30, 30))
        self.twitterButton.setFont(font4)

        self.SocialConnectLayout_2.addWidget(self.twitterButton)

        self.ytButton = QPushButton(self.socialFrame)
        self.ytButton.setObjectName(u"ytButton")
        self.ytButton.setMaximumSize(QSize(30, 30))
        self.ytButton.setFont(font4)

        self.SocialConnectLayout_2.addWidget(self.ytButton)

        self.linkedinButton = QPushButton(self.socialFrame)
        self.linkedinButton.setObjectName(u"linkedinButton")
        self.linkedinButton.setMaximumSize(QSize(30, 30))
        self.linkedinButton.setFont(font4)

        self.SocialConnectLayout_2.addWidget(self.linkedinButton)


        self.verticalLayout_31.addWidget(self.socialFrame, 0, Qt.AlignHCenter)


        self.verticalLayout_28.addWidget(self.widget_6)


        self.horizontalLayout_14.addWidget(self.loginFormCont)

        self.mainPages.addWidget(self.loginPage)
        self.registerPage = QWidget()
        self.registerPage.setObjectName(u"registerPage")
        self.horizontalLayout_15 = QHBoxLayout(self.registerPage)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.registerFormCont = QWidget(self.registerPage)
        self.registerFormCont.setObjectName(u"registerFormCont")
        self.registerFormCont.setMinimumSize(QSize(311, 461))
        self.registerFormCont.setMaximumSize(QSize(311, 461))
        self.registerFormCont.setStyleSheet(u"QPushButton#registerBtn{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#registerBtn:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#registerBtn:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QPushButton#fbButton_2, #linkedinButton_2, #ytButton_2, #twitterButton_2,  #loginButton_2{	\n"
"	background-color:  transparent;\n"
"	color:rgba(85, 98, 112, 255);\n"
"}\n"
"QPushButton#fbButton_2:hover, #linkedinButton_2:hover, #ytButton_2:hover, #twitterButton_2:hover,  #loginButton_2::hover{	\n"
"	color:rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#fbButton_2:pressed, #linkedinButton_2:pressed, #ytButton_2:pressed, #twitterButton_2:press"
                        "ed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	color:rgba(115, 128, 142, 255);\n"
"}\n"
"\n"
"#socialFrame_2, #pFrame, #frame_12, #vWidget {\n"
"background-color:  transparent;\n"
"}\n"
"\n"
"#lineEdit_Fname, #lineEdit_Lname, #lineEdit_pass, #lineEdit_passVerif, #lineEdit_Email{\n"
"	background-color: transparent;\n"
"    border:none;\n"
"	border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"	color:rgba(255, 255, 255, 230);\n"
"	padding-bottom:7px;\n"
"}\n"
"\n"
"#iconeLabel_adduser{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#label_8, #registerLabel{\n"
"color:rgba(255, 255, 255, 140);\n"
"background-color: transparent;\n"
"}\n"
"")
        self.label_29 = QLabel(self.registerFormCont)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(9, 9, 300, 450))
        self.label_29.setStyleSheet(u"border-image: url(:/images/images/app/background.png);\n"
"border-bottom-right-radius: 50px;")
        self.label_30 = QLabel(self.registerFormCont)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(9, 9, 300, 450))
        self.label_30.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
"border-bottom-right-radius: 50px;")
        self.label_31 = QLabel(self.registerFormCont)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(20, 40, 277, 420))
        self.label_31.setStyleSheet(u"background-color:rgba(0, 0, 0, 100);\n"
"\n"
"border-bottom-right-radius: 50px;")
        self.pFrame = QFrame(self.registerFormCont)
        self.pFrame.setObjectName(u"pFrame")
        self.pFrame.setGeometry(QRect(50, 40, 221, 421))
        self.verticalLayout_33 = QVBoxLayout(self.pFrame)
        self.verticalLayout_33.setSpacing(9)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.iconeLabel_adduser = QLabel(self.pFrame)
        self.iconeLabel_adduser.setObjectName(u"iconeLabel_adduser")
        sizePolicy5.setHeightForWidth(self.iconeLabel_adduser.sizePolicy().hasHeightForWidth())
        self.iconeLabel_adduser.setSizePolicy(sizePolicy5)
        self.iconeLabel_adduser.setMinimumSize(QSize(65, 65))
        self.iconeLabel_adduser.setMaximumSize(QSize(65, 65))
        self.iconeLabel_adduser.setFont(font1)
        self.iconeLabel_adduser.setStyleSheet(u"padding-right: 2px;")
        self.iconeLabel_adduser.setPixmap(QPixmap(u":/icons/icons/feather/user-plus.svg"))
        self.iconeLabel_adduser.setScaledContents(True)
        self.iconeLabel_adduser.setAlignment(Qt.AlignCenter)
        self.iconeLabel_adduser.setMargin(2)
        self.iconeLabel_adduser.setIndent(-1)
        self.iconeLabel_adduser.setOpenExternalLinks(False)

        self.verticalLayout_33.addWidget(self.iconeLabel_adduser, 0, Qt.AlignHCenter)

        self.frame_12 = QFrame(self.pFrame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(204, 41))
        self.frame_12.setMaximumSize(QSize(202, 41))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_37.setSpacing(6)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_Lname = QLineEdit(self.frame_12)
        self.lineEdit_Lname.setObjectName(u"lineEdit_Lname")
        sizePolicy5.setHeightForWidth(self.lineEdit_Lname.sizePolicy().hasHeightForWidth())
        self.lineEdit_Lname.setSizePolicy(sizePolicy5)
        self.lineEdit_Lname.setMinimumSize(QSize(90, 40))
        self.lineEdit_Lname.setMaximumSize(QSize(85, 40))
        self.lineEdit_Lname.setFont(font2)
        self.lineEdit_Lname.setStyleSheet(u"")

        self.horizontalLayout_37.addWidget(self.lineEdit_Lname)

        self.lineEdit_Fname = QLineEdit(self.frame_12)
        self.lineEdit_Fname.setObjectName(u"lineEdit_Fname")
        sizePolicy5.setHeightForWidth(self.lineEdit_Fname.sizePolicy().hasHeightForWidth())
        self.lineEdit_Fname.setSizePolicy(sizePolicy5)
        self.lineEdit_Fname.setMinimumSize(QSize(90, 40))
        self.lineEdit_Fname.setMaximumSize(QSize(85, 40))
        self.lineEdit_Fname.setFont(font2)
        self.lineEdit_Fname.setStyleSheet(u"")

        self.horizontalLayout_37.addWidget(self.lineEdit_Fname)


        self.verticalLayout_33.addWidget(self.frame_12, 0, Qt.AlignHCenter)

        self.lineEdit_Email = QLineEdit(self.pFrame)
        self.lineEdit_Email.setObjectName(u"lineEdit_Email")
        self.lineEdit_Email.setMinimumSize(QSize(190, 40))
        self.lineEdit_Email.setMaximumSize(QSize(190, 40))
        self.lineEdit_Email.setFont(font2)
        self.lineEdit_Email.setStyleSheet(u"")
        self.lineEdit_Email.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_33.addWidget(self.lineEdit_Email, 0, Qt.AlignHCenter)

        self.lineEdit_pass = QLineEdit(self.pFrame)
        self.lineEdit_pass.setObjectName(u"lineEdit_pass")
        self.lineEdit_pass.setMinimumSize(QSize(190, 40))
        self.lineEdit_pass.setMaximumSize(QSize(190, 40))
        self.lineEdit_pass.setFont(font2)
        self.lineEdit_pass.setStyleSheet(u"")
        self.lineEdit_pass.setEchoMode(QLineEdit.Password)

        self.verticalLayout_33.addWidget(self.lineEdit_pass, 0, Qt.AlignHCenter)

        self.lineEdit_passVerif = QLineEdit(self.pFrame)
        self.lineEdit_passVerif.setObjectName(u"lineEdit_passVerif")
        self.lineEdit_passVerif.setMinimumSize(QSize(190, 40))
        self.lineEdit_passVerif.setMaximumSize(QSize(190, 40))
        self.lineEdit_passVerif.setFont(font2)
        self.lineEdit_passVerif.setStyleSheet(u"")
        self.lineEdit_passVerif.setEchoMode(QLineEdit.Password)

        self.verticalLayout_33.addWidget(self.lineEdit_passVerif, 0, Qt.AlignHCenter)

        self.vWidget = QWidget(self.pFrame)
        self.vWidget.setObjectName(u"vWidget")
        self.verticalLayout_34 = QVBoxLayout(self.vWidget)
        self.verticalLayout_34.setSpacing(6)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(-1, 9, -1, 0)
        self.registerBtn = QPushButton(self.vWidget)
        self.registerBtn.setObjectName(u"registerBtn")
        sizePolicy5.setHeightForWidth(self.registerBtn.sizePolicy().hasHeightForWidth())
        self.registerBtn.setSizePolicy(sizePolicy5)
        self.registerBtn.setMinimumSize(QSize(175, 40))
        self.registerBtn.setMaximumSize(QSize(175, 40))
        self.registerBtn.setFont(font3)

        self.verticalLayout_34.addWidget(self.registerBtn, 0, Qt.AlignHCenter)

        self.registerLabel = QLabel(self.vWidget)
        self.registerLabel.setObjectName(u"registerLabel")
        self.registerLabel.setMinimumSize(QSize(189, 25))
        self.registerLabel.setMaximumSize(QSize(189, 25))
        self.registerLabel.setAlignment(Qt.AlignCenter)
        self.registerLabel.setMargin(0)
        self.registerLabel.setOpenExternalLinks(False)

        self.verticalLayout_34.addWidget(self.registerLabel, 0, Qt.AlignHCenter)

        self.socialFrame_2 = QFrame(self.vWidget)
        self.socialFrame_2.setObjectName(u"socialFrame_2")
        sizePolicy5.setHeightForWidth(self.socialFrame_2.sizePolicy().hasHeightForWidth())
        self.socialFrame_2.setSizePolicy(sizePolicy5)
        self.socialFrame_2.setMinimumSize(QSize(145, 40))
        self.socialFrame_2.setMaximumSize(QSize(145, 40))
        self.socialFrame_2.setFrameShape(QFrame.StyledPanel)
        self.socialFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.socialFrame_2)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.fbButton_2 = QPushButton(self.socialFrame_2)
        self.fbButton_2.setObjectName(u"fbButton_2")
        sizePolicy5.setHeightForWidth(self.fbButton_2.sizePolicy().hasHeightForWidth())
        self.fbButton_2.setSizePolicy(sizePolicy5)
        self.fbButton_2.setMinimumSize(QSize(30, 30))
        self.fbButton_2.setMaximumSize(QSize(30, 30))
        self.fbButton_2.setFont(font4)

        self.horizontalLayout_38.addWidget(self.fbButton_2)

        self.twitterButton_2 = QPushButton(self.socialFrame_2)
        self.twitterButton_2.setObjectName(u"twitterButton_2")
        self.twitterButton_2.setMinimumSize(QSize(30, 30))
        self.twitterButton_2.setMaximumSize(QSize(30, 30))
        self.twitterButton_2.setFont(font4)

        self.horizontalLayout_38.addWidget(self.twitterButton_2)

        self.ytButton_2 = QPushButton(self.socialFrame_2)
        self.ytButton_2.setObjectName(u"ytButton_2")
        self.ytButton_2.setMinimumSize(QSize(30, 30))
        self.ytButton_2.setMaximumSize(QSize(30, 30))
        self.ytButton_2.setFont(font4)

        self.horizontalLayout_38.addWidget(self.ytButton_2)

        self.linkedinButton_2 = QPushButton(self.socialFrame_2)
        self.linkedinButton_2.setObjectName(u"linkedinButton_2")
        self.linkedinButton_2.setMinimumSize(QSize(30, 30))
        self.linkedinButton_2.setMaximumSize(QSize(30, 30))
        self.linkedinButton_2.setFont(font4)

        self.horizontalLayout_38.addWidget(self.linkedinButton_2)


        self.verticalLayout_34.addWidget(self.socialFrame_2, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_33.addWidget(self.vWidget, 0, Qt.AlignVCenter)


        self.horizontalLayout_15.addWidget(self.registerFormCont)

        self.mainPages.addWidget(self.registerPage)
        self.profilPage = QWidget()
        self.profilPage.setObjectName(u"profilPage")
        self.profilPage.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.profilPage.sizePolicy().hasHeightForWidth())
        self.profilPage.setSizePolicy(sizePolicy6)
        self.verticalLayout_20 = QVBoxLayout(self.profilPage)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_5 = QScrollArea(self.profilPage)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setEnabled(True)
        self.scrollArea_5.setMinimumSize(QSize(621, 661))
        self.scrollArea_5.setFrameShadow(QFrame.Raised)
        self.scrollArea_5.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_5.setWidgetResizable(True)
        self.profilCont = QWidget()
        self.profilCont.setObjectName(u"profilCont")
        self.profilCont.setEnabled(True)
        self.profilCont.setGeometry(QRect(0, 0, 650, 718))
        sizePolicy6.setHeightForWidth(self.profilCont.sizePolicy().hasHeightForWidth())
        self.profilCont.setSizePolicy(sizePolicy6)
        self.verticalLayout_3 = QVBoxLayout(self.profilCont)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 9, 0)
        self.profilWidget = QWidget(self.profilCont)
        self.profilWidget.setObjectName(u"profilWidget")
        sizePolicy1.setHeightForWidth(self.profilWidget.sizePolicy().hasHeightForWidth())
        self.profilWidget.setSizePolicy(sizePolicy1)
        self.profilWidget.setMinimumSize(QSize(595, 0))
        self.verticalLayout_19 = QVBoxLayout(self.profilWidget)
        self.verticalLayout_19.setSpacing(9)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.profilHeader = QFrame(self.profilWidget)
        self.profilHeader.setObjectName(u"profilHeader")
        sizePolicy1.setHeightForWidth(self.profilHeader.sizePolicy().hasHeightForWidth())
        self.profilHeader.setSizePolicy(sizePolicy1)
        self.profilHeader.setMinimumSize(QSize(501, 111))
        self.profilHeader.setMaximumSize(QSize(16777215, 111))
        self.profilHeader.setFrameShape(QFrame.StyledPanel)
        self.profilHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.profilHeader)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pofilPixFrame = QFrame(self.profilHeader)
        self.pofilPixFrame.setObjectName(u"pofilPixFrame")
        sizePolicy5.setHeightForWidth(self.pofilPixFrame.sizePolicy().hasHeightForWidth())
        self.pofilPixFrame.setSizePolicy(sizePolicy5)
        self.pofilPixFrame.setStyleSheet(u"background-color: transparent;")
        self.verticalLayout_9 = QVBoxLayout(self.pofilPixFrame)
        self.verticalLayout_9.setSpacing(9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(9, 0, 0, 0)
        self.profilPixLabel = QLabel(self.pofilPixFrame)
        self.profilPixLabel.setObjectName(u"profilPixLabel")
        sizePolicy5.setHeightForWidth(self.profilPixLabel.sizePolicy().hasHeightForWidth())
        self.profilPixLabel.setSizePolicy(sizePolicy5)
        self.profilPixLabel.setMinimumSize(QSize(80, 80))
        self.profilPixLabel.setMaximumSize(QSize(80, 80))
        self.profilPixLabel.setStyleSheet(u"")
        self.profilPixLabel.setPixmap(QPixmap(u":/images/images/profile/circled3.png"))
        self.profilPixLabel.setScaledContents(True)

        self.verticalLayout_9.addWidget(self.profilPixLabel)


        self.horizontalLayout_11.addWidget(self.pofilPixFrame)

        self.frame_45 = QFrame(self.profilHeader)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy3.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy3)
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_45)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 9)
        self.label_74 = QLabel(self.frame_45)
        self.label_74.setObjectName(u"label_74")

        self.verticalLayout_8.addWidget(self.label_74)

        self.pushButton_60 = QPushButton(self.frame_45)
        self.pushButton_60.setObjectName(u"pushButton_60")
        sizePolicy5.setHeightForWidth(self.pushButton_60.sizePolicy().hasHeightForWidth())
        self.pushButton_60.setSizePolicy(sizePolicy5)
        self.pushButton_60.setMinimumSize(QSize(157, 0))
        self.pushButton_60.setStyleSheet(u"border: 1px solid #555;\n"
"padding: 3px 5px;\n"
"font-weight: bold;\n"
"border-radius: 5px;\n"
"background-color: #2C2828")

        self.verticalLayout_8.addWidget(self.pushButton_60)


        self.horizontalLayout_11.addWidget(self.frame_45)

        self.horizontalSpacer = QSpacerItem(148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.frame_66 = QFrame(self.profilHeader)
        self.frame_66.setObjectName(u"frame_66")
        sizePolicy5.setHeightForWidth(self.frame_66.sizePolicy().hasHeightForWidth())
        self.frame_66.setSizePolicy(sizePolicy5)
        self.frame_66.setMinimumSize(QSize(41, 0))
        self.frame_66.setMaximumSize(QSize(41, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.frame_66)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, -1)
        self.profilActionBtn = QPushButton(self.frame_66)
        self.profilActionBtn.setObjectName(u"profilActionBtn")
        sizePolicy5.setHeightForWidth(self.profilActionBtn.sizePolicy().hasHeightForWidth())
        self.profilActionBtn.setSizePolicy(sizePolicy5)
        self.profilActionBtn.setMinimumSize(QSize(36, 0))
        self.profilActionBtn.setMaximumSize(QSize(36, 50))
        self.profilActionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.profilActionBtn.setLayoutDirection(Qt.LeftToRight)
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/feather/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profilActionBtn.setIcon(icon13)
        self.profilActionBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.profilActionBtn)

        self.verticalSpacer_2 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_11.addWidget(self.frame_66)

        self.Frame_77 = QFrame(self.profilHeader)
        self.Frame_77.setObjectName(u"Frame_77")
        self.verticalLayout_4 = QVBoxLayout(self.Frame_77)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.profilEdit = QCustomSlideMenu(self.Frame_77)
        self.profilEdit.setObjectName(u"profilEdit")
        sizePolicy3.setHeightForWidth(self.profilEdit.sizePolicy().hasHeightForWidth())
        self.profilEdit.setSizePolicy(sizePolicy3)
        self.profilEdit.setMaximumSize(QSize(100, 82))
        self.profilEdit.setStyleSheet(u"*{\n"
"padding: 3px 5px;\n"
"font-weight: bold;\n"
"border-radius: 10px;\n"
"background-color: #2C2828\n"
"}\n"
"\n"
"\n"
"QPushButton#editBtn:hover, #securityBtn:hover, #editPostBtn::hover{	\n"
"background-color:  rgba(138, 138, 138, 100);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#editBtn:pressed, #securityBtn:pressed, #editPostBtn::pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(138, 138, 138, 100);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.profilEdit)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.editBtn = QPushButton(self.profilEdit)
        self.editBtn.setObjectName(u"editBtn")
        sizePolicy5.setHeightForWidth(self.editBtn.sizePolicy().hasHeightForWidth())
        self.editBtn.setSizePolicy(sizePolicy5)
        self.editBtn.setMinimumSize(QSize(80, 25))
        self.editBtn.setMaximumSize(QSize(101, 25))
        self.editBtn.setLayoutDirection(Qt.LeftToRight)
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/feather/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editBtn.setIcon(icon14)

        self.verticalLayout_2.addWidget(self.editBtn)

        self.editPostBtn = QPushButton(self.profilEdit)
        self.editPostBtn.setObjectName(u"editPostBtn")
        self.editPostBtn.setMinimumSize(QSize(80, 25))
        self.editPostBtn.setMaximumSize(QSize(101, 25))
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/feather/tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editPostBtn.setIcon(icon15)

        self.verticalLayout_2.addWidget(self.editPostBtn)

        self.securityBtn = QPushButton(self.profilEdit)
        self.securityBtn.setObjectName(u"securityBtn")
        sizePolicy5.setHeightForWidth(self.securityBtn.sizePolicy().hasHeightForWidth())
        self.securityBtn.setSizePolicy(sizePolicy5)
        self.securityBtn.setMinimumSize(QSize(80, 25))
        self.securityBtn.setMaximumSize(QSize(101, 25))
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/feather/lock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.securityBtn.setIcon(icon16)

        self.verticalLayout_2.addWidget(self.securityBtn)


        self.verticalLayout_4.addWidget(self.profilEdit)

        self.verticalSpacer_4 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.horizontalLayout_11.addWidget(self.Frame_77)


        self.verticalLayout_19.addWidget(self.profilHeader)

        self.FFL_Frame = QFrame(self.profilWidget)
        self.FFL_Frame.setObjectName(u"FFL_Frame")
        sizePolicy5.setHeightForWidth(self.FFL_Frame.sizePolicy().hasHeightForWidth())
        self.FFL_Frame.setSizePolicy(sizePolicy5)
        self.FFL_Frame.setMinimumSize(QSize(375, 0))
        self.FFL_Frame.setMaximumSize(QSize(417, 16777215))
        self.FFL_Frame.setFrameShape(QFrame.StyledPanel)
        self.FFL_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.FFL_Frame)
        self.horizontalLayout_41.setSpacing(6)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(9, 0, 0, 0)
        self.label_99 = QLabel(self.FFL_Frame)
        self.label_99.setObjectName(u"label_99")

        self.horizontalLayout_41.addWidget(self.label_99)

        self.label_100 = QLabel(self.FFL_Frame)
        self.label_100.setObjectName(u"label_100")

        self.horizontalLayout_41.addWidget(self.label_100)

        self.label_101 = QLabel(self.FFL_Frame)
        self.label_101.setObjectName(u"label_101")

        self.horizontalLayout_41.addWidget(self.label_101)


        self.verticalLayout_19.addWidget(self.FFL_Frame)

        self.bioFrame = QFrame(self.profilWidget)
        self.bioFrame.setObjectName(u"bioFrame")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.bioFrame.sizePolicy().hasHeightForWidth())
        self.bioFrame.setSizePolicy(sizePolicy7)
        self.bioFrame.setMinimumSize(QSize(577, 0))
        self.bioFrame.setFrameShape(QFrame.StyledPanel)
        self.bioFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.bioFrame)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(9, 0, 0, 0)
        self.bioLabel = QLabel(self.bioFrame)
        self.bioLabel.setObjectName(u"bioLabel")
        sizePolicy3.setHeightForWidth(self.bioLabel.sizePolicy().hasHeightForWidth())
        self.bioLabel.setSizePolicy(sizePolicy3)
        self.bioLabel.setWordWrap(True)

        self.verticalLayout_89.addWidget(self.bioLabel)


        self.verticalLayout_19.addWidget(self.bioFrame)

        self.tabWidget_2 = QTabWidget(self.profilWidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy1.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy1)
        self.tabWidget_2.setMinimumSize(QSize(585, 434))
        self.tabWidget_2.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget_2.setIconSize(QSize(24, 24))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        sizePolicy6.setHeightForWidth(self.tab_3.sizePolicy().hasHeightForWidth())
        self.tab_3.setSizePolicy(sizePolicy6)
        self.tab_3.setMinimumSize(QSize(500, 0))
        font5 = QFont()
        font5.setKerning(True)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.tab_3.setFont(font5)
        self.gridLayoutWidget = QWidget(self.tab_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 611, 391))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setSpacing(9)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_4.setContentsMargins(9, 9, 9, 9)
        self.tabWidget_2.addTab(self.tab_3, icon11, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/feather/heart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget_2.addTab(self.tab_4, icon17, "")

        self.verticalLayout_19.addWidget(self.tabWidget_2)


        self.verticalLayout_3.addWidget(self.profilWidget)

        self.scrollArea_5.setWidget(self.profilCont)

        self.verticalLayout_20.addWidget(self.scrollArea_5)

        self.mainPages.addWidget(self.profilPage)
        self.livePage = QWidget()
        self.livePage.setObjectName(u"livePage")
        self.label_69 = QLabel(self.livePage)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(181, 300, 288, 117))
        self.mainPages.addWidget(self.livePage)
        self.followingfPage = QWidget()
        self.followingfPage.setObjectName(u"followingfPage")
        self.horizontalLayout_33 = QHBoxLayout(self.followingfPage)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_16 = QLabel(self.followingfPage)
        self.label_16.setObjectName(u"label_16")
        font6 = QFont()
        font6.setPointSize(42)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_16.setFont(font6)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_16)

        self.mainPages.addWidget(self.followingfPage)
        self.profilEditPage = QWidget()
        self.profilEditPage.setObjectName(u"profilEditPage")
        self.profilEditPage.setStyleSheet(u"")
        self.horizontalLayout_17 = QHBoxLayout(self.profilEditPage)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.profilEditWidget = QWidget(self.profilEditPage)
        self.profilEditWidget.setObjectName(u"profilEditWidget")
        sizePolicy5.setHeightForWidth(self.profilEditWidget.sizePolicy().hasHeightForWidth())
        self.profilEditWidget.setSizePolicy(sizePolicy5)
        self.profilEditWidget.setStyleSheet(u"*{\n"
"border: 1px solid #555;\n"
"padding: 3px 5px;\n"
"font-weight: bold;\n"
"border-radius: 10px;\n"
"background-color:  #2C2828;\n"
"/** qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2C2828, stop:1 rgba(0, 0, 0, 255));**/\n"
"}\n"
"\n"
"#firstnameQline, #lastnameQline, #emailQline, #usernameQline, #stateQline, #countryQline, #phoneQline, #StateQline, #femaleBox, #maleBox, #biotextEdit{\n"
"	border-radius: 5px;\n"
"	color:rgba(255, 255, 255, 150);\n"
"	padding-bottom:4px;\n"
"	background-color: #2C2828;\n"
"}\n"
"\n"
"\n"
"#verticalFrame_2, #horizontalWidget, #horizontalFrame, #horizontalFrame_1, #horizontalFrame_2, #horizontalFrame_3, #horizontalFrame_4{\n"
"background-color: none;\n"
"border : none;\n"
"}\n"
"\n"
"#saveBtn, #CancelBtn{	\n"
"border: 1px solid #555;\n"
"font-weight: bold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254, 44, 85, 100), stop:1 rgba(0, 0, 0, 255));\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"}\n"
"#saveBtn::hover, #Cance"
                        "lBtn::hover{	\n"
"font-weight: bold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254, 44, 85, 150), stop:1 rgba(0, 0, 0, 255));\n"
"}\n"
"\n"
"#saveBtn::pressed, #CancelBtn::pressed{	\n"
"font-weight: bold;\n"
"padding-left:10px;\n"
"padding-top:5px;\n"
"background-color: #2C2828;\n"
"}\n"
"\n"
"#frame_4, #frame_8{\n"
"border: none; background-color: none;\n"
"}\n"
"\n"
"#edithumbnailBtn{\n"
"	background-color: #2C2828;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#edithumbnailBtn:hover{\n"
"	background-color:transparent;\n"
"    border-top:none;	\n"
"}\n"
"#edithumbnailBtn:pressed{\n"
"	background-color: #2C2828;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#formFrame{\n"
"border-radius: 10px;\n"
"border: 1px solid #555;\n"
"background-color: rgb(14, 15, 18);\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.profilEditWidget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.formFrame = QWidget(self.profilEditWidget)
        self.formFrame.setObjectName(u"formFrame")
        sizePolicy5.setHeightForWidth(self.formFrame.sizePolicy().hasHeightForWidth())
        self.formFrame.setSizePolicy(sizePolicy5)
        self.formFrame.setMinimumSize(QSize(431, 521))
        self.formFrame.setMaximumSize(QSize(16777215, 16777215))
        self.formFrame.setLayoutDirection(Qt.LeftToRight)
        self.formFrame.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.formFrame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalWidget = QWidget(self.formFrame)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy5.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy5)
        self.horizontalWidget.setStyleSheet(u"")
        self.horizontalLayout_22 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.frame_4 = QFrame(self.horizontalWidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy7.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy7)
        self.frame_4.setMinimumSize(QSize(110, 150))
        self.frame_4.setMaximumSize(QSize(110, 150))
        self.frame_4.setLayoutDirection(Qt.LeftToRight)
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_13 = QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 12, 0, 20)
        self.avatarLabel = QLabel(self.frame_4)
        self.avatarLabel.setObjectName(u"avatarLabel")
        self.avatarLabel.setMinimumSize(QSize(100, 100))
        self.avatarLabel.setMaximumSize(QSize(100, 100))
        self.avatarLabel.setStyleSheet(u"")
        self.avatarLabel.setPixmap(QPixmap(u":/images/images/profile/circled3.png"))
        self.avatarLabel.setScaledContents(True)
        self.avatarLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.avatarLabel)

        self.edithumbnailBtn = QPushButton(self.frame_4)
        self.edithumbnailBtn.setObjectName(u"edithumbnailBtn")
        sizePolicy5.setHeightForWidth(self.edithumbnailBtn.sizePolicy().hasHeightForWidth())
        self.edithumbnailBtn.setSizePolicy(sizePolicy5)
        self.edithumbnailBtn.setMinimumSize(QSize(100, 25))
        self.edithumbnailBtn.setMaximumSize(QSize(100, 100))
        self.edithumbnailBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.edithumbnailBtn.setStyleSheet(u"")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/feather/edit-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.edithumbnailBtn.setIcon(icon18)

        self.verticalLayout_13.addWidget(self.edithumbnailBtn)


        self.horizontalLayout_22.addWidget(self.frame_4)

        self.verticalFrame_2 = QFrame(self.horizontalWidget)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        sizePolicy5.setHeightForWidth(self.verticalFrame_2.sizePolicy().hasHeightForWidth())
        self.verticalFrame_2.setSizePolicy(sizePolicy5)
        self.verticalFrame_2.setMinimumSize(QSize(275, 114))
        self.verticalFrame_2.setMaximumSize(QSize(275, 114))
        self.verticalFrame_2.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.verticalFrame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setContentsMargins(9, 9, 9, 0)
        self.biotextEdit = QTextEdit(self.verticalFrame_2)
        self.biotextEdit.setObjectName(u"biotextEdit")
        sizePolicy5.setHeightForWidth(self.biotextEdit.sizePolicy().hasHeightForWidth())
        self.biotextEdit.setSizePolicy(sizePolicy5)
        self.biotextEdit.setMinimumSize(QSize(251, 51))
        self.biotextEdit.setMaximumSize(QSize(251, 51))

        self.gridLayout.addWidget(self.biotextEdit, 2, 0, 1, 1)

        self.usernameQline = QLineEdit(self.verticalFrame_2)
        self.usernameQline.setObjectName(u"usernameQline")
        self.usernameQline.setMaximumSize(QSize(141, 16777215))
        self.usernameQline.setMaxLength(40)
        self.usernameQline.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.usernameQline, 0, 0, 1, 1)

        self.maleBox = QRadioButton(self.verticalFrame_2)
        self.maleBox.setObjectName(u"maleBox")
        sizePolicy5.setHeightForWidth(self.maleBox.sizePolicy().hasHeightForWidth())
        self.maleBox.setSizePolicy(sizePolicy5)
        self.maleBox.setMinimumSize(QSize(0, 25))
        self.maleBox.setMaximumSize(QSize(50, 25))
        self.maleBox.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.maleBox, 0, 1, 1, 1)

        self.femaleBox = QRadioButton(self.verticalFrame_2)
        self.femaleBox.setObjectName(u"femaleBox")
        self.femaleBox.setMinimumSize(QSize(0, 25))
        self.femaleBox.setMaximumSize(QSize(50, 25))

        self.gridLayout.addWidget(self.femaleBox, 0, 2, 1, 1)


        self.horizontalLayout_22.addWidget(self.verticalFrame_2)


        self.verticalLayout_14.addWidget(self.horizontalWidget)

        self.horizontalFrame = QFrame(self.formFrame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy7.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy7)
        self.horizontalLayout_20 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.firstnameQline = QLineEdit(self.horizontalFrame)
        self.firstnameQline.setObjectName(u"firstnameQline")
        self.firstnameQline.setMinimumSize(QSize(0, 0))
        self.firstnameQline.setMaximumSize(QSize(141, 16777215))
        self.firstnameQline.setFocusPolicy(Qt.WheelFocus)
        self.firstnameQline.setMaxLength(32767)
        self.firstnameQline.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.firstnameQline.setClearButtonEnabled(True)

        self.horizontalLayout_20.addWidget(self.firstnameQline)

        self.lastnameQline = QLineEdit(self.horizontalFrame)
        self.lastnameQline.setObjectName(u"lastnameQline")
        self.lastnameQline.setMaximumSize(QSize(141, 16777215))
        self.lastnameQline.setMaxLength(10)
        self.lastnameQline.setClearButtonEnabled(True)

        self.horizontalLayout_20.addWidget(self.lastnameQline)


        self.verticalLayout_14.addWidget(self.horizontalFrame)

        self.horizontalFrame_4 = QFrame(self.formFrame)
        self.horizontalFrame_4.setObjectName(u"horizontalFrame_4")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.horizontalFrame_4.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_4.setSizePolicy(sizePolicy8)
        self.horizontalFrame_4.setMaximumSize(QSize(16777215, 49))
        self.horizontalLayout_23 = QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.emailQline = QLineEdit(self.horizontalFrame_4)
        self.emailQline.setObjectName(u"emailQline")
        self.emailQline.setMinimumSize(QSize(250, 25))
        self.emailQline.setMaximumSize(QSize(250, 25))
        self.emailQline.setMaxLength(25)
        self.emailQline.setDragEnabled(False)
        self.emailQline.setReadOnly(False)
        self.emailQline.setClearButtonEnabled(False)

        self.horizontalLayout_23.addWidget(self.emailQline)


        self.verticalLayout_14.addWidget(self.horizontalFrame_4)

        self.horizontalFrame_1 = QFrame(self.formFrame)
        self.horizontalFrame_1.setObjectName(u"horizontalFrame_1")
        sizePolicy7.setHeightForWidth(self.horizontalFrame_1.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_1.setSizePolicy(sizePolicy7)
        self.horizontalLayout_21 = QHBoxLayout(self.horizontalFrame_1)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.stateQline = QLineEdit(self.horizontalFrame_1)
        self.stateQline.setObjectName(u"stateQline")
        self.stateQline.setMaximumSize(QSize(141, 16777215))
        self.stateQline.setMaxLength(15)
        self.stateQline.setClearButtonEnabled(True)

        self.horizontalLayout_21.addWidget(self.stateQline)

        self.countryQline = QLineEdit(self.horizontalFrame_1)
        self.countryQline.setObjectName(u"countryQline")
        self.countryQline.setMaximumSize(QSize(141, 16777215))
        self.countryQline.setMaxLength(15)
        self.countryQline.setClearButtonEnabled(True)

        self.horizontalLayout_21.addWidget(self.countryQline)


        self.verticalLayout_14.addWidget(self.horizontalFrame_1)

        self.horizontalFrame_3 = QFrame(self.formFrame)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        sizePolicy7.setHeightForWidth(self.horizontalFrame_3.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_3.setSizePolicy(sizePolicy7)
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.phoneQline = QLineEdit(self.horizontalFrame_3)
        self.phoneQline.setObjectName(u"phoneQline")
        self.phoneQline.setMinimumSize(QSize(250, 25))
        self.phoneQline.setMaximumSize(QSize(250, 25))
        self.phoneQline.setMaxLength(16)
        self.phoneQline.setClearButtonEnabled(True)

        self.horizontalLayout_19.addWidget(self.phoneQline)


        self.verticalLayout_14.addWidget(self.horizontalFrame_3)

        self.horizontalFrame_2 = QFrame(self.formFrame)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        sizePolicy3.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy3)
        self.horizontalFrame_2.setStyleSheet(u"")
        self.horizontalLayout_24 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 0, -1, 0)
        self.CancelBtn = QPushButton(self.horizontalFrame_2)
        self.CancelBtn.setObjectName(u"CancelBtn")
        self.CancelBtn.setMinimumSize(QSize(100, 25))
        self.CancelBtn.setMaximumSize(QSize(110, 31))
        font7 = QFont()
        font7.setPointSize(8)
        font7.setBold(True)
        font7.setItalic(False)
        font7.setWeight(75)
        self.CancelBtn.setFont(font7)
        self.CancelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.CancelBtn.setStyleSheet(u"")
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/feather/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CancelBtn.setIcon(icon19)
        self.CancelBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_24.addWidget(self.CancelBtn)

        self.saveBtn = QPushButton(self.horizontalFrame_2)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setMinimumSize(QSize(100, 25))
        self.saveBtn.setMaximumSize(QSize(110, 31))
        self.saveBtn.setFont(font7)
        self.saveBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveBtn.setLayoutDirection(Qt.LeftToRight)
        self.saveBtn.setStyleSheet(u"")
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons/feather/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveBtn.setIcon(icon20)
        self.saveBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_24.addWidget(self.saveBtn)


        self.verticalLayout_14.addWidget(self.horizontalFrame_2)


        self.horizontalLayout_12.addWidget(self.formFrame)


        self.horizontalLayout_17.addWidget(self.profilEditWidget)

        self.mainPages.addWidget(self.profilEditPage)
        self.uploadPage = QWidget()
        self.uploadPage.setObjectName(u"uploadPage")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.uploadPage.sizePolicy().hasHeightForWidth())
        self.uploadPage.setSizePolicy(sizePolicy9)
        self.horizontalLayout_32 = QHBoxLayout(self.uploadPage)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.profilEditWidget_2 = QWidget(self.uploadPage)
        self.profilEditWidget_2.setObjectName(u"profilEditWidget_2")
        sizePolicy5.setHeightForWidth(self.profilEditWidget_2.sizePolicy().hasHeightForWidth())
        self.profilEditWidget_2.setSizePolicy(sizePolicy5)
        self.profilEditWidget_2.setStyleSheet(u"*{\n"
"border: 1px solid #555;\n"
"padding: 3px 5px;\n"
"font-weight: bold;\n"
"border-radius: 10px;\n"
"background-color:  #2C2828;\n"
"/** qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2C2828, stop:1 rgba(0, 0, 0, 255));**/\n"
"}\n"
"\n"
"#titleQline, #legendTextEdit, #pathLabel {\n"
"	border-radius: 5px;\n"
"	color:rgba(255, 255, 255, 150);\n"
"	padding-bottom:4px;\n"
"	background-color: #2C2828;\n"
"}\n"
"\n"
"#horizontalWidget_2, #horizontalFrame_8, #horizontalFrame_9, #horizontalFrame_2, #horizontalFrame_3, #horizontalFrame_4{\n"
"background-color: none;\n"
"border : none;\n"
"}\n"
"\n"
"#uploadFileBtn, #addFileBtn{	\n"
"border: 1px solid #555;\n"
"font-weight: bold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254, 44, 85, 100), stop:1 rgba(0, 0, 0, 255));\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"}\n"
"#uploadFileBtn::hover{	\n"
"font-weight: bold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254, 44, 85"
                        ", 150), stop:1 rgba(0, 0, 0, 255));\n"
"}\n"
"\n"
"#uploadFileBtn::pressed{	\n"
"font-weight: bold;\n"
"padding-left:10px;\n"
"padding-top:5px;\n"
"background-color: #2C2828;\n"
"}\n"
"\n"
"\n"
"\n"
"#horizontalFrame_5{\n"
"	background-color: transparent;\n"
"    border: none;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#addFileBtn:hover{\n"
"border: 1px solid #555;\n"
"	border-radius: 8px;\n"
"	color:rgba(255, 255, 255, 150);\n"
"\n"
"	background-color: #2C2828;\n"
"}\n"
"#addFileBtn:pressed{\n"
"border: 1px solid #555;\n"
"padding-left:6px;\n"
"padding-top:4px;\n"
"		border-radius: 8px;\n"
"\n"
"	background-color: #2C2828;\n"
"}\n"
"\n"
"#formFrame_2{\n"
"border-radius: 10px;\n"
"border: 1px solid #555;\n"
"background-color: rgb(14, 15, 18);\n"
"}")
        self.verticalLayout_22 = QVBoxLayout(self.profilEditWidget_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.formFrame_2 = QWidget(self.profilEditWidget_2)
        self.formFrame_2.setObjectName(u"formFrame_2")
        sizePolicy5.setHeightForWidth(self.formFrame_2.sizePolicy().hasHeightForWidth())
        self.formFrame_2.setSizePolicy(sizePolicy5)
        self.formFrame_2.setMinimumSize(QSize(370, 300))
        self.formFrame_2.setMaximumSize(QSize(16777215, 16777215))
        self.formFrame_2.setLayoutDirection(Qt.LeftToRight)
        self.formFrame_2.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.formFrame_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalWidget_2 = QWidget(self.formFrame_2)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        sizePolicy3.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy3)
        self.horizontalWidget_2.setMinimumSize(QSize(341, 0))
        self.horizontalWidget_2.setLayoutDirection(Qt.LeftToRight)
        self.horizontalWidget_2.setStyleSheet(u"")
        self.horizontalLayout_29 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, 0, -1, 0)
        self.titleQline = QLineEdit(self.horizontalWidget_2)
        self.titleQline.setObjectName(u"titleQline")
        self.titleQline.setMaximumSize(QSize(331, 16777215))
        self.titleQline.setLayoutDirection(Qt.LeftToRight)
        self.titleQline.setMaxLength(40)
        self.titleQline.setClearButtonEnabled(True)

        self.horizontalLayout_29.addWidget(self.titleQline)


        self.verticalLayout_17.addWidget(self.horizontalWidget_2)

        self.horizontalFrame_5 = QFrame(self.formFrame_2)
        self.horizontalFrame_5.setObjectName(u"horizontalFrame_5")
        self.horizontalLayout_31 = QHBoxLayout(self.horizontalFrame_5)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, -1, 0, -1)
        self.legendTextEdit = QTextEdit(self.horizontalFrame_5)
        self.legendTextEdit.setObjectName(u"legendTextEdit")
        sizePolicy3.setHeightForWidth(self.legendTextEdit.sizePolicy().hasHeightForWidth())
        self.legendTextEdit.setSizePolicy(sizePolicy3)
        self.legendTextEdit.setMinimumSize(QSize(251, 51))
        self.legendTextEdit.setMaximumSize(QSize(331, 71))

        self.horizontalLayout_31.addWidget(self.legendTextEdit)


        self.verticalLayout_17.addWidget(self.horizontalFrame_5)

        self.horizontalFrame_8 = QFrame(self.formFrame_2)
        self.horizontalFrame_8.setObjectName(u"horizontalFrame_8")
        sizePolicy7.setHeightForWidth(self.horizontalFrame_8.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_8.setSizePolicy(sizePolicy7)
        self.horizontalLayout_30 = QHBoxLayout(self.horizontalFrame_8)
        self.horizontalLayout_30.setSpacing(9)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, -1, -1, 9)
        self.pathLabel = QLabel(self.horizontalFrame_8)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.pathLabel.sizePolicy().hasHeightForWidth())
        self.pathLabel.setSizePolicy(sizePolicy5)
        self.pathLabel.setMaximumSize(QSize(241, 16777215))
        self.pathLabel.setAcceptDrops(False)
        self.pathLabel.setLayoutDirection(Qt.LeftToRight)
        self.pathLabel.setScaledContents(True)
        self.pathLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.pathLabel)

        self.addFileBtn = QPushButton(self.horizontalFrame_8)
        self.addFileBtn.setObjectName(u"addFileBtn")
        sizePolicy5.setHeightForWidth(self.addFileBtn.sizePolicy().hasHeightForWidth())
        self.addFileBtn.setSizePolicy(sizePolicy5)
        self.addFileBtn.setMinimumSize(QSize(56, 29))
        self.addFileBtn.setMaximumSize(QSize(16777215, 16777215))
        self.addFileBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addFileBtn.setStyleSheet(u"")
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons/feather/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addFileBtn.setIcon(icon21)
        self.addFileBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_30.addWidget(self.addFileBtn)


        self.verticalLayout_17.addWidget(self.horizontalFrame_8)

        self.horizontalFrame_9 = QFrame(self.formFrame_2)
        self.horizontalFrame_9.setObjectName(u"horizontalFrame_9")
        sizePolicy3.setHeightForWidth(self.horizontalFrame_9.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_9.setSizePolicy(sizePolicy3)
        self.horizontalFrame_9.setMinimumSize(QSize(351, 0))
        self.horizontalFrame_9.setStyleSheet(u"")
        self.horizontalLayout_25 = QHBoxLayout(self.horizontalFrame_9)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.uploadFileBtn = QPushButton(self.horizontalFrame_9)
        self.uploadFileBtn.setObjectName(u"uploadFileBtn")
        self.uploadFileBtn.setMinimumSize(QSize(100, 25))
        self.uploadFileBtn.setMaximumSize(QSize(106, 25))
        self.uploadFileBtn.setFont(font7)
        self.uploadFileBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.uploadFileBtn.setLayoutDirection(Qt.LeftToRight)
        self.uploadFileBtn.setStyleSheet(u"")
        icon22 = QIcon()
        icon22.addFile(u":/icons/icons/feather/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.uploadFileBtn.setIcon(icon22)
        self.uploadFileBtn.setIconSize(QSize(18, 18))
        self.uploadFileBtn.setFlat(False)

        self.horizontalLayout_25.addWidget(self.uploadFileBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_17.addWidget(self.horizontalFrame_9)


        self.verticalLayout_22.addWidget(self.formFrame_2)


        self.horizontalLayout_32.addWidget(self.profilEditWidget_2)

        self.mainPages.addWidget(self.uploadPage)
        self.editPostPage = QWidget()
        self.editPostPage.setObjectName(u"editPostPage")
        sizePolicy5.setHeightForWidth(self.editPostPage.sizePolicy().hasHeightForWidth())
        self.editPostPage.setSizePolicy(sizePolicy5)
        self.editPostPage.setStyleSheet(u"#nextBtn, #prevBtn{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"border: 1px solid #555;\n"
"}\n"
"#nextBtn::pressed{	\n"
"padding-left:5px;\n"
"padding-top:2px;\n"
"}\n"
"#prevBtn::pressed{\n"
"padding-right:5px;\n"
"padding-top:2px;\n"
"}\n"
"")
        self.horizontalLayout_18 = QHBoxLayout(self.editPostPage)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.prevBtn = QPushButton(self.editPostPage)
        self.prevBtn.setObjectName(u"prevBtn")
        self.prevBtn.setMinimumSize(QSize(31, 28))
        self.prevBtn.setMaximumSize(QSize(31, 28))
        icon23 = QIcon()
        icon23.addFile(u":/icons/icons/feather/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.prevBtn.setIcon(icon23)

        self.horizontalLayout_18.addWidget(self.prevBtn)

        self.editPostWidget = QCustomStackedWidget(self.editPostPage)
        self.editPostWidget.setObjectName(u"editPostWidget")
        self.editPostWidget.setMinimumSize(QSize(580, 480))
        self.editPostWidget.setMaximumSize(QSize(580, 480))
        self.editPostWidget.setStyleSheet(u"#editPostWidget{\n"
"border: 1px solid #555;\n"
"padding: 3px 5px;\n"
"font-weight: bold;\n"
"border-radius: 10px;\n"
"background-color:  #2C2828;\n"
"/** qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2C2828, stop:1 rgba(0, 0, 0, 255));**/\n"
"}")

        self.horizontalLayout_18.addWidget(self.editPostWidget)

        self.nextBtn = QPushButton(self.editPostPage)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setMinimumSize(QSize(31, 28))
        self.nextBtn.setMaximumSize(QSize(31, 28))
        icon24 = QIcon()
        icon24.addFile(u":/icons/icons/feather/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nextBtn.setIcon(icon24)

        self.horizontalLayout_18.addWidget(self.nextBtn)

        self.mainPages.addWidget(self.editPostPage)
        self.securityPage = QWidget()
        self.securityPage.setObjectName(u"securityPage")
        self.securityPage.setStyleSheet(u"#widget_4{\n"
"background-color:  #2C2828;\n"
"border-radius: 10px;\n"
"}\n"
"#verticalWidget{\n"
"border: 1px solid #555;\n"
"padding: 3px 5px;\n"
"font-weight: bold;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"#ancienpass, #newpass {\n"
"	border-radius: 5px;\n"
"	color:rgba(255, 255, 255, 150);\n"
"	background-color: #2C2828;\n"
"    border: 1px solid #555;\n"
"	padding: 3px 5px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#verticalFrame, #horizontalFrame_7, #horizontalFrame_6{\n"
"background-color: transparent;\n"
"border : none;\n"
"}\n"
"\n"
"#savePassBtn, #backBtn2{	\n"
"border: 1px solid #555;\n"
"font-weight: bold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254, 44, 85, 100), stop:1 rgba(0, 0, 0, 255));\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"\n"
"}\n"
"#savePassBtn::hover, #backBtn2::hover{	\n"
"font-weight: bold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254, 44, 85, 150), stop:1 rgba(0, 0, 0, 255));\n"
"}\n"
"\n"
"#s"
                        "avePassBtn::pressed, #backBtn2::pressed{	\n"
"font-weight: bold;\n"
"padding-left:10px;\n"
"padding-top:5px;\n"
"background-color: #2C2828;\n"
"}\n"
"\n"
"#deleteAccountBtn{\n"
"border: 1px solid #555;\n"
"font-weight: bold;\n"
"background-color: rgba(254, 44, 85, 100);\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"}\n"
"\n"
"\n"
"#deleteAccountBtn:hover{\n"
"font-weight: bold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254, 44, 85, 150), stop:1 rgba(0, 0, 0, 255));\n"
"\n"
"}\n"
"#deleteAccountBtn:pressed{\n"
"border: 1px solid #555;\n"
"padding-left:6px;\n"
"padding-top:4px;\n"
"		border-radius: 8px;\n"
"\n"
"	background-color: #2C2828;\n"
"}\n"
"")
        self.horizontalLayout_28 = QHBoxLayout(self.securityPage)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.widget_4 = QWidget(self.securityPage)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(441, 351))
        self.widget_4.setStyleSheet(u"")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalWidget = QWidget(self.widget_4)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy5.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy5)
        self.verticalWidget.setMinimumSize(QSize(421, 331))
        self.verticalWidget.setMaximumSize(QSize(421, 331))
        self.verticalWidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_11 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalFrame = QFrame(self.verticalWidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        sizePolicy3.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy3)
        self.verticalLayout_6 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ancienpass = QLineEdit(self.verticalFrame)
        self.ancienpass.setObjectName(u"ancienpass")
        self.ancienpass.setClearButtonEnabled(True)

        self.verticalLayout_6.addWidget(self.ancienpass)

        self.newpass = QLineEdit(self.verticalFrame)
        self.newpass.setObjectName(u"newpass")
        self.newpass.setClearButtonEnabled(True)

        self.verticalLayout_6.addWidget(self.newpass)


        self.verticalLayout_11.addWidget(self.verticalFrame)

        self.horizontalFrame_7 = QFrame(self.verticalWidget)
        self.horizontalFrame_7.setObjectName(u"horizontalFrame_7")
        sizePolicy7.setHeightForWidth(self.horizontalFrame_7.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_7.setSizePolicy(sizePolicy7)
        self.horizontalFrame_7.setMinimumSize(QSize(251, 49))
        self.horizontalFrame_7.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalFrame_7)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.backBtn2 = QPushButton(self.horizontalFrame_7)
        self.backBtn2.setObjectName(u"backBtn2")
        self.backBtn2.setMinimumSize(QSize(93, 28))
        self.backBtn2.setMaximumSize(QSize(93, 28))
        self.backBtn2.setIcon(icon19)

        self.horizontalLayout_16.addWidget(self.backBtn2)

        self.savePassBtn = QPushButton(self.horizontalFrame_7)
        self.savePassBtn.setObjectName(u"savePassBtn")
        self.savePassBtn.setMinimumSize(QSize(93, 28))
        self.savePassBtn.setMaximumSize(QSize(93, 28))
        self.savePassBtn.setIcon(icon20)

        self.horizontalLayout_16.addWidget(self.savePassBtn)


        self.verticalLayout_11.addWidget(self.horizontalFrame_7)

        self.horizontalFrame_6 = QFrame(self.verticalWidget)
        self.horizontalFrame_6.setObjectName(u"horizontalFrame_6")
        sizePolicy3.setHeightForWidth(self.horizontalFrame_6.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_6.setSizePolicy(sizePolicy3)
        self.horizontalFrame_6.setMinimumSize(QSize(0, 74))
        self.horizontalFrame_6.setMaximumSize(QSize(16777215, 66))
        self.horizontalLayout_26 = QHBoxLayout(self.horizontalFrame_6)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, -1, -1, 9)
        self.deleteAccountBtn = QPushButton(self.horizontalFrame_6)
        self.deleteAccountBtn.setObjectName(u"deleteAccountBtn")
        self.deleteAccountBtn.setMinimumSize(QSize(141, 28))
        self.deleteAccountBtn.setMaximumSize(QSize(141, 28))
        self.deleteAccountBtn.setLayoutDirection(Qt.LeftToRight)
        icon25 = QIcon()
        icon25.addFile(u":/icons/icons/feather/alert-triangle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteAccountBtn.setIcon(icon25)
        self.deleteAccountBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_26.addWidget(self.deleteAccountBtn)


        self.verticalLayout_11.addWidget(self.horizontalFrame_6, 0, Qt.AlignHCenter)


        self.horizontalLayout_27.addWidget(self.verticalWidget)


        self.horizontalLayout_28.addWidget(self.widget_4)

        self.mainPages.addWidget(self.securityPage)

        self.verticalLayout_21.addWidget(self.mainPages)


        self.horizontalLayout_13.addWidget(self.homeSection)


        self.verticalLayout_24.addWidget(self.mainbody)

        self.footer = QWidget(self.centralwidget)
        self.footer.setObjectName(u"footer")
        sizePolicy3.setHeightForWidth(self.footer.sizePolicy().hasHeightForWidth())
        self.footer.setSizePolicy(sizePolicy3)
        self.horizontalLayout_10 = QHBoxLayout(self.footer)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_6 = QFrame(self.footer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")

        self.horizontalLayout_9.addWidget(self.label)


        self.horizontalLayout_10.addWidget(self.frame_6)

        self.sizeGrip = QFrame(self.footer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        sizePolicy5.setHeightForWidth(self.sizeGrip.sizePolicy().hasHeightForWidth())
        self.sizeGrip.setSizePolicy(sizePolicy5)
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.sizeGrip)


        self.verticalLayout_24.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.pushButton, self.searchLine)
        QWidget.setTabOrder(self.searchLine, self.searchButton)
        QWidget.setTabOrder(self.searchButton, self.uploadBtn)
        QWidget.setTabOrder(self.uploadBtn, self.notifBtn)
        QWidget.setTabOrder(self.notifBtn, self.msgBtn)
        QWidget.setTabOrder(self.msgBtn, self.profileBtn)
        QWidget.setTabOrder(self.profileBtn, self.minimizeWindow)
        QWidget.setTabOrder(self.minimizeWindow, self.restoreWindow)
        QWidget.setTabOrder(self.restoreWindow, self.closeWindow)
        QWidget.setTabOrder(self.closeWindow, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.homeBtn1)
        QWidget.setTabOrder(self.homeBtn1, self.followingBtn1)
        QWidget.setTabOrder(self.followingBtn1, self.liveBtn1)
        QWidget.setTabOrder(self.liveBtn1, self.homeBtn)
        QWidget.setTabOrder(self.homeBtn, self.followingBtn)
        QWidget.setTabOrder(self.followingBtn, self.liveBtn)
        QWidget.setTabOrder(self.liveBtn, self.pushButton_17)
        QWidget.setTabOrder(self.pushButton_17, self.pushButton_24)
        QWidget.setTabOrder(self.pushButton_24, self.pushButton_18)
        QWidget.setTabOrder(self.pushButton_18, self.pushButton_19)
        QWidget.setTabOrder(self.pushButton_19, self.pushButton_20)
        QWidget.setTabOrder(self.pushButton_20, self.pushButton_21)
        QWidget.setTabOrder(self.pushButton_21, self.scrollArea_5)

        self.retranslateUi(MainWindow)

        self.homeBtn.setDefault(False)
        self.acceuilSection.setCurrentIndex(-1)
        self.mainPages.setCurrentIndex(7)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.searchLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search accounts and videos", None))
        self.searchButton.setText("")
        self.uploadBtn.setText("")
        self.notifBtn.setText("")
        self.msgBtn.setText("")
        self.profileBtn.setText("")
        self.themeBtn.setText("")
        self.minimizeWindow.setText("")
        self.restoreWindow.setText("")
        self.closeWindow.setText("")
#if QT_CONFIG(whatsthis)
        self.followingBtn1.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Following </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.followingBtn1.setText(QCoreApplication.translate("MainWindow", u"Following", None))
        self.homeBtn1.setText(QCoreApplication.translate("MainWindow", u"For You", None))
        self.liveBtn1.setText(QCoreApplication.translate("MainWindow", u"LIVE", None))
        self.homeBtn.setText("")
        self.liveBtn.setText("")
        self.followingBtn.setText("")
        self.label2.setText(QCoreApplication.translate("MainWindow", u"Suggested accounts", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">user_101<img width=\"10\" src=\":/images/images/app/twitter-verified-png-original.png\"/></span><br>User 100\n"
"</p></body></html>", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"See all", None))
        self.label_7.setText("")
        self.label_5.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">spacerock</span><br>Space Science</p></body></html>", None))
        self.label_6.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">realme</span><br>My Real Profile</p></body></html>", None))
        self.label2_3.setText(QCoreApplication.translate("MainWindow", u"Following Accounts", None))
        self.label_9.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">user_101<img width=\"10\" src=\":/images/images/app/twitter-verified-png-original.png\"/></span><br>User 100\n"
"</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">spacerock</span><br>Space Science</p></body></html>", None))
        self.label_13.setText("")
        self.label_10.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">realme</span><br>My Real Profile</p></body></html>", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.label4.setText(QCoreApplication.translate("MainWindow", u"Discover", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"#football", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"#lifestyle", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"#memes", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"#news", None))
        self.label_19.setText("")
        self.label_20.setText("")
        self.label_21.setText("")
        self.iconeLabel.setText("")
        self.usernameLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Email", None))
        self.passwordLine.setText("")
        self.passwordLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Password", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"L o g  I n", None))
#if QT_CONFIG(whatsthis)
        self.loginLabel.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.loginLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Haven't an Account?  <a href=\"#\"><span style=\" text-decoration: underline; color:rgba(255,255,255,0.54902);\">Sign up</span></a></p></body></html>", None))
        self.fbButton.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.twitterButton.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.ytButton.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.linkedinButton.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_29.setText("")
        self.label_30.setText("")
        self.label_31.setText("")
        self.iconeLabel_adduser.setText("")
        self.lineEdit_Lname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Last Name", None))
        self.lineEdit_Fname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  First Name", None))
        self.lineEdit_Email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Email Address", None))
        self.lineEdit_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Password", None))
        self.lineEdit_passVerif.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Confirm Password", None))
        self.registerBtn.setText(QCoreApplication.translate("MainWindow", u"R e g i s t e r", None))
        self.registerLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Already have an Account?  <a href=\"#\"><span style=\" text-decoration: underline; color:rgba(255,255,255,140);\">Log in</span></a></p></body></html>", None))
        self.fbButton_2.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.twitterButton_2.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.ytButton_2.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.linkedinButton_2.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.profilPixLabel.setText("")
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">mortive</span><span style=\" font-weight:600;\"/><img src=\":/images/images/app/twitter-verified-png-original.png\" width=\"20\"/><br/><span style=\" font-size:12pt;\">Mortivaton Profile</span></p></body></html>", None))
        self.pushButton_60.setText(QCoreApplication.translate("MainWindow", u"Following", None))
        self.profilActionBtn.setText("")
        self.editBtn.setText(QCoreApplication.translate("MainWindow", u" Account", None))
        self.editPostBtn.setText(QCoreApplication.translate("MainWindow", u" Edit       ", None))
        self.securityBtn.setText(QCoreApplication.translate("MainWindow", u" Security", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p style=\"color: rgb(81, 81, 81);\"><span style=\" font-size:12pt; font-weight:600;\">8388 </span><span style=\" font-size:12pt;\">Following</span></p></body></html>", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#515151;\">10.8K </span><span style=\" font-size:12pt; color:#515151;\">Folowers</span></p></body></html>", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#515151;\">61.7K </span><span style=\" font-size:12pt; color:#515151;\">Likes</span></p></body></html>", None))
        self.bioLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Weak people revenge. Strong people forgive. Intelligent People Ignore.</span></p><p><span style=\" font-size:10pt;\">@AlbertEinstein</span></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Videos", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Liked", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:48pt; font-weight:600;\">LIVE</span><img src=\":/icons/icons/feather/video.svg\"/></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.label_16.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">FOLLOWING</span><img src=\":/icons/icons/feather/users.svg\"/></p></body></html>", None))
        self.avatarLabel.setText("")
        self.edithumbnailBtn.setText("")
        self.biotextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bio ...</p></body></html>", None))
        self.usernameQline.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.maleBox.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.femaleBox.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.firstnameQline.setInputMask("")
        self.firstnameQline.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.lastnameQline.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.emailQline.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.stateQline.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.countryQline.setText(QCoreApplication.translate("MainWindow", u"Country", None))
        self.phoneQline.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.CancelBtn.setText(QCoreApplication.translate("MainWindow", u" C a n c e l", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u" S A V E", None))
        self.titleQline.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.legendTextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Description ...</p></body></html>", None))
        self.pathLabel.setText("")
        self.addFileBtn.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.uploadFileBtn.setText(QCoreApplication.translate("MainWindow", u"U P L O A D", None))
        self.prevBtn.setText("")
        self.nextBtn.setText("")
        self.ancienpass.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.newpass.setText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.backBtn2.setText(QCoreApplication.translate("MainWindow", u"B A C K", None))
        self.savePassBtn.setText(QCoreApplication.translate("MainWindow", u"S A V E", None))
        self.deleteAccountBtn.setText(QCoreApplication.translate("MainWindow", u"DELETE ACCOUNT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IKarma V1", None))
    # retranslateUi

