print("สวัสดีครับ โปรแกรมนี้คือโปรแกรมทายตัวเลขในหัวคุณ")

print("               กติกา   ")
print("คิดเลข 1-15 ไว้ในใจและตอบคำถามของเรา 4 ข้อ ")
input("หากพร้อมแล้ว Press enter:")

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for num in numbers:
    if num%2==1:
        print(num," ",end="")
        
print(" ")
a1=input("เลขที่คุณกำลังคิดอยู่ในนี้ไหม (ถ้าอยู่พิมพ์ 1 ถ้าไม่อยู่พิมพ์ 0) : ")

for num2 in numbers:
    if str(bin(num2))[-2]== '1':
        print(num2," ",end="")
print(" ")
a2=input("เลขที่คุณกำลังคิดอยู่ในนี้ไหม (ถ้าอยู่พิมพ์ 1 ถ้าไม่อยู่พิมพ์ 0) : ")

for num3 in numbers:
    if str(bin(num3))[-3]== '1':
        print(num3," ",end="")
print(" ")
a3=input("เลขที่คุณกำลังคิดอยู่ในนี้ไหม (ถ้าอยู่พิมพ์ 1 ถ้าไม่อยู่พิมพ์ 0) : ")

for num4 in numbers:
    binary_num4 = bin(num4)[2:]  
    if len(binary_num4) == 4 and binary_num4[-4] == '1':
        print(num4," ",end="")
print(" ")
a4=input("เลขที่คุณกำลังคิดอยู่ในนี้ไหม (ถ้าอยู่พิมพ์ 1 ถ้าไม่อยู่พิมพ์ 0) : ")

binary = "0b"+a4+a3+a2+a1
a = int(binary,2)
print(" !!เรารู้แล้วว่าคุณกำลังคิดเลขอะไรอยู่!!")
print(" นั่นคึือ เลข : ", a)
