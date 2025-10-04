from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Bio, Project, Award, GalleryImage, BlogPost, 
    Testimonial, Message, SiteSettings
)


@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'organization', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'organization', 'photo', 'bio')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'linkedin', 'twitter')
        }),
        ('Documents', {
            'fields': ('cv',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'start_date', 'featured', 'created_at']
    list_filter = ['status', 'featured', 'start_date']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description', 'detailed_description', 'image')
        }),
        ('Timeline', {
            'fields': ('start_date', 'end_date', 'status')
        }),
        ('Display Options', {
            'fields': ('featured', 'link')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization', 'date', 'category', 'featured']
    list_filter = ['category', 'featured', 'date']
    search_fields = ['name', 'organization', 'description']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Award Information', {
            'fields': ('name', 'organization', 'description', 'image')
        }),
        ('Details', {
            'fields': ('date', 'category', 'featured')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['caption', 'category', 'date', 'featured']
    list_filter = ['category', 'featured', 'date']
    search_fields = ['caption', 'description']
    readonly_fields = ['created_at']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;" />', obj.image.url)
        return "No image"
    image_preview.short_description = "Preview"
    
    fieldsets = (
        ('Image Information', {
            'fields': ('image', 'image_preview', 'caption', 'description')
        }),
        ('Categorization', {
            'fields': ('category', 'date', 'featured')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published', 'featured', 'date']
    list_filter = ['published', 'featured', 'date']
    search_fields = ['title', 'body', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['date', 'updated_at']
    fieldsets = (
        ('Post Information', {
            'fields': ('title', 'slug', 'excerpt', 'body', 'image')
        }),
        ('Author & Publishing', {
            'fields': ('author', 'published', 'featured', 'tags')
        }),
        ('Timestamps', {
            'fields': ('date', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['author', 'organization', 'featured', 'created_at']
    list_filter = ['featured', 'created_at']
    search_fields = ['author', 'organization', 'quote']
    readonly_fields = ['created_at']
    fieldsets = (
        ('Testimonial Information', {
            'fields': ('author', 'position', 'organization', 'quote', 'image')
        }),
        ('Display Options', {
            'fields': ('featured',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'read', 'replied', 'sent_at']
    list_filter = ['read', 'replied', 'sent_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['sent_at']
    fieldsets = (
        ('Message Information', {
            'fields': ('name', 'email', 'subject', 'message')
        }),
        ('Status', {
            'fields': ('read', 'replied')
        }),
        ('Timestamps', {
            'fields': ('sent_at',),
            'classes': ('collapse',)
        }),
    )

    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = "Mark selected messages as read"

    def mark_as_replied(self, request, queryset):
        queryset.update(replied=True)
    mark_as_replied.short_description = "Mark selected messages as replied"

    actions = [mark_as_read, mark_as_replied]


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Site Information', {
            'fields': ('site_title', 'site_description')
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'contact_phone', 'address')
        }),
        ('Social Media', {
            'fields': ('social_linkedin', 'social_twitter', 'social_facebook')
        }),
        ('Analytics', {
            'fields': ('google_analytics_id',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']

    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of the only instance
        return False
