import tkinter as tk

# Define the player's inventory as a dictionary
inventory = {}

# Define the buttons outside of the functions
button1 = None
button2 = None
button3 = None
room_image_label = None
inventory_label = None

def update_inventory_label():
    inventory_label.config(text="Inventory: {}".format(inventory))
    
def room1():
    global inventory  # Make sure to use the global inventory variable inside the function
    global button1, button2, button3  # Make sure to use the global button variables inside the function
    print("You are in room 1")
    inventory['key'] = 1  # Add a key to the inventory
    # Change the room options
    button1.config(text="Go to room 2")
    button1.config(command=room2)
    button2.config(text="Inspect room 1")
    button2.config(command=lambda: print("You see a table and a chair."))
    button3.config(text="Go to room 3")
    button3.config(command=room3)
    room_image = tk.PhotoImage(file="./images/room1.png").subsample(12, 12)
    room_image_label.config(image=room_image)
    room_image_label.image = room_image
    update_inventory_label()
    

def room2():
    global inventory  # Make sure to use the global inventory variable inside the function
    global button1, button2, button3  # Make sure to use the global button variables inside the function
    print("You are in room 2")
    if 'key' in inventory:  # Check if the player has the key in their inventory
        print("You unlocked the door!")
        # Change the room options
        button1.config(text="Go to room 1")
        button1.config(command=room1)
        button2.config(text="Inspect room 2")
        button2.config(command=lambda: print("You see a bookshelf and a window."))
        room_image = tk.PhotoImage(file="./images/room2.png").subsample(12, 12)
        room_image_label.config(image=room_image)
        room_image_label.image = room_image
    else:
        print("The door is locked.")
        # Change the room options
        button1.config(text="Go to room 1")
        button1.config(command=room1)
        
def room3():
    global inventory  # Make sure to use the global inventory variable inside the function
    global button1, button2, button3  # Make sure to use the global button variables inside the function
    print("You are in room 3")
    button1.config(text="Go to room 4")
    button1.config(command=room1)
    button2.config(text="Inspect room 3")
    button2.config(command=lambda: print("You see a knife"))
    room_image = tk.PhotoImage(file="./images/room.png").subsample(12, 12)
    room_image_label.config(image=room_image)
    room_image_label.image = room_image
    
def main():
    global button1, button2, button3, room_image_label, inventory_label
    root = tk.Tk()
    root.title("Text Adventure Game")

    # Create a label for the game output
    output_label = tk.Label(root, text="Welcome to the game!")
    output_label.grid(row=0, column=1)

    # Create entry widget for player input
    input_entry = tk.Entry(root)
    input_entry.grid(row=1, column=1)

    # Create buttons for player choices
    button1 = tk.Button(root, text="Go to room 1", command=room1)
    button1.grid(row=4, column=1)
    button2 = tk.Button(root, text="Inspect room", command=lambda: print("You are not in a room yet."))
    button2.grid(row=2, column=1)
    button3 = tk.Button(root, text="Go to room 2", command=room2)
    button3.grid(row=5, column=1)
    button4 = tk.Button(root, text="Pick up", command=lambda: print("There is nothing to pick up yet."))
    button4.grid(row=3, column=1)

    # Create a label for the player's inventory
    inventory_label = tk.Label(root, text="Inventory: {}".format(inventory))
    inventory_label.grid(row=6, column=1)

    # Create a label for the room image
    room_image_label = tk.Label(root)
    room_image_label.grid(row=2, column=0, rowspan=3, sticky="w")

    # Set the initial room image
    room_image = tk.PhotoImage(file="./images/room.png").subsample(12, 12)
    room_image_label.config(image=room_image)
    room_image_label.image = room_image

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
