def func(x=1, y=2):
    print(x,y)

func(10,20)
func(10)
func(x = 10)
func(y = 20)
func(x = 10, y = 20)
func(y = 10, x = 20)
#func(x = 10, 20)#Wrong - optional parameters must come at the end
