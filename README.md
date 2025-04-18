# Task Manager API - Coding Challenge

**Duration:** 60 minutes  
**Goal:** Assess Django fundamentals, REST API design, and practical coding ability

---

## Scenario

You’re building a backend API for a simple Task Manager. Users can:

- Create tasks  
- Mark them complete  
- Filter/sort them based on priority and due dates  

---

## Requirements

### 1. Model: `Task`

Create a Django model with the following fields:

| Field        | Type         | Notes                                |
|--------------|--------------|--------------------------------------|
| `id`         | AutoField    | Primary key                          |
| `title`      | CharField    | Required                             |
| `description`| TextField    | Optional                             |
| `priority`   | IntegerField | 1 = High, 2 = Medium, 3 = Low        |
| `due_date`   | DateField    |                                      |
| `completed`  | BooleanField | Default = `False`                    |
| `created_at` | DateTimeField| Auto set on creation (`auto_now_add`) |

---

### 2. REST API Endpoints (Use Django REST Framework)

| Method | Endpoint       | Description                            |
|--------|----------------|----------------------------------------|
| POST   | `/tasks/`      | Create a new task                      |
| GET    | `/tasks/`      | List all tasks                         |
| GET    | `/tasks/<id>/` | Get task details                       |
| PATCH  | `/tasks/<id>/` | Partially update a task (e.g., mark as complete) |
| DELETE | `/tasks/<id>/` | Delete a task                          |

---

### 3. Filters / Features

- Filter by `completed=true/false`
- Order by `due_date` or `priority`

---

### 4. Bonus (Optional)

If time permits:

- Add a `/tasks/summary/` endpoint returning:

```json
{
  "total": 10,
  "completed": 6,
  "pending": 4,
  "overdue": 1
}
```

> A task is considered **overdue** if its `due_date` is before today and it is not marked completed.

- Add **pagination** to the list endpoint

---

## Submission Instructions

- You can write everything in one Django project
- No need to build authentication
- You can run it locally and test with Postman, Swagger, or curl
