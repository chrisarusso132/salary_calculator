'''
Program GUI_template.py
Chapter 8 (Page 251)
1/18/2024

**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

Template code for any GUI-based application in Chapter 8
'''

from breezypythongui import EasyFrame
from tkinter.font import Font

# Other imports go here

# Class header (class name will change project to project)
class SalaryCalculator(EasyFrame):

	# Definition of our classes' constructor method
	def __init__(self):
		# Call to the Easy Frame class constructor
		EasyFrame.__init__(self, title = "Salary Calculator", background = "lightgreen", width = 400, height = 250)
		# variable to store a Font design for multiple labels (Must come before needing to use the variable in your code)
		labelFont = Font(family = "Georgia", size = 14)

		# Add the widgets to the window
		self.addLabel(text = "Salary Calculator", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "lightgreen", font = Font(family = "Impact", size = 22))
		self.addLabel(text = "Hourly Wage:", row = 1, column = 0, background = "lightgreen", foreground = "darkgreen", font = labelFont)
		self.wageField = self.addFloatField(value = 0.0, row = 1, column = 1)
		self.addLabel(text = "No. of Hours Worked:", row = 2, column = 0, background = "lightgreen", foreground = "darkgreen", font = labelFont)
		self.hoursField = self.addIntegerField(value = 0, row = 2, column = 1)

		# Bind the hourField to the press of the enter key event
		self.hoursField.bind("<Return>", Lambda event: self.compute())

		# Create and customize the button
		self.button = self.addButton(text  ="Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		self.button["background"] = "palegoldenrod"
		self.button["width"] = 15



		self.outputLabel = self.addLabel(text = "", row = 4, column = 0, columnspan = 2, sticky = "NEWS", background = "lightgreen", foreground = "darkgreen", font = labelFont)
		# self.addLabel(text = "The employee's salary is:", row = 4, column = 0, background = "lightgreen", foreground = "darkgreen", font = labelFont)
		# self.outputField = self.addFloatField(value = 0.0, row = 4, column = 1, precision = 2, state = "readonly")

	# Definition of the compute() function which is the event handler
	def compute(self):
		wage = self.wageField.getNumber()
		hours = self.hoursField.getNumber()
		salary = wage * hours
		# self.outputField.setNumber(salary)
		self.outputLabel["text"] = "The employee's salary is: $%0.2f" % salary





# Global definition of the main() method
def main():
	# Instantiate an object from the class into mainloop()
	SalaryCalculator().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()