import customtkinter as CTk
from tkinter import messagebox
import pandas as pd
from tkcalendar import DateEntry
import datetime
import matplotlib.pyplot as plt 




class Inventory_Database_Management():
    def __init__(self):
        # Load inventory data from CSV or create new dataframe if not found
        try:
            self.df = pd.read_csv("inventory.csv")
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["Name", "Quantity", "Cost Price", "Sale Price"])


    def add_item(self, name, quantity, cost_price, sale_price):
        # Check if item already exists in inventory
        if name in self.df["Name"].values:
            return False
        # Create new item as dataframe, append to main dataframe
        new_item = pd.DataFrame([{"Name": name, "Quantity": quantity, "Cost Price": cost_price, "Sale Price": sale_price}])
        self.df = pd.concat([self.df, new_item], ignore_index=True)
        self.save_data()
        return True


    def update_item(self, name, quantity, cost_price, sale_price):
        if name in self.df["Name"].values:
            # Update specific row and save changes
            self.df.loc[self.df["Name"] == name, ["Quantity", "Cost Price", "Sale Price"]] = [quantity, cost_price, sale_price]
            self.save_data()
            return True
        return False


    def remove_item(self, name):
        if name in self.df["Name"].values:
            # Filter out the item from datadrame and save changes
            self.df = self.df[self.df['Name'] != name]
            self.save_data()
            return True
        return False


    # Calculate total inventory value
    def get_total_inventory_value(self):
        return (self.df["Quantity"] * self.df["Sale Price"]).sum()


    # Save changes to inventory data to CSV
    def save_data(self):
        self.df.to_csv("inventory.csv", index=False)




class Sales_Tracking:
    def __init__(self):
        # Load sales daata from CSV or create new dataframe if not found
        try:
            self.df = pd.read_csv("sales_data.csv")
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["Name", "Date", "Quantity Sold"])


    # Add or update sales data for a specific item and date
    def add_sales_data(self, name, date, quantity_sold):
        new_data = {"Name": name, "Date": date, "Quantity Sold": quantity_sold}


        # Update the record if it exists or append new data
        self.df = self.df.drop(self.df[(self.df["Name"] == name) & (self.df["Date"] == date)].index)
        self.df = pd.concat([self.df, pd.DataFrame([new_data])], ignore_index=True)

        
        self.save_data()


    # Save sales data to CSV
    def save_data(self):
        self.df.to_csv("sales_data.csv", index=False)
        

    # Retrieve sales data for a specific item
    def get_sales_data(self, name):
        return self.df[self.df["Name"] == name]


    def get_restock_prediction(self, name):
        # Predict when restock might be needed based on sales frequency
        item_sales = self.get_sales_data(name)
        if item_sales.empty:
            return "No data available"

        # Calculate average days between sales
        item_sales["Date"] = pd.to_datetime(item_sales["Date"])
        item_sales = item_sales.sort_values(by="Date")
        avg_days_between_sales = item_sales["Date"].diff().dt.days.mean()

        # Estimate a restock date based on average frequency
        restock_date = datetime.datetime.now() + datetime.timedelta(days=avg_days_between_sales)
        return restock_date.strftime("%m-%d-%y")




