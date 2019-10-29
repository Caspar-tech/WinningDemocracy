from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', user_views.MainView.as_view(), name='main'),
        path('login/', auth_views.LoginView.as_view(template_name='Game/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='Game/logout.html'), name='logout'),
        path('elections/', user_views.ElectionsView.as_view(), name='elections'),
        path('counties/<int:pk>/', user_views.DetailCountiesView.as_view(), name='detail_counties'),
        path('representatives/<int:pk>/', user_views.RepresentativesDetailView.as_view(), name='detail_representatives'),
        path('parties/<int:pk>/', user_views.PartiesDetailView.as_view(), name='detail_parties'),
        path('parliament/', user_views.ParliamentView.as_view(), name='parliament'),
        path('government/', user_views.GovernmentView.as_view(), name='government'),
]