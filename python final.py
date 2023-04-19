import tkinter as tk
import random
# Define the player's inventory as a dictionary
inventory = {}

# Define the buttons outside of the functions
button1 = None
button2 = None
button3 = None
button4 = None
room_image_label = None
inventory_label = None
health = 100
def update_inventory_label():
    inventory_label.config(text="Inventory: {}".format(inventory))
    
def room1():
    global inventory  # Make sure to use the global inventory variable inside the function
    global button1, button2, button3, button4  # Make sure to use the global button variables inside the function
    print("You are in room 1")
    # Add a key to the inventory
    # Change the room options
    button1.config(text="Go to room 2")
    button1.config(command=room2)
    button2.config(text="Inspect room 1")
    button2.config(command=lambda: print("You see a table and a chair."))
    button3.config(text="Go to room 3")
    button3.config(command=room3)
    def pick_up_key():
         print("You picked up a key")
         inventory.update({"key": 1})
         update_inventory_label()
    button4.config(text="Pick up key", command=pick_up_key)
    room_image = tk.PhotoImage(file="./images/room1.png").subsample(12, 12)
    room_image_label.config(image=room_image)
    room_image_label.image = room_image

    

def room2():
    global inventory  # Make sure to use the global inventory variable inside the function
    global button1, button2, button3, button4  # Make sure to use the global button variables inside the function
    if 'key' in inventory:  # Check if the player has the key in their inventory
        print("You unlocked the door!")
        print("You are in room 2")
        # Change the room options
        button1.config(text="Go to room 1")
        button1.config(command=room1)
        button2.config(text="Inspect room 2")
        button2.config(command=lambda: print("You see a bookshelf and a window."))
        button4.config(state="disabled")
        room_image = tk.PhotoImage(file="./images/room2.png").subsample(12, 12)
        room_image_label.config(image=room_image)
        room_image_label.image = room_image
    else:
        print("The door is locked.")
        
        # Add a key to the inventory
        # Change the room options
        button1.config(text="Go to room 2")
        button1.config(command=room2)
        button2.config(text="Inspect room 1")
        button2.config(command=lambda: print("You see a table and a chair."))
        button3.config(text="Go to room 3")
        button3.config(command=room3)
        def pick_up_key():
             print("You picked up a key")
             inventory.update({"key": 1})
             update_inventory_label()
        button4.config(text="Pick up key", command=pick_up_key)
        room_image = tk.PhotoImage(file="./images/room1.png").subsample(12, 12)
        room_image_label.config(image=room_image)
        room_image_label.image = room_image
        
def room3():
    global inventory  # Make sure to use the global inventory variable inside the function
    global button1, button2, button3, button4  # Make sure to use the global button variables inside the function
    print("You are in room 3")
    button1.config(text="Go to room 4")
    button1.config(command=room4)
    button2.config(text="Inspect room 3")
    button2.config(command=lambda: print("You see a knife"))
    def pick_up_knife():
         print("You picked up a knife")
         inventory.update({"knife": 1})
         update_inventory_label()
    button4.config(state="normal", text="Pick up knife", command=pick_up_knife)
    room_image = tk.PhotoImage(file="./images/room1.png").subsample(12, 12)
    room_image_label.config(image=room_image)
    room_image_label.image = room_image
    
def room4():
    global inventory  # Make sure to use the global inventory variable inside the function
    global button1, button2, button3, button4, health # Make sure to use the global button variables inside the function
    global steve_health
    steve_health = 30
    button1.config(state="disabled", text="Go down the stairs", command=basement)
    button2.config(state="disabled", text="Inspect room", command=lambda: print("You see two doors, and a wall that is sort of cracked"))
    button3.config(state="disabled", text="Go to the left door", command=room6)
    room_image = tk.PhotoImage(file="./images/steve.png").subsample(1, 1)
    room_image_label.config(image=room_image)
    room_image_label.image = room_image
    def minecraft_steve():
        global health
        global steve_health
        global inventory
        if "knife" in inventory:
             if random.random() > 0.25:
                   damage = random.randint(5, 10)
                   print(damage)
                   steve_health -= damage
                   print(steve_health)
                   if steve_health <= 0:
                            steve_health = 0
                   print("You attacked and did {} damage. Steve's health is now {}.".format(damage, steve_health))
                   if steve_health == 0:
                            print("You killed steve and got his pick")
                            button4.config(state="disabled")
                            inventory.update({"pickaxe": 1})
                            update_inventory_label()
                            button1.config(state="normal")
                            button2.config(state="normal")
                            button3.config(state="normal")
                            room_image = tk.PhotoImage(file="./images/steve.png").subsample(1, 1)
                            room_image_label.config(image=room_image)
                            room_image_label.image = room_image
                            input_entry.bind("<Return>", lambda event: enter_secret_room() if input_entry.get() == "pickaxe" else enter_room())
             else:
                    # Take a random amount of health from the player
                    damage = random.randint(10, 30)
                    health -= damage
                    if health <= 0:
                        health = 0
                    print("You were attacked and took {} damage. Your health is now {}.".format(damage, health))
                    if health == 0:
                        print("You died")
                        quit()
        else:
            print("You don't have the knife, so you died.")
            quit()
    button4.config(state="normal", text="Attack", command=minecraft_steve)
