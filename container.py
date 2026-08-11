from dependency_injector import containers, providers
from Infrastructure.unit_of_work import SqliteUnitOfWork
from Services.task_service import TaskService
from Services.session_service import SessionService
from Services.note_service import NoteService
from Services.dialog_service import DialogService
from Services.tray_service import TrayService
from ViewModels.main_viewmodel import MainViewModel


class AppContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    uow = providers.Singleton(SqliteUnitOfWork,db_path=config.db.path)
    task_service = providers.Factory(TaskService,uow=uow)
    session_service = providers.Factory(SessionService,uow=uow)
    note_service = providers.Factory(NoteService,uow=uow)
    dialog_service = providers.Singleton(DialogService)
    tray_service = providers.Singleton(TrayService)
    viewModel = providers.Factory(MainViewModel, task_service=task_service, session_service=session_service, note_service=note_service, tray_service=tray_service, dialog_service=dialog_service)