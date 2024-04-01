from django.shortcuts import render, HttpResponse
from django.views.generic import FormView, RedirectView
from .forms import UserRegistrationForm, UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import redirect


# Create your views here.
class UserRegistrationView(FormView):
    template_name = 'user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('registration_page')
    
    def form_valid(self, form):
        user = form.save()
        # print(form.cleaned_data)
        login(self.request, user)
        return super().form_valid(form) # It(form_valid) will call if all is well
    
class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        return reverse_lazy('home_page')
    
# class UserLogoutView(LogoutView):
#     def get_success_url(self):
#         if self.request.user.is_authenticated:
#             logout(self.request)
#         return reverse_lazy('home_page')
class UserLogoutView(RedirectView):
    url = reverse_lazy('home_page')  
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super().get(request, *args, **kwargs)


class UserBankAccountUpdateView(View):
    template_name = 'profile.html'
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_page')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})
    



def home(request):
    return HttpResponse("<h1>Hello</h1>")
