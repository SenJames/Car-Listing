# from django import forms
# from listing_app.models import *
# from blog.models import Post, Category, Author, Comment
# from listing_app.models import UserProfile
# from django.forms import ModelForm
# from django.contrib.auth.models import User, auth
# from django.core import validators

# class AuthorForm(forms.ModelForm):
#     author = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=50)
#     class Meta:
#         model = Author
#         fields = ("author",)


# class PostForm(forms.ModelForm):
    
#     class Meta:
#         model = Post
#         fields = ("",)

# class CategoryForm(forms.ModelForm):
#     cat_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
#     desc = models.TextField(blank=True, null=True, verbose_name='Description')
#     class Meta:
#         model = Category
#         fields = ("",)

# class CommentForm(forms.ModelForm):
    
#     class Meta:
#         model = Comment
#         fields = ("",)
