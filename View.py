# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(793, 422)
        self.gridLayout_5 = QtWidgets.QGridLayout(Form)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.yminlabel = QtWidgets.QLabel(Form)
        self.yminlabel.setMaximumSize(QtCore.QSize(30, 16777215))
        self.yminlabel.setObjectName("yminlabel")
        self.gridLayout.addWidget(self.yminlabel, 1, 0, 1, 1)
        self.xmax = QtWidgets.QPlainTextEdit(Form)
        self.xmax.setEnabled(True)
        self.xmax.setMaximumSize(QtCore.QSize(1000, 30))
        self.xmax.setOverwriteMode(True)
        self.xmax.setObjectName("xmax")
        self.gridLayout.addWidget(self.xmax, 0, 3, 1, 1)
        self.ymaxlabel = QtWidgets.QLabel(Form)
        self.ymaxlabel.setMaximumSize(QtCore.QSize(30, 16777215))
        self.ymaxlabel.setObjectName("ymaxlabel")
        self.gridLayout.addWidget(self.ymaxlabel, 1, 2, 1, 1)
        self.ymin = QtWidgets.QPlainTextEdit(Form)
        self.ymin.setEnabled(True)
        self.ymin.setMaximumSize(QtCore.QSize(1000, 30))
        self.ymin.setOverwriteMode(True)
        self.ymin.setObjectName("ymin")
        self.gridLayout.addWidget(self.ymin, 1, 1, 1, 1)
        self.xminlabel = QtWidgets.QLabel(Form)
        self.xminlabel.setMaximumSize(QtCore.QSize(30, 16777215))
        self.xminlabel.setObjectName("xminlabel")
        self.gridLayout.addWidget(self.xminlabel, 0, 0, 1, 1)
        self.xmin = QtWidgets.QPlainTextEdit(Form)
        self.xmin.setEnabled(True)
        self.xmin.setMaximumSize(QtCore.QSize(1000, 30))
        self.xmin.setOverwriteMode(True)
        self.xmin.setObjectName("xmin")
        self.gridLayout.addWidget(self.xmin, 0, 1, 1, 1)
        self.xmaxlabel = QtWidgets.QLabel(Form)
        self.xmaxlabel.setMaximumSize(QtCore.QSize(30, 16777215))
        self.xmaxlabel.setObjectName("xmaxlabel")
        self.gridLayout.addWidget(self.xmaxlabel, 0, 2, 1, 1)
        self.ymax = QtWidgets.QPlainTextEdit(Form)
        self.ymax.setEnabled(True)
        self.ymax.setMaximumSize(QtCore.QSize(1000, 30))
        self.ymax.setOverwriteMode(True)
        self.ymax.setObjectName("ymax")
        self.gridLayout.addWidget(self.ymax, 1, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 340))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_3.addWidget(self.graphicsView, 0, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Reload = QtWidgets.QPushButton(Form)
        self.Reload.setObjectName("Reload")
        self.gridLayout_4.addWidget(self.Reload, 0, 0, 1, 1)
        self.Load = QtWidgets.QPushButton(Form)
        self.Load.setObjectName("Load")
        self.gridLayout_4.addWidget(self.Load, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setMinimumSize(QtCore.QSize(100, 0))
        self.listView.setMaximumSize(QtCore.QSize(300, 16777215))
        self.listView.setObjectName("listView")
        self.gridLayout_3.addWidget(self.listView, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setMinimumSize(QtCore.QSize(150, 0))
        self.textBrowser.setMaximumSize(QtCore.QSize(150, 16777215))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.yminlabel.setText(_translate("Form", "ymin"))
        self.xmax.setPlainText(_translate("Form", "1"))
        self.ymaxlabel.setText(_translate("Form", "ymax"))
        self.ymin.setPlainText(_translate("Form", "0"))
        self.xminlabel.setText(_translate("Form", "xmin"))
        self.xmin.setPlainText(_translate("Form", "0"))
        self.xmaxlabel.setText(_translate("Form", "xmax"))
        self.ymax.setPlainText(_translate("Form", "1"))
        self.Reload.setText(_translate("Form", "Reload"))
        self.Load.setText(_translate("Form", "Load"))