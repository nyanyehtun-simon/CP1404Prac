price_per_kWh = float(input('Price per kWh in cents: ')) / 100 # since it is in cents
daily_use_in_kWh = float(input('Daily user in kWh: '))
num_of_days_in_billing_period = float(input('Number of days in billing period: '))

estimated_bill = price_per_kWh * daily_use_in_kWh * num_of_days_in_billing_period

print('Estimated bill: ${:.2f}'.format(estimated_bill))