from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView
from .forms import LoginForm


class LoginView(FormView):

    template_name = 'form.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def form_invalid(self, form, user_not_authenticated=False):
        if user_not_authenticated:
            form.add_error(None, 'Invalid email or password')
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
