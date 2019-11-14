Socks, Capacity, Diff = map(int, input().split())

colors = list(map(int, input().split()))

colors = sorted(colors)

if Capacity >= Socks:
    num_machines = 1
else:
    num_machines = 0
    low = 0
    while True:
        if low >= Socks:
            break
        up = low + Capacity - 1
        if up >= Socks:
            up = Socks - 1
        while up >= low:
            if colors[up] - colors[low] <= Diff:
                num_machines += 1
                low = up + 1
                break
            up -= 1
        
print(num_machines)


