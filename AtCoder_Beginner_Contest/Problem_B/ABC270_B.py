x, y, z = map(int, input().split())

#ゴールが正の数の場合
if 0 < x:   
    #ゴールまでの間に壁がある場合
    if 0 < y < x: 
        #原点から壁までの間にハンマーがある場合
        if 0 < z < y: 
            print(x)
            
        #原点より後ろにハンマーがある場合
        elif z < 0: 
            print(2 * abs(z) + x)
            
        #ハンマーが手に入らない場合
        else: 
            print(-1)
            
    #ゴールまでの間に壁がない場合
    else:
        print(x)

#ゴールが負の数の場合
else:
    #ゴールまでの間に壁がある場合
    if x < y < 0: 
        #原点から壁までの間にハンマーがある場合
        if y < z < 0: 
            print(abs(x))
            
        #原点より後ろにハンマーがある場合
        elif 0 < z: 
            print(2 * z + abs(x))
            
        #ハンマーが手に入らない場合
        else: 
            print(-1)
            
    #ゴールまでの間に壁がない場合
    else:
        print(abs(x))