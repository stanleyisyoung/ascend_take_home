from django.test import TestCase
from insurance.models import Customer, InsurancePolicy, FinanceTerms
from rest_framework.test import APIClient

class CustomerModelTest(TestCase):
  def test_create_customer(self):
    customer = Customer.objects.create(name='Harry Potter')
    self.assertEqual(customer.name, 'Harry Potter')

class InsurancePolicyModelTest(TestCase):
  def test_create_insurance_policy(self):
    customer = Customer.objects.create(name='Harry Potter')
    policy = InsurancePolicy.objects.create(
      premium=200.00,
      tax_fee=50.00,
      customer=customer
    )
    self.assertEqual(policy.premium, 200.00)
    self.assertEqual(policy.tax_fee, 50.00)
    self.assertEqual(policy.customer.name, 'Harry Potter')

class FinanceTermsModelTest(TestCase):
  def test_create_finance_terms(self):
    terms = FinanceTerms.objects.create(
      downpayment=200.00,
      due_date='2024-12-12',
      amount_financed=400.00
    )
    self.assertEqual(terms.downpayment, 200.00)
    self.assertEqual(terms.due_date, '2024-12-12')
    self.assertEqual(terms.amount_financed, 400.00)

class FinanceTermsAPITest(TestCase):
  def setUp(self):
    self.client = APIClient()

  def test_create_finance_terms(self):
    policies = [
      {"premium": 200, "tax_fee": 50, "customer": {"name": "Harry Potter"}},
      {"premium": 300, "tax_fee": 50, "customer": {"name": "Hermione Granger"}}
    ]
    response = self.client.post('/finance-terms/', {"policies": policies, "due_date": "2024-12-12"}, format='json')
    self.assertEqual(response.status_code, 201)

  def test_agree_finance_terms(self):
    terms = FinanceTerms.objects.create(
      downpayment=200.00,
      due_date='2024-12-12',
      amount_financed=400.00
    )
    response = self.client.post(f'/agree-finance-terms/{terms.id}/', format='json')
    self.assertEqual(response.status_code, 200)
    terms.refresh_from_db()
    self.assertTrue(terms.status)

  def test_list_finance_terms(self):
    FinanceTerms.objects.create(
      downpayment=200.00,
      due_date='2024-12-12',
      amount_financed=400.00,
      status=False
    )
    FinanceTerms.objects.create(
      downpayment=250.00,
      due_date='2024-11-12',
      amount_financed=450.00,
      status=True
    )
    response = self.client.get('', format='json')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.data), 2)
