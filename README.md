# 2D Dungeon Crawler

A 2D dungeon crawler developed using **Python and Pygame**, featuring enemy AI, combat mechanics, interactive environments, inventory management, and data-driven dungeon generation.

This project is currently **in active development** and focuses on applying object-oriented programming, modular software architecture, and game development algorithms.

## Features

### Player Movement and Combat
- Four-directional player movement with sprite animations.
- Collision detection against walls, structures, and interactive objects.
- Player health, attack damage, and attack range.
- Combat mechanics with enemy health tracking.

### Enemy AI
- Enemy detection and pursuit based on player proximity.
- Movement and collision handling.
- Enemy attack behaviour and cooldown management.
- Health bars and damage handling.

### Dungeon and Room Management
- Multiple interconnected rooms with door-based transitions.
- JSON-driven room layouts and structure definitions.
- Dynamic loading of enemies, walls, and interactable objects.
- Room-state preservation when revisiting previously explored areas.

### Interactive Environment
- Doors and treasure chests.
- Item collection and inventory management.
- Environmental structures with configurable collision boundaries.
- Depth-based rendering (Y-sorting) for realistic sprite layering.

### Game States
- Gameplay state.
- Chest interaction and inventory interface.
- Game-over and restart functionality.

## Technologies Used

- **Python** — Core programming language
- **Pygame** — Game rendering, input handling, and animation
- **JSON** — Room layouts, object definitions, and game configuration
- **Object-Oriented Programming** — Modular design of game entities and systems

## Software Engineering Concepts

This project demonstrates several fundamental software engineering concepts:

- **Object-Oriented Design:** Player, enemy, structure, and interactable objects are implemented using dedicated classes.
- **Modular Architecture:** Game functionality is separated into components responsible for entities, rendering, game states, and level loading.
- **Data-Driven Design:** Dungeon rooms and environmental structures are configured using external JSON files.
- **Algorithms:** Enemy pursuit, collision detection, distance calculations, and depth-based sorting.
- **State Management:** Game states and previously visited room states are managed independently.
- **Reusable Components:** Shared systems support multiple game objects and room configurations.

## Installation

### Requirements

- Python 3
- Pygame

### Setup

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Install Pygame:

```bash
pip install pygame
```

Run the game:

```bash
python main.py
```

## Controls

| Key | Action |
|---|---|
| W | Move up |
| A | Move left |
| S | Move down |
| D | Move right |
| SPACE | Attack |
| E | Interact with doors and chests |

## Project Structure

The project uses separate modules for game entities, gameplay logic, rendering, and level loading.

Key components include:

- `main.py` — Main game loop and state management
- `classes/` — Player, enemy, structure, and interactable classes
- `levelload.py` — Room loading and configuration
- `playingstate.py` — Gameplay logic and rendering
- `environmentart.py` — Environmental sprite rendering
- `data/rooms/` — JSON room configurations
- `data/room_layouts/` — Dungeon layout definitions
- `data/structure_definitions/` — Environmental structure configurations
- `assets/` — Sprites, tilesets, and other visual assets

## Development Roadmap

The following features are planned for future development:

- [x] Player movement and collision detection
- [x] Enemy pursuit and combat mechanics
- [x] Room transitions and level loading
- [x] JSON-based room configuration
- [x] Interactive doors and treasure chests
- [x] Basic inventory system
- [x] Sprite animation and depth-based rendering
- [ ] Additional enemy types and behaviours
- [ ] Expanded dungeon environments
- [ ] Equipment and item systems
- [ ] Improved user interface
- [ ] Boss encounters
- [ ] Sound effects and background music
- [ ] Automated testing and performance optimisation

## Project Status

**In Development**

This is an ongoing personal project. New gameplay features, architectural improvements, and visual enhancements will be introduced as development progresses.

## Assets

The project uses third-party pixel-art assets. Asset creator credits and licensing information will be added as applicable.

## Author

Developed as a personal software engineering and game development project using Python and Pygame.