class Class_Node(object):
    """
    Holds table data for a class
    """
    def __init__(self, subject: str, number: int, prerec: int, elective: bool):
        self.subject = subject
        self.number = number
        self.prerec = prerec
        self.elective = elective