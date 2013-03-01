# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Sun Feb 24 13:49:45 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(996, 656)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pkgLists = QtGui.QWidget(self.centralwidget)
        self.pkgLists.setMaximumSize(QtCore.QSize(250, 16777215))
        self.pkgLists.setObjectName("pkgLists")
        self.verticalLayout = QtGui.QVBoxLayout(self.pkgLists)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchEdit = QtGui.QLineEdit(self.pkgLists)
        font = QtGui.QFont()
        font.setItalic(True)
        self.searchEdit.setFont(font)
        self.searchEdit.setInputMask("")
        self.searchEdit.setText("")
        self.searchEdit.setObjectName("searchEdit")
        self.verticalLayout.addWidget(self.searchEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.installedBtn = QtGui.QPushButton(self.pkgLists)
        self.installedBtn.setCheckable(True)
        self.installedBtn.setChecked(False)
        self.installedBtn.setAutoDefault(False)
        self.installedBtn.setDefault(False)
        self.installedBtn.setFlat(False)
        self.installedBtn.setObjectName("installedBtn")
        self.horizontalLayout.addWidget(self.installedBtn)
        self.availableBtn = QtGui.QPushButton(self.pkgLists)
        self.availableBtn.setCheckable(True)
        self.availableBtn.setChecked(False)
        self.availableBtn.setAutoDefault(False)
        self.availableBtn.setDefault(False)
        self.availableBtn.setFlat(False)
        self.availableBtn.setObjectName("availableBtn")
        self.horizontalLayout.addWidget(self.availableBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pkgList = QtGui.QListWidget(self.pkgLists)
        self.pkgList.setFrameShadow(QtGui.QFrame.Sunken)
        self.pkgList.setTabKeyNavigation(False)
        self.pkgList.setObjectName("pkgList")
        self.verticalLayout.addWidget(self.pkgList)
        self.karmaCheckBox = QtGui.QCheckBox(self.pkgLists)
        self.karmaCheckBox.setObjectName("karmaCheckBox")
        self.verticalLayout.addWidget(self.karmaCheckBox)
        self.karmaUsernameEdit = QtGui.QLineEdit(self.pkgLists)
        self.karmaUsernameEdit.setObjectName("karmaUsernameEdit")
        self.verticalLayout.addWidget(self.karmaUsernameEdit)
        self.line_3 = QtGui.QFrame(self.pkgLists)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.releaseComboBox = QtGui.QComboBox(self.pkgLists)
        self.releaseComboBox.setObjectName("releaseComboBox")
        self.releaseComboBox.addItem("")
        self.releaseComboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.releaseComboBox)
        self.loadPackagesBtn = QtGui.QPushButton(self.pkgLists)
        self.loadPackagesBtn.setObjectName("loadPackagesBtn")
        self.horizontalLayout_5.addWidget(self.loadPackagesBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addWidget(self.pkgLists)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pkgNameLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pkgNameLabel.setFont(font)
        self.pkgNameLabel.setCursor(QtCore.Qt.ArrowCursor)
        self.pkgNameLabel.setMouseTracking(False)
        self.pkgNameLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pkgNameLabel.setAcceptDrops(False)
        self.pkgNameLabel.setObjectName("pkgNameLabel")
        self.verticalLayout_4.addWidget(self.pkgNameLabel)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget_bugs = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget_bugs.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget_bugs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget_bugs.setRootIsDecorated(False)
        self.treeWidget_bugs.setWordWrap(False)
        self.treeWidget_bugs.setColumnCount(2)
        self.treeWidget_bugs.setObjectName("treeWidget_bugs")
        self.verticalLayout_2.addWidget(self.treeWidget_bugs)
        self.treeWidget_test_cases = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget_test_cases.setRootIsDecorated(False)
        self.treeWidget_test_cases.setObjectName("treeWidget_test_cases")
        self.verticalLayout_2.addWidget(self.treeWidget_test_cases)
        self.treeWidget_related_packages = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget_related_packages.setObjectName("treeWidget_related_packages")
        self.verticalLayout_2.addWidget(self.treeWidget_related_packages)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.treeWidget_feedback = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget_feedback.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget_feedback.setRootIsDecorated(False)
        self.treeWidget_feedback.setObjectName("treeWidget_feedback")
        self.treeWidget_feedback.header().setCascadingSectionResizes(False)
        self.treeWidget_feedback.header().setMinimumSectionSize(30)
        self.verticalLayout_4.addWidget(self.treeWidget_feedback)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.karmaWidget = QtGui.QWidget(self.centralwidget)
        self.karmaWidget.setObjectName("karmaWidget")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.karmaWidget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.line_2 = QtGui.QFrame(self.karmaWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_7.addWidget(self.line_2)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.usernameEdit = QtGui.QLineEdit(self.karmaWidget)
        self.usernameEdit.setObjectName("usernameEdit")
        self.horizontalLayout_3.addWidget(self.usernameEdit)
        self.passwordEdit = QtGui.QLineEdit(self.karmaWidget)
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.horizontalLayout_3.addWidget(self.passwordEdit)
        self.okBtn = QtGui.QPushButton(self.karmaWidget)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout_3.addWidget(self.okBtn)
        self.cancelBtn = QtGui.QPushButton(self.karmaWidget)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_3.addWidget(self.cancelBtn)
        self.commentEdit = QtGui.QLineEdit(self.karmaWidget)
        self.commentEdit.setObjectName("commentEdit")
        self.horizontalLayout_3.addWidget(self.commentEdit)
        self.karmaBox = QtGui.QComboBox(self.karmaWidget)
        self.karmaBox.setObjectName("karmaBox")
        self.karmaBox.addItem("")
        self.karmaBox.addItem("")
        self.karmaBox.addItem("")
        self.horizontalLayout_3.addWidget(self.karmaBox)
        self.sendBtn = QtGui.QPushButton(self.karmaWidget)
        self.sendBtn.setObjectName("sendBtn")
        self.horizontalLayout_3.addWidget(self.sendBtn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addWidget(self.karmaWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 996, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.karmaBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Fedora Gooey Karma", None, QtGui.QApplication.UnicodeUTF8))
        self.searchEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Search packages...", None, QtGui.QApplication.UnicodeUTF8))
        self.installedBtn.setText(QtGui.QApplication.translate("MainWindow", "Installed", None, QtGui.QApplication.UnicodeUTF8))
        self.availableBtn.setText(QtGui.QApplication.translate("MainWindow", "Available", None, QtGui.QApplication.UnicodeUTF8))
        self.pkgList.setSortingEnabled(True)
        self.karmaCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Karma not submitted", None, QtGui.QApplication.UnicodeUTF8))
        self.karmaUsernameEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "username", None, QtGui.QApplication.UnicodeUTF8))
        self.releaseComboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Fedora 18", None, QtGui.QApplication.UnicodeUTF8))
        self.releaseComboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Fedora 17", None, QtGui.QApplication.UnicodeUTF8))
        self.loadPackagesBtn.setText(QtGui.QApplication.translate("MainWindow", "Load Packages", None, QtGui.QApplication.UnicodeUTF8))
        self.pkgNameLabel.setText(QtGui.QApplication.translate("MainWindow", "Package name", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monospace\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_bugs.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Bug id", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_bugs.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_test_cases.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Test cases", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_related_packages.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Related packages", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_feedback.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Karma", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_feedback.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_feedback.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.usernameEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "username", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "password", None, QtGui.QApplication.UnicodeUTF8))
        self.okBtn.setText(QtGui.QApplication.translate("MainWindow", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.karmaBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "-1", None, QtGui.QApplication.UnicodeUTF8))
        self.karmaBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.karmaBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "+1", None, QtGui.QApplication.UnicodeUTF8))
        self.sendBtn.setText(QtGui.QApplication.translate("MainWindow", "Send Karma", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
