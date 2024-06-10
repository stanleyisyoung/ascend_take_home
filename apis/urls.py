from django.urls import path
from . import views

urlpatterns = [
  path('', views.FinanceTermsListView.as_view(), name='list_finance_terms'),
  path('finance-terms/', views.FinanceTermsView.as_view(), name='finance_terms'),
  path('agree-finance-terms/<int:terms_id>/', views.AgreeFinanceTermsView.as_view(), name='agree_finance_terms'),
]