def chunkify(division, grid):
    div_grid = []
    for i in range(0, len(grid), division):
        div_row = []
        for j in range(0, len(grid), division):
            out_grid = []
            for k in range(division):
                s = ""
                for m in range(division):
                    s += grid[i+k][j+m]
                out_grid.append(s)
            div_row.append(out_grid)
        div_grid.append(div_row)
    return div_grid

#print(chunkify(2, ["#..#", "....", "....", "#..#"]))
#print(chunkify(3, ["##.##.", "#..#..", "......", "##.##.", "#..#..", "......"]))

# flips a chunk left-to-right
def f(chunk):
    N = len(chunk)
    output = []
    for i in range(N):
        output_row = ""
        for j in range(N):
            output_row += chunk[i][N - j - 1]
        output.append(output_row)
    return output

# rotates a chunk counterclockwise 90 degrees
def r(chunk):
    N = len(chunk)
    output = []
    for i in range(N):
        output_row = ""
        for j in range(N):
            output_row += chunk[j][N - i - 1]
        output.append(output_row)
    return output

def parse_rules(file):
    two_rules = []
    three_rules = []
    my_f = open(file, "r")
    for line in my_f:
        w = line.split()
        lhs = w[0].split("/")
        rhs = w[2].split("/")
        if len(lhs) == 2:
            two_rules.append( ( lhs, rhs ) )
            two_rules.append( ( r(lhs), rhs ) )
            two_rules.append( ( r(r(lhs)), rhs ) )
            two_rules.append( ( r(r(r(lhs))), rhs ) )
            two_rules.append( ( f(lhs), rhs ) )
            two_rules.append( ( r(f(lhs)), rhs ) )
            two_rules.append( ( r(r(f(lhs))), rhs ) )
            two_rules.append( ( r(r(r(f(lhs)))), rhs ) )
        elif len(lhs) == 3:
            three_rules.append( ( lhs, rhs ) )
            three_rules.append( ( r(lhs), rhs ) )
            three_rules.append( ( r(r(lhs)), rhs ) )
            three_rules.append( ( r(r(r(lhs))), rhs ) )
            three_rules.append( ( f(lhs), rhs ) )
            three_rules.append( ( r(f(lhs)), rhs ) )
            three_rules.append( ( r(r(f(lhs))), rhs ) )
            three_rules.append( ( r(r(r(f(lhs)))), rhs ) )
    return (two_rules, three_rules)

# flips a chunk left-to-right
def flip(chunk):
    N = len(chunk)
    output = []
    for i in range(N):
        output_row = ""
        for j in range(N):
            output_row += chunk[i][N - j - 1]
        output.append(output_row)
    return output

# rotates a chunk counterclockwise 90 degrees
def rotate(chunk):
    N = len(chunk)
    output = []
    for i in range(N):
        output_row = ""
        for j in range(N):
            output_row += chunk[j][N - i - 1]
        output.append(output_row)
    return output

def match_chunk(chunk, pattern):
    N = len(chunk)
    for i in range(N):
        for j in range(N):
            if chunk[i][j] != pattern[i][j]:
                return False
    return True

def match_rules(chunk, rules):
    for rule in rules:
        lhs, rhs = rule
        if match_chunk(chunk, lhs):
            return rhs
    assert(False)
    return None

def step(chunkified, rules):
    out = []
    for i in range(len(chunkified)):
        row = []
        for j in range(len(chunkified)):
            row.append(match_rules(chunkified[i][j], rules))
        out.append(row)
    return out

def connect(chunkified):
    s = len(chunkified[0][0])
    N = len(chunkified) * s
    out = []
    for i in range(N):
        row = ""
        for j in range(N):
            row += chunkified[i // s][j // s][i % s][j % s]
        out.append(row)
    return out

#print(connect(chunkify(2, ["####", "####", "####", "####"])))
#print(connect(chunkify(2, ["####", "#..#", "#..#", "####"])))

def print_grid(grid):
    for row in grid:
        print(row)
    print("")

def artwork(iterations, rules):
    two_rules, three_rules = rules
    grid = [".#.", "..#", "###"]
    for i in range(iterations):
        # decide if /2 or /3
        if len(grid[0]) % 2 == 0:
            # recursively break into chunks
            div_grid = chunkify(2, grid)
            # apply a rule
            unconnected = step(div_grid, two_rules)
        else: #divides into 3
            # recursively break into chunks
            div_grid = chunkify(3, grid)
            # apply a rule
            unconnected = step(div_grid, three_rules)
        # reform into grid
        grid = connect(unconnected)

    # count up on pixels
    count = 0
    for row in grid:
        for c in row:
            if c == "#":
                count += 1
    return count

rules = parse_rules("day21input.txt")
#print_grid(artwork(0, rules))
#print_grid(artwork(1, rules))
#print_grid(artwork(2, rules))
print(artwork(18, rules))
