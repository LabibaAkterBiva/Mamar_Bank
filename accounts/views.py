from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm,ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from transaction.views import send_transaction_email
# Create your views here.
class UserRegistrationView(FormView):
    template_name='user_registration.html'
    form_class=UserRegistrationForm
    success_url=reverse_lazy('register')
    
    def form_valid(self, form):
        user=form.save()
        login(self.request,user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name='user_login.html'
    def get_success_url(self) :
        return reverse_lazy('profile')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
class UserUpdateView(View):
    template_name = 'profile.html'
    
    def get(self, request):
        form = ProfileUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = ProfileUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Profile'
        })
        return context
@login_required
def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password change successfully')
            update_session_auth_hash(request, form.user)
            send_transaction_email(request.user, 0, 'Password Change Confirmation', 'pass_change_email.html' )
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html', {'form':form})
