from functions import average, normalize_text, select_numbers, sum_digits
 
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert sum_digits(9) == 9
assert sum_digits(1000) == 1
 
assert average([]) is None
assert average([2, 4, 6]) == 4
assert abs(average([1, 2]) - 1.5) < 1e-9
numbers_for_average = [3, 5, 10]
copy_for_average = numbers_for_average[:]
average(numbers_for_average)
assert numbers_for_average == copy_for_average
 
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
assert normalize_text("Один") == "один"
 
assert select_numbers([-5, 0, 2, 5], 2) == []
assert select_numbers([], 2) == []
assert select_numbers([1, 2, 3, 4, 5, 6], 2) == [4, 6]
assert select_numbers([3, 4, 5], 3) == [4]
assert select_numbers([4], 4) == []
assert select_numbers([4], 3) == [4]
assert select_numbers([-2, 0, 2, 4], 0) == [2, 4]
assert select_numbers([4, 4, 6, 4], 2) == [4, 4, 6, 4]
 
original = [6, 3, 8, 8]
saved_copy = original[:]
select_numbers(original, 2)
assert original == saved_copy
 
print("Базовые проверки пройдены")