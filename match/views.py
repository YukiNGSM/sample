from django.views import generic

class ChatView(generic.TemplateView):
    template_name = "chat.html"

class Edit_plofileView(generic.TemplateView):
    template_name = "edit_plofile.html"

class HomeView(generic.TemplateView):
    template_name = "home.html"

class Iine_meView(generic.TemplateView):
    template_name = "iine_me.html"

class InquiryView(generic.TemplateView):
    template_name = "inquiry.html"

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

class ReportView(generic.TemplateView):
    template_name = "report.html"

class SearchView(generic.TemplateView):
    template_name = "search.html"

class Stop_serviceView(generic.TemplateView):
    template_name = "stop_sevice.html"

class Term_of_serviceView(generic.TemplateView):
    template_name = "term_of_service.html"