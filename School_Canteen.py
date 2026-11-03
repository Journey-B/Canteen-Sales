number_of_items = input("Enter the number of items : ")
for i in range(int(number_of_items)):
    total_sales = input("Enter the total sales : ")



def calculate_average(total_sales,number_of_items):
    average = total_sales/number_of_items
    meeting_target = 0
    Below_target = 0
    if number_of_items >= 500:
        meeting_target = meeting_target + 1
    if number_of_items < 500:
        Below_target = Below_target + 1

    return average,meeting_target,Below_target



def canteen_sales_report(average,meeting_target,Below_target):













