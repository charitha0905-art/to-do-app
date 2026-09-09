# To-Do App - Full Stack (Frontend + Backend)

A complete to-do application with HTML/CSS/Bootstrap frontend and Python Flask backend.

---

## 📁 Project Structure

```
todoapp/
├── index.html              # Main HTML file (frontend)
├── style.css               # CSS styling
├── script.js               # Frontend-only JavaScript (in-memory)
├── script_backend.js       # Backend-integrated JavaScript
├── app.py                  # Flask backend API
├── requirements.txt        # Python dependencies
└── tasks.db               # SQLite database (auto-created)
```

---

## 🚀 Quick Start

### Option 1: Frontend Only (No Backend)
1. Open `index.html` in a browser
2. Use `script.js` (default) for in-memory tasks

### Option 2: Frontend + Backend (Recommended)
#### Step 1: Setup Python Backend

```bash
# Install dependencies
pip install -r requirements.txt

# Run Flask server
python app.py
```

Backend will start at `http://localhost:5000`

#### Step 2: Update Frontend

Replace the script source in `index.html`:
```html
<!-- Change from: -->
<script src="script.js"></script>

<!-- To: -->
<script src="script_backend.js"></script>
```

#### Step 3: Open Frontend
Open `index.html` in your browser and start using the app!

---

## 📡 API Endpoints

### Get All Tasks
```
GET /api/tasks
```
**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "text": "Buy groceries",
      "completed": false,
      "created_at": "2026-09-09 10:30:45"
    }
  ],
  "count": 1
}
```

### Get Single Task
```
GET /api/tasks/<task_id>
```

### Create Task
```
POST /api/tasks
Content-Type: application/json

{
  "text": "Buy groceries"
}
```

### Update Task
```
PUT /api/tasks/<task_id>
Content-Type: application/json

{
  "text": "Buy groceries and fruits",
  "completed": true
}
```

### Toggle Task Completion
```
PATCH /api/tasks/<task_id>/toggle
```

### Delete Task
```
DELETE /api/tasks/<task_id>
```

### Delete All Tasks
```
DELETE /api/tasks
```

### Health Check
```
GET /api/health
```

---

## ⚙️ Tech Stack

### Frontend
- **HTML5** — Semantic structure
- **CSS3** — Custom styling with animations
- **Bootstrap 5** — Responsive layout
- **JavaScript** — DOM manipulation & API calls

### Backend
- **Python 3.x** — Programming language
- **Flask** — Web framework
- **Flask-SQLAlchemy** — Database ORM
- **Flask-CORS** — Cross-Origin Resource Sharing
- **SQLite** — Lightweight database

---

## 🎯 Features

### Frontend
✅ Add tasks via form  
✅ Mark tasks complete (strikethrough)  
✅ Delete individual tasks  
✅ Task counter (remaining tasks)  
✅ Responsive design (mobile-friendly)  
✅ Smooth animations  

### Backend
✅ RESTful API endpoints  
✅ Persistent data storage (SQLite)  
✅ CRUD operations (Create, Read, Update, Delete)  
✅ Error handling & validation  
✅ CORS enabled for frontend requests  

---

## 🔄 How It Works

### Frontend-Only Mode (script.js)
- Tasks stored in JavaScript array
- No persistence (resets on page refresh)
- No backend required

### Full Stack Mode (script_backend.js)
1. User submits form
2. JavaScript sends API request to Flask server
3. Flask validates and stores task in SQLite database
4. Frontend updates UI with response
5. Tasks persist across page refreshes

---

## 📝 Database Schema

### Tasks Table
```sql
CREATE TABLE task (
    id INTEGER PRIMARY KEY,
    text VARCHAR(200) NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🛠️ Development Tips

### Running Backend in Debug Mode
```bash
python app.py
```

### Database Management
- Database file: `tasks.db`
- To reset: Delete `tasks.db` and restart Flask
- Tables auto-create on first run

### Testing API with curl
```bash
# Get all tasks
curl http://localhost:5000/api/tasks

# Create task
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"text": "My task"}'

# Toggle task
curl -X PATCH http://localhost:5000/api/tasks/1/toggle

# Delete task
curl -X DELETE http://localhost:5000/api/tasks/1
```

---

## 🐛 Troubleshooting

### Backend Connection Error
- Ensure Flask is running on port 5000
- Check browser console for CORS errors
- Verify `script_backend.js` is linked in HTML

### Database Issues
- Delete `tasks.db` to reset database
- Restart Flask server after changes
- Check file permissions in project folder

### CORS Errors
- Flask-CORS is included in `app.py`
- Ensure frontend is on a different origin than backend
- Check browser console for specific CORS errors

---

## 📚 Learning Outcomes

By working through this project, you'll learn:

**Frontend Skills**
- HTML semantic structure & forms
- CSS styling & animations
- Bootstrap framework usage
- Vanilla JavaScript & DOM manipulation
- Async/await & fetch API
- Error handling & user feedback

**Backend Skills**
- Python fundamentals
- Flask web framework basics
- RESTful API design
- Database design with SQLalchemy
- CRUD operations
- Error handling & validation
- CORS and cross-origin requests

---

## 📄 License

This project is open-source and free to use for learning purposes.

---

## 🎓 For Students

This is a beginner-friendly full-stack project perfect for learning:
- Frontend-backend communication
- API design principles
- Database persistence
- Separation of concerns (frontend vs backend)
- HTTP methods (GET, POST, PUT, DELETE)

Happy coding! 🚀
