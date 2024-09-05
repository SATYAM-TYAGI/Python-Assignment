def compute_stats(input_list):
    
    if not input_list:
        return 0, 0, None, None, []

    total_sum = sum(input_list)
    avg = total_sum / len(input_list)
    min_val = min(input_list)
    max_val = max(input_list)

    cumulative_sum = [sum(input_list[:i + 1]) for i in range(len(input_list))]

    return total_sum, avg, min_val, max_val, cumulative_sum

def user_input():

    try:
        input_str = input("Enter a list of numbers (comma-separated): ")
        input_list = [float(num) for num in input_str.split(",")]
        total_sum, avg, min_val, max_val, cumulative_sum = compute_stats(input_list)

        print(f"Sum: {total_sum}")
        print(f"Average: {avg:.2f}")
        print(f"Minimum: {min_val}")
        print(f"Maximum: {max_val}")
        print(f"Cumulative Sum: {cumulative_sum}")

    except ValueError:
        print("Invalid input. Please enter a valid list of numbers.")

user_input()