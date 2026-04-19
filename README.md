# Breakout

A **Pygame** Breakout-style game: paddle, ball, bricks, score, levels, and background music. The codebase is organized into several **versions** that show how the game evolved from simpler scripts to a modular design with sprites.

## Prerequisites

- **Python 3** (3.8+ recommended)
- **[Pygame](https://www.pygame.org/)**

## Setup

Create a virtual environment (recommended), then install Pygame:

```bash
cd breakout
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install pygame
```

## Run (latest version)

The most complete build is under **`Version 6/`**. Run the main module **from that directory** so asset paths resolve correctly:

```bash
cd "Version 6"
python Breakout.py
```

**Version 5** works the same way (`cd "Version 5"` then `python Breakout.py`).

Older experiments:

| Folder | How to run |
|--------|------------|
| `Version 1`–`3` | `python game_breaker_version_1.py` (or `_2`, `_3`) from inside that folder |
| `Version 4` | `python levels.py` from `Version 4/` |
| `Sprite/` | `python Sprite_Animation.py` (sprite animation demo) |
| Project root | `python basic_template.py` — minimal Pygame window (template) |

## Controls

In **Version 5** and **Version 6**, the paddle defaults to **keyboard** control (see `PADDLE_CONTROL` in `Breakout.py`; set to `False` for mouse-driven movement in code).

| Keys | Action |
|------|--------|
| **←** / **A** | Move paddle left |
| **→** / **D** | Move paddle right |

Close the window to quit.

## Project layout

| Path | Contents |
|------|----------|
| `Version 6/` | Current-style game: `Breakout.py`, `Ball.py`, `Brick.py`, `Paddle.py`, `Progress.py`, `Text.py`, `Assets/`, `Sounds/` |
| `Version 5/` | Same structure as v6 (earlier iteration) |
| `Version 4/` | `levels.py` and assets |
| `Version 1`–`3` | Earlier single-file style games + assets |
| `Sprite/` | `Sprite_Animation.py` and shared sprite assets/sounds |
| `basic_template.py` | Reusable minimal Pygame template |

## Stack

- **Language:** Python 3  
- **Graphics / audio:** [Pygame](https://www.pygame.org/) (display, sprites, mixer)
