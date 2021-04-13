from msilib.schema import ListView

from django.shortcuts import render, redirect
from . models import task
from . forms import Todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
class TaskListView(ListView):
    model = task
    template_name = "task_view.html"
    context_object_name = 'obj1'

class TaskDetailView(DetailView):
    model = task
    template_name = "detail.html"
    context_object_name = 'i'

class TaskUpdateView(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('taskdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = task
    template_name = "delete.html"
    success_url = reverse_lazy("taskview")





def task_view(request):
    if request.method=='POST':
        name = request.POST.get("name")
        priority = request.POST.get("priority")
        date = request.POST.get("date")
        obj = task(name=name,priority=priority,date=date)
        obj.save()
    obj1 = task.objects.all()

    return render(request,"task_view.html",{"obj1":obj1})

def delete(request,id):
    if request.method=='POST':
        Task=task.objects.get(id=id)
        Task.delete()
        return redirect("task_view")
    return render(request,"delete.html")

def clear_all(request):
    if request.method == 'POST':
        Task=task.objects.all()
        Task.delete()
        return redirect('task_view')
    return render(request,"clear_all.html")


def update(request,id):
    Task = task.objects.get(id=id)
    form = Todoform(request.POST or None,instance=Task)
    if form.is_valid():
        form.save()
        return redirect("task_view")
    return render(request,"edit.html",{'task':task,'form':form})
