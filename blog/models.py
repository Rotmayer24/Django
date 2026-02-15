from django.db import models
# Create your models here.

class AppUser(models.Model):
    roles = [
        ("admin", "Admin"),
        ("user", "User"),
    ]
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=10, choices=roles, default="user")
    
    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=3000)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True, blank=True)

    def published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=7)


    def __str__(self):
        return self.title

