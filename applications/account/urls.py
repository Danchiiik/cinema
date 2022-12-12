from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshSlidingView

from applications.account.views import RegisterApiView


urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshSlidingView.as_view())
]
