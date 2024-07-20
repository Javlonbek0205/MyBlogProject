from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # (LoginRequiredMixin) bu foydalanuvchini login qilmasdan saytga kirishini taqiqlaydi, (UserPassesTestMixin) bu esa foydalanuvchini haqiqiy avtorimi yoki yo`q tekshiradi
from django.views.generic import ListView, DetailView, CreateView # article model uchun listview dan foydalanildi
from django.views.generic.edit import UpdateView, DeleteView
from .models import Article, Comment # view hosil qilish uchun Article modeli chaqirildi
from  django.urls import reverse_lazy
from .forms import  CommentForm

# Create your views here.
class ArticleListView(LoginRequiredMixin,ListView):
  model = Article
  template_name = 'article_list.html'

class ArticleDetailView(DetailView):
  model = Article
  template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin,  UserPassesTestMixin, UpdateView):
  model = Article
  fields = ('title', 'summary', 'body', 'photo')
  template_name = 'article_edit.html'

  def test_func(self):
    obj =self.get_object()
    return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Article
  template_name = 'article_delete.html'
  success_url = reverse_lazy('article_list')

  def test_func(self):
    obj =self.get_object()
    return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
  model = Article
  template_name = 'article_new.html'
  fields = ('title', 'summary', 'body', 'photo',)

  def form_valid(self, form):
    #bu funksiya authorni avtomat ravishda o`zi qo`yib qo`yadi
    form.instance.author = self.request.user
    return super().form_valid(form)

  def test_func(self):
    return self.request.user.is_superuser


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'

    def form_valid(self, form):
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.kwargs['pk']})