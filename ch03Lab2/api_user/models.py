from django.db import models

# Create your models here.


class User(models.Model):
    email = models.CharField(max_length=128, null=False)
    password = models.CharField(max_length=128, null=False)
    address = models.CharField(max_length=256, null=True)

    class Meta:
        # Table이름을 "User"로 정한다. default 이름은 api_user_user가 된다.
        db_table = "User"
