from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Entry

class HomeView(ListView):
    template_name = 'html/index.html'
    queryset = Entry.objects.order_by('-created_at')


class EntryDetail(DetailView):
    template_name = 'html/entry_detail.html'
    model = Entry
