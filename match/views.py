from django.views import generic
from .models import Match
from .forms import InquiryForm ,Edit_profileForm ,ChatForm ,SearchForm, MemberForm
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import AccountForm, AddAccountForm # ユーザーアカウントフォーム
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import psycopg2

class ChatView(generic.TemplateView):
    template_name = "chat.html"

class Chat_listView(generic.TemplateView):
    template_name = "chat_list.html"

class Edit_profileView(generic.FormView):
    model = Match
    template_name = "edit_profile.html"
    form_class = Edit_profileForm
    success_url = reverse_lazy('match:edit_profile')

class HomeView(generic.TemplateView):
    template_name = "home.html"

class Iine_meView(generic.TemplateView):
    template_name = "iine_me.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('match:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class MemberView(generic.TemplateView):
    template_name = "member.html"

class Member_byeView(generic.TemplateView):
    template_name = "member_bye.html"

class Point_freeView(generic.TemplateView):
    template_name = "Point_free.html"

class Point_memberView(generic.TemplateView):
    template_name = "point_member.html"

class Random_matchView(generic.TemplateView):
    template_name = "random_match.html"
    form_class = ChatForm


class ReportView(generic.TemplateView):
    template_name = "report.html"

class SearchView(generic.TemplateView):
    template_name = "search.html"
    form_class = SearchForm

    def receive_checkbox(request):
        check = request.POST.getlist["area"]

class Stop_serviceView(generic.TemplateView):
    template_name = "stop_sevice.html"

class Terms_of_serviceView(generic.TemplateView):
    template_name = "terms_of_service.html"

class  AccountRegistration(generic.TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    # Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"signup.html",context=self.params)

    # Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        # フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            add_account = self.params["add_account_form"].save(commit=False)
            #AccountForm & AddAccountForm #1vs1 紐付け
            add_account.user = account

            # 画像アップロード有無検証
            if 'account_image' in request.FILES:
                add_account.account_image = request.FILES['account_image']

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"signup.html",context=self.params)