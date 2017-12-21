class Particle:
    def __init__(self, pos, vel, acc):
        self.pos_x = int(pos[0])
        self.pos_y = int(pos[1])
        self.pos_z = int(pos[2])
        self.vel_x = int(vel[0])
        self.vel_y = int(vel[1])
        self.vel_z = int(vel[2])
        self.acc_x = int(acc[0])
        self.acc_y = int(acc[1])
        self.acc_z = int(acc[2])

    def tick(self):
        self.vel_x += self.acc_x
        self.vel_y += self.acc_y
        self.vel_z += self.acc_z
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.pos_z += self.vel_z

    def distance(self):
        return abs(self.pos_x) + abs(self.pos_y) + abs(self.pos_z)

    def position(self):
        return (self.pos_x, self.pos_y, self.pos_z)


def init_particles(file):
    particles = {}
    particle_id = 0
    f = open(file, "r")
    for line in f:
        w = line.split()
        n = []
        for word in w:
            number_string = word.strip(",")[3:-1]
            n.append(number_string.split(","))
        particles[particle_id] = Particle(n[0], n[1], n[2])
        particle_id += 1
    return particles

def get_answers(f):
    particles = init_particles(f)
    for i in range(1000):
        print(i)
        to_remove = set()
        for p in particles:
            for t in particles:
                if p is not t and particles[p].position() == particles[t].position():
                    to_remove.add(p)
                    to_remove.add(t)
        for key in to_remove:
            del particles[key]
        for p in particles:
            particles[p].tick()

    # mins = None
    # so_far = None
    # for i, p in enumerate(particles):
    #     if not so_far or particles[p].distance() < so_far:
    #         mins = i
    #         so_far = particles[p].distance()
    # return mins
    return len(particles)

#print(get_answers("day20test.txt"))
print(get_answers("day20input.txt"))
