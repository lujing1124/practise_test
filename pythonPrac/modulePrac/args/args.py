def milk_tea_shop(kind,*argument, **keywords):
    print(f"老板来杯{kind}奶茶！")
    for arg in argument:
        print(f"{arg}")
    for key in keywords:
        print(f"{key},{keywords[key]}")
        
        
milk_tea_shop(
    "杨枝甘露",
    "加糖","少冰","珍珠","假茅台",
    price="10元",address="和静路26-101"
)