
from djongo import models
from api.models.User import User

class Contest(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=50)
    created_user = models.ForeignKey("user", on_delete=models.CASCADE, null=False, related_name='created_user')
    created = models.DateTimeField(auto_now_add=True)
    constestants = models.ManyToManyField("user", related_name='contestants')
    language = models.ManyToManyField("language")
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    # created_by = models.OneToOneField(
    #     User,
    #     on_delete=models.CASCADE,
    # )
    class Meta:
        db_table = 'contest'
    # def __str__(self):
    #     return self

    def save(self, *args, **kwargs):
        super(Contest, self).save(**kwargs)
# print(list(User.objects.all()))

# e = User.objects.get(username='bkdn')
# c = Contest(title='bkdnContest', created_user=e)
# c.save()
# print(list(Contest.objects.all()))