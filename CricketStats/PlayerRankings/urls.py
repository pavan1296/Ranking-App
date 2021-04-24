from django.urls import path
from .views import (
    MensBattingStats,
    MensBowlingStats,
    MensAllRounderStats,
    WomensBattingStats,
    WomenBowlingStats,
    WomenAllRounderStats
)
urlpatterns = [
    path('men/batting/<str:match_type>/v1/', MensBattingStats.as_view()),
    path('men/bowling/<str:match_type>/v1/', MensBowlingStats.as_view()),
    path('men/all-rounder/<str:match_type>/v1/', MensAllRounderStats.as_view()),
    path('women/batting/<str:match_type>/v1/', WomensBattingStats.as_view()),
    path('women/bowling/<str:match_type>/v1/', WomenBowlingStats.as_view()),
    path('women/all-rounder/<str:match_type>/v1/', WomenAllRounderStats.as_view())
]