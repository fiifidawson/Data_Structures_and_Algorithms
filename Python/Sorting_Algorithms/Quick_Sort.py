class SortableArray:
    def __init__(self, array):
        self.array = array

    def partition(self, left_pointer, right_pointer):
        """
        We always choose the right-most element as the pivot.
        We keep the index of the pivot for later use.
        """
        pivot_index = right_pointer
        # We grab the pivot value itself
        pivot = self.array[pivot_index]

        # We start the right pointer immediately to the left of the pivot
        right_pointer -= 1

        while True:
            """
            Move the left pointer to the right as long as it
            points to value that is less than the pivot.
            """
            while self.array[left_pointer] < pivot:
                left_pointer += 1

            """
            Move the right pointer to the left as long as it
            points to a value that is greater than the pivot.
            """
            while self.array[right_pointer] > pivot:
                right_pointer -= 1

            """
            We've now reached the point where we've stopped
            moving both the left and right pointers.
            We check whether the left pointer has reached
            or gone beyond the right pointer. If it has,
            we break out of the loop so we can swap the pivot later
            on in our code.
            """
            if left_pointer >= right_pointer:
                break

                """
                If the left pointer is still to the left of the right
                pointer, we swap the values of the left and right pointers.
                """
            else:
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[left_pointer]
                    # We move the left pointer over to the right, gearing up for the next round of left and right pointer movements
                left_pointer += 1

        """
        As the final step of the partition, we swap the value
        of the left pointer with the pivot.
        """
        self.array[left_pointer], self.array[pivot_index] = self.array[pivot_index], self.array[left_pointer]

        """
        We return the left_pointer for the sake of the quicksort method
        which will appear later in this chapter.
        """
        return left_pointer
