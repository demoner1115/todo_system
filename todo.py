import json

def load_todos():
    try:
        with open('todos.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    if not isinstance(data, list):   # 리스트가 아니면 옛날 형식
        return []
    return data

def save_todos(todos):
    with open('todos.json', 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def add(name):
    todos = load_todos()
    todos.append({"name": name, "success": False})
    save_todos(todos)

def show_todos():
    todos = load_todos()
    if not todos:
        print("할 일이 없습니다.")
        return
    for i, todo in enumerate(todos, start=1):
        mark = "[x]" if todo["success"] else "[ ]"
        print(f"{i}. {mark} {todo['name']}")

def done(number):
    todos = load_todos()
    if not (1 <= number <= len(todos)):
        print("존재하지 않는 번호입니다.")
        return
    todos[number - 1]["success"] = True
    save_todos(todos)

def delete(number):
    todos = load_todos()
    if not (1 <= number <= len(todos)):
        print("존재하지 않는 번호입니다.")
        return
    del todos[number - 1]
    save_todos(todos)
