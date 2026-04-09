<b>Bug Report:</b> <a href="https://github.com/cjdduarte/MDS_Time_Left/issues">https://github.com/cjdduarte/MDS_Time_Left/issues</a>

<b>#### New Change:</b>

<b>Updated stats layout and cleaned configuration</b>

<b>#### About:</b>

This add-on shows extra deck overview stats in the order <b>New, Learn, Due, Reviews, Total, Tomorrow</b>, plus the current <b>average cards/minute</b>.

<ul>
  <li><b>Due</b> shows only review cards.</li>
  <li><b>Reviews</b> shows <code>Learn + Due</code>.</li>
  <li><b>Total</b> shows the full sum for today.</li>
  <li>The old time-left estimate has been removed.</li>
</ul>

<b>Before:</b>

<p align="center">
  <img src="https://i.ibb.co/JKzqR6H/image.png" alt="Before">
</p>

<b>After:</b>

<p align="center">
  <img src="https://i.ibb.co/Ptk82k1/image.png" alt="After">
</p>

<b>#### Configuration option:</b>

<b>DaysToConsider [number]:</b>

This setting controls how many days of revlog history are used to calculate the average <code>cards/minute</code>. By default, only the current day's data is used.

<ul>
  <li>DaysToConsider = 1 (default) | Consider only the current day's review data.</li>
  <li>DaysToConsider = 2 | Consider the current day and the previous day's review data.</li>
  <li>DaysToConsider = n | Consider the current day and the previous n-1 days' review data.</li>
</ul>

<b>Colors:</b>

<ul>
  <li><code>NewColorLight</code> / <code>NewColorDark</code> control <b>New</b>.</li>
  <li><code>TotalDueColorLight</code> / <code>TotalDueColorDark</code> control both <b>Due</b> and <b>Tomorrow</b>.</li>
  <li><b>Learn</b> is fixed to red.</li>
  <li><b>Reviews</b> is fixed to yellow.</li>
  <li><b>Total</b> is fixed to black in light theme and white in dark theme.</li>
</ul>

<b>Number colors [Name]:</b> <a href="https://www.w3schools.com/colors/colors_groups.asp">Color Names Sorted by Color Groups</a>

All modern browsers support the following 140 color names (click on a color name, or a hex value, to view the color as the background-color along with different text colors):

<ul>
  <li>Copyright(C)| Carlos Duarte</li>
  <li>Based on | Dmitry Mikheev code, in add-on "More decks overview stats"</li>
  <li>Based on | calumks code, in add-on <a href="https://github.com/calumks/anki-deck-stats">add-on</a></li>
  <li>License | <a href="http://www.gnu.org/licenses/agpl.html">GNU AGPL</a>, version 3 or later;</li>
  <li><a href="https://github.com/cjdduarte/MDS_Time_Left">Source in</a></li>
</ul>

<b> #### Change Log:</b>

<ul>

  <li>v3.0 - 2026-04-09 - Remapped deck stats to New/Learn/Due/Reviews/Total/Tomorrow, removed time-left, kept average cards/minute, and cleaned stale configuration/docs.</li>
  <li>v2.9 - 2025-06-23 - Fix deprecated API usage</li>
  <li>v2.8 - 2025-05-22 - Downgrade to 2.6 (BugFix)</li>
  <li>v2.7 - 2025-05-21 - Fixed compatibility with Anki 25.02.5 (using `deck_due_tree`) and resolved potential conflict during Anki closing/profile switching.</li>
  <li>v2.6 - 2025-04-24 - Tested compatibility with Anki 25.02.4</li>
  <li>v2.5 - 2024-08-19 - Added 'DaysToConsider' configuration for multi-day review statistics.</li>
  <li>v2.4 - 2024-04-11 - Added 'ShowTimeLeft' toggle for study time visibility.</li>
  <li>v2.3 - 2023-09-24 - Bug with version 23.10</li>
  <li>v2.2 - 2023-08-21 + Minor visual adjustments (Tanks @Okosh50)</li>
  <li>v2.1 - 2023-08-17 + Fully translated</li>
  <li>v2.0 - 2023-08-15 + New code (Clean)</li>
  <li>v1.9 - 2022-10-09 + dayCutoff deprecated (Tanks @khonkhortisan)</li>
  <li>v1.8 - 2022-05-20 + Night mode compatibility.</li>
  <li>v1.7 - 2021-01-27 + Clean code (removed compatibility with Anki 2.0).</li>
  <li>v1.6 - 2020-03-31 + Adjust Grammar and translation.</li>
  <li>v1.5 - 2020-01-21 + Change the number colors in the configuration options.</li>
  <li>v1.4 - 2019-12-26 + New configuration option (tanks @MedAnki)</li>
  <li>v1.3 - 2019-12-09 - Easier to the user change the colors (tanks @renbosa)</li>
  <li>v1.2 - 2019-02-27 - Indentation</li>
  <li>v1.1 - 2019-02-21 - Color Correction and unified code</li>
  <li>v1.0 - 2019-02-20 - Initial Release</li>
</ul>
