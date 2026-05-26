import numpy as np

def run_mini_tool():
    while True:
        print("\n--- Array Operations Mini-Tool ---")
        # 1. Get user input and convert it to a list of numbers
        raw_input = input("Enter numbers separated by spaces (e.g., 10 20 30): ")
        
        # 2. Check if the user wants to stop the tool
        if raw_input.lower() == 'exit':
            print("Exiting the mini-tool. Goodbye!")
            break

        try: 
            num_list = [int(x) for x in raw_input.split()]
            arr = np.array(num_list)

            print(f"\nYour Array: {arr.tolist()}")
            print(f"Sum: {np.sum(arr)}")
            print(f"Average: {np.mean(arr)}")
            print(f"Max Value: {np.max(arr)} at index {np.argmax(arr)}")
            print(f"Min Value: {np.min(arr)} at index {np.argmin(arr)}")

        except ValueError:
            print("Mali. Ulitin mo.")


if __name__ == "__main__": 
    run_mini_tool()