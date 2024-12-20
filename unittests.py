import unittest
from unittest.mock import MagicMock, patch
import gui_calculator

class TestCalculatorGUI(unittest.TestCase):
    def setUp(self):
        # Create a test instance of the GUI
        self.root = gui_calculator.tk.Tk()
        self.entry1 = gui_calculator.tk.Entry(self.root)
        self.entry2 = gui_calculator.tk.Entry(self.root)
        self.result_label = gui_calculator.tk.Label(self.root)
        self.operation_var = gui_calculator.tk.StringVar(value="Addition")

    def tearDown(self):
        self.root.destroy()

    @patch("gui_calculator.messagebox.showerror")
    def test_empty_input(self, mock_showerror):
        """Test behavior when input fields are empty."""
        self.entry1.insert(0, "")
        self.entry2.insert(0, "")

        gui_calculator.entry1 = self.entry1
        gui_calculator.entry2 = self.entry2
        gui_calculator.operation_var = self.operation_var
        gui_calculator.result_label = self.result_label

        gui_calculator.calculate()
        mock_showerror.assert_called_with("Error", 'Both input fields are empty.')

    @patch("gui_calculator.messagebox.showerror")
    def test_invalid_number_input(self, mock_showerror):
        """Test behavior when invalid numbers are input."""
        self.entry1.insert(0, "abc")  # Invalid input
        self.entry2.insert(0, "5")

        gui_calculator.entry1 = self.entry1
        gui_calculator.entry2 = self.entry2
        gui_calculator.operation_var = self.operation_var
        gui_calculator.result_label = self.result_label

        gui_calculator.calculate()
        mock_showerror.assert_called_with("Error", "could not convert string to float: 'abc'")

    @patch("gui_calculator.messagebox.showerror")
    def test_divide_by_zero(self, mock_showerror):
        """Test behavior for division by zero."""
        self.entry1.insert(0, "10")
        self.entry2.insert(0, "0")

        gui_calculator.entry1 = self.entry1
        gui_calculator.entry2 = self.entry2
        gui_calculator.operation_var.set("Division")
        gui_calculator.result_label = self.result_label

        gui_calculator.calculate()
        mock_showerror.assert_called_with("Error", "Cannot divide by zero.")

    def test_correct_result_display(self):
        """Test that the correct result is displayed for addition."""
        self.entry1.insert(0, "10")
        self.entry2.insert(0, "5")

        gui_calculator.entry1 = self.entry1
        gui_calculator.entry2 = self.entry2
        gui_calculator.operation_var.set("Addition")
        gui_calculator.result_label = self.result_label

        gui_calculator.calculate()
        self.assertEqual(self.result_label.cget("text"), "Result: 15.0")

    def test_operation_selection(self):
        """Test that operation selection updates the result correctly."""
        self.entry1.insert(0, "9")
        self.entry2.insert(0, "3")

        gui_calculator.entry1 = self.entry1
        gui_calculator.entry2 = self.entry2
        gui_calculator.operation_var.set("Multiplication")
        gui_calculator.result_label = self.result_label

        gui_calculator.calculate()
        self.assertEqual(self.result_label.cget("text"), "Result: 27.0")

if __name__ == "__main__":
    unittest.main()
