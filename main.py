from utils import add_visitor, show_visitors

def main():
    visitors = []

    while True:
        print("\n--- Barangay Visitor Log ---")
        name = input("Enter visitor name: ")
        purpose = input("Enter visitor purpose: ")

        add_visitor(visitors, name, purpose)

        another = input("Add another visitor? (yes/no): ").strip().lower()
        if another != "yes":
            break

    print("\n--- Recorded Visitors ---")
    show_visitors(visitors)
    print(f"\nTotal number of visitors recorded: {len(visitors)}")

if __name__ == "__main__":
    main()
