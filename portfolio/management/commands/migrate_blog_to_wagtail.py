# portfolio/management/commands/migrate_blog_to_wagtail.py
from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from django.conf import settings
from django.utils.text import slugify
from pathlib import Path

from portfolio.models import BlogPost  # legacy model
from blogcms.models import BlogIndexPage, BlogPage
from wagtail.models import Page, Site
from wagtail.images.models import Image as WagtailImage
from taggit.models import Tag

class Command(BaseCommand):
    help = "Copy legacy BlogPost rows into Wagtail BlogPage items"

    def add_arguments(self, parser):
        parser.add_argument("--index-title", default="Blog", help="Title of the BlogIndexPage to import into")

    def handle(self, *args, **opts):
        index_title = opts["index_title"]

        # Find the blog index page (create one if not found)
        root_page = Site.objects.get(is_default_site=True).root_page
        blog_index = root_page.get_children().type(BlogIndexPage).first()
        if not blog_index:
            blog_index = BlogIndexPage(title=index_title, slug=slugify(index_title))
            root_page.add_child(instance=blog_index)
            blog_index.save_revision().publish()
            self.stdout.write(self.style.SUCCESS(f"Created BlogIndexPage '{index_title}'"))

        count = 0
        for legacy in BlogPost.objects.all():
            # Skip if a BlogPage with same slug already exists
            if blog_index.get_children().type(BlogPage).filter(slug=legacy.slug).exists():
                continue

            page = BlogPage(
                title=legacy.title,
                slug=legacy.slug or slugify(legacy.title),
                excerpt=getattr(legacy, "excerpt", "") or "",
                date=getattr(legacy, "date", None),
                featured=getattr(legacy, "featured", False),
                body=getattr(legacy, "body", "")  # if legacy body is plain HTML; okay in RichTextField
            )

            # Attach header image if the legacy model had one
            img_field = getattr(legacy, "image", None)
            if img_field and getattr(img_field, "path", None) and Path(img_field.path).exists():
                with open(img_field.path, "rb") as f:
                    wi = WagtailImage.objects.create(
                        title=Path(img_field.name).name,
                        file=ImageFile(f, name=Path(img_field.name).name),
                    )
                page.header_image = wi

            # Add tags
            if hasattr(legacy, "tags"):
                for t in legacy.tags.all():
                    page.tags.add(t)

            blog_index.add_child(instance=page)
            page.save_revision().publish()
            count += 1

        self.stdout.write(self.style.SUCCESS(f"Migrated {count} legacy posts into Wagtail"))
