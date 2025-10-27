#!/usr/bin/env python3
"""
Generate placeholder vehicle images as SVG files that can be converted to PNG
These are temporary placeholders - replace with actual vehicle images
"""

import os

# Ensure the vehicles directory exists
os.makedirs('/Users/szioni/Documents/myProjects/clipFactory/assets/vehicles', exist_ok=True)

# Vehicle definitions with colors and basic shapes
vehicles = {
    'car.svg': {
        'color': '#FF6B6B',
        'width': 300,
        'height': 180,
        'name': 'Car'
    },
    'bus.svg': {
        'color': '#FFD93D', 
        'width': 400,
        'height': 200,
        'name': 'School Bus'
    },
    'train.svg': {
        'color': '#6BCF7F',
        'width': 450,
        'height': 180,
        'name': 'Train'
    },
    'airplane.svg': {
        'color': '#4ECDC4',
        'width': 400,
        'height': 150,
        'name': 'Airplane'
    },
    'police_car.svg': {
        'color': '#4D79FF',
        'width': 300,
        'height': 180,
        'name': 'Police Car'
    },
    'fire_truck.svg': {
        'color': '#FF4757',
        'width': 380,
        'height': 200,
        'name': 'Fire Truck'
    },
    'ambulance.svg': {
        'color': '#FFFFFF',
        'width': 320,
        'height': 180,
        'name': 'Ambulance'
    }
}

def generate_car_svg(color, width, height, name):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bodyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:{color};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{darker_color(color)};stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Car body -->
  <rect x="30" y="80" width="{width-60}" height="70" rx="10" fill="url(#bodyGrad)" stroke="#2C3E50" stroke-width="3"/>
  
  <!-- Car top -->
  <rect x="80" y="40" width="{width-160}" height="50" rx="15" fill="#74B9FF" stroke="#2C3E50" stroke-width="2"/>
  
  <!-- Wheels -->
  <circle cx="80" cy="160" r="25" fill="#2C3E50" stroke="#34495E" stroke-width="3"/>
  <circle cx="{width-80}" cy="160" r="25" fill="#2C3E50" stroke="#34495E" stroke-width="3"/>
  
  <!-- Wheel centers -->
  <circle cx="80" cy="160" r="12" fill="#95A5A6"/>
  <circle cx="{width-80}" cy="160" r="12" fill="#95A5A6"/>
  
  <!-- Headlights -->
  <circle cx="15" cy="100" r="8" fill="#F1C40F" stroke="#E67E22" stroke-width="2"/>
  <circle cx="15" cy="130" r="8" fill="#F1C40F" stroke="#E67E22" stroke-width="2"/>
  
  <!-- Label -->
  <text x="{width//2}" y="{height-10}" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold" fill="#2C3E50">{name}</text>
</svg>'''

def generate_bus_svg(color, width, height, name):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <!-- Bus body -->
  <rect x="20" y="60" width="{width-40}" height="90" rx="8" fill="{color}" stroke="#2C3E50" stroke-width="3"/>
  
  <!-- Windows -->
  <rect x="40" y="75" width="50" height="30" rx="5" fill="#74B9FF" stroke="#2C3E50" stroke-width="2"/>
  <rect x="100" y="75" width="50" height="30" rx="5" fill="#74B9FF" stroke="#2C3E50" stroke-width="2"/>
  <rect x="160" y="75" width="50" height="30" rx="5" fill="#74B9FF" stroke="#2C3E50" stroke-width="2"/>
  <rect x="220" y="75" width="50" height="30" rx="5" fill="#74B9FF" stroke="#2C3E50" stroke-width="2"/>
  <rect x="280" y="75" width="50" height="30" rx="5" fill="#74B9FF" stroke="#2C3E50" stroke-width="2"/>
  
  <!-- Wheels -->
  <circle cx="70" cy="160" r="20" fill="#2C3E50"/>
  <circle cx="330" cy="160" r="20" fill="#2C3E50"/>
  
  <!-- Door -->
  <rect x="30" y="110" width="25" height="40" rx="3" fill="#E74C3C" stroke="#2C3E50" stroke-width="2"/>
  
  <!-- Front -->
  <rect x="{width-25}" y="90" width="15" height="60" rx="8" fill="#34495E"/>
  
  <text x="{width//2}" y="{height-10}" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold" fill="#2C3E50">{name}</text>
</svg>'''

def generate_airplane_svg(color, width, height, name):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <!-- Fuselage -->
  <ellipse cx="200" cy="75" rx="150" ry="25" fill="{color}" stroke="#2C3E50" stroke-width="3"/>
  
  <!-- Wings -->
  <rect x="120" y="65" width="160" height="20" rx="10" fill="#95A5A6" stroke="#2C3E50" stroke-width="2"/>
  
  <!-- Tail -->
  <polygon points="50,75 20,60 20,90" fill="#95A5A6" stroke="#2C3E50" stroke-width="2"/>
  <polygon points="40,45 30,30 50,75" fill="#95A5A6" stroke="#2C3E50" stroke-width="2"/>
  
  <!-- Cockpit -->
  <ellipse cx="320" cy="75" rx="30" ry="20" fill="#74B9FF" stroke="#2C3E50" stroke-width="2"/>
  
  <!-- Windows -->
  <circle cx="280" cy="75" r="8" fill="#74B9FF"/>
  <circle cx="250" cy="75" r="8" fill="#74B9FF"/>
  <circle cx="220" cy="75" r="8" fill="#74B9FF"/>
  
  <text x="{width//2}" y="{height-10}" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold" fill="#2C3E50">{name}</text>
</svg>'''

def darker_color(hex_color):
    """Make a color darker"""
    return hex_color.replace('FF', 'CC').replace('4E', '3A').replace('6B', '55')

# Generate all vehicle SVGs
for filename, props in vehicles.items():
    if 'car' in filename:
        svg_content = generate_car_svg(props['color'], props['width'], props['height'], props['name'])
    elif 'bus' in filename:
        svg_content = generate_bus_svg(props['color'], props['width'], props['height'], props['name'])
    elif 'airplane' in filename:
        svg_content = generate_airplane_svg(props['color'], props['width'], props['height'], props['name'])
    else:
        # Use car template for other vehicles with different colors
        svg_content = generate_car_svg(props['color'], props['width'], props['height'], props['name'])
    
    filepath = f"/Users/szioni/Documents/myProjects/clipFactory/assets/vehicles/{filename}"
    with open(filepath, 'w') as f:
        f.write(svg_content)
    
    print(f"Generated: {filename}")

print("\n🎨 Generated placeholder vehicle SVG files!")
print("These are basic placeholders - replace with high-quality vehicle images for production.")