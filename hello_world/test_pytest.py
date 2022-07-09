from hello_world import hello_world

param_list = [["Mike", "Hello World!! My name is Mike"],["Mary", "Hello World!! My name is Mary"],["Tom", "Hello World!! My name is Tom"]]

def test_myMessage():
    for name, message in param_list:
        assert hello_world.myMessage(name) == message