import sys
from core.pdf_splitter import pdf_splitter_interactive
from core.pdf_merger import pdf_merger_interactive
from core.pdf_protector import pdf_protector_interactive

def main_menu():
    print(r"""
  _____                 _____  _            _    
 |  __ \               |  __ \| |          | |   
 | |__) |_ _  __ _  ___| |__) | |_   _  ___| | __
 |  ___/ _` |/ _` |/ _ \  ___/| | | | |/ __| |/ /
 | |  | (_| | (_| |  __/ |    | | |_| | (__|   < 
 |_|   \__,_|\__, |\___|_|    |_|\__,_|\___|_|\_\
              __/ |                              
             |___/                               
|--------------------------------------------------------------------|
| Created By: Krishna Gopal Jha                                      |
| Checkout my LinkedIn: https://www.linkedin.com/in/krishnagopaljha/ |
| Lookup at my insta: https://instagram.com/theindianpsych           |
|--------------------------------------------------------------------|

Welcome to Page Pluck PDF Tool
Available Features:
1. PDF Splitter
2. PDF Merger
3. Protect PDF with Password
0. Exit
""")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            pdf_splitter_interactive()
        elif choice == "2":
            pdf_merger_interactive()
        elif choice == "3":
            pdf_protector_interactive()
        elif choice == "0":
            print("Exiting. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
