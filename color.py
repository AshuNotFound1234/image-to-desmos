from PIL import Image


image_path = "rickroll.png"
output_path = "color.txt"
i = 0.03 # grid step size
precision = 4 

img = Image.open(image_path).convert("RGB") 
width, height = img.size

steps = int(1 / i) + 1
pixel_dx = width / (steps - 1)
pixel_dy = height / (steps - 1)

color_entries = []

for y_step in range(steps):
    y = int(round(y_step * pixel_dy))
    for x_step in range(steps):
        x = int(round(x_step * pixel_dx))

        x = min(x, width - 1)
        y = min(y, height - 1)

        r, g, b = img.getpixel((x, y))
        color_entries.append(f"\\operatorname{{rgb}}\\left({r},{g},{b}\\right)")

formatted = f"c=\\left[{','.join(color_entries)}\\right]"

with open(output_path, "w") as f:
    f.write(formatted)

print(f"Saved {len(color_entries)} RGB color entries to {output_path}")
