#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :MusicPlayer.py
# @Time      :2021/6/25 12:04
# @Author    :Amundsen Severus Rubeus Bjaaland


import sys

from PyQt5.QtWidgets import QApplication

import Source_rc
from windows.Controller import MainWeight


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainApplication = MainWeight()
    MainApplication.show()
    sys.exit(app.exec_())

