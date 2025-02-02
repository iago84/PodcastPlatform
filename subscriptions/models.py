from django.db import models

class Plan(models.Model):
    model_state = models.BooleanField(default=True)
    date_created = models.DateTimeField('Date Creation', auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField('Date Update', auto_now=True, auto_now_add=False)
    name = models.CharField(max_length=100, verbose_name='Plan Name')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    duration_months = models.IntegerField(default=1, verbose_name='Duration (Months)')

    def __str__(self):
        return f'Plan - {self.name}'

class Subscription(models.Model):
    model_state = models.BooleanField(default=True)
    date_created = models.DateTimeField('Date Creation', auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField('Date Update', auto_now=True, auto_now_add=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='subscriptions', verbose_name='User')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='subscriptions', verbose_name='Plan')
    start_date = models.DateTimeField('Start Date', auto_now=False)
    end_date = models.DateTimeField('End Date', auto_now=False)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', verbose_name='Status')

    def __str__(self):
        return f'Subscription - {self.user.username} to {self.plan.name}'

class Transaction(models.Model):
    model_state = models.BooleanField(default=True)
    date_created = models.DateTimeField('Date Creation', auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField('Date Update', auto_now=True, auto_now_add=False)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='transactions', verbose_name='Subscription')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')
    payment_method = models.CharField(max_length=50, choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal'), ('bank_transfer', 'Bank Transfer')], verbose_name='Payment Method')
    transaction_date = models.DateTimeField('Transaction Date', auto_now=False)
    transaction_status = models.CharField(max_length=50, choices=[('completed', 'Completed'), ('pending', 'Pending'), ('failed', 'Failed')], default='completed', verbose_name='Transaction Status')

    def __str__(self):
        return f'Transaction - {self.id} for {self.subscription.user.username}'