# Create the main application class using customtkinter
class Main_App_GUI():
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        CTk.set_appearance_mode("Dark")


        self.Inventory_Database_Management = Inventory_Database_Management()
        self.Sales_Tracking = Sales_Tracking()


        self.create_homepage_window()


    def create_homepage_window(self):
        self.main_greeting = CTk.CTkLabel(root, text="Welcome!", font=("Arial", 20, "bold")).grid(row=0, column=0, padx=20, pady=20)
        self.subheader = CTk.CTkLabel(root, text="Please select an option below to continue.", font=("Arial", 20)).grid(row=1, column=0, padx=20, pady=20)


        self.button1 = CTk.CTkButton(root, text="Inventory Management", command=self.create_inventory_management_window).grid(row=2, column=0, padx=20, pady=20)
        self.button2 = CTk.CTkButton(root, text="Sales Tracking", command=self.create_sales_tracking_window).grid(row=3, column=0, padx=20, pady=20)


    def create_inventory_management_window(self):
        self.root.withdraw()
        self.inventory_management_window = CTk.CTkToplevel(self.root)
        self.inventory_management_window.title("Inventory Management System")


        self.header = CTk.CTkLabel(self.inventory_management_window, text="Inventory Management", font=("Arial", 20, "bold")).grid(row=0, column=0, padx=20, pady=20)
        self.subheader = CTk.CTkLabel(self.inventory_management_window, text="Would you like to add a new item or\n\nupdate / remove an existing one?", font=("Arial", 20)).grid(row=1, column=0, padx=20, pady=20)


        self.button1 = CTk.CTkButton(self.inventory_management_window, text="Add Item", command=self.create_add_item_window).grid(row=2, column=0, padx=20, pady=20)
        self.button2 = CTk.CTkButton(self.inventory_management_window, text="Update / Remove Item", command=self.create_u_r_item_window).grid(row=3, column=0, padx=20, pady=20)


        inventory_value = self.Inventory_Database_Management.get_total_inventory_value()
        self.inventory_value_output = CTk.CTkLabel(self.inventory_management_window, text=f"Total Inventory Value: ${inventory_value:.2f}", font=("Arial", 15))
        self.inventory_value_output.grid(row=4, column=0, padx=20, pady=20)


        self.back_button = CTk.CTkButton(self.inventory_management_window, text="Back", command=lambda: [self.inventory_management_window.destroy(), self.root.deiconify()]).grid(row=5, column=0, padx=20, pady=20)


    def create_add_item_window(self):
        self.inventory_management_window.destroy()
        self.add_item_window = CTk.CTkToplevel(self.root)
        self.add_item_window.title("Inventory Management System")


        self.header = CTk.CTkLabel(self.add_item_window, text="Item Addition", font=("Arial", 20, "bold")).grid(columnspan=2, padx=20, pady=20)


        self.item_name_label = CTk.CTkLabel(self.add_item_window, text="Item Name:")
        self.item_name_label.grid(row=1, column=0, padx=20, pady=20)
        self.quantity_label = CTk.CTkLabel(self.add_item_window, text="Quantity:")
        self.quantity_label.grid(row=2, column=0, padx=20, pady=20)
        self.cost_price_label = CTk.CTkLabel(self.add_item_window, text="Cost Price:")
        self.cost_price_label.grid(row=3, column=0, padx=20, pady=20)
        self.sale_price_label = CTk.CTkLabel(self.add_item_window, text="Sale Price")
        self.sale_price_label.grid(row=4, column=0, padx=20, pady=20)


        # Separate widget creation from .grid() call
        self.item_name_entry = CTk.CTkEntry(self.add_item_window)
        self.item_name_entry.grid(row=1, column=1, padx=20, pady=20)
        self.quantity_box = CTk.CTkEntry(self.add_item_window)
        self.quantity_box.grid(row=2, column=1, padx=20, pady=20)
        self.cost_price_entry = CTk.CTkEntry(self.add_item_window)
        self.cost_price_entry.grid(row=3, column=1, padx=20, pady=20)
        self.sale_price_entry = CTk.CTkEntry(self.add_item_window)
        self.sale_price_entry.grid(row=4, column=1, padx=20, pady=20)


        self.add_item_button = CTk.CTkButton(self.add_item_window, text="Add Item", command=self.add_item_to_inventory)
        self.add_item_button.grid(columnspan=2, padx=20, pady=20)


        self.back_button = CTk.CTkButton(self.add_item_window, text="Back", command=lambda: [self.add_item_window.destroy(), self.create_inventory_management_window()])
        self.back_button.grid(row=6, columnspan=2, padx=20, pady=20)


    # Create the update / remove item window
    def create_u_r_item_window(self):
        self.inventory_management_window.destroy()
        self.u_r_item_window = CTk.CTkToplevel(self.root)
        self.u_r_item_window.title("Inventory Management System")


        self.header = CTk.CTkLabel(self.u_r_item_window, text="Item Updater / Remover", font=("Arial", 20, "bold")).grid(row=0, columnspan=5, padx=20, pady=20)


        self.dropdown_menu = CTk.CTkComboBox(self.u_r_item_window, values=list(self.Inventory_Database_Management.df["Name"]), command=self.populate_fields, variable="")
        self.dropdown_menu.grid(row=1, column=0, padx=20, pady=20)


        self.quantity_label = CTk.CTkLabel(self.u_r_item_window, text="Quantity:").grid(row=1, column=1, padx=20, pady=20)
        self.cost_price_label = CTk.CTkLabel(self.u_r_item_window, text="Cost Price:").grid(row=2, column=1, padx=20, pady=20)
        self.sale_price_label = CTk.CTkLabel(self.u_r_item_window, text="Sale Price").grid(row=3, column=1, padx=20, pady=20)
        

        self.cost_price_entry = CTk.CTkEntry(self.u_r_item_window)
        self.cost_price_entry.grid(row=2, column=2, columnspan=1, padx=20, pady=20)
        self.sale_price_entry = CTk.CTkEntry(self.u_r_item_window)
        self.sale_price_entry.grid(row=3, column=2, padx=20, pady=20)


        self.quantity_box = CTk.CTkEntry(self.u_r_item_window)
        self.quantity_box.grid(row=1, column=2, pady=20)


        self.plus_sign_button = CTk.CTkButton(self.u_r_item_window, text="+", command=self.increment_quantity, font=("Arial", 20), height=25, width=25).grid(row=1, column=3, pady=20)
        self.minus_sign_button = CTk.CTkButton(self.u_r_item_window, text="-", command=self.decrement_quantity, font=("Arial", 20), height=25, width=30).grid(row=1, column=4, padx=20, pady=20)


        self.update_item_button = CTk.CTkButton(self.u_r_item_window, text="Update Item", command=self.update_item_in_inventory, width=20).grid(row=4, column=1, padx=20, pady=20)
        self.remove_item_button = CTk.CTkButton(self.u_r_item_window, text="Remove Item", command=self.remove_item_from_inventory, width=20).grid(row=4, column=1, columnspan=3, padx=20, pady=20)


        self.back_button = CTk.CTkButton(self.u_r_item_window, text="Back", command=lambda: [self.u_r_item_window.destroy(), self.create_inventory_management_window()]).grid(row=6, columnspan=5, padx=20, pady=20)


    # Create the sales tracking window
    def create_sales_tracking_window(self):
        self.root.withdraw()
        self.sales_tracking_window = CTk.CTkToplevel(self.root)
        self.sales_tracking_window.title("Sales Tracking")


        CTk.CTkLabel(self.sales_tracking_window, text="Sales Tracking", font=("Arial", 20, "bold")).grid(row=0, columnspan=2, padx=20, pady=20)


        self.sales_dropdown = CTk.CTkComboBox(self.sales_tracking_window, values=list(self.Inventory_Database_Management.df["Name"]), command=self.load_sales_data, variable="")
        self.sales_dropdown.grid(row=1, column=0, padx=20, pady=20)


        self.date_picker = DateEntry(self.sales_tracking_window, date_pattern="mm-dd-y")
        self.date_picker.grid(row=1, column=1, padx=20, pady=20)


        self.quantity_sold_label = CTk.CTkLabel(self.sales_tracking_window, text="Quantity Sold:").grid(row=2, column=0, padx=20, pady=20)
        self.quantity_sold_entry = CTk.CTkEntry(self.sales_tracking_window)
        self.quantity_sold_entry.grid(row=2, column=1, padx=20, pady=20)


        self.add_update_button = CTk.CTkButton(self.sales_tracking_window, text="Add/Update Sale", command=self.add_update_sales)
        self.add_update_button.grid(row=3, columnspan=2, padx=20, pady=20)


        self.show_sales_graph_button = CTk.CTkButton(self.sales_tracking_window, text="Show Sales Trend", command=self.display_sales_trend_graph)
        self.show_sales_graph_button.grid(row=4, column=0, columnspan=2, padx=20, pady=20)


        self.restock_prediction_label = CTk.CTkLabel(self.sales_tracking_window, text="", font=("Arial", 15))
        self.restock_prediction_label.grid(row=5, columnspan=2, padx=20, pady=20)


        CTk.CTkButton(self.sales_tracking_window, text="Back", command=lambda: [self.sales_tracking_window.destroy(), self.root.deiconify()]).grid(row=6, columnspan=2, padx=20, pady=20)

    
    # Add a new item to the inventory
    def add_item_to_inventory(self):
        try:
            # Retrieve item details from user input fields
            name = self.item_name_entry.get()
            quantity = int(self.quantity_box.get())
            cost_price = float(self.cost_price_entry.get())
            sale_price = float(self.sale_price_entry.get())
            

            # Attempts to add item by calling the add_item_to_inventory method of the Inventory_Database_Management class
            if self.Inventory_Database_Management.add_item(name, quantity, cost_price, sale_price):
                messagebox.showinfo("Success", f"{name} added to inventory!")
            else:
                messagebox.showerror("Error", f"{name} already exists in inventory.")


        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid values.")

    
    # Populate fields with the current values of the selected item
    def populate_fields(self, selected_item):
        item_data = self.Inventory_Database_Management.df[self.Inventory_Database_Management.df["Name"] == selected_item].iloc[0]
        self.quantity_box.delete(0, CTk.END)
        self.quantity_box.insert(0, str(item_data["Quantity"]))
        self.cost_price_entry.delete(0, CTk.END)
        self.cost_price_entry.insert(0, str(item_data["Cost Price"]))
        self.sale_price_entry.delete(0, CTk.END)
        self.sale_price_entry.insert(0, str(item_data["Sale Price"]))

    
    # Increment the quantity in the entry field, saves it in real time
    def increment_quantity(self):
        name = self.dropdown_menu.get()
        quantity = int(self.quantity_box.get())
        cost_price = float(self.cost_price_entry.get())
        sale_price = float(self.sale_price_entry.get())
        self.quantity_box.delete(0, CTk.END)
        self.quantity_box.insert(0, str(quantity + 1))
        self.Inventory_Database_Management.update_item(name, quantity + 1, cost_price, sale_price)

        
    # Decrement the quantity in the entry field, saves it in real time
    def decrement_quantity(self):
        name = self.dropdown_menu.get()
        quantity = int(self.quantity_box.get())
        cost_price = float(self.cost_price_entry.get())
        sale_price = float(self.sale_price_entry.get())
        if quantity > 0:
            self.quantity_box.delete(0, CTk.END)
            self.quantity_box.insert(0, str(quantity - 1))
            self.Inventory_Database_Management.update_item(name, quantity - 1, cost_price, sale_price)


    # Update item details in database
    def update_item_in_inventory(self):
        try:
            # Retrieve item details from user input fields
            name = self.dropdown_menu.get()
            quantity = int(self.quantity_box.get())
            cost_price = float(self.cost_price_entry.get())
            sale_price = float(self.sale_price_entry.get())
    

            # Attempts to update item by calling the update_item_in_inventory method of the Inventory_Database_Management class
            if self.Inventory_Database_Management.update_item(name, quantity, cost_price, sale_price):
                messagebox.showinfo("Success", f"{name} updated in inventory!")
            else:
                messagebox.showerror("Error", f"{name} not found in inventory.")
        
        
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid values.")


    # Remove the selected item from inventory
    def remove_item_from_inventory(self):
        name = self.dropdown_menu.get()

        
        # Attempts to remove item by calling the remove_item_from_inventory method of the Inventory_Database_Management class
        if self.Inventory_Database_Management.remove_item(name):
            messagebox.showinfo("Success", f"{name} removed from inventory.")
            # Clears input fields and refreshes the dropdown menu with the remaining items
            self.dropdown_menu.set("")  # Reset dropdown
            self.quantity_box.delete(0, CTk.END)
            self.cost_price_entry.delete(0, CTk.END)
            self.sale_price_entry.delete(0, CTk.END)
            self.dropdown_menu.configure(values=list(self.Inventory_Database_Management.df["Name"]))
        else:
            messagebox.showerror("Error", f"{name} not found in inventory.")

    # Display restock prediction
    def load_sales_data(self, item_name):
        restock_date = self.Sales_Tracking.get_restock_prediction(item_name)
        self.restock_prediction_label.configure(text=f"Next Expected Restock Date: {restock_date}")


    # Add or update sales data
    def add_update_sales(self):
        item_name = self.sales_dropdown.get()
        date = self.date_picker.get()


        try:
            # Retrieve sales data from user input fields and saves to database
            quantity_sold = int(self.quantity_sold_entry.get())
            self.Sales_Tracking.add_sales_data(item_name, date, quantity_sold)
            self.load_sales_data(item_name)
            messagebox.showinfo("Success", f"Sales data for {item_name} on {date} updated!")
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid number for quantity sold.")
            return
            

    # Show sales trend graph using matplotlib
    def display_sales_trend_graph(self):


        # Filter the data for the selected item
        item_name = self.sales_dropdown.get()
        sales_data = self.Sales_Tracking.get_sales_data(item_name)

        
        if sales_data.empty:
            messagebox.showwarning("Warning", f"No sales data available for {item_name}.")
            return

        
        # Sort data by date for proper plotting
        sales_data = sales_data.sort_values("Date")

        
        # Plot sales trend
        plt.figure(figsize=(10, 6))
        plt.plot(sales_data["Date"], sales_data["Quantity Sold"], marker='o', linestyle='-', color='b', label="Quantity Sold")

        
        # Adding labels and title
        plt.xlabel("Date")
        plt.ylabel("Quantity Sold")
        plt.title(f"Sales Trend for {item_name}")
        plt.legend()

        
        # Display the plot
        plt.show()




# Calls main function to run the application
root = CTk.CTk()
main_window = Main_App_GUI(root)
root.mainloop()