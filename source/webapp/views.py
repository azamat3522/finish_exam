from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView

from webapp.forms import FileForm, SimpleSearchForm
from webapp.models import File


class IndexView(ListView):
    model = File
    template_name = 'index.html'
    context_object_name = 'files'
    paginate_by = 10
    paginate_orphans = 2
    ordering = '-created_date'

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_query = self.get_search_query()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if self.search_query:
            context['query'] = urlencode({'search': self.search_query})
        context['form'] = self.form
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_query:
            queryset = queryset.filter(
                Q(name__icontains=self.search_query)
            )
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_query(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class FileView(DetailView):
    model = File
    template_name = 'detail.html'


class FileCreateView(CreateView):
    model = File
    form_class = FileForm
    template_name = 'create.html'

    def form_valid(self, form):
        if str(self.request.user) != 'AnonymousUser':
            form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:index')


class FileDeleteView(DeleteView):
    template_name = 'delete.html'
    model = File
    context_object_name = 'file'
    success_url = reverse_lazy('webapp:index')


class FileUpdateView(UpdateView):
    form_class = FileForm
    template_name = 'update.html'
    model = File
    context_object_name = 'file'


    def get_success_url(self):
        return reverse('webapp:file_detail', kwargs={'pk': self.object.pk})





