from djongo import models

class HtmlDocument(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    html_content = models.TextField()

    class Meta:
        db_table = 'html_document'

