"""
File to connect to our SGBD and perform necesary queries.



DATA DEFINITIONS:

event_type: str
    "Ambos", "Casamento", "Festa"

date_start: datetime.date

date_end: datetime.date

organizer_cpf: str
    "nnn.nnn.nnn.nn" where "n" is a numeric(0-9)
    None    if the user doesnt care

organizer_name: str
    None    if the user doesnt care

"""

def temporary_test():
    data = []
    with open("sample_text.txt", "r") as f:
        data = [line.rstrip() for line in f]
    return data

def connect_database():
    pass

def search_events(event_type, date_start, date_end, organizer_cpf, organizer_name):
    """
    Returns as a list of strings the events that match the query
     -- Example of what to return (inside a string the layout can be different):
    ["Casamento, 12/01/2018, 111.111.111.11, Carlão", 
     "Festa, 26/04/2018, 111.111.111.11, Carlão", 
    ]

    """
    return temporary_test()     # TODO: Remove


def main():
    temporary_test()

if __name__ == "__main__":
    main()
