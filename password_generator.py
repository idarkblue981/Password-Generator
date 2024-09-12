import tkinter as tk
from tkinter import ttk
from random import choice
from string import digits, ascii_uppercase, ascii_lowercase
from tkinter.messagebox import showwarning, showinfo


# Function to generate a password
def generate_password():
    length = int(length_scale.get())
    include_numbers = numbers_var.get()
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()

    character_pool = ""
    if include_numbers:
        character_pool += digits
    if include_uppercase:
        character_pool += ascii_uppercase
    if include_lowercase:
        character_pool += ascii_lowercase

    if not character_pool:
        showwarning("Selection Error", "Please select at least one option.")
        return

    password = ''.join(choice(character_pool) for _ in range(length))
    output_field.config(text = password)

# Function to copy the password to clipboard
def copy_to_clipboard():
    password = output_field.cget("text")
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        showinfo("Success", "Password copied to clipboard!")
    else:
        showwarning("Copy Error", "No password to copy!")

# Function to close the app
def close_app():
    window.destroy()

# Function to update the scale value display
def update_length_display(event = None):
    length_display.config(text = f"Password Length: {int(length_scale.get())}")

# Window Setup
window = tk.Tk()
window.title("Password Generator")
window.geometry("600x400")
window.resizable(False, False)

# Frames
output_frame = ttk.Frame(window)
input_frame = ttk.Frame(window)
bottom_frame = ttk.Frame(window)

output_frame.place(x = 0, y = 0, relwidth = 1, relheight = 0.25)
input_frame.place(x = 0, rely = 0.25, relwidth = 1, relheight = 0.5)
bottom_frame.place(x = 0, rely = 0.75, relwidth = 1, relheight = 0.25)

# Output Field
output_field = ttk.Label(output_frame, text="Your password will appear here", background="lightgray", anchor="center", font=("Helvetica", 16))
output_field.pack(expand = True, fill = "both", padx = 50, pady = 25)

# Variables for Checkbuttons
numbers_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()

# Label to show the selected length
length_display = ttk.Label(input_frame, text = "12")    # Initial default text
length_display.pack()

# Scale to select length
length_scale = ttk.Scale(input_frame, from_ = 6, to = 32, orient = 'horizontal', command = update_length_display)
length_scale.set(12)    # Default length
length_scale.pack(expand = True, fill = "both", padx = 100, pady = 1)

# Buttons
numbers = ttk.Checkbutton(input_frame, text = "Include Numbers", variable = numbers_var)
numbers.pack(expand = True, fill = "both", padx = 100, pady = 1)

uppercase = ttk.Checkbutton(input_frame, text = "Include Uppercase Letters", variable = uppercase_var)
uppercase.pack(expand = True, fill = "both", padx = 100, pady = 1)

lowercase = ttk.Checkbutton(input_frame, text = "Include Lowercase Letters", variable = lowercase_var)
lowercase.pack(expand = True, fill = "both", padx = 100, pady = 1)

generate_button = ttk.Button(input_frame, text = "Generate Password", command = generate_password)
generate_button.pack(expand = True, fill = "both", padx = 150, pady = 1)

# Bottom Frame Widgets
copy_button = ttk.Button(bottom_frame, text = "Copy", command = copy_to_clipboard)
copy_button.place(relx = 0.05, rely = 0.1, relwidth = 0.4, relheight = 0.4)

exit_button = ttk.Button(bottom_frame, text = "Exit", command = close_app)
exit_button.place(relx = 0.55, rely = 0.1, relwidth = 0.4, relheight = 0.4)

credits_label = ttk.Label(bottom_frame, text = "A Paul Jimon Production\nArad, Romania\n2024", anchor = "center", justify = "center", font = ("Helvetica", 8))
credits_label.place(x = 0, rely = 0.5, relwidth = 1, relheight = 0.5)


# Run
if __name__ == "__main__":
    window.mainloop()