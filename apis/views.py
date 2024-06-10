from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializers import InsurancePolicySerializer, FinanceTermsSerializer
from insurance.models import Customer, InsurancePolicy, FinanceTerms, FinanceTermsInsurancePolicy

class FinanceTermsView(APIView):
  def post(self, request):
    policies = request.data.get('policies', [])
    due_date = request.data.get('due_date')
    
    if not policies or not due_date:
      return Response({"error": "Policies and due date are required."}, status=status.HTTP_400_BAD_REQUEST)
    
    total_premium = sum(policy['premium'] for policy in policies)
    total_tax_fee = sum(policy['tax_fee'] for policy in policies)
    downpayment = sum((policy['premium'] * 0.20) + policy['tax_fee'] for policy in policies)
    amount_financed = (total_premium + total_tax_fee) - downpayment
    
    finance_terms = FinanceTerms.objects.create(
      downpayment=downpayment,
      due_date=due_date,
      amount_financed=amount_financed
    )
    
    for policy in policies:
      customer_data = policy['customer']
      customer, created = Customer.objects.get_or_create(name=customer_data['name'])
      insurance_policy = InsurancePolicy.objects.create(
        premium=policy['premium'],
        tax_fee=policy['tax_fee'],
        customer=customer,
        due_date=due_date
      )
      FinanceTermsInsurancePolicy.objects.create(
        finance_terms=finance_terms,
        insurance_policy=insurance_policy
      )
    
    return Response(FinanceTermsSerializer(finance_terms).data, status=status.HTTP_201_CREATED)

class AgreeFinanceTermsView(APIView):
  def post(self, request, terms_id):
    try:
      finance_terms = FinanceTerms.objects.get(id=terms_id)
      finance_terms.status = True
      finance_terms.save()
      return Response(FinanceTermsSerializer(finance_terms).data, status=status.HTTP_200_OK)
    except FinanceTerms.DoesNotExist:
      return Response({"error": "Finance terms not found."}, status=status.HTTP_404_NOT_FOUND)

class FinanceTermsListView(ListAPIView):
  queryset = FinanceTerms.objects.all()
  serializer_class = FinanceTermsSerializer

  def get_queryset(self):
    queryset = super().get_queryset()
    downpayment = self.request.query_params.get('downpayment')
    status = self.request.query_params.get('status')
    order_by = self.request.query_params.get('order_by')

    if downpayment:
      queryset = queryset.filter(downpayment__exact=downpayment)
    if status is not None:
      queryset = queryset.filter(status=status)
    if order_by:
      queryset = queryset.order_by(order_by)

    return queryset
