text = input("Enter a word or text: ")
style = input("Choose style (t / r / f): ").lower()
length = len(text)

if style == "t":
    for i in range(length):
        for j in range(i + 1):
            print(text[j] + " ", end="")
        print()
    print("Final:", " ".join(text))  # แสดงคำทั้งหมด

elif style == "r":
    for i in range(length):
        spaces = "  " * (length - i - 1)
        print(spaces, end="")
        for j in range(i + 1):
            print(text[j] + " ", end="")
        print()
    print("Final:", " ".join(text))  # แสดงคำทั้งหมด

elif style == "f":
    for i in range(length):
        spaces = "  " * (length - i - 1)
        left = text[:i][::-1]  # ด้านซ้าย (ย้อนกลับ)
        center = text[i]       # ตัวกลาง
        right = text[:i][::-1] # ด้านขวา (เหมือนซ้ายเพื่อสมมาตร)
        line = " ".join(left + center + right)
        print(spaces + line)
    print("Final:", " ".join(text))  # แสดงคำทั้งหมด

else:
    print("Invalid style. Please choose triangle, right-pyramid, or full-pyramid.")