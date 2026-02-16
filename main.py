from ploting import create_plot
import tkinter as tk
from PIL import Image, ImageTk

#Funktion zum anzeigen von des Plots in einem tkinter Label als png
def plot():
    community = comm.get()
    party = part.get()
    if community != "":
        error = create_plot(party, community)

        if error:
            plot_label.config(text="Gemeinde oder Partei falsch!!", fg="red", image="")
            plot_label.image = None
        else:
            image = Image.open("plot.png")
            image = image.resize((700, 500), Image.LANCZOS)
            plot_im = ImageTk.PhotoImage(image)

            plot_label.config(image=plot_im)
            plot_label.image = plot_im

root = tk.Tk()
root.title("Landtagswahlen auswerter")
root.geometry("800x800")
root.config(bg="#1e1e1e")

label1 = tk.Label(text="Geimeinde:",font=("Arial",18), width=15, height=1 )
label1.grid(row=0,column=0, padx=10, pady=20)

comm = tk.Entry(width=40, font=("Arial", 18))
comm.grid(row=0, column=1)

label2 = tk.Label(text="Partei:",font=("Arial",18), width=15, height=1 )
label2.grid(row=1,column=0, padx=10, pady=20)

part = tk.Entry(width=40,font=("Arial", 18))
part.grid(row=1, column=1)

plot_bttn = tk.Button(text="Plot", command=plot, font=("Segoe UI", 12, "bold"),bg="grey", width=50)
plot_bttn.grid(row=2,column=0,columnspan=2)

plot_label = tk.Label(bg="#1e1e1e")
plot_label.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()

