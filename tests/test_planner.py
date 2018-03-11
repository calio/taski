import pytest
from app.planner import PriorityPlanner
from app.todoist_wrapper import Project, Task

def test_priority_planner():
    def choose_func(planner_item):
        tasks = planner_item.item.tasks
        if len(tasks) > 0:
            r = tasks[0]
            planner_item.item.tasks = tasks[1:]
            return r
        else:
            return None

    planner = PriorityPlanner({})

    P1 = Project()
    P1.id = 1
    P1.tasks = ["A1", "A2", "A3", "A4", "A5"]
    P1.priority = 6
    P2 = Project()
    P2.id = 2
    P2.tasks = ["B1", "B2", "B3", "B4", "B5"]
    P2.priority = 3
    P3 = Project()
    P3.id = 3
    P3.tasks = ["C1", "C2", "C3", "C4", "C5"]
    P3.priority = 1
    projects = [P1, P2, P3]

    res = []
    for t in planner.plan(projects, choose_func):
        res.append(t)

    print(res)
