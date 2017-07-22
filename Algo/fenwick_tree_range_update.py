"""
5 3
2 3 100
1 2 200
4 5 200

[0, 0, 0, 0, 0]
[0, 100, 100, 0, 0]
[200, 300, 100, 0, 0]
[200, 300, 100, 200, 200]

returns 300

"""

class Fenwick:

    def __init__(self, a):
        self.length = a
        self.data = [0] * a

    def __str__(self):
        out = []
        for x in range(0, self.length):
            out.append(self.query(x))
        return str(out)

    def update(self, at, by):
        while at < len(self.data):
            self.data[at] += by;
            at |= (at + 1)

    def query(self, at):
        res = 0
        while at >= 0:
            res += self.data[at]
            at = (at & (at + 1)) - 1

        return res

# runner
array_length = 5
instructions = 3
instructions_array = [[2, 3, 100], [1, 2, 200], [4, 5, 200]]

ft = Fenwick(array_length)
for ins in instructions_array:
    ft.update(ins[0], ins[2])
    ft.update(ins[1] + 1, -ins[2])
    print(ft)
result = 0
for x in range(0, array_length):
    result = max(ft.query(x), result)

print(result)
