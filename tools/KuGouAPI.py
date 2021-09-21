#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :KuGouAPI.py
# @Time      :2021/9/20 18:16
# @Author    :Amundsen Severus Rubeus Bjaaland


from PyQt5.Qt import QThread
from PyQt5.QtCore import pyqtSignal

from KuGou.Tools import GetMusicList, GetMusicInfo


class MusicList(QThread):
    Finished = pyqtSignal(list)

    def __init__(self, MusicName: str):
        super(MusicList, self).__init__()
        self.MusicName = MusicName

    def run(self) -> None:
        Result = GetMusicList(self.MusicName)
        self.Finished.emit(Result)
        # print("Finished!")
        return None
