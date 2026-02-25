# Quick Map Test Guide

## 🚀 Fast Test (30 seconds)

### 1. Start the App
```bash
# Terminal 1 - Backend
cd backend && source venv/bin/activate && python main.py

# Terminal 2 - Webapp
cd webapp && npm start
```

### 2. Test Standalone HTML
Open: http://localhost:3000/test-map.html

**✅ Should see**: 3 red pins you can hover and click

**❌ If not working**: Browser/CSS issue - check browser console

### 3. Test React Map
Open: http://localhost:3000

Click "Explore Map"

**✅ Should see**:
- Blue-tinted map background
- 13 red pins with pulse animations
- Info cards on hover
- Navigation on click

**❌ If not working**: Run diagnostic tool

### 4. Run Diagnostic
Open: http://localhost:3000/map-diagnostic.html

Click "Add Test Pins" button

**✅ All tests should pass** (green checkmarks)

## 🔍 Quick Debug

### Open Browser Console (F12)
Look for these logs:
```
Map component rendered, landmarks: 13
Pin hovered: taj_mahal
Landmark clicked: {id: 'taj_mahal', ...}
```

### No logs?
- Map component not loading
- Check App.js has Map import
- Hard refresh: Ctrl+Shift+R

### Logs but no pins visible?
- CSS not loading
- Check Map.css exists
- Clear cache and refresh

### Pins visible but not clickable?
- Already fixed with pointerEvents
- Try diagnostic tool
- Check for overlaying elements

## 📋 Checklist

- [ ] Backend running on port 8000
- [ ] Webapp running on port 3000
- [ ] test-map.html shows 3 pins
- [ ] Diagnostic tool all green
- [ ] React map shows 13 pins
- [ ] Hover shows info cards
- [ ] Click navigates to Result
- [ ] No console errors

## 🎯 Expected Behavior

**Map loads**: Blue background, white grid, 13 red pins
**Hover pin**: Scales up, glows red, shows info card
**Click pin**: Navigates to Result page with cultural perspectives

## 🆘 Still Broken?

1. Check MAP_TROUBLESHOOTING.md
2. Run map-diagnostic.html
3. Copy console output
4. Check Network tab for failed requests

## ✨ Success!

If you see the map with clickable pins, you're all set! 🎉

The map is now fully functional and ready to demo.
