from django.urls import path, include

urlpatterns = [
    path('chat/', include('chat.urls')),  # Make sure this line exists
]
