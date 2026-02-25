# CultureLens - Testing Checklist

Use this checklist to verify all features are working correctly.

## ✅ Pre-Flight Checks

### Backend
- [ ] Virtual environment activated: `source backend/venv/bin/activate`
- [ ] Backend running: `python backend/main.py`
- [ ] Backend accessible: Open http://localhost:8000 in browser
- [ ] Should see: `{"message":"CultureLens API","status":"running"}`

### Web App
- [ ] Dependencies installed: `npm install` in webapp folder
- [ ] Web app running: `npm start` in webapp folder
- [ ] Web app opens: http://localhost:3000
- [ ] Video background loads (if video file is in place)

## 🗺️ Interactive Map Testing

### Map Display
- [ ] Click "Explore Map" button on home page
- [ ] Map loads with blue gradient background
- [ ] 13 red pins are visible on the map
- [ ] Pins have pulse animation effect
- [ ] "Back" button is visible in top-left

### Map Interactions
- [ ] Hover over any pin
- [ ] Info card appears above the pin
- [ ] Card shows landmark name and country
- [ ] Pin scales up and bounces on hover
- [ ] Card disappears when mouse leaves

### Map Navigation
- [ ] Click on "Taj Mahal" pin
- [ ] Navigates to Result page
- [ ] Shows Taj Mahal information
- [ ] Cultural lenses are available
- [ ] Click "Back" button returns to map

### Test All Landmarks
Test at least 3 different landmarks:
- [ ] Taj Mahal (India) - x: 72%, y: 52%
- [ ] Eiffel Tower (France) - x: 48%, y: 35%
- [ ] Statue of Liberty (USA) - x: 22%, y: 38%
- [ ] Pyramids of Giza (Egypt) - x: 52%, y: 48%
- [ ] Great Wall (China) - x: 78%, y: 38%

## 📸 Camera/Upload Testing

### Upload Flow
- [ ] Click "Scan Landmark" on home page
- [ ] Camera page loads
- [ ] "Upload Image" button is visible
- [ ] Click "Upload Image"
- [ ] File picker opens
- [ ] Select an image of a landmark
- [ ] Image uploads and processes
- [ ] Navigates to Result page
- [ ] Shows recognized landmark

### Live Capture Flow
- [ ] Click "Capture Live" button
- [ ] Browser asks for camera permission
- [ ] Grant camera permission
- [ ] Live video feed appears
- [ ] Click "Capture Photo" button
- [ ] Photo is captured
- [ ] Image processes
- [ ] Navigates to Result page

### Test with Known Landmarks
Upload images of these landmarks to test recognition:
- [ ] Statue of Liberty
- [ ] Eiffel Tower
- [ ] Taj Mahal
- [ ] Colosseum
- [ ] Great Wall of China

## 🌍 Cultural Perspectives Testing

### Lens Switching
- [ ] Result page shows 4 lens buttons
- [ ] "Local" lens is selected by default
- [ ] Click "Asian" lens
- [ ] Content updates with Asian perspective
- [ ] Click "European" lens
- [ ] Content updates with European perspective
- [ ] Click "Indigenous" lens
- [ ] Content updates with Indigenous perspective
- [ ] Active lens is highlighted

### Content Display
For each lens, verify:
- [ ] Narrative text is displayed
- [ ] Narrative is different for each lens
- [ ] Text is readable and well-formatted
- [ ] No loading errors

## 📊 Additional Features Testing

### Historical Facts
- [ ] "Historical Facts" section is visible
- [ ] Shows landmark name
- [ ] Shows location
- [ ] Shows year built
- [ ] Shows significance
- [ ] Shows architectural style

### Bias Transparency
- [ ] "Bias Transparency" section is visible
- [ ] Shows source dominance
- [ ] Shows missing perspectives
- [ ] Shows power imbalances
- [ ] Shows representation gaps
- [ ] Shows diversity score

