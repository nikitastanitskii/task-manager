class TasksNameCannotBeEmpty(Exception):
    """Название задачи пустое."""


class TasksAlreadyExists(Exception):
    """Задача с таким именем уже существует"""


class TasksNotFoundException(Exception):
    """Задача не найден"""
