from datetime import datetime
from uuid import uuid1
from json import dumps


class Task:
    def __init__(self, title, description, 
                 category, due_date: datetime, priority, status = "Not done", id=str(uuid1())[:6]) -> None:
        
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def __eq__(self, other):
        if not isinstance(other, Task):
            return False
        return (
            self.id == other.id and
            self.title == other.title and
            self.description == other.description and
            self.due_date == other.due_date and
            self.category == other.category and
            self.priority == other.priority
        )

    def __hash__(self):
        return hash(self.id)

    @property
    def due_date(self):
        return self._due_date.strftime("%d %B %Y")

    @due_date.setter
    def due_date(self, value):
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, "%d %B %Y") 
            except ValueError:
                raise ValueError("Invalid date format. Expected '28 May 1994'.")
        self._due_date = value

    @property
    def date(self):
        return self._due_date.strftime("%d %B %Y")

    @date.setter
    def date(self, value):
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, "%d %B %Y") 
            except ValueError:
                raise ValueError("Invalid date format. Expected '28 May 1994'.")
        self._due_date = value
    
    def to_dict(self):
        return {
        "id": self.id,
        "title": self.title,
        "description": self.description,
        "category": self.category,
        "due_date": self.due_date,
        "priority": self.priority,
        "status": self.status
        }
    
    def to_json(self):
        data = self.to_dict()
        data["due_date"] = str(data["due_date"])
        
        return dumps(data, ensure_ascii=False)
    
    def to_list(self):
        return [self.title, self.description, self.category, self.due_date, self.priority, self.status, self.id]
    
    def get_attrs(self):
        return (attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__") and not attr.startswith("_") and attr != "id")
    
