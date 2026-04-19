# Breakout

## Description

A **Pygame** Breakout-style game: paddle, ball, bricks, score, levels, and background music. Several **version folders** show how the project evolved from small scripts to a modular sprite-based design.

## Prerequisites

- **Python 3** (3.8+ recommended)
- **[Pygame](https://www.pygame.org/)**

## Installation

Create a virtual environment (recommended), then install Pygame:

```bash
cd breakout
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install pygame
```

## Usage

### Latest version (recommended)

The most complete build is **`Version 6/`**. Run from that directory so asset paths resolve:

```bash
cd "Version 6"
python Breakout.py
```

**`Version 5/`** works the same (`cd "Version 5"` then `python Breakout.py`).

### Other versions

| Folder | Command |
|--------|---------|
| `Version 1`–`3` | `python game_breaker_version_1.py` (or `_2`, `_3`) from that folder |
| `Version 4` | `python levels.py` from `Version 4/` |
| `Sprite/` | `python Sprite_Animation.py` |
| Project root | `python basic_template.py` — minimal Pygame template |

Close the game window to quit.

### Controls (Version 5 & 6)

Paddle uses **keyboard** by default (`PADDLE_CONTROL` in `Breakout.py`; set to `False` for mouse in code).

| Keys | Action |
|------|--------|
| **←** / **A** | Move paddle left |
| **→** / **D** | Move paddle right |

## Project structure

| Path | Contents |
|------|----------|
| `Version 6/` | Main game: `Breakout.py`, `Ball.py`, `Brick.py`, `Paddle.py`, `Progress.py`, `Text.py`, `Assets/`, `Sounds/` |
| `Version 5/` | Same layout as v6 (earlier iteration) |
| `Version 4/` | `levels.py` and assets |
| `Version 1`–`3` | Earlier single-file games + assets |
| `Sprite/` | `Sprite_Animation.py` and assets |
| `basic_template.py` | Minimal Pygame starter |

## Stack

- **Language:** Python 3  
- **Graphics / audio:** [Pygame](https://www.pygame.org/)
