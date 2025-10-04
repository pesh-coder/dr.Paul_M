from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    
    # Projects
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    
    # Awards
    path('awards/', views.AwardListView.as_view(), name='awards'),
    
    # Gallery
    path('gallery/', views.gallery, name='gallery'),
    
    # Blog
    #path('blog/', views.BlogListView.as_view(), name='blog'),
    #path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    
    # Testimonials
    path('testimonials/', views.testimonials, name='testimonials'),
    
    # AJAX endpoints
    path('api/contact/', views.contact_ajax, name='contact_ajax'),
]
