import pytest
from task import Task
from commands.filter_task import filter_tasks, filter_tasks_by_keyword

@pytest.fixture
def sample_tasks():
    return {

        Task(
            id="1", 
            title="Important meeting", 
            category="Work", 
            status="Pending", 
            priority="High", 
            description="Discuss project updates", 
            due_date="23 December 2025"
        ),
        Task(
            id="2", 
            title="Grocery shopping", 
            category="Personal", 
            status="Completed", 
            priority="Medium", 
            description="Buy vegetables and fruits", 
            due_date="23 December 2025"
        ),
        Task(
            id="3", 
            title="Team standup call", 
            category="Work", 
            status="Pending", 
            priority="Low", 
            description="Daily team sync-up", 
            due_date="23 December 2025"
        ),
    }

def test_filter_tasks_by_category(sample_tasks):
    filtered = filter_tasks(sample_tasks, category="Work")
    assert len(filtered) == 2

def test_filter_tasks_by_keywords(sample_tasks):
    filtered = filter_tasks(sample_tasks, keywords="meeting")
    assert len(filtered) == 1
    assert filtered[0].title == "Important meeting"

def test_filter_tasks_by_priority(sample_tasks):
    filtered = filter_tasks(sample_tasks, priority="High")
    assert len(filtered) == 1
    assert filtered[0].title == "Important meeting"