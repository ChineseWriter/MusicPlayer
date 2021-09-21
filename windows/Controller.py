#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Controller.py
# @Time      :2021/6/25 12:19
# @Author    :Amundsen Severus Rubeus Bjaaland


from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QHeaderView
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt

from ReadSettings import SETTINGS
from .Main import Ui_MainWindow

from tools.KuGouAPI import MusicList
from KuGou import Music, SUPPORTED


class MainWeight(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MainWeight, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        if True:
            self.GetMusicListThread = None
            self.SelectResultModel = None
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
            self.SetBackgroundImage(SETTINGS.DefaultItems.BackGroundImagePath)
            self.Center()
        if True:
            self.SearchButton.clicked.connect(self.GetMusicName)

    def Center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        return None

    def SetSize(self, Width: int, Height: int):
        self.resize(Width, Height)
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
        return None

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.MouseLeftButtonClickFlag:
            self.move(QMouseEvent.globalPos() - self.MousePosition)
            QMouseEvent.accept()
        return None

    def mouseReleaseEvent(self, QMouseEvent):
        self.MouseLeftButtonClickFlag = False
        return None

    def GetMusicName(self):
        self.GetMusicListThread = MusicList(self.MusicNameLineEdit.text())
        self.GetMusicListThread.start()
        self.GetMusicListThread.Finished.connect(self.ShowMusicList)
        return None

    def ShowMusicList(self, MusicListResult: list):
        self.SelectResultModel = QStandardItemModel(0, 5)
        self.SelectResultModel.setHorizontalHeaderLabels(["歌曲名称", "演唱者", "来源网站", "第一标识", "第二标识"])
        for OneMusic in MusicListResult:
            OneMusic: Music
            MusicName = QStandardItem(OneMusic.Name)
            Singer = QStandardItem(OneMusic.Author.FreshNames)
            Source = QStandardItem(OneMusic.From)
            ID_1 = QStandardItem(OneMusic.FileId)
            if OneMusic.From == SUPPORTED.KuGou:
                ID_2 = QStandardItem(OneMusic.AlbumID)
            elif OneMusic.From == SUPPORTED.QQ:
                ID_2 = QStandardItem(OneMusic.MusicId)
            else:
                ID_2 = QStandardItem("")
            self.SelectResultModel.appendRow([MusicName, Singer, Source, ID_1, ID_2])
        self.MusicSelectResultTable.setModel(self.SelectResultModel)
        self.MusicSelectResultTable.hideColumn(3)
        self.MusicSelectResultTable.hideColumn(4)
        self.MusicSelectResultTable.horizontalHeader().setStretchLastSection(True)
        self.MusicSelectResultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.MusicSelectResultTable.horizontalHeader().setStyleSheet("QHeaderView::section {background: transparent}")
        self.MusicSelectResultTable.verticalHeader().hide()
        self.MusicSelectResultTable.setShowGrid(False)
        return None
