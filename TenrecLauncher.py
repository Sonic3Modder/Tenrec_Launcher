import subprocess
import customtkinter
from tkinter import *
from CTkMenuBar import CTkTitleMenu, CustomDropdownMenu
from PIL import Image
from pathlib import Path
import tkinter.filedialog as fd
import os

GameSetPath = "Tenrec_Launcher/Game"
GamePath = Path(GameSetPath)
GameFolderIfDir = GamePath / "TenrecGame"

os.makedirs(GamePath, exist_ok=True)
os.makedirs(GameFolderIfDir, exist_ok=True)

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("Tenrec Launcher - Game")
        self.resizable(True, True)

        try:
            TopLevelImage = customtkinter.CTkImage(light_image=Image.open("images/TenrecIconLight.jpg"), 
                                            dark_image=Image.open("images/TenrecIconDark.jpg"), 
                                            size=(100, 100))
            TopLevelImageLabel = customtkinter.CTkLabel(master=self, 
                                                    image=TopLevelImage, 
                                                    text="",
                                                    fg_color=("#E3E3E3", "#2D2D2D"),
                                                    corner_radius=10)
            TopLevelImageLabel.pack(padx=20, pady=20)
        except Exception as e:
            print(f"Error loading images: {e}")
            TopLevelImageLabel = customtkinter.CTkLabel(master=self, 
                                                    text="",
                                                    fg_color=("#E3E3E3", "#2D2D2D"),
                                                    corner_radius=10)
            TopLevelImageLabel.pack(padx=20, pady=20)
            
            current_dir = os.path.dirname(__file__)
            HogGamePath = os.path.join(current_dir, "HogGame.exe")


        if GameFolderIfDir.exists():
            print(f"Game directory found at: {GameFolderIfDir}")
            try:
                GameOpen = subprocess.Popen([HogGamePath], cwd=GameFolderIfDir, shell=True)
                if GameOpen.returncode == 0:
                    self.quit()
            except FileNotFoundError:
                print("HogGame.exe not found in the game directory.")
                self.quit()
            GameProgress = customtkinter.CTkProgressBar(self, orientation="horizontal", corner_radius=10)
            GameProgress.pack(padx=20, pady=20)
            GameProgress.configure(mode="indeterminate")
            GameProgress.start()
            
        else:
            print(f"Path issue - Created directory at: {GameFolderIfDir}")
            errorLabel = customtkinter.CTkLabel(master=self, 
                                              text=f"Game directory was created at:\n{GameFolderIfDir}\n\nPlease place game files there.",
                                              fg_color=("#FFE0E0", "#502020"),
                                              corner_radius=10)
            errorLabel.pack(padx=20, pady=20)


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("850x500")
        self.title("Tenrec Launcher")
        self.resizable(True, True)
        
        try:
            customtkinter.set_default_color_theme("themes/lavender.json")
        except Exception as e:
            print(f"Error loading theme: {e}")
            
        customtkinter.set_appearance_mode("system")

        menu = CTkTitleMenu(master=self)
        button = menu.add_cascade("Menu") 

        main_container = customtkinter.CTkFrame(master=self, fg_color="transparent")
        main_container.pack(fill="both", expand=True)

        image_frame = customtkinter.CTkFrame(master=main_container, fg_color="transparent")
        image_frame.pack(padx=10, pady=10, side="left", fill="y")

        tab_frame = customtkinter.CTkFrame(master=main_container, fg_color="transparent")
        tab_frame.pack(padx=10, pady=10, side="right", fill="both", expand=True)

        GameTabImage = customtkinter.CTkImage(light_image=Image.open("images/joystick.png"), 
                                            dark_image=Image.open("images/joystick.png"), 
                                            size=(20, 20))
        SettingsTabImage = customtkinter.CTkImage(light_image=Image.open("images/gear.png"), 
                                            dark_image=Image.open("images/gear.png"), 
                                            size=(20, 20))
        AboutTabImage = customtkinter.CTkImage(light_image=Image.open("images/file-earmark-person.png"), 
                                            dark_image=Image.open("images/file-earmark-person.png"), 
                                            size=(20, 20))

        tabview = customtkinter.CTkTabview(master=tab_frame, corner_radius=10)
        tabview.pack(fill="both", expand=True)
        tabview.add("Game")
        tabview.add("Settings")
        tabview.add("About")

        tabview._segmented_button._buttons_dict["Game"].configure(image=GameTabImage, compound="left")
        tabview._segmented_button._buttons_dict["Settings"].configure(image=SettingsTabImage, compound="left")
        tabview._segmented_button._buttons_dict["About"].configure(image=AboutTabImage, compound="left")

        LabelGame = customtkinter.CTkLabel(master=tabview.tab("Game"), text="Game")
        LabelGame.pack(padx=10, pady=0, fill="both", expand=True)

        try:
            PlayButtonImage = customtkinter.CTkImage(light_image=Image.open("images/play-fill.png"), 
                                            dark_image=Image.open("images/play-fill.png"), 
                                            size=(20, 20))
            GameStartButton = customtkinter.CTkButton(master=tabview.tab("Game"), text="Start Game", image=PlayButtonImage, font=("Montserrat", 12), corner_radius=0, command=self.open_toplevel)
        except Exception as e:
            print(f"Error loading button image: {e}")
            GameStartButton = customtkinter.CTkButton(master=tabview.tab("Game"), text="Start Game", font=("Montserrat", 12), corner_radius=0, command=self.open_toplevel)
            
        GameStartButton.pack(padx=10, pady=10)

        try:
            TenrecImage = customtkinter.CTkImage(light_image=Image.open("images/TenrecIconLight.jpg"), 
                                            dark_image=Image.open("images/TenrecIconDark.jpg"), 
                                            size=(100, 100))
            TenrecImageLabel = customtkinter.CTkLabel(master=image_frame, 
                                                    image=TenrecImage, 
                                                    text="",
                                                    fg_color=("#E3E3E3", "#2D2D2D"),
                                                    corner_radius=10)
        except Exception as e:
            print(f"Error loading Tenrec image: {e}")
            TenrecImageLabel = customtkinter.CTkLabel(master=image_frame, 
                                                    text="Tenrec",
                                                    fg_color=("#E3E3E3", "#2D2D2D"),
                                                    corner_radius=10)

        TenrecImageLabel.pack(padx=10, pady=(20, 10))

        TenrecTextLabel = customtkinter.CTkLabel(master=image_frame,
                                            text="Tenrec Launcher",
                                            font=("Arial", 16, "bold"))
        TenrecTextLabel.pack(padx=10, pady=(0, 20))

        CopyrightText = customtkinter.CTkLabel(self, text="Copyright (c) Inpuca12 and Sonic3Modder", font=("Arial", 8, "bold"), text_color="#424242")
        CopyrightText.pack(padx=10, pady=10, anchor="center", side="bottom")

        settings_frame = customtkinter.CTkFrame(master=tabview.tab("Settings"), fg_color="transparent")
        settings_frame.pack(padx=10, pady=10, fill="both", expand=True)

        LabelSettings = customtkinter.CTkLabel(master=settings_frame, text="Settings Configuration")
        LabelSettings.pack(padx=10, pady=(20, 10))

        LabelGamePathSettings = customtkinter.CTkLabel(master=settings_frame, text=f"Game path is {GameFolderIfDir.absolute()}")
        LabelGamePathSettings.pack(padx=10, pady=(10, 20))

        def change_game_path():
            new_path = fd.askdirectory()
            if new_path:
                global GamePath, GameFolderIfDir
                GamePath = Path(new_path)
                GameFolderIfDir = GamePath / "TenrecGame"
                os.makedirs(GameFolderIfDir, exist_ok=True)
                LabelGamePathSettings.configure(text=f"Game path is {GameFolderIfDir.absolute()}")

        ButtonGamePathSettings = customtkinter.CTkButton(master=settings_frame, text="Change Game Path", command=change_game_path)
        ButtonGamePathSettings.pack(padx=10, pady=(10, 20))
        
        version = "1.0.0"
        LabelAbout = customtkinter.CTkLabel(master=tabview.tab("About"), text=f"About Tenrec Launcher, Version is {version}")
        LabelAbout.pack(padx=10, pady=150, fill="both", expand=True)

        dropdown = CustomDropdownMenu(widget=button)
        dropdown.add_option(option="Quit", command=self.quit_app) 
        dropdown.add_separator() 

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self) 
        else:
            self.toplevel_window.focus()
    
    def quit_app(self):
        self.quit()
        self.destroy()

if __name__ == "__main__":
    print(f"Starting Tenrec Launcher")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Game directory path: {GameFolderIfDir.absolute()}")
    print(f"Game directory exists: {GameFolderIfDir.exists()}")
    
    app = App()
    app.mainloop()