collected_money = 0
Indebted_shops = int(input("จำนวนร้านที่ต้องไปทวงหนี้วันนี้ฮ้าฟฟู่ว: "))
for i in range(Indebted_shops):
    money = int(input("เงินส่วยที่เก็บมาได้: "))
    collected_money += money
    print(collected_money)