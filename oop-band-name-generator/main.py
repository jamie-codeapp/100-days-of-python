class BandNameGenerator:
    """A class to generate a band name based on the city and pet name provided by the user."""

    def __init__(self):
        """Initializes the BandNameGenerator with empty city and pet attributes."""
        self.city = ""
        self.pet = ""

    def get_user_input(self):
        """
        Prompts the user for the city they grew up in and their pet's name.
        These inputs are used to generate a band name.
        """
        self.city = input("What's the name of the city you grew up in?\n").title()
        self.pet = input("What's your pet's name?\n").title()

    def generate_band_name(self):
        """
        Generates a band name using the user's city and pet's name.

        Returns:
            str: The generated band name.
        """
        return f"Your band name could be {self.city} {self.pet}"

    def display_band_name(self):
        """Displays the generated band name to the user."""
        print(self.generate_band_name())


if __name__ == "__main__":
    """
    Runs the Band Name Generator program.
    Prompts the user for their city and pet name, and displays a generated band name.
    """
    print("Welcome to the Band Name Generator.")
    band_name_generator = BandNameGenerator()
    band_name_generator.get_user_input()
    band_name_generator.display_band_name()
