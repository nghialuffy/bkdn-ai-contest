
from djongo import models
from api.models import Language, Contest

class Problem(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=50)
    contest = models.ForeignKey('contest', on_delete=models.CASCADE, related_name="contest_id")
    languages = models.ArrayReferenceField(
        to=Language, 
        on_delete=models.DO_NOTHING
    )
    description = models.FileField(upload_to="contest/%s" % contest)
    score = models.FloatField()
    # enctype="multipart/form-data"
    code_test = models.FileField(upload_to="contest/%s" % contest)
    data_sample = models.FileField(upload_to="contest/%s" % contest)
    train_data = models.FileField(upload_to="contest/%s" % contest)
    test_data = models.FileField(upload_to="contest/%s" % contest)
    time_executed_limit = models.FloatField()

    class Meta:
        db_table = 'problem'

    def __str__(self):
        return self.title 
        super(Problem, self).save(**kwargs)

# c = Contest.objects.get(title='BKDN AI')
# l1 = Language.objects.get(name='Python') 
# print(l1)
# p = Problem(title='Predict Object', contest=c, description='Something like that', score=1, time_executed_limit=0.5, languages=[l1])
# # p.languages.add(l1)
# print(p)
# # p.save()
# # print(list(Problem.objects.all()))