from django.contrib.auth.models import AbstractUser

class MeplusUser(AbstractUser):
    # 拡張ユーザーモデル
    class Meta:
        verbose_name_plural = 'MeplusUser'