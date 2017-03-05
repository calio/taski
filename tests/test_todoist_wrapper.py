import pytest
import base
from app.todoist_wrapper import Todoist


def test_read_write():
    gtd = base.GTDSystem()
    proj = gtd.add_project("Wing")
    proj.add_task("Build a navigation system")
    proj.add_task("Find a manufacture")

    td = Todoist(user, pwd)
