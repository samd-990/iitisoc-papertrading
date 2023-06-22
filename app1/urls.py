from . import views
from django.urls import path


urlpatterns = [
    path("",views.home,name="home"),
    path("about",views.about,name="aboutpage"),
    path("portfolio",views.portfolio,name="portfolio"),
    path("view_market",views.view_market,name="view_market")
]
