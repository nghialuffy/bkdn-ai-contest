from django.db import models


class User(models.Model):
    id = models.CharField(max_length=10, primary_key=True, blank=True)
    username = models.CharField(max_length=50)
    password = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'

    def save(self, *args, **kwargs):
        if not hasattr(self, 'id') or self.id == '':
            self.id = User.get_new_id()
        super(User, self).save(**kwargs)