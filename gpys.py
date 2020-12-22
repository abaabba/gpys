#%%
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import PyQt5
from PyQt5.QtCore import pyqtSlot, QRect, QRectF, QSizeF
from PyQt5.QtWidgets import QApplication, QGraphicsItem
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5 import QtCore
import View
import os
import numpy as np
import sys
from PyQt5.QtGui import QBrush, QColor, QImage, QPalette, QPixmap


class Point(QRectF):
    pass


class PlotScene(QtWidgets.QGraphicsScene):
    def mousePressEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent):
        if event.button() == QtCore.Qt.LeftButton:
            self.pp = event.scenePos()
            self.rectItem = self.addRect(Point(self.pp, self.pp))
            self.rectItem.setBrush(QBrush(QColor(255, 0, 0, 0.8)))
            self.rectItem.setFlags(QGraphicsItem.ItemIsMovable
                                   | QGraphicsItem.ItemIsSelectable)
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent):
        pp = event.scenePos()
        dx = np.abs(self.pp.x() - pp.x())**2
        dy = np.abs(self.pp.y() - pp.y())**2
        ds = np.sqrt(dx + dy)
        if ds > 10:
            pass
        else:
            if self.rectItem != None:
                self.rectItem.setRect(QRectF(self.pp, QSizeF(10, 10)))

        self.rec = None
        return super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent):

        return super().mouseMoveEvent(event)


class Model(QWidget, View.Ui_Form):
    def __init__(self, parent=None):
        super(Model, self).__init__(parent)
        self.setupUi(self)

        lst = [
            _ for _ in os.listdir() if (os.path.splitext(_)[1] == ".jpg") or (
                os.path.splitext(_)[1] == ".png")
        ]
        self.FileListModel = QtCore.QStringListModel()
        self.FileListModel.setStringList(lst)
        self.listView.setModel(self.FileListModel)

        self.Reload.clicked.connect(self.ReloadClicked)
        self.Load.clicked.connect(self.LoadClicked)

    def ReloadClicked(self):
        lst = [
            _ for _ in os.listdir() if (os.path.splitext(_)[1] == ".jpg") or (
                os.path.splitext(_)[1] == ".png")
        ]

        self.FileListModel.setStringList(lst)
        self.listView.setModel(self.FileListModel)

    def LoadClicked(self):
        index = self.listView.selectedIndexes()[0]
        r, c = index.row(), index.column()
        print(r, c)
        file = self.FileListModel.index(r, c).data()
        image = QImage(file)
        self.scene = PlotScene()
        self.scene.addPixmap(QPixmap.fromImage(image))
        self.graphicsView.setScene(self.scene)
        print(self.scene.width(), self.scene.height(), self.graphicsView.pos())
        self.graphicsView.installEventFilter(self)


app = QApplication(sys.argv)
ex = Model()
ex.show()
app.exec_()
