# Backend Setup Guide

This guide will help you set up and run the Python Flask backend for the To-Do App.

---

## Prerequisites

- **Python 3.7+** installed on your system
- **pip** (Python package manager)
- Command line/terminal access

---

## Installation Steps

### Step 1: Check Python Installation

Verify Python is installed by running:

```bash
python --version
# or
python3 --version
```

You should see a version number like `Python 3.9.0` or higher.

### Step 2: Navigate to Project Directory

```bash
cd /path/to/todoapp
```

### Step 3: Create Virtual Environment (Recommended)

It's best practice to use a virtual environment to isolate project dependencies.

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

After activation, your terminal should show `(venv)` at the beginning of the line.

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- Flask-CORS (cross-origin support)
- Flask-SQLAlchemy (database ORM)
- SQLAlchemy (database toolkit)

### Step 5: Run the Backend Server

```bash
python app.py
```

You should see output like:
```
🚀 To-Do App Backend Starting...
📍 Server running at http://localhost:5000
📚 API Docs: http://localhost:5000/api/tasks
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

---

## Testing the Backend

### Option 1: Using Browser

Visit `http://localhost:5000/api/tasks` in your browser. You should see:

```json
{
  "success": true,
  "data": [],
  "count": 0
}
```

### Option 2: Using curl (Terminal)

If you have curl installed:

```bash
# Get all tasks
curl http://localhost:5000/api/tasks

# Create a new task
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"text": "Test task"}'
```

### Option 3: Using Postman

Download [Postman](https://www.postman.com/downloads/) and import these requests:

```
GET http://localhost:5000/api/tasks
```

---

## Connecting Frontend to Backend

1. Open `index.html` in your code editor
2. Find the script section at the bottom:

```html
<!-- Change this line: -->
<script src="script.js"></script>

<!-- To this: -->
<script src="script_backend.js"></script>
```

3. Save the file
4. Open `index.html` in your browser
5. The app will now use your backend server!

---

## Database Management

### View Database

The database file `tasks.db` is automatically created in the project folder.

### Reset Database

To clear all tasks and start fresh:

```bash
# Simply delete the database file
rm tasks.db          # macOS/Linux
del tasks.db         # Windows Command Prompt
```

Then restart the server:
```bash
python app.py
```

### Using Database Tools

You can view/edit the database using tools like:
- **DB Browser for SQLite** (free, cross-platform)
- **SQLiteStudio** (web-based)
- **VS Code Extension**: SQLite

---

## Troubleshooting

### Issue: "ModuleNotFoundError"

**Solution**: Make sure you installed dependencies:
```bash
pip install -r requirements.txt
```

### Issue: "Address already in use"

**Solution**: Port 5000 is already in use. Either:
1. Close other apps using port 5000
2. Change port in `app.py`: `app.run(port=5001)`

### Issue: CORS Errors in Console

**Solution**: Make sure:
1. Backend is running (`python app.py`)
2. Frontend is using `script_backend.js`
3. Backend is accessible at `http://localhost:5000`

### Issue: "Connection refused"

**Solution**: Backend is not running. Start it with:
```bash
python app.py
```

---

## Deactivating Virtual Environment

When done, deactivate the virtual environment:

```bash
# Any OS
deactivate
```

---

## Production Deployment

For deploying to production, use:
- **Gunicorn** (production WSGI server)
- **Docker** (containerization)
- **Heroku, PythonAnywhere, AWS** (hosting platforms)

But for learning and development, `python app.py` is perfect!

---

## Next Steps

1. ✅ Run the backend server
2. ✅ Test API endpoints
3. ✅ Connect frontend to backend
4. ✅ Add tasks through the web interface
5. ✅ Explore the code and make modifications

Happy coding! 🚀
