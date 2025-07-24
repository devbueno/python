import tkinter as tk
from selenium import webdriver

def search():
    query = entry.get()  # Get the search query from the entry field
    # Navigate to the Google search page
    driver.get(f"https://www.google.com/search?q={query}")

def navigate_back():
    driver.back()  # Navigate back to the previous page

def navigate_forward():
    driver.forward()  # Navigate forward to the next page

# Initialize the webdriver instance (driver)
driver = webdriver.Chrome()

# Create the GUI window
window = tk.Tk()
window.title("Web Navigation")

# Create an entry field for the search query
entry = tk.Entry(window)
entry.pack()

# Create a search button
search_button = tk.Button(window, text="Search", command=search)
search_button.pack()

# Create navigation buttons
back_button = tk.Button(window, text="Back", command=navigate_back)
back_button.pack(side=tk.LEFT)
forward_button = tk.Button(window, text="Forward", command=navigate_forward)
forward_button.pack(side=tk.LEFT)

# Run the GUI event loop
window.mainloop()

# After the GUI window is closed, quit the webdriver
driver.quit()
