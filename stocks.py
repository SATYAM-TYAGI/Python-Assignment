import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

API_KEY = 'YOUR_API_KEY'
STOCK_SYMBOLS = ['WIPRO.BSE', 'TATAPOWER.BSE'] 
def fetch_stock_price(symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if 'Global Quote' in data:
        return float(data['Global Quote']['05. price'])
    else:
        print(f"Error fetching data for {symbol}: {data}")
        return None

def display_stock_prices():
    prices = []
    for symbol in STOCK_SYMBOLS:
        price = fetch_stock_price(symbol)
        if price:
            prices.append(f"{symbol}: {price} INR")
        else:
            prices.append(f"{symbol}: Data not available")
    price_label.config(text=f"Current Stock Prices:\n{', '.join(prices)}")

root = tk.Tk()
root.title("Stock Price Display")
root.geometry("400x400")


canvas = tk.Canvas(root, width=400, height=400) 
canvas.pack(fill="both", expand=True) 


bg_image = ImageTk.PhotoImage(Image.open("1605294660-0711.png")) 
canvas.create_image(0, 0, image=bg_image, anchor="nw")

 
price_label = tk.Label(root, text="Current Stock Prices: ", font=("Helvetica", 16), bg="skyblue", wraplength=380, justify="left") 
price_window = canvas.create_window(10, 100, anchor="nw", window=price_label) 

fetch_button = tk.Button(root, text="Fetch Stock Prices", command=display_stock_prices, font=("Helvetica", 14), bg="red", fg="white") 
button_window = canvas.create_window(120, 300, anchor="nw", window=fetch_button) 


root.mainloop()