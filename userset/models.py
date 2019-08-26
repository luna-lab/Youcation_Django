from django.db import models


class UserProfile(models.Model):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True
    )

    date_of_birth = models.DateField()
    username = models.CharField(max_length=16)
    nickname = models.CharField(max_length=24, unique=True)
    school = models.CharField(max_length=10, default="0000000000")
    sex = models.CharField(max_length=4)
    phone = models.CharField(max_length=11)
    profile_photo = models.ImageField(blank=True, upload_to="profile_photo/%Y/%m/%d")

    def __str__(self):
        return self.email
