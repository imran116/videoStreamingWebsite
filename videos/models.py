from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    youtube_link = models.URLField()

    # Add other fields like description, uploader, etc. as needed

    def __str__(self):
        return self.title


class Feedback(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()

    # Add user field if users need to be authenticated for leaving feedback

    def __str__(self):
        return f"Feedback for {self.video.title}"
