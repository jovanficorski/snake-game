# snake-game
# 🐍 Snake Game – Проект со 3 Нивоа

Оваа игра е направена во Python користејќи ја библиотеката pygame.  
Играта претставува класична Snake игра со додадени 3 нивоа на тежина.

---

# 🎮 Како се игра

- Змијата се движи со стрелките на тастатурата.
- Целта е да јаде црвени топчиња.
- Со секое изедено топче змијата расте.
- Ако змијата удри во:
  - ѕид
  - сопственото тело  
  играта завршува со порака YOU LOSE.

---

# 🏆 Нивоа

## 🟢 Level 1
- Само рамка (ѕидови по краевите).
- Победа на 25 поени.

## 🟢 Level 2
- Нов почеток.
- Score се ресетира.
- Има дополнителни ѕидови во полето (не во центар).

## 🟢 Level 3
- Уште повеќе ѕидови.
- Поголема тежина.
- Нема ѕидови во почетната позиција.

По победа на Level 3 се појавува порака:  
YOU BEAT ALL LEVELS!

---

# ⚙ Технички информации

- Програмски јазик: Python
- Библиотека: pygame
- Големина на прозорец: 600x600
- Контроли: Arrow Keys
- Победа по ниво: 25 поени

---

# ▶ Како да се стартува

1. Инсталирај pygame:
   pip install pygame

2. Стартирај ја играта:
   python snake_game.py

============================================================

# 🐍 Snake Game – 3 Level Project

This game is developed in Python using the pygame library.  
It represents a classic Snake game with 3 difficulty levels.

---

# 🎮 How to Play

- Control the snake using the arrow keys.
- The goal is to eat the red food squares.
- Each time the snake eats food, it grows.
- The game ends with YOU LOSE if the snake hits:
  - the wall
  - its own body

---

# 🏆 Levels

## 🟢 Level 1
- Only border walls.
- Win after reaching 25 points.

## 🟢 Level 2
- Snake resets to initial size.
- Score resets to 0.
- Additional walls appear inside the field (not in the center).

## 🟢 Level 3
- More internal walls.
- Higher difficulty.
- No walls in the starting center position.

After completing Level 3, the message  
YOU BEAT ALL LEVELS!  
is displayed.

---

# ⚙ Technical Information

- Programming Language: Python
- Library: pygame
- Window size: 600x600
- Controls: Arrow Keys
- Win condition per level: 25 points

---

# ▶ How to Run

1. Install pygame:
   pip install pygame

2. Run the game:
   python snake_game.py
![win.png](../../Desktop/win.png)