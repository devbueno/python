import tkinter as tk
from selenium import webdriver

def search():
    query = entry.get()  # Get the search query from the entry field
    # Navigate to the Google search page
    driver.get(f"https://www.google.com/search?q={query}")
    driver.get("https://www.google.com")
def navigate_back():
    driver.back()  # Navigate back to the previous page

def navigate_forward():
    driver.forward()  # Navigate forward to the next page

def switch_to_search_frame():
    # Hide other frames and show the search frame
    search_frame.pack()
    navigation_frame.pack_forget()

def switch_to_navigation_frame():
    # Hide other frames and show the navigation frame
    navigation_frame.pack()
    search_frame.pack_forget()

# Initialize the webdriver instance (driver)
driver = webdriver.Chrome()

# Create the main GUI window
window = tk.Tk()
window.title("Web Navigation")

# Create frames for different sections
search_frame = tk.Frame(window)
navigation_frame = tk.Frame(window)

# Create an entry field for the search query
entry = tk.Entry(search_frame)
entry.pack()

# Create a search button
search_button = tk.Button(search_frame, text="Search", command=search)
search_button.pack()

# Create navigation buttons
back_button = tk.Button(navigation_frame, text="Back", command=navigate_back)
back_button.pack(side=tk.LEFT)
forward_button = tk.Button(navigation_frame, text="Forward", command=navigate_forward)
forward_button.pack(side=tk.LEFT)

# Create buttons to switch between frames
search_button = tk.Button(window, text="Search", command=switch_to_search_frame)
search_button.pack(side=tk.LEFT)
navigation_button = tk.Button(window, text="Navigation", command=switch_to_navigation_frame)
navigation_button.pack(side=tk.LEFT)

# Initially show the search frame
switch_to_search_frame()

# Run the GUI event loop
window.mainloop()

# After the GUI window is closed, quit the webdriver
driver.quit()
