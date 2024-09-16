from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, CreateView
from .forms import RegistrationForm, LoginForm
from .models import User


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'registration_form.html'
    instance = None
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save()
        new_user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
        login(self.request, new_user)
        return HttpResponseRedirect(self.get_success_url())


class LoginView(FormView):

    template_name = 'login_form.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def form_invalid(self, form, user_not_authenticated=False):
        if user_not_authenticated:
            form.add_error('email', 'Invalid email or password')
        return super().form_invalid(form)

    def form_valid(self, form):
        user_data = form.cleaned_data
        user = authenticate(self.request, **user_data)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        return self.form_invalid(form, user_not_authenticated=True)


class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        print(request.user)
        print(request.user.is_authenticated)
        return super().get(request, *args, **kwargs)
