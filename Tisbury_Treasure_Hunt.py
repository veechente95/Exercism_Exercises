"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate."""
    return record[-1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components."""
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match."""
    if tuple(azara_record[1]) == rui_record[1]:
        return True
    else:
        return False


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group."""
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    else:
        return "not a match"
    
 
