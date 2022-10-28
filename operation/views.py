from django.views import generic

class Ban_accountView(generic.TemplateView):
    template_name = 'ban_account.html'

class Check_ageView(generic.TemplateView):
    template_name = 'check_Age.html'

class Check_inquiryView(generic.TemplateView):
    template_name = 'check_inquiry.html'
