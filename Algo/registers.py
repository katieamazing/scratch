import operator as op

ops = { "==": op.eq, ">=": op.ge, ">": op.gt, "<=": op.le, "<": op.lt, "!=": op.ne, "inc": op.add, "dec": op.sub }

def parse_into_list(file):
    a = []
    f = open(file, "r")
    for line in f:
        a.append(line.strip())
    return a

def init_register_dict(a):
    s = set()
    for instruction in a:
        s.add(instruction.split()[0])
    d = {}
    for register in s:
        d[register] = 0
    return d

def process_instructions(f):
    a = parse_into_list(f)
    d = init_register_dict(a)
    for instruction in a:
        words = instruction.split()
        if ops[words[5]](d[words[4]], int(words[6])):
            d[words[0]] = ops[words[1]](d[words[0]], int(words[2]))

    return max(d.values())

assert(process_instructions("registerex.txt") == 1)
print(process_instructions("registerinput.txt"))
