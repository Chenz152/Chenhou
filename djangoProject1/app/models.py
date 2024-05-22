from django.db import models
from django.contrib.auth.models import User
import random
# Create your models here.

class Pictures(models.Model):
    upload = models.ImageField(upload_to='images')

    @staticmethod
    def random_picture():
        total = Pictures.objects.count()
        count = min(total, 10)
        seed = random.sample(range(0, total), count)
        res = []
        for i in seed:
            p = Pictures.objects.all()[i]
            res.append(
                {
                    "id": p.id,
                    "url": p.upload.url,
                    "filename": p.upload.name.split("/")[-1],
                    "comments": [{"id": j.id, "user": j.user.username, "content": j.content} for j in Comment.objects.filter(picture=p.id).all()]
                }
            )
        return res

    class Meta:
        db_table = "picture"


class Comment(models.Model):
    picture = models.ForeignKey(Pictures, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "comment"
