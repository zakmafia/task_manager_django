from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from .forms import OrderForm, TaskForm
from .models import Task, Order

# Create your views here.
def home(request):
    return render(request, 'home.html')

def create_order(request):
    submitted = False
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.slug = slugify(order.name)
            order.save()
            return HttpResponseRedirect('/create_order?submitted=True')
        else:
            print(form.errors)
            return HttpResponseRedirect('/create_order?error')
    else:
        form = OrderForm
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'form': form,
        'submitted': submitted
    }
    return render(request, 'task_controller/create_order.html', context)

def create_task(request):
    submitted = False
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create_task?submitted=True')
        else:
            print(form.errors)
            return HttpResponseRedirect('/create_task?error')
    else:
        form = TaskForm
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'form': form,
        'submitted': submitted
    }
    return render(request, 'task_controller/create_task.html', context)

def view_order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    context = {
        'orders': orders,
        'orders_count': orders_count
    }
    return render(request, 'task_controller/view_order.html', context)

def view_task(request, slug):
    order = get_object_or_404(Order, slug=slug)
    tasks = Task.objects.filter(order=order, is_finished=False)
    tasks_count = tasks.count()
    request.session['slug'] = slug
    context = {
        'tasks': tasks,
        'tasks_count': tasks_count,
    }
    return render(request, 'task_controller/view_task.html', context)

def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('view_order')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    slug = request.session.get('slug')
    return HttpResponseRedirect('/view_task/' + slug)

def edit_order(request, order_id):
    order = Order.objects.get(id=order_id)
    name = order.name
    try:
        if request.method == "POST":
            name = request.POST['name']
            file = request.FILES['file'] if 'file' in request.FILES else False
            if file is not False:
                order.images = file
            order.name = name
            order.slug = slugify(order.name)
            order.save()
            return HttpResponseRedirect('/edit_order/' + order_id)
    except:
        return HttpResponseRedirect('/edit_order/' + order_id + '?not_edited')
    context = {
        'name': name,
        'order': order,
    }
    return render(request, 'task_controller/edit_order.html', context)

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    name = task.name
    try:
        if request.method == "POST":
            name = request.POST['name']
            task.name = name
            task.save()
            return HttpResponseRedirect('/edit_task/' + task_id)
    except:
        return HttpResponseRedirect('/edit_task/' + task_id + '?not_edited')
    context = {
        'name': name,
        'task': task,
    }
    return render(request, 'task_controller/edit_task.html', context)

def do_task(request, task_id):
    task = Task.objects.get(id=task_id)
    name = task.name

    time_stored = task.time_counter if task.time_counter else ""
    time_stored_hour = task.time_counter.hour if task.time_counter else ""
    time_stored_minute = task.time_counter.minute if task.time_counter else ""
    time_stored_second = task.time_counter.second if task.time_counter else ""

    try:
        if 'store_paused_data' in request.POST:
            time = request.POST['time_counter']
            task.time_counter = time
            task.save()
            task = Task.objects.get(id=task_id)
            time_stored = task.time_counter
            time_stored_hour = task.time_counter.hour
            time_stored_minute = task.time_counter.minute
            time_stored_second = task.time_counter.second

        if 'stop_save' in request.POST:
            time = request.POST['time_counter']
            task.time_counter = time
            task.is_finished = True
            task.save()
            return redirect('finished_tasks')
    except:
        pass
    context = {
        'name': name,
        'task': task,
        'time_stored': time_stored,
        'time_stored_hour': time_stored_hour,
        'time_stored_minute': time_stored_minute,
        'time_stored_second': time_stored_second,
    }
    return render(request, 'task_controller/do_task.html', context)

def view_finished_tasks(request):
    tasks = Task.objects.filter(is_finished=True)
    tasks_count = tasks.count()
    context = {
        'tasks': tasks,
        'tasks_count': tasks_count,
    }
    return render(request, 'task_controller/finished_tasks.html', context)