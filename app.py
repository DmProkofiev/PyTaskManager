import os
import sys
from dependency_injector.wiring import Provide, inject
from PySide6.QtWidgets import QApplication
from ViewModels.main_viewmodel import MainViewModel
from Views.main_window import MainWindow
from container import AppContainer


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

@inject
def main(viewModel: MainViewModel = Provide[AppContainer.viewModel]) -> None:
    app = QApplication(sys.argv)
    style_path = resource_path("Resources/styles.qss")

    with open(style_path, "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    window = MainWindow(viewModel)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    container = AppContainer()
    container.config.db.path.from_env("DB_PATH", default="source.db")
    container.wire(modules=[__name__])
    main()