from django.urls import path
from authentication import views as authViews

urlpatterns = [
   path('',authViews.home,name = 'home'),
   path('signup/',authViews.signup,name = 'signup'),
   path('signin',authViews.signin,name='signin'),
   path('signout',authViews.signout,name='signout'),
   path('resetPassword',authViews.resetPassword,name='resetPassword'),
]