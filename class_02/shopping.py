drinks = {'1': 3.5, '2': 4, '3': 2, '4': 4.5}
sum_money = 0
while True:
    choose = input('请选择你要购买的饮料，1橙汁，2椰汁，3矿泉水，4早餐奶，q去结账')
    if choose in drinks.keys():
        sum_money += drinks[choose]
        print('已选择饮料总金额{0}'.format(sum_money))
    elif choose == 'q':
        break
    else:
        print('不买也得买，给我选')
toubi = 0
while True:
    money = input('您已选择{0}元的商品，还需支付{1}请支付\n只能支付1，5，10元的硬币或纸币'.format(sum_money, sum_money - toubi))
    if money == '1' or money == '5' or money == '10':
        toubi += int(money)
        if toubi > sum_money:
            print('您已支付{0}元，找零{1}'.format(toubi, toubi - sum_money))
            break
        elif toubi < sum_money:
            print('商品总金额为{0}元,您已支付{1}元，还需支付{2}元'.format(sum_money, toubi, sum_money - toubi))
        else:
            print('商品总金额为{0}元,您已支付{1}元，已支付完毕'.format(sum_money, toubi))
            break
    else:
        print('投入金币不正确，重新投给我！')
