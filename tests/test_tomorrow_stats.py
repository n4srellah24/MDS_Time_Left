import unittest

from tomorrow_stats import calculate_tomorrow_count, get_tomorrow_scheduled_count


class CalculateTomorrowCountTest(unittest.TestCase):
    def test_returns_only_tomorrow_due(self):
        self.assertEqual(calculate_tomorrow_count(tomorrow_due=7), 7)

    def test_handles_zero_tomorrow_due(self):
        self.assertEqual(calculate_tomorrow_count(tomorrow_due=0), 0)


class GetTomorrowScheduledCountTest(unittest.TestCase):
    def test_queries_next_scheduler_day_using_non_new_queues(self):
        class FakeDB:
            def __init__(self):
                self.calls = []

            def scalar(self, query, *args):
                self.calls.append((query, args))
                return 6

        class FakeSched:
            today = 42

        class FakeCol:
            def __init__(self):
                self.db = FakeDB()
                self.sched = FakeSched()

        col = FakeCol()

        result = get_tomorrow_scheduled_count(col)

        self.assertEqual(result, 6)
        self.assertEqual(col.db.calls[0][1], (43,))
        self.assertIn("queue in (1, 2, 3)", col.db.calls[0][0].lower())


if __name__ == "__main__":
    unittest.main()
