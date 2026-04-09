## Configuration

### DaysToConsider [number]
This setting controls how many days of revlog history are used for the average `cards/minute` display on the right side. By default, only the current day's data is used.

**Values:**<br/>
- `"DaysToConsider" = 1` (default)<br/>
  Consider only the current day's review data.<br/>
- `"DaysToConsider" = 2`<br/>
  Consider the current day and the previous day's review data.<br/>
- `"DaysToConsider" = n`<br/>
  Consider the current day and the previous n-1 days' review data.<br/>

### Displayed stats
The add-on now shows the counters in this order:

- `New`
- `Learn`
- `Due`
- `Reviews`
- `Total`
- `Tomorrow`

Meaning:
- `Due` shows only review cards.
- `Reviews` shows `Learn + Due`.
- `Total` shows the full sum for today.
- The time-left estimate is no longer shown.

### Number colors [Name]
[Color Names Sorted by Color Groups](https://www.w3schools.com/colors/colors_groups.asp)<br/>
All modern browsers support the following 140 color names (click on a color name, or a hex value, to view the color as the background-color along with different text colors):

Configurable colors:
- `NewColorLight` / `NewColorDark` control `New`.
- `TotalDueColorLight` / `TotalDueColorDark` control both `Due` and `Tomorrow`.

Fixed colors:
- `Learn` is red.
- `Reviews` is yellow.
- `Total` is black in light theme and white in dark theme.
