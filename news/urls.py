from django.urls import path, include
from news.views import home, news_details, categories, news, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:id>/", news_details, name="news-details-page"),
    path("categories/", categories, name="categories-form"),
    path("news/", news, name="news-form"),
    path('api/', include(router.urls)),

]
