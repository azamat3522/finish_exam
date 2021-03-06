from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from accounts.forms import SignUpForm
from webapp.models import File


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('accounts:login')


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['user_obj'])
        files = context['user_obj'].users_file.order_by('-created_date')
        self.paginate_files_to_context(files, context)
        return context

    def paginate_files_to_context(self, files, context):
        paginator = Paginator(files, 10, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['files'] = page.object_list
        context['is_paginated'] = page.has_other_pages()

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     print(queryset)
    #     queryset = queryset.filter(type='common')
    #     return queryset

