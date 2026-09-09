// Get DOM elements
const taskForm = document.getElementById('taskForm');
const taskInput = document.getElementById('taskInput');
const taskList = document.getElementById('taskList');
const taskCount = document.getElementById('taskCount');

// Task array (in-memory storage)
let tasks = [];

// Event listener for form submission
taskForm.addEventListener('submit', addTask);

// Add task function
function addTask(e) {
    e.preventDefault();

    const taskText = taskInput.value.trim();

    // Validation
    if (taskText === '') {
        alert('Please enter a task!');
        return;
    }

    // Create task object
    const task = {
        id: Date.now(),
        text: taskText,
        completed: false
    };

    // Add to tasks array
    tasks.push(task);

    // Clear input
    taskInput.value = '';
    taskInput.focus();

    // Render tasks
    renderTasks();
}

// Render tasks function
function renderTasks() {
    // Clear task list
    taskList.innerHTML = '';

    // Check if tasks exist
    if (tasks.length === 0) {
        taskList.innerHTML = '<p class="text-muted text-center">No tasks yet. Add one to get started!</p>';
        updateTaskCount();
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
    updateTaskCount();
}

// Toggle complete function
function toggleComplete(id) {
    const task = tasks.find(t => t.id === id);
    if (task) {
        task.completed = !task.completed;
        renderTasks();
    }
}

// Delete task function
function deleteTask(id) {
    tasks = tasks.filter(t => t.id !== id);
    renderTasks();
}

// Update task counter
function updateTaskCount() {
    const remainingTasks = tasks.filter(t => !t.completed).length;
    taskCount.textContent = remainingTasks;
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Focus input on page load
document.addEventListener('DOMContentLoaded', () => {
    taskInput.focus();
});
