from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()
    username = models.CharField(max_length=50, unique=True)
    password = models.TextField()
    role = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    # ## Contest contain many User
    # contests = models.ManyToManyField(
    #     Contest,
    #     blank=True, null=True,
    #     related_name="attend_contests"
    # )    

    class Meta:
        db_table = 'user'
    def __str__(self):
        return self.username




# e = User(username='bkdn', password='123',role='admin')
# # e.save()
# print(list(User.objects.all()))