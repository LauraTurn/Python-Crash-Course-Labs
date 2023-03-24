print("\n8-9 Messages")
print("Passing a List\n")

def show_messages(texts):
    """Print a list of text messages"""
    for text in texts:
        message = f"{text}"
        print(message)

text_messages = ['Hey sweetie, we on for shopping today?',
                 'This is Schickler Elementary, Nathan needs to be picked up immediately.',
                 'We are doing Easter at our house this year. We will eat at 1pm.']

show_messages(text_messages)


print("\n\n8-10 Sending Messages")
print("Modifying a List in a Function")

def send_messages(unsent_messages, sent_messages):
    """
    Simulate sending each text message until none are left.
    Move each text to sent messages after sending.
    """
    while unsent_messages:
        sent_text = unsent_messages.pop()
        print(f"\nSending...\n{sent_text}")
        sent_messages.append(sent_text)

def show_messages(sent_messages):
    """Print a list of text messages"""
    print("\nThe following text messages have been sent:")
    for sent_message in sent_messages:
        print(f"\t\"{sent_message}\"")

unsent_messages = ['Hey sweetie, we on for shopping today?',
                 'This is Schickler Elementary, Nathan needs to be picked up immediately.',
                 'We are doing Easter at our house this year. We will eat at 1pm.']
sent_messages = []

send_messages(unsent_messages, sent_messages)

show_messages(sent_messages)

print(f"\nMessages not sent: \n{unsent_messages}")
print(f"\nMessages successfully sent: \n{sent_messages}")


print("\n\n8-11 Archived Messages")
print("Preventing a Function from Modifying a List\n")

def send_messages(unsent_messages, sent_messages):
    """
    Simulate sending each text message until none are left.
    Move each text to sent messages after sending.
    """
    while unsent_messages:
        sent_text = unsent_messages.pop()
        print(f"\nSending...\n{sent_text}")
        sent_messages.append(sent_text)

def show_messages(sent_messages):
    """Print a list of text messages"""
    print("\nThe following text messages have been sent:")
    for sent_message in sent_messages:
        print(f"\t\"{sent_message}\"")

unsent_messages = ['Hey sweetie, we on for shopping today?',
                 'This is Schickler Elementary, Nathan needs to be picked up immediately.',
                 'We are doing Easter at our house this year. We will eat at 1pm.']
sent_messages = []

send_messages(unsent_messages[:], sent_messages)

show_messages(sent_messages)

print(f"\nArchived Texts: \n{unsent_messages}")
print(f"\nTexts successfully sent: \n{sent_messages}\n")
