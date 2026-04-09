import unittest


from stats_layout import (
    build_average_stats,
    build_display_stats,
    get_learn_color,
    get_reviews_color,
    build_stat_rows,
    get_total_color,
)


class BuildDisplayStatsTest(unittest.TestCase):
    def test_maps_duo_reviews_and_total(self):
        stats = build_display_stats(new=3, learn=5, review=7)

        self.assertEqual(
            stats,
            {
                "new": 3,
                "learn": 5,
                "duo": 7,
                "reviews": 12,
                "total": 15,
            },
        )


class BuildAverageStatsTest(unittest.TestCase):
    def test_keeps_average_and_cards_per_min_without_time_left(self):
        stats = build_average_stats(days_to_consider=2, cards_per_min="12.5")

        self.assertEqual(
            stats,
            {
                "show_average_days": True,
                "cards_per_min": "12.5",
            },
        )


class BuildStatRowsTest(unittest.TestCase):
    def test_uses_due_label_and_requested_color_classes(self):
        rows = build_stat_rows(
            {
                "new": 3,
                "learn": 5,
                "duo": 7,
                "reviews": 12,
                "total": 15,
            },
            tomorrow_total=9,
        )

        self.assertEqual(
            rows,
            [
                ("New", "new-color", 3),
                ("Learn", "learn-color", 5),
                ("Due", "review-color", 7),
                ("Reviews", "totaldue-color", 12),
                ("Total", "total-color", 15),
                ("Tomorrow", "tomorrow-color", 9),
            ],
        )


class GetTotalColorTest(unittest.TestCase):
    def test_uses_black_in_light_mode(self):
        self.assertEqual(get_total_color(is_night_mode=False), "#000000")

    def test_uses_white_in_dark_mode(self):
        self.assertEqual(get_total_color(is_night_mode=True), "#FFFFFF")


class StatAccentColorTest(unittest.TestCase):
    def test_learn_is_red_in_light_and_dark_modes(self):
        self.assertEqual(get_learn_color(is_night_mode=False), "#FF0000")
        self.assertEqual(get_learn_color(is_night_mode=True), "#FF0000")

    def test_reviews_is_yellow_in_light_and_dark_modes(self):
        self.assertEqual(get_reviews_color(is_night_mode=False), "#FFD700")
        self.assertEqual(get_reviews_color(is_night_mode=True), "#FFD700")


if __name__ == "__main__":
    unittest.main()
