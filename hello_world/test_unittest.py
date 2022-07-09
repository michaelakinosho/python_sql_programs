from hello_world import hello_world
import unittest

param_list = [["Mike", "Hello World!! My name is Mike"],["Mary", "Hello World!! My name is Mary"],["Tom", "Hello World!! My name is Tom"]]

class Test_TestmyMessage(unittest.TestCase):
        
    def test_myMessage(self):
        for name, message in param_list:
            self.assertEqual(hello_world.myMessage(name),message)
        
        
if __name__ == '__main__':
    unittest.main()