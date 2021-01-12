from django.urls import path,include
# from .views import login_view,logout_view,register
from .views import RegistrationAPIView,LoginView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [


    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]