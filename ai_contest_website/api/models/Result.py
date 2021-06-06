from djongo import models
from api.models import User
from api.models import Contest, Language, Problem
from ai_contest_website.settings import MEDIA_URL
from os.path import join
from django.core.files.storage import FileSystemStorage
from datetime import datetime


class Result(models.Model):
    def get_result_directory_path(self, filename):
        time_file = str(int(self.time_submit.timestamp()))
        return "result/{0}/{1}/{2}/{3}".format(self.problem._id, self.created_user._id, time_file, filename)

    _id = models.ObjectIdField()
    problem = models.ForeignKey("problem", on_delete=models.CASCADE)
    created_user = models.ForeignKey("user", on_delete=models.CASCADE, related_name='result_created_user')
    time_submit = models.DateTimeField(auto_now_add=True)
    model_file = models.FileField(upload_to=get_result_directory_path)
    code_test = models.FileField(upload_to=get_result_directory_path)
    code_train = models.FileField(upload_to=get_result_directory_path)
    accuracy = models.FloatField()
    language = models.ForeignKey('language', on_delete=models.CASCADE)
    status = models.TextField(default='N')
    time_excute = models.FloatField(default=0)

    class Meta:
        db_table = 'result'

    def save(self, *args, **kwargs):
        super(Result, self).save(**kwargs)

    # print("Create result")

# u = User.objects.get(username='bkdn')
# p = Problem.objects.get(_id='6071fd0401e22f2cbb5471a2')
# l1 = Language.objects.get(name='python')
# r = Result(created_user=u, problem=p, language=l1)

# print(r)
# r.save()
# print(list(Result.objects.all()))
