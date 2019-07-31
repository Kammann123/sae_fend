"""
Sample 03. Testing SAEFend object's state flow.
"""

# python native modules

# third-party modules

# sae project modules
from pystates.state_event import StateEvent

from fend.core.sae_fend import SAEFend
from fend.core.events import GoBack
from fend.core.events import Finished
from fend.core.events import Close


def choice_menu() -> StateEvent:
    """ Option menu. """
    print(""" Choose one option from the following ones:
    0: Quit/Exit the program. 
    1: Generate GoBack event.
    2: Generate Finished event.
    3: Generate Close event.
    4: Generate ErrorOccurred event. """)

    options = ["Quit",
               GoBack("Sample", None),
               Finished("Sample", None),
               Close("Sample", None)
               ]
    choice_index = 0

    while True:
        try:
            choice = input("User wants -> ")
            choice_index = int(choice)
            break
        except:
            print("Invalid input! READ!!!")
            continue

    return options[choice_index]


if __name__ == "__main__":
    fend = SAEFend(50)

    while True:
        print("SAEFend state: {}".format(str(fend.current_state())))

        choice = choice_menu()

        if str(choice) == "Quit":
            print("Ciao!")
            break

        fend.send_event(choice)
        fend.run_event()
