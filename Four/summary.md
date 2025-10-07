## Screen Updates

turtle.tracer(x)
* x = 0: no updates, turtle.update() must be called to show drawing
  * most commonly used
* x = 1: default
* x > 1: on every nth regular screen, update is performed
turtle.update()

## Keyboard Input

```python
screen = turtle.Screen()
def f():
    do something
screen.onkey(f, [key])
screen.listen()
```
