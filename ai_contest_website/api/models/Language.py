from djongo import models


class Language(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50, unique=True)
    path = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    file_extensions = models.TextField(default='')

    class Meta:
        db_table = 'language'

    def __str__(self):
        return self.name
