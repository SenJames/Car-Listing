from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.
"""
Blog Should have a 
1. Post
2. Author
3. Category
4. Comments
"""


class Author(models.Model):
    """
    This model takes the author details
    """
    author = models.OneToOneField(User, related_name='author', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.author.first_name
    
    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})


class Category(models.Model):
    """
    This model takes the category of the post
    """
    cat_name = models.CharField(max_length=100, verbose_name='Category Name')
    desc = models.TextField(blank=True, null=True, verbose_name='Description')

    def __str__(self):
        return self.cat_name

class Post(models.Model):
    """
    This model takes the diverse posts
    """
    pst_title = models.CharField(max_length=150, verbose_name='Post Title')
    pst_img = models.ImageField(blank=True, null=True, upload_to='uploads/')
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, blank=True)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pst_title

class Comment(models.Model):
    
    name = models.CharField(verbose_name="Name", max_length=50)
    email= models.EmailField(verbose_name="Email", max_length=254)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(blank=True, auto_now=True)

    def title(self):
        if len(self.comment) >= 5:
            title = self.comment.split()[:4]
            return " ".join(title) + "..."
        else:
            return '...'


    def __str__(self):
        return self.comment.title()



