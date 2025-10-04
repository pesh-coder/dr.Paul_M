from django.db import models
from django.urls import reverse
from django.utils import timezone


class Bio(models.Model):
    """Biography information for Dr. Paul Mwambu"""
    name = models.CharField(max_length=100, default="Dr. Paul Mwambu")
    title = models.CharField(max_length=200, default="Commissioner for Crop Inspection & Certification")
    organization = models.CharField(max_length=200, default="Ministry of Agriculture, Animal Industry, and Fisheries (MAAIF), Uganda")
    photo = models.FileField(upload_to='photos/', help_text="Professional headshot", blank=True)
    bio = models.TextField(help_text="Detailed biography")
    cv = models.FileField(upload_to='cv/', blank=True, help_text="Curriculum Vitae PDF")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Biography"
        verbose_name_plural = "Biography"

    def __str__(self):
        return self.name


class Project(models.Model):
    """Projects and initiatives led by Dr. Paul Mwambu"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    detailed_description = models.TextField(blank=True, help_text="Extended project details")
    image = models.FileField(upload_to='projects/', help_text="Project showcase image", blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('ongoing', 'Ongoing'),
            ('completed', 'Completed'),
            ('planned', 'Planned'),
        ],
        default='ongoing'
    )
    link = models.URLField(blank=True, help_text="External project link")
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-start_date']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:project_detail', kwargs={'pk': self.pk})


class Award(models.Model):
    """Awards and honors received by Dr. Paul Mwambu"""
    name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200, help_text="Awarding organization")
    date = models.DateField()
    description = models.TextField()
    image = models.FileField(upload_to='awards/', help_text="Award certificate or photo", blank=True)
    category = models.CharField(
        max_length=50,
        choices=[
            ('agriculture', 'Agriculture'),
            ('leadership', 'Leadership'),
            ('research', 'Research'),
            ('service', 'Public Service'),
            ('international', 'International Recognition'),
        ],
        default='agriculture'
    )
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-date']
        verbose_name = "Award"
        verbose_name_plural = "Awards"

    def __str__(self):
        return f"{self.name} - {self.organization}"


class GalleryImage(models.Model):
    """Gallery images for showcasing Dr. Paul Mwambu's work"""
    image = models.FileField(upload_to='gallery/', blank=True)
    caption = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)
    category = models.CharField(
        max_length=50,
        choices=[
            ('events', 'Events'),
            ('field_work', 'Field Work'),
            ('meetings', 'Meetings'),
            ('awards', 'Awards'),
            ('projects', 'Projects'),
            ('general', 'General'),
        ],
        default='general'
    )
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return self.caption


class BlogPost(models.Model):
    """Blog posts and updates"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL-friendly version of title")
    body = models.TextField()
    excerpt = models.TextField(max_length=300, help_text="Short description for previews")
    image = models.FileField(upload_to='blog/', blank=True, help_text="Featured image")
    author = models.CharField(max_length=100, default="Dr. Paul Mwambu")
    published = models.BooleanField(default=False)
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags")


    class Meta:
        ordering = ['-date']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:blog_detail', kwargs={'slug': self.slug})


class Testimonial(models.Model):
    """Testimonials from colleagues and partners"""
    author = models.CharField(max_length=100)
    position = models.CharField(max_length=200, help_text="Job title or position")
    organization = models.CharField(max_length=200)
    quote = models.TextField()
    image = models.FileField(upload_to='testimonials/', blank=True, help_text="Author photo")
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.author} - {self.organization}"


class Message(models.Model):
    """Contact form messages"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    replied = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sent_at']
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return f"{self.name} - {self.subject}"


class SiteSettings(models.Model):
    """Site-wide settings and configuration"""
    site_title = models.CharField(max_length=200, default="Dr. Paul Mwambu - Agricultural Leader")
    site_description = models.TextField(default="Professional portfolio of Dr. Paul Mwambu, Commissioner for Crop Inspection & Certification, Uganda")
    contact_email = models.EmailField(default="contact@drpaulmwambu.com")
    contact_phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    social_linkedin = models.URLField(blank=True)
    social_twitter = models.URLField(blank=True)
    social_facebook = models.URLField(blank=True)
    google_analytics_id = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteSettings.objects.exists():
            return SiteSettings.objects.first()
        return super().save(*args, **kwargs)
