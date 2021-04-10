from djongo import models

class Language(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    path = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'language'

    def save(self, *args, **kwargs):
        # if not hasattr(self, 'id') or self._id == '':
        #     self.id = User.get_new_id()
        super(Language, self).save(**kwargs)



# l = Language(name='c++')
# l.save()
# print(list(Language.objects.all()))