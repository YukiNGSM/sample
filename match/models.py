from django.db import models

# ユーザー認証
from django.contrib.auth.models import User

# ユーザーアカウントのモデルクラス
class Account(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 追加フィールド

    #自己の性別
    SELECT = (
        (1, 'L:レズビアン'),
        (2, 'G:ゲイ'),
        (3, 'B:バイセクシャル'),
        (4, 'T:トランスジェンダー'),
        (5, 'Q:クエスチョ二ング')
    )

    SELECT2 = (
        (1, 'L:レズビアン'),
        (2, 'G:ゲイ'),
        (3, 'B:バイセクシャル'),
        (4, 'T:トランスジェンダー'),
        (5, 'Q:クエスチョ二ング')
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
        (1, '有'),
        (2, '無'),
    )

    # def get_image_path(self, filename):
    #     """カスタマイズした画像パスを取得する.
    #
    #     :param self: インスタンス (models.Model)
    #     :param filename: 元ファイル名
    #     :return: カスタマイズしたファイル名を含む画像パス
    #     """
    #     prefix = 'images/'
    #     name = str(uuid.uuid4).replace('-', '')
    #     extension = os.path.splitext(filename)[-1]
    #     return prefix + name + extension
    #
    # def delete_previous_file(function):
    #     """不要となる古いファイルを削除する為のデコレータ実装.
    #
    #     :param function: メイン関数
    #     :return: wrapper
    #     """
    #
    #     def wrapper(*args, **kwargs):
    #         """Wrapper 関数.
    #
    #         :param args: 任意の引数
    #         :param kwargs: 任意のキーワード引数
    #         :return: メイン関数実行結果
    #         """
    #         self = args[0]
    #
    #         # 保存前のファイル名を取得
    #         result = Image.objects.filter(pk=self.pk)
    #         previous = result[0] if len(result) else None
    #         super(Image, self).save()
    #
    #         # 関数実行
    #         result = function(*args, **kwargs)
    #
    #         # 保存前のファイルがあったら削除
    #         if previous:
    #             os.remove(MEDIA_ROOT + '/' + previous.image.name)
    #         return result
    #
    #     return wrapper
    #
    # class Image(models.Model):
    #
    #     def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #         super(Image, self).save()
    #
    #     def delete(self, using=None, keep_parents=False):
    #         super(Image, self).delete()

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=40)
    cardnum = models.IntegerField()
    cardmonth = models.IntegerField()
    cardyear = models.IntegerField()
    cardcode = models.IntegerField()
    job = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to="img/")
    gender = models.IntegerField(choices=SELECT)
    target = models.IntegerField(choices=SELECT2)
    annual_income = models.IntegerField(choices=SELECT3, blank=True, null=True)
    marry = models.IntegerField(choices=SELECT4, blank=True, null=True )
    hobby = models.CharField(max_length=40, blank=True, null=True )
    introduce = models.CharField(max_length=300,blank=True, null=True )

    def __str__(self):
        return self.user.username

# アカウントモデルの残し
# class Match(models.Model):


    # SELECT = (
    #     ('L','L:レズビアン'),
    #     ('G','G:ゲイ'),
    #     ('B','B:バイセクシャル'),
    #     ('T','T:トランスジェンダー'),
    #     ('Q','Q:クエスチョ二ング')
    # )

    # SELECT2 = (
    #     ('L','L:レズビアン'),
    #     ('G','G:ゲイ'),
    #     ('B','B:バイセクシャル'),
    #     ('T','T:トランスジェンダー'),
    #     ('Q','Q:クエスチョ二ング')
    # )

    # SELECT3 = (
    #     (1,'50-100'),
    #     (2,'100-300'),
    #     (3,'300-500'),
    #     (4,'500-700'),
    #     (5, '700-900'),
    #     (6, '900-'),
    # )

    # SELECT4 = (
    #     ('有','有'),
    #     ('無','無'),
    # )


    # ForeignKeyで登録されているユーザー以外の登録はできなくする
    # 追加:主キー側から 削除:外部キー側から
    # user_ID = models.ForeignKey(Account, verbose_name='ユーザー', on_delete=models.PROTECT)
    # gender = models.IntegerField(choices=SELECT, verbose_name='性別')
    # name = models.CharField(verbose_name='名前', max_length=40)
    # user_name = models.CharField(verbose_name='ニックネーム', max_length=40)
    # mailaddress = models.EmailField(verbose_name='メールアドレス', blank=True,null=True)
    # password = models.CharField(verbose_name='パスワード', max_length=20)
    # cardnum = models.IntegerField(verbose_name='カード番号', max_length=16, blank=True, null=True)
    # cardmonth = models.IntegerField(verbose_name='有効期限(月)', max_length=1, blank=True, null=True)
    # cardyear = models.IntegerField(verbose_name='有効期限(年)', max_length=2, blank=True, null=True)
    # cardcode = models.IntegerField(verbose_name='セキュリティコード(カード裏面印字されている下3桁または4桁)', max_length=4, blank=True,null=True)
    # job = models.CharField(verbose_name='職業', blank=True, null=True, max_length=40)
    # target = models.IntegerField(choices=SELECT2, verbose_name='相手に求める性別')
    # annual_income = models.IntegerField(choices=SELECT3, verbose_name='年収')
    # marry = models.IntegerField(choices=SELECT4, verbose_name='結婚歴')
    # hobby = models.CharField(verbose_name='趣味', max_length=40)
    # introduce = models.CharField(verbose_name='自己紹介', max_length=300)
    # address = models.CharField(verbose_name='住所', max_length=40)
    # age = models.IntegerField(verbose_name='年齢', max_length=3)

    # created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    # updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    # class Meta:
    #     verbose_name_plural = 'Match'
    #
    # def __str__(self):
    #     return  self.title


