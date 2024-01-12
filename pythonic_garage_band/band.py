class Band:
    """
    A class representing a musical band.

    Attributes:
    - name (str): The name of the band.
    - members (list): List of members in the band.
    """

    def __init__(self, name="Nirvana", members=None):
        """
        Initialize a Band instance.

        Parameters:
        - name (str): The name of the band.
        - members (list): List of members in the band.
        """
        self.members = members or None
        self.name = name


class Guitarist:
    """
    A class representing a guitarist.

    Attributes:
    - name (str): The name of the guitarist.
    """

    def __init__(self, name="Joan Jett"):
        """
        Initialize a Guitarist instance.

        Parameters:
        - name (str): The name of the guitarist.
        """
        self.name = name

    def __str__(self):
        """
        Return a string representation of the guitarist.

        Returns:
        str: A formatted string describing the guitarist and their instrument.
        """
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        """
        Return a string representation of the Guitarist instance.

        Returns:
        str: A formatted string describing the guitarist instance.
        """
        return f"Guitarist instance. Name = {self.name}"


class Drummer:
    """
    A class representing a drummer.

    Attributes:
    - name (str): The name of the drummer.
    """

    def __init__(self, name="Sheila E."):
        """
        Initialize a Drummer instance.

        Parameters:
        - name (str): The name of the drummer.
        """
        self.name = name

    def __str__(self):
        """
        Return a string representation of the drummer.

        Returns:
        str: A formatted string describing the drummer and their instrument.
        """
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        """
        Return a string representation of the Drummer instance.

        Returns:
        str: A formatted string describing the drummer instance.
        """
        return f"Drummer instance. Name = {self.name}"


class Bassist:
    """
    A class representing a bassist.

    Attributes:
    - name (str): The name of the bassist.
    """

    def __init__(self, name="Meshell Ndegeocello"):
        """
        Initialize a Bassist instance.

        Parameters:
        - name (str): The name of the bassist.
        """
        self.name = name

    def __str__(self):
        """
        Return a string representation of the bassist.

        Returns:
        str: A formatted string describing the bassist and their instrument.
        """
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        """
        Return a string representation of the Bassist instance.

        Returns:
        str: A formatted string describing the bassist instance.
        """
        return f"Bassist instance. Name = {self.name}"
