import tkinter as tk
from tkinter import messagebox

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def sort_numbers():
    input_text = entry_numbers.get()
    try:
        numbers = list(map(int, input_text.split(',')))
        global sorted_list
        sorted_list = quicksort(numbers)
        result_label.config(text=f"Отсортированный список: {','.join(map(str, sorted_list))}")
        
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста введите целые числа разделенные запятыми.")
        
def linear_search(target):
    for index, value in enumerate(sorted_list):
        if value == target:
            return index
    return -1

def search_number():
    if 'sorted_list' not in globals():
        messagebox.showwarning("Предупреждение", "Сначала выполните сортировку")
        return
    try:
        target = int(entry_search.get())
        index = linear_search(target)
        if index != -1:
            messagebox.showinfo("Результат", f"Число {target} найдено на индексе {index}.")
        else:
            messagebox.showinfo("Резултат", f"Число {target} отсутсвует в списке.")
    except:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целое число для поиска.")


root = tk.Tk()
root.title("Сортировка и посик чисел")

label_numbers = tk.Label(root, text="Введите целые числа через запятую:")
label_numbers.pack()

entry_numbers = tk.Entry(root, width=20)
entry_numbers.pack()

sort_button = tk.Button(root, text="Сортировать", command=sort_numbers)
sort_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

label_search = tk.Label(root, text="Введите число для поиска: ")
label_search.pack()

entry_search = tk.Entry(root, width=20)
entry_search.pack()

search_button = tk.Button(root, text="Поиск", command=search_number)
search_button.pack()

root.mainloop()