from django.urls import path
from .views import DepositMoneyView, WithdrawalMoneyView, LoanListView, LoanRequestView, PayLoanView, TransactionReportView 


urlpatterns = [
    path('deposit/', DepositMoneyView.as_view(), name='deposit_money'),
    path('report/', TransactionReportView.as_view(), name='transaction_report'),
    path('withdraw/', WithdrawalMoneyView.as_view(), name='withdraw_money'),
    path('loan_request/', LoanRequestView.as_view(), name='loan_request'),
    path('loans/', LoanListView.as_view(), name='loan_list'),
    path('loans/<int:loan_id>', PayLoanView.as_view(), name='pay_loan'),
    # path('transfer-money/', TransferMoneyView.as_view(), name='transfer_money'),
]