# Generated by Django 3.2.7 on 2022-11-08 00:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真')),
                ('name', models.CharField(max_length=40, verbose_name='名前')),
                ('nickname', models.CharField(max_length=40, verbose_name='ニックネーム')),
                ('mail', models.EmailField(blank=True, max_length=254, null=True, verbose_name='メールアドレス')),
                ('password', models.CharField(max_length=20, verbose_name='パスワード')),
                ('card', models.IntegerField(blank=True, null=True, verbose_name='カード情報')),
                ('job', models.CharField(blank=True, max_length=40, null=True, verbose_name='職業')),
                ('sex', models.IntegerField(choices=[('L', 'L:レズビアン'), ('G', 'G:ゲイ'), ('B', 'B:バイセクシャル'), ('T', 'T:トランスジェンダー'), ('Q', 'Q:クエスチョ二ング')], verbose_name='性別')),
                ('sex_your', models.IntegerField(choices=[('L', 'L:レズビアン'), ('G', 'G:ゲイ'), ('B', 'B:バイセクシャル'), ('T', 'T:トランスジェンダー'), ('Q', 'Q:クエスチョ二ング')], verbose_name='相手に求める性別')),
                ('money', models.IntegerField(choices=[(1, '50-100'), (2, '100-300'), (3, '300-500'), (4, '500-700'), (5, '700-900'), (6, '900-')], verbose_name='年収')),
                ('marry', models.IntegerField(choices=[('有', '有'), ('無', '無')], verbose_name='結婚歴')),
                ('hobby', models.CharField(max_length=40, verbose_name='趣味')),
                ('intro_me', models.CharField(max_length=40, verbose_name='自己紹介')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name_plural': 'Match',
            },
        ),
    ]
