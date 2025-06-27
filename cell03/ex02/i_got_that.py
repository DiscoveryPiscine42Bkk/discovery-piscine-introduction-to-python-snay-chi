def main():
    while True:
        user_input = input("What you gotta say? : ") if not 'got_any' in locals() else input("I got that! Anything else? : ")
        # Normalize input to check for "STOP"
        if user_input == "STOP":
            break

        # After first iteration, we prompt differently
        got_any = True

if __name__ == "__main__":
    main()
