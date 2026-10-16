paper_sheets=int(input("Enter number paper sheets: "))
total=0
below_range=0
in_range=0
above_range=0
def classify(value):
    if value<208:
        return "Below range"
    elif 208<=value<=212:
        return "In range"
    else:
        return "Above range"
for i in range(paper_sheets):
    value=int(input("Enter the paper sheet width: "))
    cat=classify(value)
    print(cat)
    total=total+value
    if cat=="Below range":
        below_range=below_range+1
    elif cat=="In range":
        in_range=in_range+1
    else:
        above_range=above_range+1
def calculate_average(total,paper_sheets):
    return total/paper_sheets
wolf=calculate_average(total,paper_sheets)
print(f"Total width: {total} mm")
print(f"Average width: {wolf} mm")
print(f"Below range: {below_range}")
print(f"In range: {in_range}")
print(f"Above range: {above_range}")
    