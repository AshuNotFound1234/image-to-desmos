i = 0.03 # grid step size
precision = 10  
points = []

steps = int(1 / i) + 1

for y in range(steps):
    for x in range(steps):
        x_val = round(x * i, precision)
        y_val = round(-y * i, precision)
        points.append(f"\\left({x_val},{y_val}\\right)")

formatted = "P=\\left[" + ",".join(points) + "\\right]"

with open("points.txt", "w") as f:
    f.write(formatted)

print(f"Saved {len(points)} points to points.txt")