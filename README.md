# CultureLens - See What Others See

<div align="center">

**An AI-powered platform that transforms how we experience cultural heritage by revealing multiple perspectives on the same monument, artwork, or historical site.**

</div>

---

## The Problem

I love visiting museums, historical places, and religious sites. But when I walk through places like Washington Square Park and see names like Giuseppe Garibaldi or Sybil Ludington, I often wonder who they are. While these figures may be well known within the local culture and history, someone like me, who isn't from here, may not understand their significance or the role they played, and as a result, the importance of the sculpture can be lost.

On the other hand, if I learn more about who this person was, what they stood for, or how their story connects to my own culture or experiences, I can engage with the artwork on a much deeper level. That context transforms the sculpture from something I simply pass by into something I can truly understand and appreciate.

**Today's digital guides and AI systems present culture through a single dominant narrative**, often shaped by historical power imbalances, colonial perspectives, or limited datasets. This risks reducing rich, living cultures into simplified explanations and unintentionally marginalizing voices that do not fit a "standard" interpretation.

##  My Solution

**CultureLens** is an AI-agent based computer vision application designed to transform how people experience art, monuments, and cultural heritage by **embracing diversity as a source of knowledge** rather than a problem of cultural barriers.

By combining edge-based computer vision, agent-driven AI reasoning, and community-informed perspectives, CultureLens allows users to point their camera at a painting or monument and receive explanations through **multiple cultural lenses**. These lenses reflect how people from different backgrounds—such as local communities, religious traditions, or regional cultures—interpret meaning, emotion, and historical significance differently.

**Rather than asking "What is the correct explanation?", CultureLens asks: "How do different people understand the same heritage, and why?"**

This shift is the core of our **AI for Good** mission.

---

## Why CultureLens exists (the non-tech reason)

Cultural heritage isn’t just architecture, dates, and Wikipedia summaries. It’s identity, memory, power, and lived experience — and different communities will interpret the same landmark in genuinely different ways.

So CultureLens tries to answer:

What does this landmark mean locally to the people who live near it?

How might it be framed through a European historical/architectural lens?

What changes when you interpret it from an Asian lens (craft, ancestry, spirituality, continuity)?

How does an Indigenous lens shift the story toward land, sacredness, and traditional knowledge?

Instead of hiding the disagreement, CultureLens highlights it. And instead of pretending the system is “neutral,” it shows the user what sources dominate and what perspectives are under-represented.

----- 

## Features

### AI-Powered Recognition
- **GPT-4o Vision API** for accurate landmark and monument identification
- Real-time image analysis with confidence scoring
- Support for 13+ world heritage sites (expandable)

### Multiple Cultural Perspectives
- **5 AI Agents** working together to provide diverse viewpoints:
  - **Vision Agent**: Identifies landmarks using computer vision
  - **Knowledge Agent**: Provides historical facts and context
  - **Cultural Agent**: Interprets significance through different cultural lenses (Local, Western, Eastern, Indigenous)
  - **Bias Agent**: Reveals historical biases and power dynamics
  - **Community Agent**: Shares visitor experiences and emotional responses

### Interactive World Map
- Explore 13 world heritage sites on a realistic map
- Accurate geographic positioning with OpenStreetMap
- Click any marker to dive into cultural analysis

### Multilingual Audio Narration
- **10 languages supported**: English, Spanish, Hindi, Italian, French, German, Portuguese, Chinese, Japanese, Arabic
- AI-powered translation using OpenAI GPT-4o-mini
- Natural voice synthesis with ElevenLabs multilingual TTS
- Listen to cultural perspectives in your preferred language

### Bias Transparency
- Exposes colonial narratives and historical power imbalances
- Highlights marginalized perspectives
- Promotes critical thinking about cultural heritage

### Community Insights
- Aggregated visitor emotions and themes
- Real quotes from diverse perspectives
- Crowdsourced cultural understanding

