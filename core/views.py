from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import User, Project, Task
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')   # send to login page

# 🔐 LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html')


# 🆕 SIGNUP
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = User.objects.create_user(
            username=username,
            password=password,
            role=role
        )

        login(request, user)
        return redirect('dashboard')

    return render(request, 'signup.html')


# 📊 DASHBOARD
@login_required
def dashboard(request):
    if request.user.role == 'admin':
        projects = Project.objects.all()
        tasks = Task.objects.all()
    else:
        projects = Project.objects.filter(created_by=request.user)
        tasks = Task.objects.filter(assigned_to=request.user)

    return render(request, 'dashboard.html', {
        'projects': projects,
        'tasks': tasks
    })


# ➕ CREATE PROJECT
@login_required
def create_project(request):
    if request.method == "POST":
        name = request.POST['name']

        Project.objects.create(
            name=name,
            created_by=request.user
        )
        return redirect('dashboard')

    return render(request, 'create_project.html')


# 📝 CREATE TASK
@login_required
def create_task(request):
    if request.method == "POST":
        title = request.POST['title']
        project_id = request.POST['project']
        user_id = request.POST['user']

        Task.objects.create(
            title=title,
            project_id=project_id,
            assigned_to_id=user_id
        )
        return redirect('dashboard')

    users = User.objects.all()
    projects = Project.objects.all()

    return render(request, 'create_task.html', {
        'users': users,
        'projects': projects
    })


# ✅ MARK DONE
@login_required
def mark_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.status = 'done'
    task.save()

    return redirect('dashboard')