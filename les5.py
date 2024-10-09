coinRoblox = 50
boots = 2*coinRoblox
jacket = 10*coinRoblox
devices = 10*coinRoblox
charsis = 8*coinRoblox
allPrice = boots+jacket+devices+charsis
print("Всего мы должны потратить - ",allPrice)
usd = allPrice//88.10
print("Всего вы потратили в долларах - ", int(usd),"$")
rubOst =allPrice-usd*88.10
print("У вас осталось рублей - ",rubOst)
print("-------------------------------")
vaniaS = 1000/1000
yaroslavS = 300/1000
auto_V_Vania = 60
yaroslav_V = 7
timeVania = vaniaS/auto_V_Vania
timeYaroslav = yaroslavS/yaroslav_V
print("Время Вани на автобусе",timeVania*60*60)
print("Время Ярослава пешком",timeYaroslav*60*60)




