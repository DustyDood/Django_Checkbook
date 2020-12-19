from django.forms import ModelForm
from .models import Account, Transaction


# Creating a form based off the Account model
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

# Creating a form based off of the Transaction model
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
