from process_command import execute

def main():
    """
    Основной цикл программы.
    Полуает команду через input()
    """
    print("Enter a command (or 'exit' to quit):")

    while True: 
        try:
            command = input("> ").strip().lower()

            if command == "exit":
                print("Exiting the program. Goodbye!")
                break

            execute(command)

        except Exception as e:

            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
