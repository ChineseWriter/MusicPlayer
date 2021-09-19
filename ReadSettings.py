#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :ReadSettings.py
# @Time      :2021/9/19 12:55
# @Author    :Amundsen Severus Rubeus Bjaaland


import json


class Default(object):
    def __init__(self):
        self.__Settings = json.load(open("./static/Settings.json", "r", encoding="UTF-8"))

    @property
    def Width(self) -> int:
        return self.__Settings["DefaultItems"]["Size"][0]

    @property
    def Height(self) -> int:
        return self.__Settings["DefaultItems"]["Size"][1]

    @property
    def BackGroundImagePath(self):
        return self.__Settings["DefaultItems"]["BackGroundImagePath"]


class Settings(object):
    def __init__(self):
        self.__DefaultItems = Default()

    @property
    def DefaultItems(self) -> Default:
        return self.__DefaultItems


SETTINGS = Settings()
