from django.shortcuts import render, redirect
from .models import Cource
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


def mainpage(request):
    return render(request, 'mainapp/mainpage.html')

class CreateCource(LoginRequiredMixin,CreateView):
    model = Cource
    template_name ='mainapp/add_cource.html'
    fields = ['slug', 'titel', 'description','img']

    def form_valid(self, form):
        form.instance.name = self.request.user
        # super().form_valid(form)
        messages.success(self.request, f'Курс успешно добавлен')
        return redirect('add_cource')



class SeeCourcePaige(ListView):
    model = Cource
    template_name = 'mainapp/all_cource.html'
    context_object_name = 'slug'
    ordering = ['-slug']