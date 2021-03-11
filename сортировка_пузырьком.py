pr = [52, 123, 5, 77, 1, 13,54,12]
print(pr)
# cортировка пузырьком:
def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 2, 0, -1):
        if (pass_num % 2) == 1:
            for i in range(pass_num):
                 #if (pass_num % 2) == 1:
                     if a_list[i] > a_list[i +2]:
                         a_list[i], a_list[i + 2] = a_list[i + 2],a_list[i]
    return a_list
print(bubble_sort(pr))