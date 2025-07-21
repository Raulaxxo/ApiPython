class ToDoModel:
    def __init__(self):
        self.todos = []
        self.counter = 1

    def all(self):
        return self.todos

    def get(self, todo_id):
        return next((todo for todo in self.todos if todo["id"] == todo_id), None)

    def create(self, data):
        todo = data.dict()
        todo["id"] = self.counter
        self.todos.append(todo)
        self.counter += 1
        return todo

    def update(self, todo_id, data):
        todo = self.get(todo_id)
        if todo:
            todo.update(data.dict())
        return todo

    def delete(self, todo_id):
        todo = self.get(todo_id)
        if todo:
            self.todos.remove(todo)
        return todo
