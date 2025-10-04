from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import (
    ProjectViewSet, AwardViewSet, GalleryImageViewSet, 
    BlogPostViewSet, TestimonialViewSet, BioViewSet
)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'awards', AwardViewSet)
router.register(r'gallery', GalleryImageViewSet)
router.register(r'blog', BlogPostViewSet)
router.register(r'testimonials', TestimonialViewSet)
router.register(r'bio', BioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
