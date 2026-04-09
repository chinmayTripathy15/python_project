# Final Smart Calculator (Natural Input + Short Commands)

import datetime

history = []

# Load history
try:
    file = open("history.txt", "r")
    history = file.readlines()
    file.close()
except:
    pass


while True:
    print("\n==== CALCULATOR ====")
    print("Type calculation directly (e.g., 7+(7-7)*1)")
    print("h  → history")
    print("cl → clear history")
    print("exit → quit")

    expr = input("Enter: ").strip()

    if expr == "exit":
        print("Exiting...")
        break

    elif expr == "h":
        if len(history) == 0:
            print("No history")
        else:
            for h in history:
                print(h.strip())
        continue

    elif expr == "cl":
        history = []
        open("history.txt", "w").close()
        print("History cleared")
        continue

    # Check empty input
    if expr == "":
        print("Empty input!")
        continue

    try:
        result = eval(expr)

        print("Result:", result)

        # Add time
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        output = time_now + " | " + expr + " = " + str(result)

        history.append(output)

        file = open("history.txt", "a")
        file.write(output + "\n")
        file.close()

    except ZeroDivisionError:
        print("Error: Division by zero")
    except:
        print("Invalid expression!")