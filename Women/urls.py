from django.urls import path
from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name = "home"),
    path('women/', women, name = "women"),
    path('about/', about, name = "about"),
    path('cats/<int:catId>/', categories),
    path('getTest/', get_test),
    #path('posts/<slug:post_slug>/', show_post, name = 'post'),
    path('posts/<slug:post_slug>/', ShowPost.as_view(), name = 'post'),
    #path('women/category/<int:category_id>/', show_category, name = 'category'),
    path('women/category/<slug:cat_slug>/', WomenCategory.as_view(), name = 'category'),
    # path('addPage', add_page_related_with_db, name = 'add page')
    path('addPage', AddPage.as_view(), name = 'add page')

]
