from tkinter import * 
from tkcalendar import Calendar  # Calendar widget for selecting dates
import csv  

# Define the main class for the Calendar application and instantiate 'root' and 'title.' For the title, give it a title of 'Calendar App to CSV'
class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App to CSV")

        # Create a Calendar widget with day selection mode, initialized to Oct 1, 2024
        self.cal = Calendar(self.root, selectmode="day", year=2024, month=10, day=1)
        
        # Add padding to position the calendar nicely in the window
        self.cal.grid(row=0, column=0, padx=10, pady=10)
        
        # Create a button that, when clicked, will trigger the function to save the selected date
        self.save_button = Button(self.root, text="Save Date", command=self.save_date)
    
        # Add padding around the button for spacing
        self.save_button.grid(row=3, column=0, padx=10, pady=10)
    
        # Create an entry field where users can input additional information to save with the date
        self.info_entry = Entry(self.root)
    
        # Add padding to position the entry field
        self.info_entry.grid(row=2, column=0, padx=10)
    
    # Create a Function to save the selected date and input from the entry widget
    def save_date(self):
    
        # Retrieve the selected date from the calendar widget
        selected_date = self.cal.get_date()

        # Retrieve the user input from the Entry widget
        info = self.info_entry.get()

        # Call the function to save the date and the user input to a CSV file
        self.save_to_csv(selected_date, info)

        # Print a confirmation message to the console (for testing purposes)
        print("Date and info collected successfully!")

    # Create Function to write the selected date and entry to a CSV file, which will pass the selected date and entry as parameters.
    def save_to_csv(self, selected_data, info):
        
        # Open or create the CSV file in append mode to avoid overwriting existing data
        with open("calendar_data.csv", "a", newline="") as csvfile:
            Header = ["Date", "Entry"]  # Header for the CSV file (date and user input fields)

            # Create a CSV writer object
            writer = csv.writer(csvfile)
            
            # Check if the file is empty and write the header if necessary
            if csvfile.tell() == 0:
                writer.writerow(Header)

            # Write the selected date and user input as a new row in the CSV file
            writer.writerow([selected_data, info])

# Create the main application window
root = Tk()

# Instantiate the CalendarApp class, passing the root window as the parent
CalendarApp(root)

# Start the main event loop to run the Tkinter GUI application
root.mainloop()