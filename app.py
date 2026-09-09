from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Enable CORS for frontend requests
CORS(app)

# ==================== Database Model ====================
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert task object to dictionary"""
        return {
            'id': self.id,
            'text': self.text,
            'completed': self.completed,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }


# ==================== Create Tables ====================
with app.app_context():
    db.create_all()


# ==================== API Routes ====================

# GET all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Fetch all tasks"""
    try:
        tasks = Task.query.all()
        return jsonify({
            'success': True,
            'data': [task.to_dict() for task in tasks],
            'count': len(tasks)
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# GET a single task by ID
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Fetch a single task by ID"""
    try:
        task = Task.query.get_or_404(task_id)
        return jsonify({
            'success': True,
            'data': task.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': 'Task not found'}), 404


# POST create a new task
@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    try:
        data = request.get_json()

        # Validation
        if not data or not data.get('text'):
            return jsonify({'success': False, 'error': 'Task text is required'}), 400

        text = data.get('text').strip()
        if len(text) == 0:
            return jsonify({'success': False, 'error': 'Task cannot be empty'}), 400

        # Create task
        task = Task(text=text, completed=False)
        db.session.add(task)
        db.session.commit()

        return jsonify({
            'success': True,
            'message': 'Task created successfully',
            'data': task.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


# PUT update a task
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task (text and/or completion status)"""
    try:
        task = Task.query.get_or_404(task_id)
        data = request.get_json()

        # Update text if provided
        if 'text' in data:
            text = data['text'].strip()
            if len(text) == 0:
                return jsonify({'success': False, 'error': 'Task cannot be empty'}), 400
            task.text = text

        # Update completion status if provided
        if 'completed' in data:
            task.completed = data['completed']

        db.session.commit()

        return jsonify({
            'success': True,
            'message': 'Task updated successfully',
            'data': task.to_dict()
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


# PATCH toggle task completion
@app.route('/api/tasks/<int:task_id>/toggle', methods=['PATCH'])
def toggle_task(task_id):
    """Toggle task completion status"""
    try:
        task = Task.query.get_or_404(task_id)
        task.completed = not task.completed
        db.session.commit()

        return jsonify({
            'success': True,
            'message': 'Task toggled successfully',
            'data': task.to_dict()
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


# DELETE a task
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    try:
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()

        return jsonify({
            'success': True,
            'message': 'Task deleted successfully'
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


# DELETE all tasks
@app.route('/api/tasks', methods=['DELETE'])
def delete_all_tasks():
    """Delete all tasks"""
    try:
        Task.query.delete()
        db.session.commit()

        return jsonify({
            'success': True,
            'message': 'All tasks deleted successfully'
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'success': True,
        'message': 'Backend is running'
    }), 200


# ==================== Error Handlers ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'success': False,
        'error': 'Resource not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500


# ==================== Main ====================

if __name__ == '__main__':
    print("🚀 To-Do App Backend Starting...")
    print("📍 Server running at http://localhost:5000")
    print("📚 API Docs: http://localhost:5000/api/tasks")
    app.run(debug=True, host='localhost', port=5002)
