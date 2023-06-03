from django.db import models
from django.urls import reverse

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name= 'Title') #verbose_name to change name in admin panel
    slug = models.SlugField(max_length=255, unique=True, db_index = True, verbose_name="URL")
    content = models.TextField(blank = True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_change = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs = {'post_slug': self.slug})
    
    class Meta:
        verbose_name = "Famous women" #Change name in admin panel
        verbose_name_plural = "Famous women" #To remove plural 's' in name
        ordering = ['title'] #To set sorting setting in admin's panel. If we set '-title' we get reverse order
    
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True) #db_index = True means that this firld is indexed and search in db will be a little faster 
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name="URL")
    def get_absolute_url(self):
        #return reverse('category', kwargs = {'category_id': self.pk})
        return reverse('category', kwargs = {'cat_slug': self.slug})
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Category" #Change name in admin panel
        verbose_name_plural = "Categories" #To remove plural 's' in name
        ordering = ['id'] #To set sorting setting in admin's panel. If we set '-title' we get reverse order
    