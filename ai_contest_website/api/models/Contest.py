
from djongo import models

class Contest(models.Model):
    _id = models.ObjectIdField()
    
    class Meta:
        db_table = 'contest'

    def save(self, *args, **kwargs):
        if not hasattr(self, 'id') or self._id == '':
            self.id = Contest.get_new_id()
        super(Contest, self).save(**kwargs)
