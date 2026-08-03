from dependency_injector import containers, providers

from Services.Repositories.note_repository import SqliteNoteRepository
from Services.Repositories.task_repository import SqliteTaskRepository
from Services.Repositories.timer_session_repository import SqliteTimerSessionRepository
from Services.dialog_service import TrayService
from ViewModels.main_viewmodel import MainViewModel


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    tray_service = providers.Singleton(TrayService)
    dialog_service = providers.Singleton(TrayService)
    task_repository = providers.Singleton(SqliteTaskRepository,db_path = config.db.path)
    note_repository = providers.Singleton(SqliteNoteRepository, db_path = config.db.path)
    timer_session_repository = providers.Singleton(SqliteTimerSessionRepository, db_path = config.db.path)
    viewModel = providers.Factory(MainViewModel)