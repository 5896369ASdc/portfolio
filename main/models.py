from django.db import models
from cloudinary.models import CloudinaryField   # ✅ IMPORTANT


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        related_name="images",
        on_delete=models.CASCADE
    )

    # 🔥 CHANGE THIS LINE
    image = CloudinaryField('image')

    def __str__(self):
        return f"{self.project.title} Image"