import os ; os.environ["KIVY_NO_ARGS"] = "1" # hack for making tests loadable in VS Code
import unittest
from calculator.ui.gui import CalculatorApp


class CalculatorGUITestCase(unittest.TestCase):
    def setUp(self):
        self.app = CalculatorApp()
        self.app._run_prepare()

    def press_button(self, button_text):
        self.app.find_button_by(button_text).trigger_action()
        #finding the button and actually pressing it

    def assert_display(self, value):
        self.assertEqual(self.app.display.text, value)   

    def tearDown(self):
        self.app.stop()
    
    def assert_button_exists(self, button_text):
        self.assertIsNotNone(self.app.find_button_by(button_text))

class TestExpressions(CalculatorGUITestCase):
    def test_integer_expression(self):
        self.press_button("1")
        self.press_button("+")
        self.press_button("2")
        self.assert_display("1+2")
        self.press_button("=")
        self.assert_display("3")

    def test_float_expression(self):
        self.press_button("1")
        self.press_button(".")
        self.press_button("2")
        self.press_button("+")
        self.press_button("2")
        self.assert_display("1.2+2")
        self.press_button("=")
        self.assert_display("3.2")
        
class TextComplexExpressions(CalculatorGUITestCase):
    def test_gui_have_parenthesis_buttons(self):
        self.press_button("(")
        self.press_button(")")
        
    def test_gui_have_sqrt_and_power_buttons(self):
        self.press_button("√") #square root
        self.press_button("^") #power
    
    def test_gui_supports_complex_expressions(self):
      # sqrt(11-2)*(2^2)=12
        self.press_button("√")
        self.assert_display("sqrt")
        self.press_button("(")
        self.press_button("1")
        self.press_button("1")
        self.press_button("-")
        self.press_button("2")
        self.press_button(")")
        self.assert_display("sqrt(11-2)")
        self.press_button("*")
        self.press_button("(")
        self.press_button("2")
        self.press_button("^")
        self.press_button("2")
        self.press_button(")")
        self.assert_display("sqrt(11-2)*(2**2)")
        self.press_button("=")
        self.assert_display("12.0")

class TestLayout(CalculatorGUITestCase):
    
    def test_display(self):
        self.app = CalculatorApp()
        self.app._run_prepare()
    
    def test_initial_expression(self):
        for button_text in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "=", "C", "."]:
            #with statement enables me to see each single case
            with self.subTest(button=button_text):
                self.assert_button_exists(button_text)