from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

# Create your views here.


# def home(request):
#     return render(request, 'home/home.html')

class HomeView(ListView):
    model = Post
    template_name = 'home/home.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class SearchPostView(ListView):
    model = Post
    template_name = 'home/search.html'

    def get_queryset(self):
        busqueda = self.request.GET.get('kword', '')
        return Post.objects.lista_post(busqueda).order_by('-id')


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'home/article_details.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'home/add_post.html'
    fields = ['title', 'category', 'author', 'body']


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'home/update_post.html'
    fields = ['title', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'home/delete_post.html'
    success_url = reverse_lazy('home')


def CatListView(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category=category).order_by('-id')
    return render(request, 'home/category_post.html', {'category': category, 'posts': posts})


def ContactView(request):
    if request.method == 'POST':
        message_web = request.POST['message']
        from_email = request.POST['from_email']
        message = f'Mensaje: "{message_web}" de {from_email}'
        subject = request.POST['subject']

        # Enviar el correo
        send_mail(subject, message, from_email, [
                  'ivanlegranbizarro@gmail.com'], fail_silently=False)

        return render(request, 'home/contact.html', {'message': message, 'from_email': from_email, 'subject': subject})

    else:
        return render(request, 'home/contact.html', {})
