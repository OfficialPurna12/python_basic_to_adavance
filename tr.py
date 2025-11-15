# Traffic light using match-case (Python 3.10+)

light = input("Enter traffic light color (red / yellow / green): ").lower()

match light:
    case "red":
        print("STOP 🚫")
    case "yellow":
        print("READY ⚠️")
    case "green":       
        print("GO ✅")
    case _:
        print("Invalid color! Please enter red, yellow, or green.")
