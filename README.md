# 🚗 Transport World - Kids Video Generator

An automated kids video generator built with **PixiJS** that creates engaging animated presentations about transportation vehicles. The system reads JSON scripts and generates interactive educational content with text-to-speech narration, smooth animations, and hide-and-seek gameplay elements.

![Transport World Demo](https://img.shields.io/badge/Status-Ready%20to%20Use-brightgreen)
![PixiJS](https://img.shields.io/badge/PixiJS-v8.0.0-blue)
![No Dependencies](https://img.shields.io/badge/Dependencies-None-green)

## ✨ Features

### 🎭 **Interactive Animations**
- **Hide & Seek Gameplay** - Vehicles hide behind clouds before "Where is the...?" questions
- **Dramatic Reveals** - Bouncing animations when vehicles reappear for "Here is the...!" 
- **Smooth Transitions** - Vehicles slide in from off-screen with easing effects
- **Idle Animations** - Gentle floating, breathing, and swaying during narration

### 🗣️ **Text-to-Speech Integration**
- **Web Speech API** - Built-in browser text-to-speech
- **Child-Friendly Voices** - Automatically selects appropriate voices
- **Adjustable Speed** - Slower pace perfect for toddlers
- **Multi-Language Support** - Ready for localization

### 🎵 **Audio System**
- **Background Music** - Loops soft instrumental music during presentation
- **Smart Volume Control** - Music at 30% volume for clear narration
- **Graceful Fallbacks** - Works perfectly with or without music files

### 🖼️ **Flexible Asset System**
- **PNG Image Support** - High-quality vehicle images with transparency
- **SVG Fallbacks** - Vector graphics for crisp scaling
- **Smart Loading** - Automatic fallback chain: PNG → SVG → Graphics
- **Easy Replacement** - Drop new images in `/assets/vehicles/` folder

## 🚀 Quick Start

### 1. **Clone & Run**
```bash
git clone [repository-url]
cd clipFactory
python3 -m http.server 8000
```

### 2. **Open in Browser**
Navigate to: `http://localhost:8000/transportWorld.html`

### 3. **Click "Start Adventure!"**
The presentation will automatically begin with all 7 vehicles.

## 📁 Project Structure

```
clipFactory/
├── transportWorld.html          # Main application (HTML + JS + CSS)
├── scripts/
│   └── transport_episode_1.json # Episode script with 7 vehicles
├── assets/
│   └── vehicles/               # Vehicle images (PNG/SVG)
│       ├── car.png            # (You can replace with your images)
│       ├── bus.png
│       ├── train.png
│       ├── airplane.png
│       ├── police_car.png
│       ├── fire_truck.png
│       └── ambulance.png
├── music/
│   └── classic_soft.mp3       # Background music (optional)
└── README.md
```

## 🎯 Vehicle List

The current episode includes these 7 transportation vehicles:

1. 🚗 **Car** - Family vehicle
2. 🚌 **Bus** - School bus  
3. 🚂 **Train** - Locomotive
4. ✈️ **Airplane** - Passenger jet
5. 🚔 **Police Car** - Emergency vehicle
6. 🚒 **Fire Truck** - Fire engine
7. 🚑 **Ambulance** - Medical emergency vehicle

## 🛠️ Customization

### **Adding New Vehicles**
1. Add vehicle image to `/assets/vehicles/[name].png`
2. Update `transport_episode_1.json`:
```json
{
  "id": "helicopter_intro",
  "object": "helicopter",
  "image": "assets/vehicles/helicopter.png",
  "text": [
    "Helicopter",
    "Where is the helicopter?", 
    "Here is the helicopter!",
    "Goodbye helicopter!"
  ]
}
```

### **Changing Voices**
Modify the `preferredVoices` array in `transportWorld.html`:
```javascript
const preferredVoices = [
    'Google UK English Female',
    'Microsoft Zira',
    'Your Preferred Voice'
];
```

### **Adjusting Animation Speed**
Update timing values in the animation functions:
- `duration` - Animation length
- `setTimeout()` delays - Pause between actions
- `utterance.rate` - Speech speed

### **Adding Background Music**
1. Place MP3 file at: `/music/classic_soft.mp3`
2. Or update the path in `transport_episode_1.json`

## 🎨 Asset Requirements

### **Vehicle Images**
- **Format**: PNG with transparent background (preferred)
- **Size**: 300-450px wide, 150-200px tall
- **Style**: Colorful, cartoon-like, child-friendly
- **Orientation**: Side view (profile), facing right

### **Background Music**
- **Format**: MP3 (best compatibility)
- **Duration**: 3+ minutes (loops automatically)
- **Style**: Soft instrumental, no lyrics
- **Volume**: App automatically sets to 30%

## 🌟 Educational Benefits

- **Object Permanence** - Hide-and-seek teaches that objects exist when hidden
- **Vocabulary Building** - Repeated vehicle names and questions
- **Visual Recognition** - Colorful, detailed vehicle illustrations  
- **Anticipation & Surprise** - Engaging reveal animations
- **Auditory Learning** - Clear pronunciation and pacing

## 🔧 Technical Details

### **Built With**
- **PixiJS v8** - High-performance 2D graphics
- **Web Speech API** - Cross-browser text-to-speech
- **HTML5 Audio** - Background music support
- **Pure JavaScript** - No frameworks or build process required

### **Browser Support**
- ✅ Chrome 80+
- ✅ Firefox 75+
- ✅ Safari 13+
- ✅ Edge 80+

### **Performance**
- Lightweight (~500KB total)
- 60 FPS animations
- Instant loading on modern browsers
- Mobile-friendly responsive design

## 🎪 Demo Flow

1. **Welcome Screen** - Colorful title with pulsing start button
2. **Vehicle Introduction** - Each vehicle slides in dramatically
3. **Hide Animation** - Cloud covers vehicle before question
4. **Question Phase** - "Where is the [vehicle]?" with suspense
5. **Reveal Animation** - Vehicle bounces back with celebration
6. **Confirmation** - "Here is the [vehicle]!" with excitement
7. **Farewell** - "Goodbye [vehicle]!" before next scene
8. **Celebration** - Confetti animation when all vehicles complete

## 🔄 Future Enhancements

### **Planned Features**
- [ ] Multiple episode support
- [ ] Interactive clicking (repeat words)
- [ ] Sound effects for each vehicle
- [ ] Different backgrounds per scene
- [ ] Subtitle/text display options
- [ ] Video export functionality
- [ ] Multiple language support
- [ ] Parent dashboard with progress tracking

### **Advanced Animations**
- [ ] Vehicle-specific movements (plane flying, train wheels)
- [ ] Weather effects (rain, snow)  
- [ ] Day/night backgrounds
- [ ] Seasonal themes
- [ ] Interactive hotspots

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **PixiJS Team** - For the amazing graphics library
- **Web Speech API** - For cross-browser text-to-speech
- **Educational Inspiration** - Montessori and early childhood learning principles
- **Kids Everywhere** - The real judges of what makes content engaging!

---

**Made with ❤️ for kids learning about the world around them** 🌟

*Ready to create magical learning experiences? Clone this repo and start customizing!*