
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth import authenticate, login

from noteit.forms import LoginForm


# class LoginView(generic.FormView):
#     print("loginView runs")
#     next = "/noteit/notes/"
#     # model = User
#     form_class = LoginForm

#     def form_valid(self, form):
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(self.request, user)
#             return redirect('/noteit/notes/')
#         else:
#             form.add_error(None, 'Invalid username or password.')
#         return super().form_valid(form)
