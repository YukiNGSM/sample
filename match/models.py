from django.db import models
from accounts.models import MeplusUser

# 日記モデル
class Match(models.Model):

    SELECT = (
        ('L','L:レズビアン'),
        ('G','G:ゲイ'),
        ('B','B:バイセクシャル'),
        ('T','T:トランスジェンダー'),
        ('Q','Q:クエスチョ二ング')
    )

    SELECT2 = (
        ('L','L:レズビアン'),
        ('G','G:ゲイ'),
        ('B','B:バイセクシャル'),
        ('T','T:トランスジェンダー'),
        ('Q','Q:クエスチョ二ング')
    )

    SELECT3 = (
        (1,'50-100'),
        (2,'100-300'),
        (3,'300-500'),
        (4,'500-700'),
        (5, '700-900'),
        (6, '900-'),
    )
    SELECT4 = (
        ('有','有'),
        ('無','無'),
    )


    # ForeignKeyで登録されているユーザー以外の登録はできなくする
    # 追加:主キー側から 削除:外部キー側から
    user_ID = models.ForeignKey(MeplusUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    gender = models.IntegerField(choices=SELECT, verbose_name='性別')
    name = models.CharField(verbose_name='名前', max_length=40)
    user_name = models.CharField(verbose_name='ニックネーム', max_length=40)
    mailaddress = models.EmailField(verbose_name='メールアドレス', blank=True,null=True)
    password = models.CharField(verbose_name='パスワード', max_length=20)
    # cardnum = models.CardNumberField(verbose_name='カード番号', blank=True, null=True)
    # cardex = models.CardExpiryField(verbose_name='有効期限', blank=True, null=True)
    # cardcode = SecurityCodeField(verbose_name='セキュリティコード(カード裏面印字されている下3桁または4桁)', blank=True, null=True)
    job = models.CharField(verbose_name='職業', blank=True, null=True, max_length=40)
    target = models.IntegerField(choices=SELECT2, verbose_name='相手に求める性別')
    annual_income = models.IntegerField(choices=SELECT3, verbose_name='年収')
    marry = models.IntegerField(choices=SELECT4, verbose_name='結婚歴')
    hobby = models.CharField(verbose_name='趣味', max_length=40)
    introduce = models.CharField(verbose_name='自己紹介', max_length=40)
    image = models.ImageField(verbose_name='写真', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Match'

    def __str__(self):
        return  self.title

