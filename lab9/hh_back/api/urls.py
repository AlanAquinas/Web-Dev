from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompanyList.as_view(), name='company-list'),
    path('companies/create/', views.CompanyCreate.as_view(), name='company_create'),
    path('companies/<int:pk>/', views.CompanyDetail.as_view(), name='company-detail'),
    path('companies/<int:company>/vacancies/', views.CompanyVacanciesList.as_view(), name='company-vacancies-list'),
    path('vacancies/', views.VacancyList.as_view(), name='vacancies-list'),
    path('vacancies/create/', views.VacancyCreate.as_view(), name='vacancy_create'),
    path('vacancies/<int:pk>/', views.VacancyDetail.as_view(), name='vacancy-detail'),
    path('vacancies/top/', views.TopTenVacanciesList.as_view(), name='vacancy-top-list')
]