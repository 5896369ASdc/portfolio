from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Tag, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "display_tags", "link")
    search_fields = ("title", "description")
    list_filter = ("tags",)
    inlines = [ProjectImageInline]

    def display_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    display_tags.short_description = "Tags"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("project", "preview")

    def preview(self, obj):
        return format_html(
            '<img src="{}" width="100" style="border-radius:6px;" />',
            obj.image.url
        )

    preview.short_description = "Preview"