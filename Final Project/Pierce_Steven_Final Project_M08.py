import tkinter as tk
import pygame
from PIL import Image, ImageTk

# Global variables for widgets
entry = output_text = name_label = name_entry = class_label = class_dropdown = submit_button = continue_button = character_window = None

# Music variable
music_playing = True
previous_volume = 0.35

# Define functions
def submit_command(event=None):  
    global music_playing, previous_volume, entry
    command = entry.get().lower()
    if command == "start":
        character_creation()
    elif command == "help":
        display_help()
    elif command == "exit":
        root.destroy()
    elif command == "character":
        if character_window is None or not character_window.winfo_exists():
            create_character_window()
    elif command == "reset":
        start_game()
    elif command == "mute":
        if music_playing:
            previous_volume = pygame.mixer.music.get_volume()  # Stores the current volume before muting
            pygame.mixer.music.pause()  # Pause the music
            display_text("Music muted.")
            music_playing = False
        else:
            pygame.mixer.music.unpause()  # Unpause the music
            display_text("Music unmuted.")
            music_playing = True
    elif command == "unmute":
        if not music_playing:
            pygame.mixer.music.set_volume(previous_volume)  # Set the volume back to the previous level
            pygame.mixer.music.unpause()  # Unpause the music
            display_text("Music volume restored.")
            music_playing = True
    
    entry.delete(0, tk.END)  # Clear the entry field after processing the command

def exit_application():
    root.destroy()  # Close the application

def reset_application():
    global name_label, name_entry, class_label, class_dropdown, submit_button
    global music_playing, previous_volume
    
    # Stop the music
    pygame.mixer.music.stop()
    
    # Clear the entry field
    entry.delete(0, tk.END)
    
    # Clear previous text
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)
    
    # Remove character creation widgets if any
    if name_label and name_entry and class_label and class_dropdown and submit_button:
        name_label.destroy()
        name_entry.destroy()
        class_label.destroy()
        class_dropdown.destroy()
        submit_button.destroy()

    # Reset music variables
    music_path = r"C:\Users\jetla\Documents\ivy tech\Intro. Software Dev\Final Project\art\music\main menu\cottagecore-17463.mp3"
    play_music(music_path, volume=0.35)

    # Start the game
    start_game()

def on_entry_click(event):
    if entry.get() == "Insert text":
        entry.delete(0, tk.END)
        entry.config(fg='black', font=('Arial', 10, 'normal'))  

def display_text(text):
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, text + '\n\n')  # Add two line breaks after each text
    output_text.config(state=tk.DISABLED)

def start_game():
    global submit_button  # Define submit_button as global
    display_text("Welcome to the world of Ilum...\n\nA land shrouded in perpetual mist, where Mothborne wanderers and Umbral Whisperers navigate the darkness.\n\nLumina's Refuge offers safety amidst the treacherous landscape, while creatures lurk beyond the illuminated paths.\n\nType 'start' to begin your adventure. Click on the lantern in the bottom right corner for help.")
    entry.bind("<Return>", submit_command)
    entry.delete(0, tk.END)
    entry.config(state=tk.NORMAL)
    entry.focus_set()

def character_creation():
    global name_label, name_entry, class_label, class_dropdown, submit_button

    # Clear previous text and widgets
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)

    display_text("Welcome to character creation!\n\nChoose your character's name and class.")

    # Create Entry and OptionMenu widgets for character creation
    name_label = tk.Label(root, text="Name:", bg='black', fg='white')
    name_label.pack()
    
    name_entry = tk.Entry(root, bg='black', fg='white')
    name_entry.pack()
    
    class_label = tk.Label(root, text="Class:", bg='black', fg='white')
    class_label.pack()

    class_var = tk.StringVar(root)
    class_var.set("Select Class")
    class_options = ["Mothborne", "Lantern Sentinel", "Umbral Whisperer", "Mothweaver"]
    
    class_dropdown = tk.OptionMenu(root, class_var, *class_options, command=display_class_description)
    class_dropdown.config(bg='black', fg='white', activebackground='black', activeforeground='white', relief='flat')
    class_dropdown['menu'].config(bg='black', fg='white', activebackground='black', activeforeground='white')
    class_dropdown.pack()

    submit_button = tk.Button(root, text="Create Character", command=create_character, bg='black', fg='white')
    submit_button.pack()

