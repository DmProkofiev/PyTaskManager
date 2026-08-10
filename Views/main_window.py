import os
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow
from ViewModels.main_viewmodel import MainViewModel
from .ui_main_window import Ui_MainWindow

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class MainWindow(QMainWindow):
    def __init__(self, viewModel: MainViewModel):
        super().__init__()
        self._viewModel = viewModel
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._viewModel.set_ui(self.ui)
        self._viewModel.set_window(self)

        icon_path = resource_path("Resources/FIBERTMico.png")
        self.setWindowIcon(QIcon(icon_path))

        self._viewModel.timer_tick.connect(self.ui.labelTimerTime.setText)
        self._viewModel.error_occurred.connect(self._show_error)

    def _show_error(self, message: str):
        from Services.dialog_service import DialogService
        DialogService.show_error(self, message)

    def closeEvent(self, event):
        self._viewModel.handle_close_event(event)