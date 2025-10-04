from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    Bio, Project, Award, GalleryImage, BlogPost, 
    Testimonial, Message, SiteSettings
)
from .serializers import (
    BioSerializer, ProjectSerializer, AwardSerializer, 
    GalleryImageSerializer, BlogPostSerializer, 
    TestimonialSerializer, MessageSerializer, SiteSettingsSerializer
)


class BioViewSet(viewsets.ReadOnlyModelViewSet):
    """API viewset for biography information"""
    queryset = Bio.objects.all()
    serializer_class = BioSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """API viewset for projects"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['start_date', 'created_at']
    ordering = ['-start_date']

    @action(detail=False)
    def featured(self, request):
        """Get featured projects"""
        featured_projects = self.queryset.filter(featured=True)
        serializer = self.get_serializer(featured_projects, many=True)
        return Response(serializer.data)


class AwardViewSet(viewsets.ReadOnlyModelViewSet):
    """API viewset for awards"""
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'organization', 'description']
    ordering_fields = ['date', 'created_at']
    ordering = ['-date']

    @action(detail=False)
    def featured(self, request):
        """Get featured awards"""
        featured_awards = self.queryset.filter(featured=True)
        serializer = self.get_serializer(featured_awards, many=True)
        return Response(serializer.data)


class GalleryImageViewSet(viewsets.ReadOnlyModelViewSet):
    """API viewset for gallery images"""
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['caption', 'description']
    ordering_fields = ['date', 'created_at']
    ordering = ['-date']

    @action(detail=False)
    def featured(self, request):
        """Get featured gallery images"""
        featured_images = self.queryset.filter(featured=True)
        serializer = self.get_serializer(featured_images, many=True)
        return Response(serializer.data)


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    """API viewset for blog posts"""
    queryset = BlogPost.objects.filter(published=True)
    serializer_class = BlogPostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'body', 'tags']
    ordering_fields = ['date', 'updated_at']
    ordering = ['-date']

    @action(detail=False)
    def featured(self, request):
        """Get featured blog posts"""
        featured_posts = self.queryset.filter(featured=True)
        serializer = self.get_serializer(featured_posts, many=True)
        return Response(serializer.data)


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    """API viewset for testimonials"""
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['author', 'organization', 'quote']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    @action(detail=False)
    def featured(self, request):
        """Get featured testimonials"""
        featured_testimonials = self.queryset.filter(featured=True)
        serializer = self.get_serializer(featured_testimonials, many=True)
        return Response(serializer.data)


class MessageViewSet(viewsets.ModelViewSet):
    """API viewset for contact messages"""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['sent_at']
    ordering = ['-sent_at']


class SiteSettingsViewSet(viewsets.ReadOnlyModelViewSet):
    """API viewset for site settings"""
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
