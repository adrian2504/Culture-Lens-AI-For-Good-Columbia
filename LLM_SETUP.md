# LLM Integration Guide

## Current Status
By default, CultureLens uses **hardcoded interpretations** for fast demos. You can optionally enable LLM-powered dynamic interpretations.

## Why Hardcoded Works for MVP
- Instant responses (no API latency)
- No API costs
- Predictable output for demos
- Shows the concept clearly

## When to Use LLM
- Need dynamic interpretations for new landmarks
- Want to handle user questions
- Scale to 100+ monuments
- Community-contributed perspectives

---

## Option 1: OpenAI (Recommended for Hackathon)

### Setup
```bash
cd backend
pip install openai python-dotenv
```

### Configure
```bash
# Create .env file
echo "USE_LLM=true" > .env
echo "LLM_PROVIDER=openai" >> .env
echo "OPENAI_API_KEY=sk-your-key-here" >> .env
```

### Run
```bash
python main.py
```

**Cost**: ~$0.001 per interpretation (GPT-4o-mini)

---

## Option 2: Anthropic Claude

### Setup
```bash
pip install anthropic
```

### Configure
```bash
echo "USE_LLM=true" > .env
echo "LLM_PROVIDER=anthropic" >> .env
echo "ANTHROPIC_API_KEY=sk-ant-your-key-here" >> .env
```

**Cost**: ~$0.003 per interpretation (Claude 3.5 Sonnet)

---

## Option 3: Local LLM (Free, Private)

### Install Ollama
```bash
# macOS/Linux
curl -fsSL https://ollama.com/install.sh | sh

# Or download from https://ollama.com
```

### Pull Model
```bash
ollama pull llama3.2
# or
ollama pull mistral
```

### Configure
```bash
echo "USE_LLM=true" > .env
echo "LLM_PROVIDER=local" >> .env
```

### Run
```bash
# Terminal 1: Start Ollama
ollama serve

# Terminal 2: Start backend
python main.py
```

**Cost**: Free, runs on your machine

---

## Comparison

| Provider | Cost | Speed | Quality | Privacy |
|----------|------|-------|---------|---------|
| Hardcoded | Free | Instant | Good | Perfect |
| OpenAI | $0.001/req | Fast | Excellent | Cloud |
| Anthropic | $0.003/req | Fast | Excellent | Cloud |
| Local (Ollama) | Free | Medium | Good | Perfect |

---

## Testing LLM Integration

### 1. Check it's working
```bash
curl -X POST http://localhost:8000/interpret \
  -H "Content-Type: application/json" \
  -d '{
    "object_id": "taj_mahal",
    "cultural_lens": "local"
  }'
```

Look for `"generated_by": "openai/gpt-4o-mini"` in response

### 2. Try different lenses
```bash
# Asian perspective
curl -X POST http://localhost:8000/interpret \
  -H "Content-Type: application/json" \
  -d '{"object_id": "colosseum", "cultural_lens": "asian"}'

# Indigenous perspective
curl -X POST http://localhost:8000/interpret \
  -H "Content-Type: application/json" \
  -d '{"object_id": "taj_mahal", "cultural_lens": "indigenous"}'
```

---

## Switching Between Modes

### Demo Mode (Hardcoded)
```bash
# Remove or set to false
echo "USE_LLM=false" > .env
```

### LLM Mode
```bash
echo "USE_LLM=true" > .env
```

Restart backend after changing.

---

## Advanced: Custom Prompts

Edit `backend/agents/llm_cultural_agent.py` to customize prompts:

```python
def _build_prompt(self, object_id: str, lens: str, facts: dict) -> str:
    # Add your custom instructions here
    lens_instructions = {
        "local": "Your custom local perspective prompt...",
        "asian": "Your custom Asian perspective prompt...",
        # etc.
    }
```

---

## Troubleshooting

### "No module named 'openai'"
```bash
pip install openai python-dotenv
```

### "Invalid API key"
Check your `.env` file has correct key format

### Ollama connection refused
```bash
# Start Ollama first
ollama serve
```

### Slow responses with local LLM
- Use smaller model: `ollama pull llama3.2:1b`
- Or stick with hardcoded for demos

---

## Recommendation for Hackathon

**Use hardcoded mode** for demos—it's faster and more reliable. Mention LLM integration as "production-ready feature" in your pitch.

If judges ask about scalability, show them this file and explain:
- MVP uses curated interpretations for quality
- LLM integration ready for dynamic scaling
- Can switch with one environment variable
