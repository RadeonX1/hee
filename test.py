text = str(input("input text:"))

# reverse text for left side
left = text[::-1]

for i in range(len(text)):
    left_part = left[i:]   # ตัดหัวทีละตัวฝั่งซ้าย
    right_part = text[i:]  # ตัดหัวทีละตัวฝั่งขวา
    print(f"{left_part:<10}{right_part:>10}")