print('Electricity bill estimator 2.0')

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff_num = int(input('Which tariff? 11 or 31: '))
if tariff_num == 11:
    tariff_amount = TARIFF_11
elif tariff_num == 31:
    tariff_amount = TARIFF_31

# price_per_kWh = float(input('Price per kWh in cents: ')) / 100 # since it is in cents
daily_use_in_kWh = float(input('Daily user in kWh: '))
num_of_days_in_billing_period = float(input('Number of days in billing period: '))

estimated_bill = tariff_amount * daily_use_in_kWh * num_of_days_in_billing_period

print('Estimated bill: ${:.2f}'.format(estimated_bill))
