#แม่สูตรคูณแบบกำหนดช่วง
print("  สูตรคูณ")
start=int(input("ตั้งแต่:"))
end=int(input("จนถึง:"))
for i in range(start,  end+1):
    print("=================")
    print("สูตรคูณแม่:", i)
    for o in range(1, 13):
        print(i, "x", o,"=", i*o)
