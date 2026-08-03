import os
from datetime import datetime
from typing import List
from PySide6.QtCore import QObject, Signal, Qt
from PySide6.QtWidgets import QTableWidgetItem, QApplication, QSystemTrayIcon

class MainViewModel(QObject):
    def __init__(self):
        pass