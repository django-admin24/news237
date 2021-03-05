from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from .views import register, profile, p_update, authors_list



urlpatterns = [
    path('', register, name="register"),
    path('post/authors/list/', authors_list, name="authors"),
    # path('<id>/post/list/', Profileview, name="user-post-list"),
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'), name="password_reset"),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name="password_reset_complete"),
    path('profile/', profile, name="profile"),
    path('profile_update/', p_update, name="update-profile"),
    
]
