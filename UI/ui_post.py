# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'postIdvjhP.ui'
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

class Ui_PostEdit(object):
    def setupUi(self, PostEdit):
        if PostEdit.objectName():
            PostEdit.setObjectName(u"PostEdit")
        PostEdit.resize(560, 463)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PostEdit.sizePolicy().hasHeightForWidth())
        PostEdit.setSizePolicy(sizePolicy)
        PostEdit.setMinimumSize(QSize(560, 0))
        PostEdit.setStyleSheet(u"*{\n"
"border-radius: 10px;\n"
"border: 1px solid #555;\n"
"background-color: rgb(14, 15, 18);\n"
"}\n"
"#frame_09, #frame_99, #frame_88{\n"
"border: none;\n"
"}\n"
"\n"
"#title, #description {\n"
"	border-radius: 5px;\n"
"	color:rgba(255, 255, 255, 150);\n"
"	padding-bottom:4px;\n"
"	background-color: #2C2828;\n"
"}\n"
"\n"
"#horizontalFrame{\n"
"background-color: none;\n"
"border : none;\n"
"}\n"
"\n"
"#backBtn, #confirmBtn{	\n"
"border: 1px solid #555;\n"
"font-weight: bold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254, 44, 85, 100), stop:1 rgba(0, 0, 0, 255));\n"
"border-radius: 5px;\n"
"color: #fff;\n"
"}\n"
"\n"
"#deletePostBtn{\n"
"border: 1px solid #555;\n"
"font-weight: bold;\n"
"background-color: rgba(254, 44, 85, 100);\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"\n"
"}\n"
"#backBtn::hover, #confirmBtn::hover{	\n"
"font-weight: bold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254, 44, 85, 150), stop:1 rgba(0, 0,"
                        " 0, 255));\n"
"}\n"
"\n"
"#backBtn::pressed, #confirmBtn::pressed{	\n"
"font-weight: bold;\n"
"padding-left:5px;\n"
"padding-top:2px;\n"
"background-color: #2C2828;\n"
"}\n"
"\n"
"\n"
"#deletePostBtn:hover{\n"
"font-weight: bold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254, 44, 85, 150), stop:1 rgba(0, 0, 0, 255));\n"
"\n"
"}\n"
"#deletePostBtn:pressed{\n"
"border: 1px solid #555;\n"
"padding-left:6px;\n"
"padding-top:4px;\n"
"		border-radius: 8px;\n"
"\n"
"	background-color: #2C2828;\n"
"}\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(PostEdit)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.widget_09 = QWidget(PostEdit)
        self.widget_09.setObjectName(u"widget_09")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_09.sizePolicy().hasHeightForWidth())
        self.widget_09.setSizePolicy(sizePolicy1)
        self.widget_09.setMinimumSize(QSize(525, 0))
        self.horizontalLayout = QHBoxLayout(self.widget_09)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, -1, 1, -1)
        self.frame_88 = QFrame(self.widget_09)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(226, 0))
        self.frame_88.setMaximumSize(QSize(226, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.frame_88)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.thumbnailLabel = QLabel(self.frame_88)
        self.thumbnailLabel.setObjectName(u"thumbnailLabel")
        self.thumbnailLabel.setMinimumSize(QSize(212, 375))
        self.thumbnailLabel.setMaximumSize(QSize(212, 375))
        self.thumbnailLabel.setStyleSheet(u"border-radius: 10px;")
        self.thumbnailLabel.setPixmap(QPixmap(u":/images/images/thumbnail/DougSinglemann--CrowRiver2016.jpg"))
        self.thumbnailLabel.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.thumbnailLabel)

        self.deletePostBtn = QPushButton(self.frame_88)
        self.deletePostBtn.setObjectName(u"deletePostBtn")
        self.deletePostBtn.setMinimumSize(QSize(212, 28))
        self.deletePostBtn.setMaximumSize(QSize(212, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/icons/feather/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deletePostBtn.setIcon(icon)

        self.verticalLayout_11.addWidget(self.deletePostBtn)


        self.horizontalLayout.addWidget(self.frame_88)

        self.frame_99 = QFrame(self.widget_09)
        self.frame_99.setObjectName(u"frame_99")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_99.sizePolicy().hasHeightForWidth())
        self.frame_99.setSizePolicy(sizePolicy2)
        self.frame_99.setMinimumSize(QSize(280, 0))
        self.frame_99.setMaximumSize(QSize(280, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.frame_99)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.title = QLineEdit(self.frame_99)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(265, 22))
        self.title.setMaximumSize(QSize(265, 22))
        self.title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.title)

        self.description = QTextEdit(self.frame_99)
        self.description.setObjectName(u"description")
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)
        self.description.setMinimumSize(QSize(265, 121))
        self.description.setMaximumSize(QSize(265, 121))

        self.verticalLayout_6.addWidget(self.description)

        self.horizontalFrame = QFrame(self.frame_99)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalFrame.setMinimumSize(QSize(271, 51))
        self.horizontalFrame.setMaximumSize(QSize(271, 51))
        self.horizontalFrame.setStyleSheet(u"")
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.backBtn = QPushButton(self.horizontalFrame)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setMinimumSize(QSize(100, 0))
        self.backBtn.setMaximumSize(QSize(100, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/feather/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backBtn.setIcon(icon1)

        self.horizontalLayout_16.addWidget(self.backBtn)

        self.confirmBtn = QPushButton(self.horizontalFrame)
        self.confirmBtn.setObjectName(u"confirmBtn")
        self.confirmBtn.setMinimumSize(QSize(100, 0))
        self.confirmBtn.setMaximumSize(QSize(100, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/feather/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.confirmBtn.setIcon(icon2)

        self.horizontalLayout_16.addWidget(self.confirmBtn)


        self.verticalLayout_6.addWidget(self.horizontalFrame)


        self.horizontalLayout.addWidget(self.frame_99)


        self.horizontalLayout_2.addWidget(self.widget_09)


        self.retranslateUi(PostEdit)

        QMetaObject.connectSlotsByName(PostEdit)
    # setupUi

    def retranslateUi(self, PostEdit):
        PostEdit.setWindowTitle(QCoreApplication.translate("PostEdit", u"Form", None))
        self.thumbnailLabel.setText("")
        self.deletePostBtn.setText(QCoreApplication.translate("PostEdit", u"  D E L E T E   P O S T", None))
        self.title.setText(QCoreApplication.translate("PostEdit", u"Title", None))
        self.description.setHtml(QCoreApplication.translate("PostEdit", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Description ...</span></p></body></html>", None))
        self.backBtn.setText(QCoreApplication.translate("PostEdit", u"B A C K", None))
        self.confirmBtn.setText(QCoreApplication.translate("PostEdit", u"S A V E", None))
    # retranslateUi

