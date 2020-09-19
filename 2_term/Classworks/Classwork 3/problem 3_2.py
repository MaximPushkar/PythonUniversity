class VectorNd:
    def __init__(self, lst):
        self._coord = lst

    def get_view(self):
        print(self._coord)

    def get_length(self):
        ans = 0
        for i in self._coord:
            ans += i ** 2
        ans **= 0.5
        return ans

    def get_mean(self):
        ans = 0
        for i in self._coord:
            ans += i
        ans /= len(self._coord)
        return ans

    def get_min_and_max(self):
        return min(self._coord), max(self._coord)


string = input()
lst = [float(i) for i in string.split()]
vector = VectorNd(lst)
vector.get_view()
print(vector.get_length())
print(vector.get_mean())
print(vector.get_min_and_max())
