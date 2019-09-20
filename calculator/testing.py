num1 = 123
num2 = 456
operChar = "+"

test = lambda i,j: i + j
print(test(2,3))

test = lambda: 23 + 23
print(test())

test = lambda num1, num2: num1 + num2
result = (test(num1,num2))


#std_calc_action.triggered.connect(lambda: widget.stack_widget.setCurrentIndex(0))
func_list = []
func_dict = {"func_text":"+","func_":"num1 + num2"}
result2 = (func_dict["func_"])
print(result2)
test3 = eval(result2)
print(test3)