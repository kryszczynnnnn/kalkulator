from main import Window
import unittest

class TestFunctions(unittest.TestCase):
    def test_clear(self):
        self.assertEqual(Window.clear(self=Window), "cleared")
    def test_clear_all(self):
        self.assertEqual(Window.clear_all(self=Window), "all cleared")
    def test_enter(self):
        self.assertEqual(Window.enter(self=Window, letter="1"), "1")
    def test_delete(self):
        self.assertEqual(Window.delete(self=Window), "deleted")
    def test_oblicz(self):
        self.assertEqual(Window.oblicz(self=Window, liczba1="1", liczba2="2", operation="+"), "3")
        self.assertEqual(Window.oblicz(self=Window, liczba1="1", liczba2="0", operation="/"), "Syntax Error")
        self.assertEqual(Window.oblicz(self=Window, liczba1="1", liczba2="0", operation="*"), "0")
        self.assertEqual(Window.oblicz(self=Window, liczba1="1", liczba2="6", operation="-"), "-5")
        
if __name__ == '__main__':
    unittest.main()