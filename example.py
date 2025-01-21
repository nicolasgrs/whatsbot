# -*- coding: utf-8 -*-
"""
---------------------------------------------------------------
WhatsApp Bot Project

Description:
This project implements a WhatsApp bot using the Selenium WebDriver.
The bot is designed to automate various interactions on the WhatsApp
platform, such as authenticating, opening contacts, reading messages,
and sending messages.

Features:
- Authenticate: Log in to the WhatsApp platform using credentials
  or authentication tokens.
- Open Contact: Navigate to a specific contact or group chat to
  perform actions like reading and sending messages.
- Read Message: Retrieve and parse incoming messages from contacts
  or groups for further processing or analysis.
- Send Message: Send text messages, images, files, or emojis to
  individual contacts or groups.

Dependencies:
- Selenium WebDriver: Used for browser automation.

---------------------------------------------------------------
Credits:

Author: 
    Gabriel Hinz

Website:
    https://gabriel.legendproject.com.br
    
Contact: 
    Email: gabriel@legendproject.com.br
---------------------------------------------------------------
"""
from bot import WhatsBot


def send_messages_to_contact() -> None:
    """
    Opens a contact to send messages or read the last message.

    This function opens a contact and allows the user to:
    - Send messages repeatedly to that contact (use !end to select another contact)
    - Read the last message from that contact
    - Use !quit to exit the program

    Example:
        - Open a contact named 'John'
        - Choose to send messages or read the last message
        - If sending: send messages until '!end' is typed to select another contact
        - If reading: display the last message and return to contact selection
    """
    # Starting a new bot object
    bot = WhatsBot(headless=False)  # set headless to True to hide the webriver
    bot.authenticate()

    while True:
        # Selecting the contact to talk
        contact = input("\nWhich contact do you want to open? (!quit to exit) ")

        # Exit program if user types !quit
        if contact.lower() == '!quit':
            break

        # Checking if contact exists
        if bot.open_contact(contact):
            print("\nSelect an action:")
            print("1. Send messages")
            print("2. Read last message")
            print("3. Read message block")
            option = input("Option: ")

            if option == "1":
                # Message loop - use !end to select another contact
                while True:
                    message = input("Type your message (!end to change contact, !quit to exit) ")

                    # Return to contact selection
                    if message.lower() == '!end':
                        break
                    # Exit program
                    elif message.lower() == '!quit':
                        return
                    # Send the message
                    bot.send_messages(message)
            
            elif option == "2":
                # Reading last message
                message = bot.last_message()
                if message:
                    print(f"\nLast message from {contact}:")
                    print(message)
                else:
                    print("No messages found")
                input("\nPress Enter to continue...")
            
            elif option == "3":
                while True:
                    # Reading message block
                    messages = bot.message_block()
                    if messages:
                        print(f"\nMessage block from chat with {contact}:")
                        print(messages)
                    else:
                        print("No messages found")
                    
                    # Ask if user wants to load more messages
                    load_more = input("\nPress Enter to continue, or type 'more' to load more messages: ")
                    if load_more.lower() == 'more':
                        if bot.load_more_messages():
                            print("Loading more messages...")
                            continue
                        else:
                            print("No more messages available or button not found")
                            input("Press Enter to continue...")
                            break
                    break
        else:
            # if application does not find the contact
            print("Contact not found")
    
    # Close the driver when done
    bot.quit_driver()


def main():
    """
    This code has some examples of how to use the bot.
    """
    send_messages_to_contact()


if __name__ == '__main__':
    main()
