print('Electricity Bill Estimator 2.0')

TARIFF_DICT = {
    "TARIFF_11": 0.244618,
    "TARIFF_31": 0.136928
}

tariff = input("Which tariff? {0} or {1}:".format(*TARIFF_DICT.keys()))
daily_use_in_kWh = float(input('Enter daily use in kWh: '))
billing_days = float(input('Enter number of billing days: '))

estimated_bill = TARIFF_DICT[tariff] * daily_use_in_kWh * billing_days

print('Estimated bill: ${}'.format(round(estimated_bill, 2)))


