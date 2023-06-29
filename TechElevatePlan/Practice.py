# def add_until_100(array):
#     if len(array) == 0:
#         return 0
#     else:
#         sum_rest = add_until_100(array[1:])
#         if array[0] + sum_rest > 100:
#             return sum_rest
#         else:
#             return array[0] + sum_rest

class SortableArray:
    def __init__(self, array):
        self.array = array

    def partition(self, left_pointer, right_pointer):
        # Pivot position is always initialzed to the right pointer
        pivot_index = right_pointer

        pivot = self.array[pivot_index]

        # Starting right pointer immediately to the left of the ivo
        right_pointer = right_pointer - 1

        while True:

            # Moving stages
            while self.array[left_pointer] < pivot:
                left_pointer = left_pointer + 1

            while self.array[right_pointer] > pivot:
                right_pointer = right_pointer - 1

            if left_pointer >= right_pointer:
                break
            else:
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[left_pointer]

                left_pointer += 1

                self.array[left_pointer], self.array[pivot_index] = self.array[pivot_index]
            
            return left_pointer, self.array

