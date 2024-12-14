from decimal import Decimal


# class Frange:
#     def __init__(self, left, right, step):
#         self.left = left
#         self.right = right
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.left + self.step > self.right + self.step:
#             raise StopIteration
#         result = self.left
#         self.left += self.step
#         return Decimal(result)
#
#
# for i in Frange(1, 100, 3.5):
#     print(i)

class Frange:
    def __init__(self, left, right=None, step=1):
        if right is None:
            self.left = Decimal(0)
            self.right = Decimal(left)
        else:
            self.left = Decimal(left)
            self.right = Decimal(right)
        self.step = Decimal(step)

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.left >= self.right) or (self.step < 0 and self.left <= self.right):
            raise StopIteration

        result = self.left
        self.left += self.step
        return result


for i in Frange(1, 100, 3.5):
    print(i)
assert (list(Frange(5)) == [0, 1, 2, 3, 4])
assert (list(Frange(2, 5)) == [2, 3, 4])
assert (list(Frange(2, 10, 2)) == [2, 4, 6, 8])
assert (list(Frange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(Frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert (list(Frange(1, 5)) == [1, 2, 3, 4])
assert (list(Frange(0, 5)) == [0, 1, 2, 3, 4])
assert (list(Frange(0, 0)) == [])
assert (list(Frange(100, 0)) == [])
print('SUCCESS!')
