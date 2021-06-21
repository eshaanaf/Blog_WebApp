from theblog.models import Post
from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView,DetailView , CreateView , UpdateView , DeleteView
from .models import Categories, Comment, Post 
from .forms import PostForm , EditForm , CategoryForm,CommentForm
from django.urls import reverse_lazy , reverse
from django.http import HttpResponseRedirect

# def home(request):
#     return render(request , 'home.html' , {})
# Create your views here.

def LikeView(request , pk):
    post  = Post.objects.get(id = pk)
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail' , args= [str(pk)] ))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-post_date']

    def get_context_data(self , *args , **kwargs):
        cat_menu = Categories.objects.all()
        context = super(HomeView , self).get_context_data(*args , **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request ,cats):
    category_posts = Post.objects.filter(category = cats)
    return render(request , 'categories.html' , {'cats' : cats.title() , 'category_posts': category_posts})



class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    def get_context_data(self , *args , **kwargs):
        cat_menu = Categories.objects.all()
        context = super(ArticleDetailView , self).get_context_data(*args , **kwargs)
        stuff = get_object_or_404(Post , id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True


        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name ='add_post.html'
    # fields ='__all__'
    def get_context_data(self , *args , **kwargs):
        cat_menu = Categories.objects.all()
        context = super(AddPostView , self).get_context_data(*args , **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddCategoryView(CreateView):
    model = Categories
    form_class = CategoryForm
    template_name ='add_category.html'
    def get_context_data(self , *args , **kwargs):
        cat_menu = Categories.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args , **kwargs)
        context["cat_menu"] = cat_menu
        return context

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm
    def get_context_data(self , *args , **kwargs):
        cat_menu = Categories.objects.all()
        context = super(UpdatePostView , self).get_context_data(*args , **kwargs)
        context["cat_menu"] = cat_menu
        return context

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    def get_context_data(self , *args , **kwargs):
        cat_menu = Categories.objects.all()
        context = super(DeletePostView , self).get_context_data(*args , **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name ='add_comment.html'
    
    def form_valid(self , form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')