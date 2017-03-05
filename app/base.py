import json

class Task():
    def __init__(self, name, id=0, pid=0, done=False, ts_done=-1, ts_added=-1, meta={}):
        self.id = id
        self.name = name
        self.pid = pid
        self.done = done
        self.ts_done = ts_done
        self.ts_added = ts_added
        self.meta = meta

    def __repr__(self):
        return "[Task](" + self.name.encode('utf-8') + ")"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class Project():
    def __init__(self, name, id=0, priority=0, tasks=None, meta={}):
        self.id = id
        self.name = name
        ## TODO get tasks from dict
        self.tasks = []
        self.priority = priority
        self.meta = meta

    def __repr__(self):
        return "[Project](" + self.name.encode('utf-8') + ")"

    def __eq__(self, other):
        return self.tasks == other.tasks and self.__dict__ == other.__dict__

    def add_task(self, name, **kargs):
        t = Task(name, **kargs)
        self.tasks.append(t)
        return t

    def get_tasks(self):
        return self.tasks

    def delete(self):
        pass

class GTDSystem():
    def __init__(self):
        self.projects = []
        self.meta = {}
        self.add = []
        self.delete = []
        self.update = []

    def __eq__(self, other):
        return self.projects == other.projects

    def add_project(self, name, **kargs):
        p = Project(name, **kargs)
        self.projects.append(p)
        return p

    def get_projects(self):
        return self.projects()

    def write_json(self):
        projects = []
        for p in self.projects:
            tasks = []
            for t in p.tasks:
                tasks.append(t.__dict__)
            project = p.__dict__.copy()
            project["tasks"] = tasks
            projects.append(project)

        return json.dumps(projects)

    def read_json(self, json_str):
        data = json.loads(json_str)

        for p in data:
            project = self.add_project(**p)
            for t in p["tasks"]:
                project.add_task(**t)

