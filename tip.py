def tc(amount,tip):
    total=amount*(1+0.01*tip)
    total=round(total,2)
    print(f"please pay ${total}")
tc(130,20)