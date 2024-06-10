from django.db import models

class Customer(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class InsurancePolicy(models.Model):
  premium = models.DecimalField(max_digits=10, decimal_places=2)
  tax_fee = models.DecimalField(max_digits=10, decimal_places=2)
  customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
  agreed = models.BooleanField(default=False)
  due_date = models.DateField(null=True, blank=True)

  def __str__(self):
    return f'{self.customer.name} - {self.premium}'

class FinanceTerms(models.Model):
  downpayment = models.DecimalField(max_digits=10, decimal_places=2)
  due_date = models.DateField()
  amount_financed = models.DecimalField(max_digits=10, decimal_places=2)
  status = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.downpayment} - {self.due_date}'

class FinanceTermsInsurancePolicy(models.Model):
  finance_terms = models.ForeignKey(FinanceTerms, on_delete=models.CASCADE)
  insurance_policy = models.ForeignKey(InsurancePolicy, on_delete=models.CASCADE)

  class Meta:
    unique_together = ('finance_terms', 'insurance_policy')

  def __str__(self):
    return f'{self.finance_terms} - {self.insurance_policy}'