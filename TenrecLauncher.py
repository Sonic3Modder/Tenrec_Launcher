import customtkinter
from tkinter import *
from CTkMenuBar import CTkMenuBar, CTkTitleMenu, CustomDropdownMenu
from PIL import *
from pathlib import Path

GameSetPath = "Tenrec_Launcher/Game"
GamePath = Path(GameSetPath)

root = customtkinter.CTk()
root.geometry("500x500")
root.title("Tenrec Launcher")
root.resizable(True, True)
customtkinter.set_default_color_theme("themes/lavender.json")
customtkinter.set_appearance_mode("system")

menu = CTkTitleMenu(master=root)
button = menu.add_cascade("Menu") # this will be the button
tabview = customtkinter.CTkTabview(master=root)
tabview.pack(padx=10, pady=10)
tabview.pack(fill="both", expand=True)
tabview.add("Game")
tabview.add("Settings")
tabview.add("About")
LabelGame = customtkinter.CTkLabel(master=tabview.tab("Game"), text="Game")
LabelGame.pack(padx=10, pady=0, fill="both", expand=True)

LabelSettings = customtkinter.CTkLabel(master=tabview.tab("Settings"), text="Settings Configuration")
LabelSettings.pack(padx=10, pady=150, fill="both", expand=True)
LabelGamePathSettings = customtkinter.CTkLabel(master=tabview.tab("Settings"), text=f"Game path is {GamePath}")
LabelGamePathSettings.pack(padx=10, pady=100, fill="both", expand=True)

LabelAbout = customtkinter.CTkLabel(master=tabview.tab("About"), text="About Tenrec Launcher")
LabelAbout.pack(padx=10, pady=150, fill="both", expand=True)

dropdown = CustomDropdownMenu(widget=button) # attach that button
dropdown.add_option(option="Quit", command=root.quit) 
dropdown.add_separator() 

root.mainloop()
