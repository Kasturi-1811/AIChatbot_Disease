from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserCreationForm, ProfileUpdateForm


# ---------------- REGISTER ----------------
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # Automatically approve general users, doctors need approval
            if user.role == 'DOCTOR':
                user.is_approved = False
                messages.info(
                    request,
                    "Your registration is submitted. Admin approval is required."
                )
            else:
                user.is_approved = True

            user.save()
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


# ---------------- LOGIN ----------------
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()

            # 🔒 Block inactive users
            if not user.is_active:
                messages.error(request, "Your account is disabled.")
                return redirect('login')

            # 🔒 Block unapproved doctors
            if user.role == 'DOCTOR' and not user.is_approved:
                messages.warning(
                    request,
                    "Your account is under review. Please wait for admin approval."
                )
                return redirect('login')

            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})
# ---------------- PROFILE ----------------
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'accounts/profile.html', {'form': form})


# ---------------- LOGOUT ----------------
def custom_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')