def display_class_description(selected_class):
    descriptions = {
        "Mothborne": "Mothborne are enigmatic wanderers deeply connected to the ethereal world. They harness the mysterious power of moths, using their delicate yet potent abilities to manipulate shadows and light.\n\nStarting Attributes:\nStrength: 3\nDefense: 3\nDexterity: 3\nWisdom: 3\nHit Points: 9",
        "Lantern Sentinel": "Lantern Sentinels are guardians who wield lanterns as both tools of illumination and instruments of protection. They are sworn to safeguard sacred places and possess powers imbued by ancient, radiant energies.\n\nStarting Attributes:\nStrength: 4\nDefense: 6\nDexterity: 2\nWisdom: 2\nHit Points: 12",
        "Umbral Whisperer": "Umbral Whisperers are solitary figures shrouded in mystery, harnessing the enigmatic powers of the night. They have an innate connection to moths, utilizing their silent and elusive nature to weave spells of illusion and stealth.\n\nStarting Attributes:\nStrength: 2\nDefense: 3\nDexterity: 6\nWisdom: 2\nHit Points: 7",
        "Mothweaver": "The Mothweaver is a practitioner of ancient mystical arts, entwined with the ethereal realm of moths. They commune with these enigmatic creatures, drawing upon their otherworldly essence to shape spells and manipulate reality.\n\nStarting Attributes:\nStrength: 2\nDefense: 2\nDexterity: 2\nWisdom: 6\nHit Points: 6"
    }
    display_text(descriptions[selected_class])

def create_character():
    name = name_entry.get()
    character_class = class_dropdown.cget("text")
    if name.strip() == "" or character_class == "Select Class":
        display_text("Please enter a name and select a class.")
    else:
        display_text(f"Character Created!\n\nName: {name}\nClass: {character_class}\nLevel: 1\nDarkness consumes you for now.")
        name_label.pack_forget()
        name_entry.pack_forget()
        class_label.pack_forget()
        class_dropdown.pack_forget()
        submit_button.pack_forget()

        # Create a new window to display character information
        character_window = tk.Toplevel(root)
        character_window.title("Character Information")
        character_window.geometry("300x200")

        # Create a list-style display for character information
        character_info = tk.Text(character_window, bg='black', fg='white')
        character_info.pack(fill=tk.BOTH, expand=True)
        character_info.insert(tk.END, f"Name: {name}\n")
        character_info.insert(tk.END, f"Class: {character_class}\n")

        # Retrieve class attributes and display in the window
        class_attributes = get_class_attributes(character_class)
        character_info.insert(tk.END, class_attributes)

        # Set the window to focus on character information
        character_window.focus_set()

def create_character_window():
    global character_window
    
    if character_window is None or not character_window.winfo_exists():
        character_window = tk.Toplevel(root)
        character_window.title("Character Information")
        
        # Retrieve character information
        name = name_entry.get()
        character_class = class_dropdown.cget("text")
        
        # Get class attributes
        class_attributes = get_class_attributes(character_class)
        
        # Create a Text widget to display character information
        character_info = tk.Text(character_window, bg='black', fg='white')
        character_info.pack(fill=tk.BOTH, expand=True)
        character_info.insert(tk.END, f"Name: {name}\nClass: {character_class}\n{class_attributes}")
        
        # Set the window to focus on character information
        character_window.focus_set()

