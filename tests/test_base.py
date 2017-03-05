import pytest
from app import base
from app.todoist_wrapper import Todoist
import app.test_account as ta

    #td.write(gtd)
    #gtd2 = td.read()

def test_read_write_json():
    gtd = base.GTDSystem()
    gtd2 = base.GTDSystem()
    proj = gtd.add_project("Wing")
    proj.add_task("Build a navigation system")
    proj.add_task("Find a manufacture")

    s = gtd.write_json()
    gtd2.read_json(s)

    assert gtd == gtd2

def test_read_write_todoist():
    gtd = base.GTDSystem()
    proj = gtd.add_project("Wing")
    proj.add_task("Build a navigation system")
    proj.add_task("Find a manufacture")

    account = ta.get("todoist.com")
    print(account)
    td = Todoist(account["user"], account["password"])
    #td.clear()

    #td.load(gtd)
    gtd2 = td.dump()

    assert "" == gtd2.write_json()


