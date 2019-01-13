products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]

on_sale_products = [on_sale_product for on_sale_product in products if on_sale_product[-1] is True]

print(on_sale_products)
