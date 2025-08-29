import tkinter as tk
from time import strftime
from weather_api_key import get_weather


# Window setup
root = tk.Tk()
root.title("Genius Smart Mirror")
root.geometry("400x200")  # Window size (optional)
root.configure(background='black')  # Background color

# Time function
def show_time():
    time_string = strftime('%H:%M:%S %p')  # 24-hour format
    time_label.config(text=time_string)
    time_label.after(1000, show_time)  # update every 1 second

# Time label
time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
time_label.pack(anchor='center')
weather_info = get_weather()  # yeh API se data lega
weather_label = tk.Label(root, text=weather_info, font=('Helvetica', 18), fg='white', bg='black')
weather_label.pack(pady=10)


# Call function to start clock
show_time()

# Start the GUI loop
root.mainloop()
import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%I:%M:%S %p')
    current_date = time.strftime('%A, %d %B %Y')
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Genius Smart Mirror")
root.configure(background='black')
root.geometry("800x480")

time_label = tk.Label(root, font=('Helvetica', 40), fg='white', bg='black')
time_label.pack(pady=10)

date_label = tk.Label(root, font=('Helvetica', 20), fg='white', bg='black')
date_label.pack(pady=5)

update_time()
root.mainloop()
import threading
from voice_assistant import listen_and_execute  # Make sure this function exists

# Run voice assistant in background thread
def run_voice_assistant():
    listen_and_execute()

# Start the voice assistant in a separate thread so GUI doesn’t freeze
assistant_thread = threading.Thread(target=run_voice_assistant)
assistant_thread.daemon = True
assistant_thread.start()

root.mainloop()


