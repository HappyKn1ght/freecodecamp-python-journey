products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
products['Laptop'] = 1000 #new value
# print(products.values())
for product, price in products.items():
    products[product] = round(price * 0.8)

print("Products price after discount:")
print(products)

print("Products details with index:")
for index, product in enumerate(products.items()):
    print(index, product)