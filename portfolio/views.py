from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, TemplateView
from django.core.mail import send_mail
from django.conf import settings
from django.db import models
from blogcms.models import BlogPage          # <-- Wagtail page model
from .models import (
    Bio, Project, Award, GalleryImage, BlogPost, 
    Testimonial, Message, SiteSettings
)
import json


def home(request):
    """Home page view with featured content"""
    context = {
        'bio': Bio.objects.first(),
        'featured_projects': Project.objects.filter(featured=True)[:3],
        'featured_awards': Award.objects.filter(featured=True)[:3],
        'featured_gallery': GalleryImage.objects.filter(featured=True)[:6],
        'featured_blog_posts': BlogPost.objects.filter(featured=True, published=True)[:3],
        'featured_testimonials': Testimonial.objects.filter(featured=True)[:3],
        'site_settings': SiteSettings.objects.first(),
    }
    return render(request, 'portfolio/home.html', context)


def about(request):
    """About page view"""
    bio = get_object_or_404(Bio)
    context = {
        'bio': bio,
        'site_settings': SiteSettings.objects.first(),
    }
    return render(request, 'portfolio/about.html', context)


class ProjectListView(ListView):
    """List view for all projects"""
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    paginate_by = 6

    def get_queryset(self):
        return Project.objects.all().order_by('-start_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        return context


class ProjectDetailView(DetailView):
    """Detail view for individual projects"""
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        return context


class AwardListView(ListView):
    """List view for all awards"""
    model = Award
    template_name = 'portfolio/awards.html'
    context_object_name = 'awards'
    paginate_by = 9

    def get_queryset(self):
        return Award.objects.all().order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        return context


def gallery(request):
    """Gallery page view with category filtering"""
    category = request.GET.get('category', '')
    images = GalleryImage.objects.all()
    
    if category:
        images = images.filter(category=category)
    
    images = images.order_by('-date')
    
    # Pagination
    paginator = Paginator(images, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'categories': GalleryImage.CATEGORY_CHOICES if hasattr(GalleryImage, 'CATEGORY_CHOICES') else [],
        'current_category': category,
        'site_settings': SiteSettings.objects.first(),
    }
    return render(request, 'portfolio/gallery.html', context)


class BlogListView(ListView):
    template_name = 'portfolio/blog.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        # Only live (published) Wagtail pages, newest first
        return BlogPage.objects.live().public().order_by('-first_published_at')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['site_settings'] = SiteSettings.objects.first()
        return ctx


class BlogDetailView(TemplateView):
    template_name = 'portfolio/blog_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        post = get_object_or_404(
            BlogPage.objects.live().public(),
            slug=kwargs['slug']
        )
        ctx['post'] = post
        ctx['site_settings'] = SiteSettings.objects.first()
        return ctx


def testimonials(request):
    """Testimonials page view"""
    testimonials = Testimonial.objects.all().order_by('-created_at')
    context = {
        'testimonials': testimonials,
        'site_settings': SiteSettings.objects.first(),
    }
    return render(request, 'portfolio/testimonials.html', context)


def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Create message object
        Message.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Send email notification (if configured)
        try:
            send_mail(
                f'New Contact Form Message: {subject}',
                f'From: {name} ({email})\n\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=True,
            )
        except:
            pass  # Email sending is optional
        
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
        return redirect('portfolio:contact')
    
    context = {
        'site_settings': SiteSettings.objects.first(),
    }
    return render(request, 'portfolio/contact.html', context)


@csrf_exempt
@require_http_methods(["POST"])
def contact_ajax(request):
    """AJAX contact form handler"""
    try:
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        
        if not all([name, email, subject, message]):
            return JsonResponse({'success': False, 'error': 'All fields are required'})
        
        # Create message object
        Message.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
    
    except Exception as e:
        return JsonResponse({'success': False, 'error': 'An error occurred. Please try again.'})


def search(request):
    """Search functionality across all content"""
    query = request.GET.get('q', '')
    results = {
        'projects': [],
        'awards': [],
        'blog_posts': [],
    }
    
    if query:
        results['projects'] = Project.objects.filter(
            models.Q(title__icontains=query) | 
            models.Q(description__icontains=query)
        )[:5]
        
        results['awards'] = Award.objects.filter(
            models.Q(name__icontains=query) | 
            models.Q(description__icontains=query)
        )[:5]
        
        results['blog_posts'] = BlogPost.objects.filter(
            models.Q(title__icontains=query) | 
            models.Q(body__icontains=query)
        ).filter(published=True)[:5]
    
    context = {
        'query': query,
        'results': results,
        'site_settings': SiteSettings.objects.first(),
    }
    return render(request, 'portfolio/search.html', context)
