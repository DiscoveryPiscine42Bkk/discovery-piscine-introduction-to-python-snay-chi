import sys

def main():
    num_params = len(sys.argv) - 1  # Exclude the script name itself
    print(f"Number of parameters: {num_params}.")

if __name__ == "__main__":
    main()

