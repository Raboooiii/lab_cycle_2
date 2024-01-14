print("Enter a List of Elements :- ")
str_list = list(map(int, input().split()))
print(str_list)
k = int(input("enter k:"))
Rotated = [(str_list[(i - k) % len(str_list)]) for i in range(len(str_list))]
No_duplicates = list(set(Rotated))
tpl1 = tuple(No_duplicates)
print(tpl1)
No_duplicates.sort()
Squared = [(x**2 - x) for x in No_duplicates]
print(Squared)
Final = sorted(Squared + No_duplicates)
print(Final)