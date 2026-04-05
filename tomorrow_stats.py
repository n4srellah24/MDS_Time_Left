def calculate_tomorrow_count(*, tomorrow_due):
    return tomorrow_due


def get_tomorrow_scheduled_count(col):
    tomorrow = col.sched.today + 1
    return (
        col.db.scalar(
            """
            select count()
            from cards
            where due = ?
              and queue in (1, 2, 3)
            """,
            tomorrow,
        )
        or 0
    )
