import main
import unittest
import tkinter as tk
from tkinter import messagebox as mess


class TestGUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.window = tk.Tk()
        # Add setup code for initializing the GUI elements

    @classmethod
    def tearDownClass(cls):
        cls.window.destroy()

    def test_contact_button(self):
        # Simulate button click
        contact_button = self.window.children['contact_button']
        contact_button.invoke()

        # Check if the message box is displayed with the correct message
        self.assertTrue(mess._called)
        self.assertEqual(mess._title, 'Contact me')
        self.assertEqual(mess._message, "Please contact me on : 'chandrasekar@arigs.com' ")

    def test_change_pass_button(self):
        # Simulate button click
        change_pass_button = self.window.children['change_pass_button']
        change_pass_button.invoke()

        # Check if the change password window is opened
        self.assertTrue(self.window.children['change_pass_window'])

        # Add more assertions to check the behavior of the change password functionality

    def test_clear_button(self):
        # Simulate button click
        clear_button = self.window.children['clear_button']
        clear_button.invoke()

        # Check if the text entry fields are cleared
        txt_value = self.window.children['txt'].get()
        txt2_value = self.window.children['txt2'].get()
        self.assertEqual(txt_value, '')
        self.assertEqual(txt2_value, '')

        # Check if the message label is updated with the correct message
        message1 = self.window.children['message1']
        self.assertEqual(message1.cget('text'), "1)Take Images  >>>  2)Save Profile")

    # Add more test cases for other functionality


if __name__ == '__main__':
    unittest.main()
