while True:
    button = input("Enter : ")
    if button == 'B' or button == 'b':
        Base2 = input("ป้อนตัวเลขฐานสอง : ")
        Total_Base2 = 0
        Len_Base2 = len(Base2)
        Multiply_Base2 = 0
        for x in Base2:
            Len_Base2 -= 1
            Multiply_Base2 = 2**Len_Base2
            Total_Base2 += int(x) * Multiply_Base2
        print(Total_Base2)

    elif button == 'O' or button == 'o':
        Base8 = input("ป้อนตัวเลขฐานแปด : ")
        Len_Base8 = len(Base8)
        Total_Base8 = 0
        Multiply = 0
        for i in range(Len_Base8):
            Len_Base8 -= 1
            Multiply = 8**Len_Base8
            Total_Base8 += int(Base8[i]) * Multiply 
        print(Total_Base8)

    else:
        break



       

        


'''
ตัวแปร = 110110
รับขนาด = len(ตัวแปร) = 6
for x in ตัวแปร (110110) 
    #* รับขนาด -= 1
    if x != 0:
        #! รอบที่ 0 x = 1
        #* รับขนาด รอบที่ 0 = 5
        2 ** 5 = 32
        decimal = 32

        #! รอบที่ 1 x = 1
        #* รับขนาด รอบที่ 1 = 4
        2 ** 4 = 16
        decimal = 32 + 16 = 48

        #! รอบที่ 2 x = 0
        pass

        #! รอบที่ 3 x = 1
        #* รับขนาด รอบที่ 3 = 2
        2 ** 2 = 4
        decimal = 48 + 4 = 52

        #! รอบที่ 4 x = 1
        #* รับขนาด รอบที่ 4 = 1
        2 ** 1 = 2
        decimal = 52 + 2 = 54

        #! รอบที่ 5 x = 0
        pass
print (decimal)
'''

