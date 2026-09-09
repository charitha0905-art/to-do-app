// API Configuration
const API_BASE_URL = 'http://localhost:5000/api';

// Get DOM elements
const taskForm = document.getElementById('taskForm');
const taskInput = document.getElementById('taskInput');
const taskList = document.getElementById('taskList');
const taskCount = document.getElementById('taskCount');

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    taskInput.focus();
    fetchTasks();  // Load tasks from backend
});

// Event listener for form submission
taskForm.addEventListener('submit', (e) => {
    e.preventDefault();
    addTask();
});

// ==================== API Calls ====================

// Fetch all tasks from backend
async function fetchTasks() {
    try {
        const response = await fetch(`${API_BASE_URL}/tasks`);
        const result = await response.json();

        if (result.success) {
            renderTasks(result.data);
        } else {
            console.error('Error fetching tasks:', result.error);
            showError('Failed to load tasks');
        }
    } catch (error) {
        console.error('Fetch error:', error);
        showError('Connection error. Make sure backend is running on port 5000');
    }
}

// Add a new task to backend
async function addTask() {
    const taskText = taskInput.value.trim();

    // Validation
    if (taskText === '') {
        alert('Please enter a task!');
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/tasks`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: taskText })
        });

        const result = await response.json();

        if (result.success) {
            taskInput.value = '';
            taskInput.focus();
            fetchTasks();  // Refresh task list
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        console.error('Add task error:', error);
        showError('Failed to add task');
    }
}

// Toggle task completion status
async function toggleComplete(taskId) {
    try {
        const response = await fetch(`${API_BASE_URL}/tasks/${taskId}/toggle`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        const result = await response.json();

        if (result.success) {
            fetchTasks();  // Refresh task list
        } else {
            alert('Error toggling task');
        }
    } catch (error) {
        console.error('Toggle error:', error);
        showError('Failed to update task');
    }
}

// Delete a task
async function deleteTask(taskId) {
    if (!confirm('Are you sure you want to delete this task?')) {
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        const result = await response.json();

        if (result.success) {
            fetchTasks();  // Refresh task list
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        console.error('Delete error:', error);
        showError('Failed to delete task');
    }
}

// ==================== DOM Rendering ====================

// Render tasks from fetched data
function renderTasks(tasks) {
    // Clear task list
    taskList.innerHTML = '';

    // Check if tasks exist
    if (tasks.length === 0) {
        taskList.innerHTML = '<p class="text-muted text-center">No tasks yet. Add one to get started!</p>';
        updateTaskCount(tasks);
        return;
    }

    // Create task elements
    tasks.forEach(task => {
        const taskItem = document.createElement('div');
        taskItem.className = `task-item ${task.completed ? 'completed' : ''}`;
        taskItem.dataset.id = task.id;

        taskItem.innerHTML = `
            <input 
                type="checkbox" 
                class="task-checkbox" 
                ${task.completed ? 'checked' : ''}
                onchange="toggleComplete(${task.id})"
            >
            <span class="task-text" onclick="toggleComplete(${task.id})">${escapeHtml(task.text)}</span>
            <button class="btn-delete" onclick="deleteTask(${task.id})">×</button>
        `;

        taskList.appendChild(taskItem);
    });

    // Update task counter
    updateTaskCount(tasks);
}

// Update task counter
function updateTaskCount(tasks) {
    const remainingTasks = tasks.filter(t => !t.completed).length;
    taskCount.textContent = remainingTasks;
}

// Show error message
function showError(message) {
    alert(message);
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
