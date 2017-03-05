#import traceback
import json
from json import JSONEncoder

class Task():
    def __init__(self, name, id=0, pid=0, done=False, ts_done=-1, ts_added=-1, meta_data=None):
        self.id = id
        self.name = name
        self.pid = pid
        self.done = done
        self.ts_done = ts_done
        self.ts_added = ts_added
        self.meta_data = meta_data

    def __repr__(self):
        return "[Task](" + self.name.encode('utf-8') + ")"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class Project(JSONEncoder):
    def __init__(self, name, id=0, priority=0, tasks=None):
        self.id = id
        self.name = name
        ## TODO get tasks from dict
        self.tasks = []
        self.priority = priority

    def __repr__(self):
        return "[Project](" + self.name.encode('utf-8') + ")"

    def __eq__(self, other):
        return self.tasks == other.tasks and self.__dict__ == other.__dict__

    def add_task(self, name, **kargs):
        t = Task(name, **kargs)
        self.tasks.append(t)
        return t

    def delete(self):
        pass

class GTDSystem():
    def __init__(self):
        self.projects = []

    def __eq__(self, other):
        return self.projects == other.projects

    def add_project(self, name, **kargs):
        p = Project(name, **kargs)
        self.projects.append(p)
        return p

    def writeJSON(self):
        projects = []
        for p in self.projects:
            tasks = []
            for t in p.tasks:
                tasks.append(t.__dict__)
            project = p.__dict__.copy()
            project["tasks"] = tasks
            projects.append(project)

        return json.dumps(projects)

    def readJSON(self, json_str):
        data = json.loads(json_str)

        for p in data:
            project = self.add_project(**p)
            for t in p["tasks"]:
                project.add_task(**t)

