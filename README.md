# Python Cellular Automata

English | [中文](./README_zh.md)

A two-dimensional cellular automata demo built with Python and Pygame. The current implementation uses the classic Conway's Game of Life rules: each cell's next state is determined by the number of live cells in its 8-cell neighborhood, then rendered as a black-and-white grid animation.

![Cellular automata demo](./元胞自动机.gif)

## Features

- Draws an 800 x 800 automata grid with `pygame`
- Shows a multi-line operation log in the right-side panel
- Uses a default grid size of `160 x 160`
- Randomly initializes 4800 live cells by default
- Computes each generation from the 8 neighboring cells
- Wraps edges horizontally and vertically, forming a toroidal space
- Redraws only cells whose state changed on each simulation step
- Supports pausing and resuming with the space bar
- Supports left-clicking a cell to manually toggle it alive or dead
- Shows the current running state and recent operations as ASCII text
- Provides a `Help` button with rules and controls
- Provides a `Pause` / `Resume` button to control automatic evolution

## Requirements

- Python 3
- pygame

Install dependencies:

```bash
pip3 install pygame
```

Run the project:

```bash
python3 cellular_automata.py
```

After launch, a Pygame window opens:

- Black cells are alive
- White cells are dead
- Press `Space` to pause or resume
- Click `Pause` / `Resume` on the right side to pause or resume
- Left-click a grid cell to toggle its state
- Click `Help` on the right side to view the game rules and controls
- Press `Esc` or click `Close` in the Help window to close it
- The right-side log panel shows recent clicks and pause/resume actions
- Close the window to exit

## Project Structure

```text
.
├── README.md
├── README_zh.md
├── box.py
├── cellular_automata.py
└── 元胞自动机.gif
```

- `cellular_automata.py`: application entry point; initializes the window, creates the random starting state, handles events, and draws the screen
- `box.py`: defines `Cell` and `Box`; maintains the grid, looks up neighbors, and applies the Game of Life rules
- `元胞自动机.gif`: demo animation

## Rules

Each cell has two possible states:

- `1`: alive
- `0`: dead

On each simulation step, the program counts the live cells in the current cell's 8-cell neighborhood and applies these rules:

- A live cell with fewer than 2 live neighbors dies
- A live cell with 2 or 3 live neighbors stays alive
- A live cell with more than 3 live neighbors dies
- A dead cell with exactly 3 live neighbors becomes alive

## Configuration

You can edit these values at the top of `cellular_automata.py`:

```python
grid_width = 800
grid_height = 800
log_panel_width = 280
win_width = grid_width + log_panel_width
win_height = grid_height
row_cell_num = 160
life_num = 4800
max_log_lines = 40
frame_rate = 60
simulation_interval_ms = 1000
```

- `grid_width` / `grid_height`: automata grid width and height
- `log_panel_width`: width of the right-side log panel
- `win_width` / `win_height`: total window width and height
- `row_cell_num`: number of cells per row and column
- `life_num`: number of live cells created randomly at startup
- `max_log_lines`: maximum number of operation log lines shown in the right-side panel
- `frame_rate`: frame rate for UI refresh and event handling
- `simulation_interval_ms`: interval between simulation steps, in milliseconds

The program uses `frame_rate` to keep mouse and keyboard input responsive, while `simulation_interval_ms` controls the automata evolution speed separately. By default, the simulation advances once every 1000 ms. Lower this value to make it evolve faster.

## Implementation Notes

`Box.flush()` first copies the current grid state, then computes every cell's next state from that old snapshot. This prevents one cell updated earlier in a generation from affecting other cells in the same generation.

After each step, `flush()` returns only the cells whose state changed. The main loop redraws those cells only, reducing unnecessary drawing work.

## Background

Cellular automata are computational models made of discrete space, discrete time, and finite cell states. Each cell updates its state according to fixed rules based on itself and its local neighborhood. Conway's Game of Life is one of the best-known two-dimensional cellular automata: very simple local rules can produce rich and complex dynamic patterns.
