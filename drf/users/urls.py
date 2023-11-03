from django.urls import path
from .views import SignUpView, LoginView
urlpatterns = [
    path('signup/', SignUpView.as_view({
        'post':'create'
    })),

    path('login/', LoginView.as_view({
        'post':'post'
    }))

    
]