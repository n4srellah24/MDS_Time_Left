def build_display_stats(*, new, learn, review):
    return {
        "new": new,
        "learn": learn,
        "duo": review,
        "reviews": learn + review,
        "total": new + learn + review,
    }


def build_average_stats(*, days_to_consider, cards_per_min):
    return {
        "show_average_days": days_to_consider > 1,
        "cards_per_min": cards_per_min,
    }


def build_stat_rows(display_stats, *, tomorrow_total):
    return [
        ("New", "new-color", display_stats["new"]),
        ("Learn", "learn-color", display_stats["learn"]),
        ("Due", "review-color", display_stats["duo"]),
        ("Reviews", "totaldue-color", display_stats["reviews"]),
        ("Total", "total-color", display_stats["total"]),
        ("Tomorrow", "tomorrow-color", tomorrow_total),
    ]


def get_total_color(*, is_night_mode):
    return "#FFFFFF" if is_night_mode else "#000000"


def get_learn_color(*, is_night_mode):
    return "#FF0000"


def get_reviews_color(*, is_night_mode):
    return "#FFD700"
