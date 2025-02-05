from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data (in-memory)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form['task']
        if task:
            tasks.append({'id': len(tasks) + 1, 'task': task, 'done': False})
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if request.method == 'POST':
        task['task'] = request.form['task']
        return redirect(url_for('index'))
    return render_template('edit_task.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for('index'))

@app.route('/done/<int:task_id>')
def mark_done(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        task['done'] = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run( debug=True)

