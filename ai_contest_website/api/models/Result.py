
from djongo import models
from api.models import User
from api.models import Contest, Language, Problem

class Result(models.Model):
    _id = models.ObjectIdField()
    problem = models.ForeignKey("problem", on_delete=models.CASCADE)
    created_user = models.ForeignKey("user", on_delete=models.CASCADE)
    model_file = models.TextField()
    code_test = models.TextField()
    code_train = models.TextField()
    accuracy = models.FloatField()
    time_submit = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey('language', on_delete=models.CASCADE)

    class Meta:
        db_table = 'result'

    def save(self, *args, **kwargs):
        super(Result, self).save(**kwargs)
    
    # def __str__(self)
    #     return "%s "
    
# print("Create result")

# u = User.objects.get(username='bkdn')
# p = Problem.objects.get(_id='6071fd0401e22f2cbb5471a2')
# l1 = Language.objects.get(name='python')
# r = Result(created_user=u, problem=p, language=l1)

# print(r)
# r.save()
# print(list(Result.objects.all()))