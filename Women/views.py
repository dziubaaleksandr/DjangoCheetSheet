from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddPostForm, AddPostFormRelatedWithDB
from .models import Women, Category
from django.views.generic import ListView, DetailView, CreateView
from .utils import *
#menu = ['home', 'women', 'add page', 'about']

class WomenHome(DataMixin, ListView):
    model = Women #Select all records from the table and try to display them as a list
    template_name = 'women/index.html' #The path to the required html file 
    #context_object_name = 'posts' #Put list records from the table in posts 
    #extra_context = {'title': 'Home Page'} #Passing ONLY static data
    #=============With Mixin============
    def get_context_data(self, *, object_list=None, **kwargs):  #Passing static and dynamic data
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Home Page')
        return dict(list(context.items()) + list(c_def.items()))
    
    #=============Without Mixin============
    # def get_context_data(self, *, object_list=None, **kwargs):  #Passing static and dynamic data
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Home Page'
    #     context['menu'] = menu
    #     return context

    # def get_queryset(self): #Return list with elemts that meets the filter criteria
    #     return Women.objects.filter(is_published = True)

class WomenCategory(DataMixin, ListView):
    model = Category
    template_name = "women/women.html"
    context_object_name = 'cats'
    #=============Without Mixin============
    def get_context_data(self, *, object_list=None, **kwargs):  #Passing static and dynamic data
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context['women'] = Women.objects.filter(cat__slug = self.kwargs['cat_slug'], is_published = True)
        return {**context, **c_def}
    #=============Without Mixin============
    # def get_context_data(self, *, object_list=None, **kwargs):  #Passing static and dynamic data
    #     context = super().get_context_data(**kwargs)
    #     context['women'] = Women.objects.filter(cat__slug = self.kwargs['cat_slug'], is_published = True)
    #     context['menu'] = menu
    #     return context
    
    # def get_queryset(self) -> QuerySet[Any]:
    #     return Category.objects.all()

class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = "women/post.html"
    context_object_name = 'post'
    slug_url_kwarg = "post_slug" #specify the name of slug
    #=============Without Mixin============
    def get_context_data(self, *, object_list=None, **kwargs):  #Passing static and dynamic data
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'post')
        return dict(list(context.items()) + list(c_def.items()))
    #=============Without Mixin============
    # def get_context_data(self, *, object_list=None, **kwargs):  #Passing static and dynamic data
    #     context = super().get_context_data(**kwargs)
    #     # context['title'] = Women.objects.filter(slug = self.kwargs['post_slug'])[0]
    #     context['title'] = context['post']
    #     context['menu'] = menu
    #     return context

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostFormRelatedWithDB
    template_name = 'women/addPage.html'
    #success_url = reverse_lazy('home') #We have to set this variable if we haven't got get_absolute_url in model or we want to redirect to url that is not listed in get_absolute_url
    login_url = '/admin/' #If the user is unautharised django redirect him to admin page
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Add Post')
        return dict(list(context.items()) + list(c_def.items()))
    
    
# Create your views here.


# def index(request):
#     context = {
#         'menu': menu,
#         'title': "Home Page",
#         }
#     return render(request, "women/index.html", context = context)

class ShowWomen(DataMixin, ListView):
    paginate_by = 3
    model = Women
    template_name = "women/women.html"
    context_object_name = 'women'
    def get_context_data(self, *, object_list=None, **kwargs):  #Passing static and dynamic data
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context['cats'] = Category.objects.all()
        return {**context, **c_def}

def women(request):
    women = Women.objects.all()
    cats = Category.objects.all()
    return render(request, 'women/women.html', {'women': women, 'menu': menu, 'cats': cats})

# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug = post_slug) #We are taking the record from Women model with slug equal to post_slug. If there isn't such record it raises 404 error
#     context = {
#         'post': post,
#         'title': post.title,
#         'menu': menu
#         }
#     return render(request, 'women/post.html', context= context)

# def show_category(request, category_id):
#     women = Women.objects.filter(cat_id = category_id)
#     cats = Category.objects.all()
#     return render(request, 'women/women.html', {'women': women, 'menu': menu, 'cats': cats})

def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            #form = AddPostForm()
            try:
                Women.objects.create(**form.cleaned_data) #Add new post to db Women
                return redirect('home')
            except:
                form.add_error(None, "Add post error") #If an error occurs at the time of adding the new record to db. To display this error we shoild use form.non_filed_errors in html file
    else:
        form = AddPostForm()
    return render(request, 'women/addPage.html', {'menu': menu, 'form': form})

# def add_page_related_with_db(request):
#     if request.method == 'POST': #Check has the customer already posted the data
#         form = AddPostFormRelatedWithDB(request.POST)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             #form = AddPostForm()
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostFormRelatedWithDB()
#     return render(request, 'women/addPage.html', {'menu': menu, 'form': form})

def about(request):
    return HttpResponse("<h1>About</h1>")

def categories(request, catId):
    if catId == 4:
        return redirect("/cats/1") #http 302
    elif catId == 5:
        return redirect("home", permanent=True) #http 301
    elif catId > 5:
        raise Http404()
    return HttpResponse("<h1>CatId:{}</h1>".format(catId))

def get_test(request):
    if(request.GET):
        print(request.GET)
    return HttpResponse("<h1>Get TEST</h1>")

def pageNotFound(request, Exception):
    return HttpResponseNotFound("<h1>Page not Found</h1>")











