from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (replace with your actual data)
todos = [
    {'id': 1, 'task': 'Buy groceries', 'completed': False},
    {'id': 2, 'task': 'Do laundry', 'completed': True},
    {'id': 3, 'task': 'Go for a run', 'completed': False}
]


@app.route('/todos', methods=['GET'])
def get_all_todos():
    return jsonify(todos)


@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            return jsonify(todo)
    return jsonify({'message': 'Todo not found'}), 404


@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_todo = {
        'id': len(todos) + 1,
        'task': data['task'],
        'completed': data['completed']
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201


@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['task'] = request.get_json()['task']
            todo['completed'] = request.get_json().get('completed', todo['completed'])
            return jsonify(todo)
    return jsonify({'message': 'Todo not found'}), 404


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    for i, todo in enumerate(todos):
        if todo['id'] == todo_id:
            del todos[i]
            return jsonify({'message': 'Todo deleted'}), 204
    return jsonify({'message': 'Todo not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)