def calculate_area_utm(coords):
    """
    Calculates area in square meters using Shoelace formula for UTM (x, y) coordinates
    """
    n = len(coords)
    area = 0
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)
    return abs(area) / 2

# === MAIN PROGRAM ===
print("📐 Land Area Calculator (Using UTM Coordinates in meters)")
print("Enter coordinates in order around the boundary (clockwise or counter-clockwise).")
print("When you're done, type 'done'.")

coords = []
while True:
    x_str = input("Enter X (or 'done'): ")
    if x_str.lower() == 'done':
        break
    y_str = input("Enter Y: ")
    try:
        x = float(x_str)
        y = float(y_str)
        coords.append((x, y))
    except:
        print("❗ Invalid input, try again.")

if len(coords) < 3:
    print("❗ At least 3 points are needed to calculate area.")
else:
    area_m2 = calculate_area_utm(coords)
    area_acres = area_m2 / 4046.86

    print(f"\n✅ Area of the plot:")
    print(f"→ {area_m2:.2f} square meters")
    print(f"→ {area_acres:.4f} acres")

