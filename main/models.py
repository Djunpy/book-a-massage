from django.db import models
from django.urls import reverse


class Massage(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(upload_to='massage/', blank=True, null=True)
    desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("main:massage-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class Booking(models.Model):
    username = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    the_date = models.DateTimeField()
    massage = models.ForeignKey(Massage, on_delete=models.CASCADE)

    def __str__(self):
        return f'Massage:{self.massage}, Client:{self.email}'


class Comment(models.Model):
    massage = models.ForeignKey(Massage, on_delete=models.CASCADE)
    email = models.EmailField(max_length=80, blank=True, null=True)
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.massage}'






