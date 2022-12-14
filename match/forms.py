import os
from django import forms
from django.core.mail import EmailMessage
# from .models import Match

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'

        self.fields['email'].widget.attrs['class'] = 'form-control col-11'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

        self.fields['title'].widget.attrs['class'] = 'form-control col-11'
        self.fields['title'].widget.attrs['placeholder'] = '件名をここに入力してください。'


        self.fields['message'].widget.attrs['class'] = 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] = 'お問い合わせ内容をここに入力してください。'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ {}'.format(title)
        message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(name, email, message)
        from_email = os.environ.get('FROM_EMAIL')
        to_list = [
            os.environ.get('FROM_EMAIL')
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()

# class Edit_profileForm(forms.Form):
#     class Meta:
#         model = Match
#         fields = ('image', 'user_ID', 'gender', 'user_name', 'mailadress','password', 'age','hobby', 'address','annual_income', 'job', 'random', 'target', 'marry','introduce' )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'
#
#             class ChoiceForm(forms.Form):
#                 selected_time = forms.fields.ChoiceField(
#                     choices=(
#                         ('mens', 'wemens'),
#                     ),
#                 label = '性別',
#                     required = True,
#                     widget = forms.widgets.RadioSelect
#                 )
#
#
#             self.fields['user_name'].widget.attrs['class'] = 'form-control col-9'
#             self.fields['user_name'].widget.attrs['placeholder'] = '名前'
#
#             self.fields['mailadress'].widget.attrs['class'] = 'form-control col-9'
#             self.fields['mailadress'].widget.attrs['placeholder'] = 'メールアドレス'
#
#             self.fields['password'].widget.attrs['class'] = 'form-control col-9'
#             self.fields['password'].widget.attrs['placeholder'] = 'パスワード'
#
#             self.fields['age'].widget.attrs['class'] = 'form-control col-9'
#             self.fields['age'].widget.attrs['placeholder'] = '年齢'
#
#             self.fields['hobby'].widget.attrs['class'] = 'form-control col-9'
#             self.fields['hobby'].widget.attrs['placeholder'] = '趣味'
#
#             self.fields['address'].widget.attrs['class'] = 'form-control col-9'
#             self.fields['address'].widget.attrs['placeholder'] = '住所'
#
#             self.fields['annual_income'].widget.attrs['class'] = 'form-control col-9'
#             self.fields['annual_income'].widget.attrs['placeholder'] = '年収'
#
#             self.fields['job'].widget.attrs['class'] = 'form-control col-9'
#             self.fields['job'].widget.attrs['placeholder'] = '職業'

            # class ChoiceForm(forms.Form):
            #     selected_time = forms.fields.ChoiceField(
            #         choices=(
            #             ('○', '☓'),
            #         ),
            #     label = '結婚歴',
            #         required = True,
            #         widget = forms.widgets.RadioSelect
            #     )
            #
            # self.fields['introduce'].widget.attrs['class'] = 'form-control col-20'
            # self.fields['introduce'].widget.attrs['placeholder'] = '自己紹介'

class ChatForm(forms.Form):
    name = forms.CharField(label='chat', max_length=30)

class SearchForm(forms.Form):
    freeword = forms.CharField(
        initial='',
        label='フリーワード',
        required = False, # 必須ではない
    )
    age = forms.CharField(
        initial='',
        label='年齢',
        required = False,  # 必須ではない
    )

class MemberForm(forms.Form):
    name = forms.CharField(label='chat', max_length=30)

from django.contrib.auth.models import User
from .models import Account

# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="(必須)パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"(必須)ニックネーム",'email':"(必須)メール"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        fields = (
            'first_name',
            'last_name',
            'age',
            'address',
            'cardnum',
            'cardyear',
            'cardmonth',
            'cardcode',
            'job',
            'image',
            'gender',
            'target',
            'annual_income',
            'marry',
            'hobby',
            'introduce',
            )

        #verboseと同義
        labels = {
            'first_name':"(必須)名前",
            'last_name': "(必須)苗字",
            'age':"(必須)年齢",
            'address': "(必須)住所",
            'cardnum': "(必須)カード番号",
            'cardyear': "有効期限(年)",
            'cardmonth': "有効期限(月)",
            'cardcode': "セキュリティコード(カード裏面印字されている下3桁または4桁)",
            'job':"職業",
            'image':"(必須)プロフィール画像",
            'gender': "(必須)性別",
            'target': "(必須)恋愛対象",
            'annual_income': "年収",
            'marry':"結婚歴",
            'hobby': "趣味",
            'introduce': "自己紹介",
            }

class Edit_profileForm(forms.ModelForm):
    class Meta():

        model = Account
        fields = (
            'first_name',
            'last_name',
            'age',
            'address',
            'cardnum',
            'cardyear',
            'cardmonth',
            'cardcode',
            'job',
            'image',
            'gender',
            'target',
            'annual_income',
            'marry',
            'hobby',
            'introduce',
            )

        #verboseと同義
        labels = {
            'first_name':"(必須)名前",
            'last_name': "(必須)苗字",
            'age':"(必須)年齢",
            'address': "(必須)住所",
            'cardnum': "(必須)カード番号",
            'cardyear': "有効期限(年)",
            'cardmonth': "有効期限(月)",
            'cardcode': "セキュリティコード(カード裏面印字されている下3桁または4桁)",
            'job':"職業",
            'image':"(必須)プロフィール画像",
            'gender': "(必須)性別",
            'target': "(必須)恋愛対象",
            'annual_income': "年収",
            'marry':"結婚歴",
            'hobby': "趣味",
            'introduce': "自己紹介",
            }
