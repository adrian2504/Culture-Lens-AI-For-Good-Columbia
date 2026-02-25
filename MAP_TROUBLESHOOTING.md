# Map Troubleshooting Guide

## Issue: Map not showing or pins not clickable

### Quick Fixes

#### 1. Test the Map Standalone
Open this URL in your browser while the webapp is running:
```
http://localhost:3000/test-map.html
```

This is a simple HTML test file that verifies:
- SVG pins render correctly
- Hover effects work
- Click events fire
- Console logging works

If this works, the issue is with React integration. If it doesn't work, it's a browser/CSS issue.

#### 2. Check Browser Console
Open Developer Tools (F12) and check the Console tab for:
- Any JavaScript errors
- "Map component rendered" log messages
- "Pin hovered" log messages when hovering
- "Landmark clicked" log messages when clicking

#### 3. Verify the Map Route
1. Start the webapp: `npm start` in the webapp folder
2. Open http://localhost:3000
3. Click "Explore Map" button
4. Check if you see:
   - "Explore World Heritage" title
   - A blue-tinted rectangle (the map background)
   - Red pins on the map
   - Grid lines

#### 4. Check if Backend is Running
The map itself doesn't need the backend, but clicking pins does:
```bash
# In backend folder
source venv/bin/activate
python main.py
```

Should see: `INFO: Uvicorn running on http://0.0.0.0:8000`

#### 5. Clear Browser Cache
Sometimes React's hot reload doesn't update properly:
1. Hard refresh: Ctrl+Shift+R (Windows/Linux) or Cmd+Shift+R (Mac)
2. Or clear cache in DevTools: Network tab → Disable cache checkbox

#### 6. Restart the Dev Server
```bash
# Stop the webapp (Ctrl+C)
# Then restart
cd webapp
npm start
```

### Debugging Steps

#### Step 1: Verify Map Component Loads
Open browser console and look for:
```
Map component rendered, landmarks: 13
Hovered landmark: null
```

If you don't see this, the Map component isn't loading.

#### Step 2: Test Pin Hover
Hover over where pins should be (even if you can't see them). Check console for:
```
Pin hovered: taj_mahal
```

If you see this, pins are there but might not be visible (CSS issue).

#### Step 3: Test Pin Click
Click where pins should be. Check console for:
```
Landmark clicked: {id: 'taj_mahal', name: 'Taj Mahal', ...}
```

If you see this, clicks work but navigation might be broken.

### Common Issues

#### Issue: Map is completely blank
**Cause**: CSS not loading or SVG not rendering
**Fix**: 
1. Check if `Map.css` exists in `webapp/src/pages/`
2. Verify import in `Map.js`: `import './Map.css';`
3. Hard refresh browser (Ctrl+Shift+R)

#### Issue: Pins are too small or invisible
**Cause**: SVG scaling or viewBox issues
**Fix**: The pins are scaled in SVG units. They should be visible at:
- Pin size: 2.5 units tall in a 100x60 viewBox
- This scales proportionally with the SVG container

Try zooming in your browser (Ctrl/Cmd +) to see if pins appear.

#### Issue: Pins visible but not clickable
**Cause**: CSS `pointer-events` or z-index issues
**Fix**: Already fixed in the code with:
```javascript
style={{ pointerEvents: 'all' }}
```

If still not working, check if another element is overlaying the SVG.

#### Issue: Hover works but click doesn't navigate
**Cause**: Navigation function not working
**Fix**: Check console for errors. Verify `navigateTo` prop is passed from App.js.

#### Issue: Clicks navigate but Result page shows error
**Cause**: Backend not running or wrong landmark ID
**Fix**: 
1. Start backend: `python backend/main.py`
2. Check landmark IDs match backend data
3. Verify API URL in Result.js: `http://localhost:8000`

### Visual Debugging

#### Add Visible Borders
Temporarily add to `Map.css`:
```css
.world-map {
  border: 5px solid red !important;
}

.map-svg {
  border: 3px solid yellow !important;
}

.landmark-pin {
  outline: 2px solid lime !important;
}
```

This will show you exactly where elements are positioned.

#### Make Pins Huge (Temporary)
In `Map.js`, change the transform scale:
```javascript
transform={`translate(${landmark.x}, ${landmark.y}) scale(3)`}
```

This makes pins 3x larger so you can definitely see them.

### Expected Behavior

#### What You Should See:
1. **Map Container**: Dark gradient background (navy to slate)
2. **Map Card**: Lighter glassmorphism card with blur effect
3. **Map Background**: Blue-tinted rectangle (the "ocean")
4. **Grid Lines**: White lines forming a cross
5. **Pins**: 13 red teardrop-shaped pins with white dots
6. **Pulse Rings**: Animated circles around each pin

#### What Should Happen on Hover:
1. Pin scales up 1.4x
2. Pin gets red glow effect
3. Info card appears above pin
4. Card shows landmark name and country
5. Console logs "Pin hovered: [id]"

#### What Should Happen on Click:
1. Console logs "Landmark clicked: [object]"
2. Page navigates to Result page
3. Result page loads with "Local" lens
4. Shows cultural perspectives for that landmark

### Still Not Working?

#### Check File Structure
Verify these files exist:
```
webapp/
├── src/
│   ├── pages/
│   │   ├── Map.js ✓
│   │   └── Map.css ✓
│   └── App.js ✓
└── public/
    └── test-map.html ✓
```

#### Check for Typos
Common typos that break things:
- `navigateTo` vs `navigateto`
- `objectId` vs `object_id`
- `landmark.id` vs `landmark.objectId`

#### Nuclear Option: Rebuild
```bash
cd webapp
rm -rf node_modules package-lock.json
npm install
npm start
```

### Getting Help

If still not working, provide:
1. Browser console output (all messages)
2. Network tab (any failed requests?)
3. Screenshot of what you see
4. Output of `npm start` command
5. Browser and version (Chrome 120, Firefox 121, etc.)

### Success Indicators

✅ Map loads with blue background
✅ 13 red pins visible
✅ Pins pulse with animation
✅ Hover shows info card
✅ Click navigates to Result page
✅ Result page loads landmark data
✅ No console errors

If all these work, the map is functioning correctly!
