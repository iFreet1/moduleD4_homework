from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post
from .filters import NewsFilter
from .forms import PostForm
from django.core.paginator import Paginator


class NewsList(ListView):
    model = Post
    template_name = "news.html"
    context_object_name = "news"
    queryset = Post.objects.order_by('-create_date')
    paginate_by = 10
    form_class = PostForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)


class SearchList(ListView):
    model = Post
    template_name = "search.html"
    context_object_name = "news"
    queryset = Post.objects.order_by('-create_date')
    paginate_by = 10
    form_class = PostForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)


class NewsDetail(DetailView):
    model = Post
    template_name = "article.html"
    context_object_name = "article"
    queryset = Post.objects.all()


class PostDetailView(DetailView):
    template_name = 'news_detail.html'
    queryset = Post.objects.all()


class NewsCreateView(CreateView):
    template_name = 'news_create.html'
    form_class = PostForm


class NewsUpdateView(UpdateView):
    template_name = 'news_create.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class NewsDeleteView(DeleteView):
    template_name = 'news_delete.html'
    context_object_name = "article"
    success_url = '/news/'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)