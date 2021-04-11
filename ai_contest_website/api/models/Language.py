from djongo import models

class Language(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    path = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'language'


   