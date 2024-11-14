import random
from enum import Enum

# Enum to define the modes of operation for the quiz
class Mode(Enum):
    PROTOCOL_BY_PORT = 1  # Mode to identify protocol by port number
    PORT_BY_PROTOCOL = 2  # Mode to identify port number by protocol

# Class that encapsulates the quiz functionality
class PortProtocolQuiz:
    def __init__(self):
        """
        Initializes the quiz with a dictionary mapping port numbers to protocols.
        The dictionary data represents common ports and their corresponding protocols.
        """
        self.data = {
            "20": "FTP", "21": "FTP", "22": "SSH", "23": "Telnet", "25": "SMTP", "53": "DNS", 
            "67": "DHCP", "68": "DHCP", "80": "HTTP", "110": "POP3", "137": "NetBIOS", 
            "139": "NetBIOS", "143": "IMAP", "161": "SNMP", "162": "SNMP", "389": "LDAP", 
            "443": "HTTPS", "445": "SMB", "3389": "RDP"
        }

    def get_user_choice(self):
        """
        Displays the main menu and prompts the user for their choice.
        Returns the user's choice as a string.
        """
        while True:
            val = input(
                "Main Menu:\n"
                " 1. Given a port number, identify the PROTOCOL (use abbreviation).\n"
                " 2. Given a port protocol, identify a port NUMBER.\n"
                " 3. Exit\n"
            )
            # Check if the input is valid
            if val in {"1", "2", "3"}:
                return val
            print("Invalid choice. Please select 1, 2, or 3.")

    def select_random_item(self):
        """
        Selects a random key-value pair from the data dictionary.
        Returns the selected port and its corresponding protocol.
        """
        key = random.choice(list(self.data.keys()))
        return key, self.data[key]

    def ask_question(self, mode):
        """
        Asks the user a question based on the mode of operation.
        mode: Mode.PROTOCOL_BY_PORT or Mode.PORT_BY_PROTOCOL
        """
        if mode == Mode.PROTOCOL_BY_PORT:
            # Ask for the protocol corresponding to a random port
            port, protocol = self.select_random_item()
            question = f"What is the protocol for port {port} (m=Main Menu)?"
            answer = protocol
        elif mode == Mode.PORT_BY_PROTOCOL:
            # Ask for the port corresponding to a random protocol
            protocol, port = self.select_random_item({v: k for k, v in self.data.items()})
            question = f"What is the port number for protocol {protocol} (m=Main Menu)?"
            answer = port
        
        # Check the user's answer
        self.check_answer(question, answer)

    def check_answer(self, question, answer):
        """
        Checks the user's answer against the correct answer.
        Provides feedback based on the user's input.
        """
        userinput = input(question)
        if userinput == answer:
            print("Correct answer!\n\n")
        elif userinput == 'm':
            print("\n\n")
        else:
            print(f"Incorrect. The correct answer is: {answer}\n\n")

    def run_quiz(self):
        """
        Runs the quiz program, looping until the user decides to exit.
        The user can choose between identifying protocols by port numbers or port numbers by protocols.
        """
        while True:
            # Get the user's choice from the main menu
            val = self.get_user_choice()
            
            # Execute the corresponding action based on the user's choice
            if val == "1":
                self.ask_question(mode=Mode.PROTOCOL_BY_PORT)
            elif val == "2":
                self.ask_question(mode=Mode.PORT_BY_PROTOCOL)
            elif val == "3":
                print("Quitting Program.")
                break

if __name__ == "__main__":
    # Create an instance of the quiz and run it
    quiz = PortProtocolQuiz()
    quiz.run_quiz()
