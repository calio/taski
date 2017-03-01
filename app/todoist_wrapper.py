import todoist
from datetime import datetime
from base import dlog, Project, Task

class Todoist():
    def __init__(self):
        self.api = todoist.TodoistAPI()
        self.user = None
        self.data = None
        self.imgt = todoist.managers.items.ItemsManager(self.api)

    def _task_adapter(self, todoist_task):
        t = Task()
        tt = todoist_task
        t.id = tt['id']
        t.name = tt['content']
        t.done = tt['checked']
        t.pid = tt['project_id']
        if tt['completed_date']:
            t.ts_done = datetime.strptime(tt['completed_date'], "%a %d %b %Y %H:%M:%S +0000")
            t.done = True
        else:
            t.ts_added = datetime.strptime(tt['date_added'], "%a %d %b %Y %H:%M:%S +0000")

        t._data = tt

        pass

    def init(self, cfg):
        self.user = self.api.user.login(cfg["email"], cfg["password"])
        self.data = self.api.sync()

    def get_tasks(self, completed=False, since=None, until=None):
        ttasks = self.data['items']
        tasks = []
        for tt in ttasks:
            tasks.append(self._task_adapter(tt))
        return tasks

    def update_task(self, task, key, value):
        self.imgr.update(task.id, key=value)
        pass
    def get_projects(self):
        pass
    def commit(self):
        pass


def get_app():
    return None
