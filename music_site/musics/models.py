from django.db import models


class Musician(models.Model):
    name = models.CharField(max_length=111)
    main_genre = models.CharField(max_length=111)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=111)
    genre = models.CharField(max_length=111)
    release_year = models.DateField(null=True, blank=True)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=111)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title
