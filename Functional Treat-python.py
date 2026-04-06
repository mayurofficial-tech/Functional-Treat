
data_list=[]
data_summary={}

def input_data():
    global data_list
    data_list = []
    print("Enter the values one by one (integers only) separated by a space:")
    data_list=list(map(int,input().split()))
    print("Data has been stored successfully!")
def display_summary():
    if not data_list:
        print("Data is empty!")
        return
    total = len(data_list)
    min_val= min(data_list)
    max_val= max(data_list)
    sum_val= sum(data_list)
    avg_val= sum_val/total
    global data_summary
    data_summary = {"Total": total,
                    "Minimum": min_val,
                    "Maximum": max_val,
                    "Average": avg_val,
                    "Sum": sum_val}
    print("Data Summary:")
    for i,j in data_summary.items():
        print(f"{i} : {j}")

def factorial(n):
    """Calculate factorial using recursion"""
    if n <= 1:
        return 1
    return n * factorial(n-1)

def calculate_factorial():
    n=int(input("Enter  a number to calculate factorial: "))
    print(f"Factorial of {n} is :-{factorial(n)}")

def filter_data():
    threshold = int(input("Enter a threshold value: "))
    result = []
    for num in data_list:
        if num >= threshold:
            result.append(num)
    if result:
        print(f"Filtered Data (values >= {threshold}): {','.join(map(str,result))}")
    else:
        print("No values meet the threshold.")

def sort_data():
    if not data_list:
        print("Data is empty!")
        return
    print("Enter  the choose:\n1. Ascending\n2. Descending")
    ch=int(input("Enter your choice: "))
    if ch == 1:
        sort_data=sorted(data_list)
        print(f"Sorted Data is : {','.join(map(str,sort_data))}")
    elif ch == 2:
        sort_data=sorted(data_list,reverse=True)
        print(f"Sorted Data is : {','.join(map(str,sort_data))}")
    else:
        print("Invalid choice.")

def display_stat_data():
    if not data_list:
        print("Data is empty!")
        return
    min_val= min(data_list)
    max_val= max(data_list)
    sum_val= sum(data_list)
    avg_val= sum_val/len(data_list)
    print(f"Data Statistics:")
    print(f"Minimum: {min_val}\nMaximum: {max_val}\nAverage: {avg_val}\nSum: {sum_val}")
while True:
    print('''
Main Menu
1.Input Data
2. Display Data Summary(Built-in Functions)
3. Calculate Factorial(Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program
    ''')
    choice = input('Enter your choice: ')
    if (choice == '1'):
        input_data()
    elif (choice == '2'):
        display_summary()
    elif (choice == '3'):
        calculate_factorial()
    elif (choice == '4'):
        filter_data()
    elif (choice == '5'):
        sort_data()
    elif (choice == '6'):
        display_stat_data()
    elif (choice == '7'):
        break
    else:
        print("Invalid choice.")

