def triangles(max):
    line = [1]
    time = 0
    while time <= max:
        yield(line.copy())
        for i in range(len(line)-1, 0, -1):
            line[i] += line[i-1]
        line.append(1)
        time += 1

# 以下是测试代码       

for t in triangles(10):
    print(t)