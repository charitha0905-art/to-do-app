#!/usr/bin/env python3
"""
Simple To-Do App Backend
Runs on http://localhost:5000
Serves both API and static HTML/CSS/JS files
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os

# Get the directory where this script is located
APP_DIR = os.path.dirname(os.path.abspath(__file__))

# Create Flask app with static files directory
app = Flask(__name__, static_folder=APP_DIR, static_url_path='')
CORS(app)

# Get the directory where this script is located
APP_DIR = os.path.dirname(os.path.abspath(__file__))

# Create Flask app with static files directory
app = Flask(__name__, static_folder=APP_DIR, static_url_path='')
CORS(app)

# Simple file-based storage (no database needed)
TASKS_FILE = os.path.join(APP_DIR, 'tasks.json')

def load_tasks():
    """Load tasks from JSON file"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

# ==================== Serve Static Files ====================

@app.route('/')
def serve_index():
    """Serve the main index.html page"""
    return send_from_directory(APP_DIR, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files (CSS, JS, etc)"""
    return send_from_directory(APP_DIR, filename)

# ==================== API Routes ====================

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    tasks = load_tasks()
    return jsonify({'success': True, 'data': tasks})

@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    data = request.get_json()
    text = data.get('text', '').strip()
    
    if not text:
        return jsonify({'success': False, 'error': 'Task text required'}), 400
    
    tasks = load_tasks()
    new_task = {
        'id': max([t.get('id', 0) for t in tasks], default=0) + 1,
        'text': text,
        'completed': False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    
    return jsonify({'success': True, 'data': new_task}), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task"""
    data = request.get_json()
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            if 'text' in data:
                task['text'] = data['text']
            if 'completed' in data:
                task['completed'] = data['completed']
            save_tasks(tasks)
            return jsonify({'success': True, 'data': task})
    
    return jsonify({'success': False, 'error': 'Task not found'}), 404

@app.route('/api/tasks/<int:task_id>/toggle', methods=['PATCH'])
def toggle_task(task_id):
    """Toggle task completion"""
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            save_tasks(tasks)
            return jsonify({'success': True, 'data': task})
    
    return jsonify({'success': False, 'error': 'Task not found'}), 404

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    tasks = load_tasks()
    tasks = [t for t in tasks if t['id'] != task_id]
    save_tasks(tasks)
    return jsonify({'success': True, 'message': 'Task deleted'})

@app.route('/api/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({'success': True, 'message': 'Backend running'})

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 To-Do App Backend - SIMPLE VERSION")
    print("="*50)
    print("📍 Server: http://localhost:5000")
    print("📚 API: http://localhost:5000/api/tasks")
    print("💾 Storage: tasks.json")
    print("="*50 + "\n")
    app.run(debug=True, host='localhost', port=5000)
