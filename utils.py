def add_visitor(visitors_list, name, purpose):
    visitor_record = {
        "name": name,
        "purpose": purpose
    }
    visitors_list.append(visitor_record)

def show_visitors(visitors_list):
    if not visitors_list:
        print("No visitors recorded.")
        return

    for index, visitor in enumerate(visitors_list, start=1):
        print(f"{index}. Name: {visitor['name']}, Purpose: {visitor['purpose']}")
