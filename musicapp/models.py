from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=120)
    last_nmae = models.CharField(max_length=120)
    age = models.IntegerField(null=False)

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    date_released = models.DateTimeField()
    likes = models.IntegerField()

class Lyric(models.Model):
    content = models.CharField(max_length=500)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
