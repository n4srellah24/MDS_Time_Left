# Tomorrow Count Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a live `Tomorrow` stat after `Total` that shows only tomorrow-scheduled cards without changing time-left behavior.

**Architecture:** Keep the add-on’s current render flow, but move the tomorrow-count math into a small helper that can be tested independently. The deck browser will query tomorrow’s scheduled cards, pass that count into the helper, and render one extra styled metric.

**Tech Stack:** Python, Anki add-on API, pytest-style unit tests

---

### Task 1: Narrow the tomorrow-count helper to tomorrow-scheduled cards only

**Files:**
- Modify: `tests/test_tomorrow_stats.py`
- Modify: `tomorrow_stats.py`

- [ ] **Step 1: Write the failing test**

```python
from tomorrow_stats import calculate_tomorrow_count


def test_calculate_tomorrow_count_returns_only_tomorrow_due():
    assert calculate_tomorrow_count(tomorrow_due=7) == 7
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_tomorrow_stats.py`
Expected: FAIL because the helper still requires `new` and `lrn`

- [ ] **Step 3: Write minimal implementation**

```python
def calculate_tomorrow_count(*, tomorrow_due):
    return tomorrow_due
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests/test_tomorrow_stats.py`
Expected: PASS

### Task 2: Update the render path to use the narrower helper

**Files:**
- Modify: `mds_time_left.py`
- Modify: `tests/test_tomorrow_stats.py`

- [ ] **Step 1: Write the failing test**

```python
from tomorrow_stats import calculate_tomorrow_count


def test_calculate_tomorrow_count_ignores_current_new_and_learning_cards():
    assert calculate_tomorrow_count(tomorrow_due=6) == 6
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_tomorrow_stats.py`
Expected: FAIL until the helper and render path use the narrower signature

- [ ] **Step 3: Write minimal implementation**

```python
tomorrow_due = get_tomorrow_scheduled_count(self.mw.col)
tomorrow_total = calculate_tomorrow_count(tomorrow_due=tomorrow_due)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests/test_tomorrow_stats.py`
Expected: PASS

- [ ] **Step 5: Run targeted verification**

Run: `python3 -m py_compile __init__.py mds_time_left.py tomorrow_stats.py`
Expected: no output, exit code 0
