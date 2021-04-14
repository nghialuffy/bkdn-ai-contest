from djongo import models
# from django.contrib.auth.models import AbstractUser
class User(models.Model):
    _id = models.ObjectIdField()
    username = models.CharField(max_length=50, unique=True)
    first_name = models.TextField(max_length=50, default="")
    last_name = models.TextField(max_length=50, default="")

    password = models.TextField()
    role = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    isAdmin = models.BooleanField(default=False)
    isOrganizer = models.BooleanField(default=False)
    url = models.URLField()
    
    def __str__(self):
        return self.username
    class Meta:
        db_table = 'user'



# e = User(username='bkdn', password='123',role='admin')
# # e.save()
# print(list(User.objects.all()))