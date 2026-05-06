# Task Manager

A simple web-based task management application built with Django. It supports role-based access for admins and members, allowing teams to manage projects and track tasks.

## Features

- **Authentication** – User sign-up, login, and logout
- **Role-based access** – Admin users can view all projects and tasks; members see only their own
- **Projects** – Create and manage projects
- **Tasks** – Create tasks, assign them to users, and mark them as done

## Tech Stack

- **Backend:** Django 5.0
- **Database:** SQLite (default)
- **Static files:** WhiteNoise
- **Server:** Gunicorn

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/shahanawaj-bumblebee/taskmanager.git
   cd taskmanager
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

4. **Collect static files**

   ```bash
   python manage.py collectstatic --noinput
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   The app will be available at `http://127.0.0.1:8000/`.

> **Note:** Steps 2–4 are also bundled in `build.sh` for convenience.

## URL Reference

| URL | View | Description |
|-----|------|-------------|
| `/` | `login_view` | Login page |
| `/signup/` | `signup` | Register a new user |
| `/dashboard/` | `dashboard` | Main dashboard |
| `/create-project/` | `create_project` | Create a new project |
| `/create-task/` | `create_task` | Create and assign a task |
| `/done/<task_id>/` | `mark_done` | Mark a task as done |
| `/logout/` | `logout_view` | Log out |

## User Roles

| Role | Permissions |
|------|-------------|
| `admin` | View and manage all projects and tasks |
| `member` | View and manage only their own projects and assigned tasks |
