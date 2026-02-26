import re
import json

# Open the receipt file
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Extract all prices (handle spaces like "1 200,00")
# Replace comma with dot and remove spaces to convert to float
price_matches = re.findall(r'(\d{1,3}(?: \d{3})*(?:,\d{2})?)', text)
prices_float = [float(p.replace(" ", "").replace(",", ".")) for p in price_matches]

# 2. Extract product names (lines before quantity and price)
lines = text.splitlines()
products = []
for i, line in enumerate(lines):
    # Line with quantity and price: "1,000 x 51,00" or "2,000 x 154,00"
    if re.search(r'\d+,\d{3}|\d+ x \d+,\d{2}|\d+,\d{2}', line):
        if i > 0:
            product_name = lines[i-1].strip()
            products.append(product_name)

# 3. Total amount (use the total from the receipt if available)
total_amount_match = re.search(r'ИТОГО:\s*([\d\s]+,\d{2})', text)
total_amount = float(total_amount_match.group(1).replace(" ", "").replace(",", ".")) if total_amount_match else sum(prices_float)

# 4. Extract date and time
date_time_match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})', text)
date_time = date_time_match.group(1) if date_time_match else "Not found"

# 5. Extract payment method
payment_match = re.search(r'(Банковская карта|Наличные|cash|card|visa|mastercard)', text, re.IGNORECASE)
payment_method = payment_match.group(1) if payment_match else "Not found"

# 6. Structured output as JSON
receipt_info = {
    "products": products,
    "prices": prices_float,
    "total_amount": total_amount,
    "date_time": date_time,
    "payment_method": payment_method
}

# Print formatted JSON
print(json.dumps(receipt_info, indent=4, ensure_ascii=False))