def basement():
    print("k")
def room5():
    print("k")
def room6():
    print("k")
def enter_secret_room():
         global button1, button2, button3, button4, room_image_label, inventory_label, health, input_entry, output_label
         inventory.pop("pickaxe")
         print("Your pickaxe broke but you got through the wall")
         update_inventory_label()
         button1.config(text="Go to room 8")
         button1.config(command=room8)
         button2.config(text="Inspect room")
         button2.config(command=lambda: print("You feel a strange power over you, you're in a mystical void"))
         button3.config(text="Go to room 666")
         button3.config(command=room666)
         button4.config(text="Go to room 50", state="normal")
         room_image = tk.PhotoImage(file="./images/rain.png").subsample(3, 3)
         room_image_label.config(image=room_image)
         room_image_label.image = room_image
def room8():
    print("k")
def room666():
    print("You are in what appears to be hell, you hear a voice in the distance")
    button1.config(text="Go to the voices", command=Hell)
    button2.config(text="Enter the room behind you", command=room1)
    button3.config(text="Give up", command=lambda: print("There is no giving up"))
def room50():
    print("k")
def Hell():
    button1.config(state="disabled")
    button2.config(state="disabled")
    button3.config(state="disabled")
    button4.config(state="disabled")
    print("You run into Thanatos (Death) Behind him is some sort of creature in a cage")
    print("Thanatos: You seem strong, if you can defeat this boss you can keep the weapons I give you")
    button1.config(state="normal", text="Agree", command=hellfight)
    button2.config(state="normal", text="Disagree", command=lambda: print("You cannot disagree with death"))
    
def hellfight():
    global button1, button2, button3, button4, room_image_label, inventory_label, health, input_entry, output_label, demon_health
    health = 500
    print("You recieved the strange lava armor and sword")
    inventory.update({"hell sword": 1})
    update_inventory_label()
    deamon_health = 800
    def minecraft_steve():
        global health
        global deamon_health
        global inventory
        if "knife" in inventory:
             if random.random() > 0.5:
                   damage = random.randint(50, 100)
                   print(damage)
                   demon_health -= damage
                   print(deamon_health)
                   if deamon_health <= 0:
                            steve_health = 0
                   print("You attacked and did {} damage. Steve's health is now {}.".format(damage, steve_health))
                   if deamon_health == 0:
                            print("You killed steve and got his pick")
                            button4.config(state="disabled")
                            inventory.update({"pickaxe": 1})
                            update_inventory_label()
                            button1.config(state="normal")
                            button2.config(state="normal")
                            button3.config(state="normal")
                            room_image = tk.PhotoImage(file="./images/steve.png").subsample(1, 1)
                            room_image_label.config(image=room_image)
                            room_image_label.image = room_image
                            input_entry.bind("<Return>", lambda event: enter_secret_room() if input_entry.get() == "pickaxe" else enter_room())
             else:
                    # Take a random amount of health from the player
                    damage = random.randint(10, 30)
                    health -= damage
                    if health <= 0:
                        health = 0
                    print("You were attacked and took {} damage. Your health is now {}.".format(damage, health))
                    if health == 0:
                        print("You died")
                        quit()
def main():
    global button1, button2, button3, button4, room_image_label, inventory_label, health, steve_health, input_entry, output_label
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
