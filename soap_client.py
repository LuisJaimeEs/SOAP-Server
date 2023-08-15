from zeep import Client

# Use the public URL provided by pyngrok
url = 'https://7d80-177-227-58-128.ngrok.io/?wsdl'
client = Client(url)

a = 10
b = 5

result_add = client.service.add(a, b)
result_subtract = client.service.subtract(a, b)

print(f"Addition: {a} + {b} = {result_add}")
print(f"Subtraction: {a} - {b} = {result_subtract}")
