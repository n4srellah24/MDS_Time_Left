# Tomorrow Count Design

**Goal:** Add a new `Tomorrow` stat to the deck overview after `Total` without changing the existing time-left calculation.

**Behavior:**
- Show `Tomorrow: <count>` at the end of the existing stats row.
- Compute the count as only cards scheduled for the next scheduler day.
- Keep the value live by recomputing it every time the deck browser stats render.

**Data Sources:**
- Query the `cards` table directly for cards whose `due` value equals `sched.today + 1`.
- Restrict the direct query to review/learn queues so the counter reflects cards actually scheduled for tomorrow.

**Rendering:**
- Append a `Tomorrow` label/value after `Total` in the current stats layout.
- Add a dedicated CSS class and light/dark config colors following the add-on’s current pattern.

**Non-Goals:**
- Do not change `Total`.
- Do not change `Due`.
- Do not change the time-left estimation logic or `ShowTimeLeft` behavior.

**Testing Approach:**
- Extract the tomorrow count computation into a small helper function.
- Add unit tests for the helper covering:
  - the helper returning only tomorrow-scheduled cards,
  - the direct query using the next scheduler day and non-new queues.
