from djongo import models
from api.models import Contest

class User(models.Model):
    _id = models.ObjectIdField()
    username = models.CharField(max_length=50)
    password = models.TextField()
    role = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    ## Contest contain many User
    contests = models.ForeignKey(
        'Contest',
        on_delete=models.DO_NOTHING,
    )    
    class Meta:
        db_table = 'user'

    def save(self, *args, **kwargs):
        # if not hasattr(self, 'id') or self._id == '':
        #     self.id = User.get_new_id()
        super(User, self).save(**kwargs)



# e = User(username='bkdn', password='123',role='admin')
# e.save()
print(list(User.objects.all()))