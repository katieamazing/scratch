
firewall_test = [
 (0, 3),
 (1, 2),
 (4, 4),
 (6, 4)
]

def parse_into_list(file):
    firewall = []
    f = open(file, "r")
    for line in f:
        w = line.split()
        r = int(w[0].strip(":"))
        d = int(w[1])
        firewall.append((r, d))
    return firewall

class Scanners:
    def __init__(self, firewall):
        self.firewall = firewall
        self.pos_scanners = []
        for i in range(len(firewall)):
            self.pos_scanners.append(0)
        self.dir_scanners = []
        for i in range(len(firewall)):
            self.dir_scanners.append(1)

    def step(self):
        for i in range(len(self.firewall)):
            d = self.firewall[i][0]
            r = self.firewall[i][1]
            self.pos_scanners[i] += self.dir_scanners[i]
            if self.pos_scanners[i] == r - 1:
                self.dir_scanners[i] = -1
            if self.pos_scanners[i] == 0:
                self.dir_scanners[i] = 1

    def walk(self):
        severity = 0
        packet = -1
        for i in range(10):
            print("packet's turn(%d)" % i)
            self.log(packet)
            # move the packet
            packet += 1
            print("scanner's turn(%d)" % i)
            self.log(packet)
            # possibly caught
            for i in range(len(self.firewall)):
                d = self.firewall[i][0]
                r = self.firewall[i][1]
                if packet == d and self.pos_scanners[i] == 0:
                    severity += d * r
            self.step()
        return severity

    def log(self, packet):
        for i in range(10):
            found = False
            for j in range(len(self.firewall)):
                d = self.firewall[j][0]
                r = self.firewall[j][1]
                if d == i:
                    for k in range(r):
                        if d == packet and k == 0:
                            if k == self.pos_scanners[j]:
                                print("(S)", end="")
                            else:
                                print("( )", end="")
                        else:
                            if k == self.pos_scanners[j]:
                                print("[S]", end="")
                            else:
                                print("[ ]", end="")
                    print("")
                    found = True
                    break
            if not found:
                print("...")

#fw = parse_into_list("day13input.txt")
fw = firewall_test

def find_delay(fw):
    for delay in range(100000000):
        s = Scanners(fw)
        for i in range(delay):
            s.step()
        if s.walk() == 0:
            return delay
    return None

s = Scanners(fw)
for delay in range(10):
    s.step()
print(s.walk())
#print(find_delay(fw))
