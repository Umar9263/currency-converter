import tkinter as tk

# Conversion rates (as of 2024-04-01)
INR_TO_USD = 0.012
INR_TO_EUR = 0.0112
INR_TO_GBP = 0.009
INR_TO_PKR = 3.330
INR_TO_AED = 0.044
INR_TO_CAD = 0.016
INR_TO_JPY = 1.853

def convert_currency():
    try:
        amount_in_inr = float(inr_entry.get())
        amount_in_usd = amount_in_inr * INR_TO_USD
        amount_in_eur = amount_in_inr * INR_TO_EUR
        amount_in_gbp = amount_in_inr * INR_TO_GBP
        amount_in_pkr = amount_in_inr * INR_TO_PKR
        amount_in_aed = amount_in_inr * INR_TO_AED
        amount_in_cad = amount_in_inr * INR_TO_CAD
        amount_in_jpy = amount_in_inr * INR_TO_JPY

        usd_label.config(text=f"{amount_in_usd:.2f} USD")
        eur_label.config(text=f"{amount_in_eur:.2f} EUR")
        gbp_label.config(text=f"{amount_in_gbp:.2f} GBP")
        pkr_label.config(text=f"{amount_in_pkr:.2f} PKR")
        aed_label.config(text=f"{amount_in_aed:.2f} AED")
        cad_label.config(text=f"{amount_in_cad:.2f} CAD")
        jpy_label.config(text=f"{amount_in_jpy:.2f} JPY")
    except ValueError:
        usd_label.config(text="Invalid Input")
        eur_label.config(text="Invalid Input")
        gbp_label.config(text="Invalid Input")
        pkr_label.config(text="Invalid Input")
        aed_label.config(text="Invalid Input")
        cad_label.config(text="Invalid Input")
        jpy_label.config(text="Invalid Input")

# Create the main application window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x400")
root.resizable(False, False)

# Create the entry field to enter the amount in INR
inr_entry = tk.Entry(root, font=("Arial", 22))
inr_entry.pack(pady=20)

# Create the button to convert the currency
convert_button = tk.Button(root, text="Convert", font=("Arial", 20), command=convert_currency)
convert_button.pack()

# Create the labels to display converted amounts
usd_label = tk.Label(root, text="", font=("Arial", 20))
usd_label.pack()
eur_label = tk.Label(root, text="", font=("Arial", 20))
eur_label.pack()
gbp_label = tk.Label(root, text="", font=("Arial", 20))
gbp_label.pack()
pkr_label = tk.Label(root, text="", font=("Arial", 20))
pkr_label.pack()
aed_label = tk.Label(root, text="", font=("Arial", 20))
aed_label.pack()
cad_label = tk.Label(root, text="", font=("Arial", 20))
cad_label.pack()
jpy_label = tk.Label(root, text="", font=("Arial", 20))
jpy_label.pack()

# Start the application
root.mainloop()
