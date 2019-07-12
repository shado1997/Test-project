from django.shortcuts import render
from .models import Groups, Users
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import UpdateUserForm, CreateUserForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

class UsersListView(generic.ListView):
    model = Users
    template_name = 'list_of_users.html'

class GroupsListView(generic.ListView):
    model = Groups
    template_name = 'list_of_groups.html'
    
class UsersDelete(DeleteView):
    Users.objects.update()
    model = Users
    template_name = 'users_confirm_delete.html'
    success_url = reverse_lazy('list_of_users')

class GroupsCreate(CreateView):
    Users.objects.update()
    model = Groups
    fields = ['name', 'description']
    Groups.objects.update()
    template_name = 'groups_form.html'
    success_url = reverse_lazy('list_of_groups')

class GroupsUpdate(UpdateView):
    Users.objects.update()
    model = Groups
    fields = ['name','description']
    template_name = 'groups_form.html'
    Groups.objects.update()
    success_url = reverse_lazy('list_of_groups')

def update_user(request, pk):
    user_inst=get_object_or_404(Users, id = pk)
    user_ip = str(user_inst)
    baba = user_ip.split(sep=None, maxsplit=-1)[2]
    bob = baba.split('(')[1]
    user_id = bob.split(')')[0]
    if request.method == 'POST':
        form = UpdateUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            group_id = form.cleaned_data.get('group')
            group = Groups.objects.get(id=group_id)
            Users.objects.filter(id=user_id).update(name=name, group=group)
            return redirect('list_of_users')
        return HttpResponse("Invalid data", status=400)
    form = UpdateUserForm()
    return render(request, 'update_user.html', {'form': form})

def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            group_id = form.cleaned_data.get('group')
            group = Groups.objects.get(id=group_id)
            Users(name=name, group=group).save()
            return redirect('list_of_users')
        return HttpResponse("Invalid data", status=400)
    form = CreateUserForm()
    return render(request, 'create_user.html', {'form': form})

def delete_group(request, pk):
    group_name=get_object_or_404(Groups, id = pk)
    if request.method == "POST":
        res = Users.objects.filter(group=group_name)
        string_res = str(res)
        lenght_of_empty_group = 15
        if len(string_res) < lenght_of_empty_group:
            Groups.objects.get(name=group_name).delete()
            redirect('list_of_groups')
        else:
            messages.error(request, "At list one member already in this group")
    HttpResponse("Invalid data", status=400)
    context = {'group_name': group_name}
    return render(request, 'delete_group.html', context)

