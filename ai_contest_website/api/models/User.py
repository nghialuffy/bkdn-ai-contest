from djongo import models


class User(models.Model):
    _id = models.ObjectIdField()
    username = models.CharField(max_length=50, unique=True)
    first_name = models.TextField(max_length=50, default="")
    last_name = models.TextField(max_length=50, default="")
    password = models.TextField()
    attended_contests = models.ArrayReferenceField(
        to='contest',
        on_delete=models.CASCADE,
        default=[]
    )
    role = models.TextField()
    # role = models.ManyToManyField(Role)
    created = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_organizer = models.BooleanField(default=False)
    url = models.URLField()
    objects = models.DjongoManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'



# e = User(username='bkdn', password='123',role='admin')
# # e.save()
# print(list(User.objects.all()))
