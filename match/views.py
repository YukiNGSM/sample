from django.views import generic
from .models import Match
from .forms import InquiryForm ,Edit_profileForm ,ChatForm ,SearchForm, MemberForm
from django.urls import reverse_lazy

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

