from djongo import models
from api.models import User


class Contestant(models.Model):

    class Meta:
        db_table = 'contestant'

    _id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey('user', on_delete=models.CASCADE, null=False, related_name='contestant_user')
    contest = models.ForeignKey('contest', on_delete=models.CASCADE, null=False, related_name='contestant_contest_id')
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return str(self._id)

class Contest(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_user = models.ForeignKey('user', on_delete=models.CASCADE, null=False, related_name='created_user')
    created = models.DateTimeField(auto_now_add=True)
    attended_contestants = models.ArrayReferenceField(
        to='contestant',
        default=[],
        related_name='attended_contestants'
    )
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()

    class Meta:
        db_table = 'contest'

    # def __str__(self):
    #     return self

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Contest, self).save(**kwargs)
# print(list(User.objects.all()))

# e = User.objects.get(username='bkdn')
# c = Contest(title='bkdnContest', created_user=e)
# c.save()
# print(list(Contest.objects.all()))
