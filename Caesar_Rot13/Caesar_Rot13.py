chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
        'r','s','t','u','v','w','x','y','z']
input_lenght = int(input("Enter your number : "))
text = []

for c in range(input_lenght):
    text.append(input("Enter : your text : "))
n = input("Enter : ")

for x in text:
    for i in range (len(chars)):
        if x == chars[i]: #TODO ถ้าไม่ใส่ชื่อตัวแปรของ list ข้างหน้ามันจะเป็น เลข ถ้าใส่มันจะเป็นค่าใน list
            if n == 'g':
                ceasar = (i + 3)%26
                print("เข้ารหัส Ceasar",chars[ceasar])
                rot = (i + 13)%26
                print("เข้ารหัส Rot",chars[rot])
            elif n == 'f':
                ceasar = (i - 3)%26
                print(chars[ceasar])
                rot = (i - 13)%26
                print(chars[rot])

        
