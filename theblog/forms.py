from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Post , Categories, Comment

choices = Categories.objects.all().values_list('name', 'name')

choice_list  = []
for item in choices:
    choice_list.append(item)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title' , 'title_tag' , 'author' ,'category' , 'body' , 'snippet' ,'header_image')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control' , 'id' : 'elder' , 'value': '' , 'type':'hidden'}),
            # 'author' : forms.Select(attrs={'class': 'form-control'}),
            'category' : forms.Select( choices = choice_list ,attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title' , 'body', 'snippet')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            # 'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            # 'author' : forms.Select(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name' , 'body')

        widgets = {
            'Name' : forms.TextInput(attrs={'class': 'form-control'}),
            # 'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            # 'author' : forms.Select(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),   
        }