### Community Sentiment
- [ ] "Community Sentiment" section is visible
- [ ] Shows emotional responses
- [ ] Shows common themes
- [ ] Shows visitor quotes
- [ ] Shows reflection count

## 🎨 UI/UX Testing

### Home Page
- [ ] Video background plays (if video file exists)
- [ ] Video loops continuously
- [ ] Overlay is visible (45% black)
- [ ] "CultureLens" title is visible
- [ ] "Scan Landmark" button works
- [ ] "Explore Map" button works
- [ ] Feature cards are displayed
- [ ] Landmark showcase is visible

### Responsive Design
Test on different screen sizes:
- [ ] Desktop (1920x1080)
- [ ] Laptop (1366x768)
- [ ] Tablet (768x1024)
- [ ] Mobile (375x667)

### Animations
- [ ] Buttons have hover effects
- [ ] Pins pulse on the map
- [ ] Lens buttons animate on click
- [ ] Page transitions are smooth
- [ ] No janky animations

## 🔧 Error Handling

### Backend Errors
- [ ] Backend stops: Web app shows error message
- [ ] Invalid image: Shows appropriate error
- [ ] Unknown landmark: Falls back to AI recognition

### Network Errors
- [ ] Slow connection: Shows loading state
- [ ] No connection: Shows error message
- [ ] Timeout: Shows retry option

## 🚀 Performance Testing

### Load Times
- [ ] Home page loads in < 2 seconds
- [ ] Map page loads in < 2 seconds
- [ ] Image upload processes in < 5 seconds
- [ ] Lens switching is instant (< 1 second)

### Memory Usage
- [ ] No memory leaks after 10 lens switches
- [ ] Video doesn't cause performance issues
- [ ] Map interactions remain smooth

## 🐛 Known Issues to Check

### Video Background
- [ ] Video file must be at: `webapp/public/video/Culture Lens.mp4`
- [ ] If missing, background will be black
- [ ] Video should be named exactly "Culture Lens.mp4"

### Camera Permissions
- [ ] Browser must support getUserMedia API
- [ ] HTTPS or localhost required for camera access
- [ ] User must grant camera permission

### API Key
- [ ] OpenAI API key must be in `backend/.env`
- [ ] Key must be valid and have credits
- [ ] Check key format: `sk-proj-...`

## ✅ Final Verification

### Complete User Journey 1: Map Exploration
1. [ ] Start on home page
2. [ ] Click "Explore Map"
3. [ ] Hover over 3 different pins
4. [ ] Click on Taj Mahal
5. [ ] Switch between all 4 lenses
6. [ ] Scroll through all sections
7. [ ] Click "Back to Home"
8. [ ] Returns to home page

### Complete User Journey 2: Image Upload
1. [ ] Start on home page
2. [ ] Click "Scan Landmark"
3. [ ] Click "Upload Image"
4. [ ] Upload Statue of Liberty photo
5. [ ] Wait for recognition
6. [ ] View result page
7. [ ] Switch between lenses
8. [ ] Read bias transparency
9. [ ] Read community sentiment
10. [ ] Click "Back to Home"

### Complete User Journey 3: Live Capture
1. [ ] Start on home page
2. [ ] Click "Scan Landmark"
3. [ ] Click "Capture Live"
4. [ ] Grant camera permission
5. [ ] See live feed
6. [ ] Capture photo
7. [ ] View result page
8. [ ] Explore all sections

## 📝 Test Results

Date: _______________
Tester: _______________

### Summary
- Total tests: 100+
- Passed: _____
- Failed: _____
- Skipped: _____

### Critical Issues Found
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

### Minor Issues Found
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

### Notes
_______________________________________________
_______________________________________________
_______________________________________________

## 🎯 Ready for Demo?

All critical features working:
- [ ] Map loads and is interactive
- [ ] Image upload works
- [ ] AI recognition works
- [ ] Cultural lenses work
- [ ] All sections display correctly
- [ ] No critical errors

If all checked: **✅ READY FOR DEMO!**
