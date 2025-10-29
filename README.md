# DungeonCLI 🧙‍♂️

**DungeonCLI** is a lightweight, text-based dungeon generator built in Python.  
It started as an experiment in **“vibe coding”** — using ChatGPT collaboratively to explore ideas, prototype quickly, and lean into creative flow rather than rigid specs.

## 🎯 Project Goal
To create an old-school ASCII dungeon generator that can later evolve into a deeper exploration of procedural generation, roguelike logic, and world-building systems. Think early Apple II or mainframe-era adventure games, built with modern tooling and curiosity.

## 💡 Origin
This project was developed as an **experiment with ChatGPT** — intentionally blending human intuition and AI-assisted iteration.  
The goal wasn’t just to write code, but to test a new *creative workflow* where AI acts as a co-pilot for ideation, structure, and documentation.

## 🧩 Current Features
- Procedural ASCII map generation  
- Randomized room placement and simple connectivity  
- Basic loot and monster placement  
- Command-line interface with room reveal and exploration logic  

## 🏗️ Planned Next Steps
- Add player movement and fog-of-war
- Introduce combat and item systems
- Explore saving/loading maps
- Eventually add a Flask-based “Dungeon Master” view or editor

## 🛠️ Setup
```bash
git clone https://github.com/<your-username>/DungeonCLI.git
cd DungeonCLI
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python dungeon_cli.py
```

## 🤖 Acknowledgements

Built collaboratively by Eric McEntee and ChatGPT (GPT-5)
as an exploration of AI-assisted creativity, hands-on experimentation,
and a love for retro ASCII adventures.