---

## Quick Start

### Prerequisites

- **Python 3.9+**
- **Node.js 16+** and npm
- **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))
- **ElevenLabs API Key** ([Get one here](https://elevenlabs.io/)) - Optional, for audio features



###  Start Exploring!

1. **Scan a Landmark**: Click "Scan Landmark" and upload an image
2. **Choose a Lens**: Select Local, Western, Eastern, or Indigenous perspective
3. **Listen**: Choose a language and hear the narration
4. **Explore Map**: Browse 13 world heritage sites on the interactive map

---

## Architecture

### Multi-Agent AI System

```
┌─────────────────────────────────────────────────────────────┐
│                     CultureLens Platform                     │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Vision Agent │  │Knowledge Agent│  │Cultural Agent│      │
│  │  (GPT-4o)    │→ │  (GPT-4o-mini)│→ │ (GPT-4o-mini)│      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│         ↓                  ↓                  ↓              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Bias Agent  │  │Community Agent│  │  Audio Agent │      │
│  │(GPT-4o-mini) │  │ (GPT-4o-mini) │  │ (ElevenLabs) │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Tech Stack

**Backend:**
- FastAPI (Python web framework)
- OpenAI GPT-4o & GPT-4o-mini (Vision & Language models)
- ElevenLabs API (Text-to-speech with translation)
- Pydantic (Data validation)

**Frontend:**
- React 18 (UI framework)
- Leaflet.js (Interactive maps)
- Axios (API communication)
- CSS3 (Styling with gradients and animations)

**Data:**
- JSON-based landmark database
- Community sentiment data
- Historical bias annotations

---

## Supported Landmarks

Currently supporting 13 world heritage sites:

🇮🇳 Taj Mahal | 🇫🇷 Eiffel Tower | 🇺🇸 Statue of Liberty | 🇮🇹 Colosseum
🇨🇳 Great Wall | 🇪🇬 Pyramids of Giza | 🇵🇪 Machu Picchu | 🇧🇷 Christ the Redeemer
🇬🇧 Big Ben | 🇬🇧 Stonehenge | 🇬🇷 Acropolis | 🇯🇴 Petra | 🇰🇭 Angkor Wat

*Easily expandable by adding entries to `backend/data/landmarks.json`*

---

## Cultural Lenses

### Local Perspective
Understanding through the eyes of the community where the heritage exists

### Western Perspective
Historical and academic interpretation from Western scholarship

### Eastern Perspective
Philosophical and cultural understanding from Eastern traditions

### Indigenous Perspective
Original narratives and spiritual significance from indigenous peoples

---


## Use Cases

### Education
- Students learning about world history from multiple perspectives
- Teachers presenting diverse cultural viewpoints in classrooms

### Tourism
- Travelers gaining deeper understanding of monuments they visit
- Tour guides offering multilingual, multi-perspective narratives

### Museums
- Interactive exhibits that adapt to visitor backgrounds
- Accessibility features for diverse audiences

### Research
- Scholars studying how cultural heritage is interpreted differently
- Bias detection in historical narratives

---

1. **Add New Landmarks**: Expand our database with more heritage sites
2. **Improve Cultural Lenses**: Enhance perspective accuracy and depth
3. **Add Languages**: Support more languages for audio narration
4. **Fix Bugs**: Report and fix issues
5. **Improve Documentation**: Help others understand and use CultureLens



## Acknowledgments

- **OpenAI** for GPT-4o and GPT-4o-mini models
- **ElevenLabs** for multilingual text-to-speech technology
- **OpenStreetMap** contributors for map data
- **VibeFlow** main idea and content flow
- **Kiro** for development
- **Cultural heritage communities** worldwide for inspiring this project

---

## Contact

**Project Maintainer**: [Adrian Dsouza]
- Email: ad7628@nyu.edu
- GitHub: [@adrian2504](https://github.com/adrian2504)

