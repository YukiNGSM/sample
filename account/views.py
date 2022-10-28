from django.views import generic

class Forgot_passwordView(generic.TemplateView):
    template_name = 'forgot_password.html'

class LoginView(generic.TemplateView):
    template_name = 'login.html'

class Password_resetView(generic.TemplateView):
    template_name = 'password_reset.html'

class RegisterView(generic.TemplateView):
    template_name = 'register.html'