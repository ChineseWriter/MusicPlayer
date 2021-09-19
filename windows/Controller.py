#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Controller.py
# @Time      :2021/6/25 12:19
# @Author    :Amundsen Severus Rubeus Bjaaland


from PyQt5.QtWidgets import QMainWindow, QWidget, QDesktopWidget
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtCore import Qt

from ReadSettings import SETTINGS
from .Main import Ui_MainWindow
from .Player import Ui_Player


class PlayWeight(Ui_Player, QWidget):
    def __init__(self, parent=None):
        super(PlayWeight, self).__init__(parent)
        self.setupUi(self)


class MainWeight(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MainWeight, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        if True:
            self.MouseLeftButtonClickFlag = False
            self.MousePosition = None
            self.setWindowTitle("音乐播放器")
            with open("./static/qss/DefaultMain.qss", "r", encoding="UTF-8") as File:
                self.CentralWidget.setStyleSheet(File.read())
        if True:
            self.setMaximumSize(SETTINGS.DefaultItems.Width, SETTINGS.DefaultItems.Height)
            self.setWindowOpacity(0.9)
            self.setWindowFlag(Qt.FramelessWindowHint)
        if True:
            self.Player = PlayWeight()
        if True:
            self.ShowPlayerWeight()
            self.SetBackgroundImage(SETTINGS.DefaultItems.BackGroundImagePath)
            self.Center()

    def Center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def SetSize(self, Width: int, Height: int):
        self.resize(Width, Height)

    def ShowPlayerWeight(self):
        self.MainLayout.addChildWidget(self.Player)
        self.Player.show()
        return None

    def SetBackgroundImage(self, Path: str = ":/files/static/image/wallpaper/01.jpg"):
        BackGround = QPalette()
        Image = QPixmap(Path)
        Image = Image.scaled(SETTINGS.DefaultItems.Width, SETTINGS.DefaultItems.Height, Qt.KeepAspectRatio)
        Brush = QBrush(Image)
        BackGround.setBrush(QPalette.Background, Brush)
        self.setPalette(BackGround)
        return None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.MouseLeftButtonClickFlag = True
            self.MousePosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.MouseLeftButtonClickFlag:
            self.move(QMouseEvent.globalPos() - self.MousePosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.MouseLeftButtonClickFlag = False

