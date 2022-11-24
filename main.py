
import sense_hat
import time
import random
import sys
hat = sense_hat.SenseHat()
snakeOrientation = "up"
food_pos = (0,0)
score = 0

def up():
  global snakeOrientation
  if snakeOrientation != "down":
    snakeOrientation = "up"

hat.stick.direction_up = up

def right():
  global snakeOrientation
  if snakeOrientation != "left":
    snakeOrientation = "right"

hat.stick.direction_right = right
def down():
  global snakeOrientation
  if snakeOrientation != "up":
    snakeOrientation = "down"

hat.stick.direction_down = down

def left():
  global snakeOrientation
  if snakeOrientation != "right":
    snakeOrientation = "left"

hat.stick.direction_left = left

def new_food_pos(snake):
  screen = []
  for i in range(8):
    for j in range(8):
      screen.append((i,j))

  for i in snake:
    if i in screen:
      screen.remove(i)

  pos = screen[random.randrange(len(screen))]
  return pos

def game_over():
  time.sleep(0.5)

  hat.clear(255,0,0)
  time.sleep(1)
  hat.clear()

def run_game():
  global snakeOrientation
  global food_pos
  snakeOrientation = "up"
  snake = [(3,7),(3,7),(3,7)]
  food_pos = new_food_pos(snake)
  blink = True
  game_over_bool = False
  while not game_over_bool:
    if blink:
      hat.set_pixel(food_pos[0],food_pos[1],(255,0,0))
      blink = False
    else:
      hat.set_pixel(food_pos[0],food_pos[1],(0,255,0))
      blink = True

    game_over_bool = move_snake(snake)
    time.sleep(0.3)

#returns true when game over
def move_snake(snake):
  #find next position
  if snakeOrientation == "up":
    next_head_pos = (snake[0][0], snake[0][1] - 1)
  elif snakeOrientation == "right":
    next_head_pos = (snake[0][0] + 1, snake[0][1])
  elif snakeOrientation == "down":
    next_head_pos = (snake[0][0], snake[0][1] + 1)
  elif snakeOrientation == "left":
    next_head_pos = (snake[0][0] - 1, snake[0][1])

  #game over checks
  if next_head_pos[0] < 0 or next_head_pos[0] > 7 or next_head_pos[1] < 0 or next_head_pos[1] > 7:
    return True

  for i in snake:
    if i == next_head_pos:
      return True

  #eat food
  global food_pos
  global score
  if next_head_pos == food_pos:
    last_seg = snake[len(snake) - 1]
    snake.append(last_seg)
    snake.append(last_seg)
    food_pos = new_food_pos(snake)
    score += 1

  #move
  last_seg = snake[len(snake) - 1]
  hat.set_pixel(last_seg[0],last_seg[1],(0,0,0))

  for i in range(len(snake) - 1, 0, -1):
    snake[i] = snake[i - 1]

  #hat.set_pixel(next_head_pos[0],next_head_pos[1],(255,255,255))
  snake[0] = next_head_pos
  for i in snake:
    hat.set_pixel(i[0],i[1],(random.randrange(255),random.randrange(255),random.randrange(255)))

hat.clear()

while True:
  run_game()
  game_over()
