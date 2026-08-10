import os
from PySide6.QtGui import QIcon, QAction, QPixmap, QColor
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QApplication
from Interfaces.ITrayService import ITrayService


class TrayService(ITrayService):
    _instance = None
    _tray_icon = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def setup_tray(self, window, view_model, icon_path: str) -> None:
        if TrayService._tray_icon is not None:
            return
        if not QSystemTrayIcon.isSystemTrayAvailable():
            return

        icon = QIcon(icon_path)
        if icon.isNull():
            pixmap = QPixmap(64, 64)
            pixmap.fill(QColor(80, 80, 150))
            icon = QIcon(pixmap)

        self._tray_icon = QSystemTrayIcon(icon, window)
        self._tray_icon.setToolTip("FIBER Task Manager")

        menu = QMenu()
        for label, handler in [
            ("Показать", view_model.show_window),
            ("Скрыть", view_model.hide_window),
            (None, None),
            ("Выход", view_model.quit_application),
        ]:
            if label is None:
                menu.addSeparator()
            else:
                action = QAction(label, window)
                action.triggered.connect(handler)
                menu.addAction(action)

        self._tray_icon.setContextMenu(menu)
        self._tray_icon.activated.connect(view_model._on_tray_activated)
        self._tray_icon.show()

    def hide_tray(self) -> None:
        if self._tray_icon:
            self._tray_icon.hide()
            self._tray_icon = None

    def show_message(self, title: str, msg: str, icon=QSystemTrayIcon.Information, msecs: int = 2000) -> None:
        if self._tray_icon:
            self._tray_icon.showMessage(title, msg, icon, msecs)