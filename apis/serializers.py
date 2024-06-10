from rest_framework import serializers

from insurance.models import Customer, InsurancePolicy, FinanceTerms, FinanceTermsInsurancePolicy

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = '__all__'

class InsurancePolicySerializer(serializers.ModelSerializer):
  customer = CustomerSerializer()

  class Meta:
    model = InsurancePolicy
    fields = '__all__'

  def create(self, validated_data):
    customer_data = validated_data.pop('customer')
    customer, created = Customer.objects.get_or_create(**customer_data)
    insurance_policy = InsurancePolicy.objects.create(customer=customer, **validated_data)
    return insurance_policy

class FinanceTermsSerializer(serializers.ModelSerializer):
  class Meta:
    model = FinanceTerms
    fields = '__all__'

class FinanceTermsInsurancePolicySerializer(serializers.ModelSerializer):
  class Meta:
    model = FinanceTermsInsurancePolicy
    fields = '__all__'