import pytest
from datetime import date, timedelta
from Models.models import Task, OnceTask, DailyTask, WeeklyTask, MonthlyTask, YearlyTask, Note, TimerSession
from Models.enums import TaskPriority, TaskStatus


# Note
class TestNote:
    def test_valid_note_passes_validation(self, valid_note):
        valid_note.validate()

    def test_fully_empty_note_raises(self, fully_empty_note):
        with pytest.raises(ValueError, match="Заголовок или текст должны быть заполнены"):
            fully_empty_note.validate()

    def test_only_title_is_valid(self, empty_content_note):
        empty_content_note.validate()

    def test_only_content_is_valid(self, empty_title_note):
        empty_title_note.validate()

    def test_note_attributes(self, valid_note):
        assert valid_note.id == 1
        assert valid_note.task_id == 10
        assert valid_note.title == "Важная заметка"
        assert isinstance(valid_note.created_at, date)

# Task
class TestTaskValidation:
    def test_empty_title_raises(self, task_factory):
        task = task_factory("once", title="")
        with pytest.raises(ValueError, match="Название не может быть пустым"):
            task.validate()

    def test_past_due_date_raises(self, task_factory, past_date):
        task = task_factory("once", title="Задача", due_date=past_date)
        with pytest.raises(ValueError, match="Дата выполнения не может быть в прошлом"):
            task.validate()

    def test_future_due_date_passes(self, sample_once_task):
        sample_once_task.validate()

    def test_today_due_date_passes(self, task_factory, today):
        task = task_factory("once", title="Сегодня", due_date=today)
        task.validate()

    def test_invalid_priority_type_raises(self, task_factory):
        task = task_factory("once", title="T", priority="не enum")
        with pytest.raises(TypeError, match="Неверный тип приоритета"):
            task.validate()

    def test_weekly_invalid_day_raises(self):
        task = WeeklyTask(title="W", day_of_week=7)
        with pytest.raises(ValueError, match="День недели должен быть от 0 до 6"):
            task.validate()

    def test_monthly_invalid_day_raises(self):
        task = MonthlyTask(title="M", day_of_month=0)
        with pytest.raises(ValueError, match="День месяца должен быть от 1 до 31"):
            task.validate()

    def test_yearly_invalid_month_raises(self):
        task = YearlyTask(title="Y", month=13, day=1)
        with pytest.raises(ValueError, match="Месяц должен быть от 1 до 12"):
            task.validate()

    def test_yearly_invalid_day_raises(self):
        task = YearlyTask(title="Y", month=1, day=32)
        with pytest.raises(ValueError, match="День должен быть от 1 до 31"):
            task.validate()


class TestTaskComplete:
    def test_complete_changes_status(self, sample_once_task):
        assert sample_once_task.status == TaskStatus.PENDING
        sample_once_task.complete()
        assert sample_once_task.status == TaskStatus.COMPLETED

    def test_complete_updates_timestamp(self, sample_once_task, mocker):
        fake_now = date(2026, 8, 11)
        mocker.patch("Models.task.datetime")
        old_updated = sample_once_task.updated_at
        sample_once_task.complete()
        assert sample_once_task.updated_at != old_updated


class TestTaskIsOverdue:
    def test_overdue_task(self, overdue_once_task):
        assert overdue_once_task.is_overdue() is True

    def test_future_task_not_overdue(self, sample_once_task):
        assert sample_once_task.is_overdue() is False

    def test_completed_task_not_overdue_even_if_past(self, overdue_once_task):
        overdue_once_task.complete()
        assert overdue_once_task.is_overdue() is False

    @pytest.mark.parametrize("status,days_delta,expected", [
        (TaskStatus.PENDING, -1, True),
        (TaskStatus.PENDING, 1, False),
        (TaskStatus.COMPLETED, -1, False),
    ])
    def test_is_overdue_scenarios(self, task_factory, status, days_delta, expected):
        task = task_factory("once", title="T", status=status, due_date=date.today() + timedelta(days=days_delta))
        assert task.is_overdue() == expected

class TestTaskDisplayName:
    def test_display_name_pending(self, sample_once_task):
        assert sample_once_task.display_name() == "В процессе"

    def test_display_name_completed(self, overdue_once_task):
        overdue_once_task.complete()
        assert overdue_once_task.display_name() == "Завершено"

    def test_display_name_overdue(self, overdue_once_task):
        overdue_once_task.status = TaskStatus.OVERDUE
        assert overdue_once_task.display_name() == "Просрочено"

class TestTaskPeriodLabels:
    def test_once_label(self, sample_once_task):
        assert sample_once_task.get_period_label() == "Разовая"

    def test_daily_label(self, daily_task):
        assert daily_task.get_period_label() == "Ежедневная"

    def test_weekly_label(self, weekly_task):
        assert weekly_task.get_period_label() == "Еженедельная"

    def test_monthly_label(self, monthly_task):
        assert monthly_task.get_period_label() == "Ежемесячная"

    def test_yearly_label(self, yearly_task):
        assert yearly_task.get_period_label() == "Ежегодная"


# TimerSession
class TestTimerSession:
    def test_active_session_is_active(self, active_session):
        assert active_session.is_active() is True

    def test_stop_session(self, active_session):
        active_session.stop()
        assert active_session.is_active() is False
        assert active_session.duration_seconds >= 0

    def test_stopped_session_not_active(self, stopped_session):
        assert stopped_session.is_active() is False

    def test_get_duration_string_stopped(self, stopped_session):
        dur_str = stopped_session.get_duration_string()
        assert isinstance(dur_str, str)
        assert dur_str == "00:00:00" or dur_str.startswith("00:00:")

    def test_validate_future_start_time_raises(self):
        from datetime import datetime
        session = TimerSession(start_time=datetime.now() + timedelta(days=1))
        with pytest.raises(ValueError, match="Время начала не может быть в будущем"):
            session.validate()

    def test_validate_current_time_passes(self, active_session):
        active_session.validate()