def get_class_attributes(character_class):
    class_attributes = {
        "Mothborne": {
            "Strength": 3,
            "Defense": 3,
            "Dexterity": 3,
            "Wisdom": 3,
            "Hit Points": 9
        },
        "Lantern Sentinel": {
            "Strength": 4,
            "Defense": 6,
            "Dexterity": 2,
            "Wisdom": 2,
            "Hit Points": 12
        },
        "Umbral Whisperer": {
            "Strength": 2,
            "Defense": 3,
            "Dexterity": 6,
            "Wisdom": 2,
            "Hit Points": 7
        },
        "Mothweaver": {
            "Strength": 2,
            "Defense": 2,
            "Dexterity": 2,
            "Wisdom": 6,
            "Hit Points": 6
        }
    }
    
    attributes = class_attributes.get(character_class)
    if attributes:
        attribute_string = f"Class: {character_class}\n"
        for attr, value in attributes.items():
            attribute_string += f"{attr}: {value}\n"
        return attribute_string
    else:
        return "Class attributes not found."


        # Create a new window to display character information
        character_window = tk.Toplevel(root)
        character_window.title("Character Information")
        character_window.geometry("300x200")

        # Create a list-style display for character information
        character_info = tk.Listbox(character_window, bg='black', fg='white')
        character_info.pack(fill=tk.BOTH, expand=True)
        character_info.insert(tk.END, f"Name: {name}")
        character_info.insert(tk.END, f"Class: {character_class}")

        # Display attributes based on the chosen class
        if character_class in class_attributes:
            attributes = class_attributes[character_class]
            for attr, value in attributes.items():
                character_info.insert(tk.END, f"{attr}: {value}")
        else:
            character_info.insert(tk.END, "Class attributes not found.")

        # Set the window to focus on character information
        character_window.focus_set()

def create_canvas():
    global global_image
    
    canvas = tk.Canvas(root, width=80, height=76, bg='black', highlightthickness=0)
    canvas.place(x=525, y=522)
    canvas.bind("<Button-1>", on_canvas_click)  # Bind the canvas to a click event
    
    try:
        canvas_image_path = r"C:\Users\jetla\Documents\ivy tech\Intro. Software Dev\Final Project\art\glows.png"
        print("Image path:", canvas_image_path)  # Check that image path is correct
        guide_image = Image.open(canvas_image_path)
        guide_image = guide_image.resize((80, 80), Image.LANCZOS)
        global_image = ImageTk.PhotoImage(guide_image)  # Store image globally
        
        # Imate alternative text
        canvas.create_image(0, 0, anchor=tk.NW, image=global_image, tags="canvas_image")
        canvas.itemconfig("canvas_image", tags=("canvas_image", "lantern_help_guide"))
        
        return canvas
    
    except FileNotFoundError:
        print("Image not found.")
    except Exception as e:
        print(f"Error: {e}")

    return canvas

def on_canvas_click(event):
    def help_window():
        # Create a new window for displaying help commands
        help_win = tk.Toplevel(root)
        help_win.title("Help Commands")
        help_text = tk.Text(help_win, bg='black', fg='white', wrap=tk.WORD)
        help_text.pack(fill=tk.BOTH, expand=True)
        
        # Add your help commands here
        help_commands = (
            "Available commands:",
            "\nstart - Start the game",
            "help - Display available commands",
            "exit - Close the application",
            "mute - Mute the background music",
            "unmute - Unmute the background music",
            "character - Display character stats in a seperate window"
        )
        # Insert help commands into the new window
        for command in help_commands:
            help_text.insert(tk.END, command + '\n')
        help_text.config(state=tk.DISABLED)

    help_window()

def display_help():
    help_text = (
        "Available commands:\n"
        "\nstart - Start the game\n"
        "help - Display available commands\n"
        "exit - Close the application\n"
        "mute - Mute the background music\n"
        "unmute - Unmute the background music\n"
        "character - Display character stats in a separate window"
    )
    display_text(help_text)

# Create root window
root = tk.Tk()
root.title("ilum")

window_width = 600
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg='black')

# Create Text widget
output_text = tk.Text(root, bg='black', fg='white', wrap=tk.WORD)
output_text.pack(fill=tk.BOTH, expand=True)

# Create Entry widget
entry = tk.Entry(root, bg='black', fg='gray', font=('Arial', 10, 'italic'))
entry.bind("<FocusIn>", on_entry_click)  
entry.bind("<Key>", on_entry_click)  
entry.pack(fill=tk.X, pady=(0, 55), padx=0)


# Create Exit and Reset buttons
exit_button = tk.Button(root, text="Exit", command=exit_application, bg='black', fg='white')
exit_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(root, text="Reset", command=reset_application, bg='black', fg='white')
reset_button.pack(side=tk.LEFT, padx=5)

# Create the canvas
canvas = create_canvas()

def play_music(file_path, volume=0.35):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)

# Call the function directly with the music path
play_music(r"C:\Users\jetla\Documents\ivy tech\Intro. Software Dev\Final Project\art\music\main menu\cottagecore-17463.mp3")

# Start the game
start_game()

# Run the application
root.mainloop()