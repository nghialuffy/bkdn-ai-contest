from djongo import models
from api.models import User
from api.models import Contest, Language, Problem
from ai_contest_website.settings import MEDIA_URL
from os.path import join
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location=join(MEDIA_URL, 'result'))


class Result(models.Model):
    _id = models.ObjectIdField()
    problem = models.ForeignKey("problem", on_delete=models.CASCADE)
    created_user = models.ForeignKey("user", on_delete=models.CASCADE, related_name='result_created_user')
    model_file = models.FileField(storage=fs)
    code_test = models.FileField(storage=fs)
    code_train = models.FileField(storage=fs)
    accuracy = models.FloatField()
    time_submit = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey('language', on_delete=models.CASCADE)

    class Meta:
        db_table = 'result'

    def save(self, *args, **kwargs):
        super(Result, self).save(**kwargs)

    def __str__(self):
        return self._id

# print("Create result")

# u = User.objects.get(username='bkdn')
# p = Problem.objects.get(_id='6071fd0401e22f2cbb5471a2')
# l1 = Language.objects.get(name='python')
# r = Result(created_user=u, problem=p, language=l1)

# print(r)
# r.save()
# print(list(Result.objects.all()))
