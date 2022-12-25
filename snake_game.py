import snake_class as scl
import time as tm
check = False
pole = scl.Window()

snake = [scl.Snake('black', 'white', 'turtle', i*30, i*50, 5) for i in range(1)]
food = scl.Food('red', 'circle')
food.food_pos()
pole.listen_p(snake)
print(snake)
while True:
    for i in snake:
        if i.accident():
            i.step()
        else:
            check = True
            pole.end_game()
        if i.check_food(food):
            food.food_pos()
            i.more('black', 'turtle')
    pole.reload()
    tm.sleep(0.1) #задержка
    if check:
        break
        
    
