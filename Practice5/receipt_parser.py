import re
import json

# Open the receipt file
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Extract all prices (handle spaces like "1 200,00")
# Replace comma with dot and remove spaces to convert to float
price_matches = re.findall(r'(\d[\d ]*,\d{2})', text)
prices_float = [float(p.replace(" ", "").replace(",", ".")) for p in price_matches]
# 2. Extract product names (lines before quantity and price)
lines = text.splitlines()
items = []

for i, line in enumerate(lines):

    # Line with quantity and price: "1,000 x 51,00" or "2,000 x 154,00"
    match = re.search(r'([\d,]+)\s*x\s*([\d\s]+,\d{2})', line)

    if match and i > 0:
        product_name = lines[i-1].strip()

        quantity = match.group(1)
        unit_price = float(match.group(2).replace(" ", "").replace(",", "."))

        # следующая строка обычно содержит итоговую стоимость позиции
        total_price = None
        if i + 1 < len(lines):
            total_match = re.search(r'(\d[\d\s]*,\d{2})', lines[i+1])
            if total_match:
                total_price = float(total_match.group(1).replace(" ", "").replace(",", "."))

        items.append({
            "product": product_name,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_price": total_price
        })

# 3. Total amount (use the total from the receipt if available)
total_amount_match = re.search(r'ИТОГО:\s*([\d\s]+,\d{2})', text)
total_amount = float(total_amount_match.group(1).replace(" ", "").replace(",", ".")) if total_amount_match else None

# 4. Extract date and time
date_time_match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})', text)
date_time = date_time_match.group(1) if date_time_match else "Not found"

# 5. Extract payment method
payment_match = re.search(r'(Банковская карта|Наличные|cash|card|visa|mastercard)', text, re.IGNORECASE)
payment_method = payment_match.group(1) if payment_match else "Not found"

# 6. Structured output as JSON
receipt_info = {
    "items": items,
    "total_amount": total_amount,
    "date_time": date_time,
    "payment_method": payment_method
}

# Print formatted JSON
print(json.dumps(receipt_info, indent=4, ensure_ascii=False))