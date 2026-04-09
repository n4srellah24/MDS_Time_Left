# -*- coding: utf-8 -*-
# Copyright(C)   | Carlos Duarte
# Based 1 on     | Dmitry Mikheev code, in add-on "More decks overview stats"
# Based 2 on     | calumkscode, in add-on https://github.com/calumks/anki-deck-stats
# License        | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in      | https://github.com/cjdduarte/MDS_Time_Left

import anki
# from anki.lang import _, ngettext
import aqt
from aqt import mw, theme
from aqt.utils import tr
from .stats_layout import (
    build_average_stats,
    build_display_stats,
    build_stat_rows,
    get_learn_color,
    get_reviews_color,
    get_total_color,
)
from .tomorrow_stats import calculate_tomorrow_count, get_tomorrow_scheduled_count

#-------------Configuration------------------
config = mw.addonManager.getConfig(__name__)
DaysToConsider = config['DaysToConsider']
#-------------Configuration------------------

def generate_style():
    """Generate the required CSS style based on the theme mode."""
    if theme.theme_manager.night_mode:
        new_color_key = 'NewColorDark'
        due_color_key = 'TotalDueColorDark'
    else:
        new_color_key = 'NewColorLight'
        due_color_key = 'TotalDueColorLight'

    style_elements = [
        ".new-color { color:" + config[new_color_key] + ";}",
        ".review-color { color:" + config[due_color_key] + ";}",
        ".learn-color { color:" + get_learn_color(is_night_mode=theme.theme_manager.night_mode) + ";}",
        ".totaldue-color { color:" + get_reviews_color(is_night_mode=theme.theme_manager.night_mode) + ";}",
        ".total-color { color:" + get_total_color(is_night_mode=theme.theme_manager.night_mode) + ";}",
        ".tomorrow-color { color:" + config[due_color_key] + ";}",
    ]

    return "<style type=\"text/css\">" + ' '.join(style_elements) + "</style>"

def renderStats(self, _old):

    txtTomorrow = "Tomorrow"
    txtAverage  = tr.statistics_average()

    txtDaysCount = tr.statistics_in_time_span_days(DaysToConsider)
    if DaysToConsider > 1:
        txtAverage = f"{txtAverage} ({txtDaysCount})"

    # Get due and new cards
    new, lrn, due = 0, 0, 0
    
    try:
        # Nova API (Anki 2.1.50+)
        root_node = self.mw.col.sched.deck_due_tree()
        if root_node:
            new = root_node.new_count
            lrn = root_node.learn_count
            due = root_node.review_count
    except AttributeError:
        # API antiga (Anki < 2.1.50) - fallback
        print("Using deprecated API")
        for tree in self.mw.col.sched.deckDueTree():
            new += tree[4]
            lrn += tree[3]
            due += tree[2]

    display_stats = build_display_stats(new=new, learn=lrn, review=due)
    tomorrow_due = get_tomorrow_scheduled_count(self.mw.col)
    tomorrow_total = calculate_tomorrow_count(tomorrow_due=tomorrow_due)
    stat_rows = build_stat_rows(display_stats, tomorrow_total=tomorrow_total)
    total_seconds = 86400 * DaysToConsider
    query_time_param = self.mw.col.sched.day_cutoff - total_seconds
    cards, thetime = self.mw.col.db.first(
        """select count(), sum(time)/1000 from revlog where id > ?""",
        query_time_param * 1000,
    )
    cards = cards or 0
    thetime = thetime or 0
    speed = cards * 60 / max(1, thetime)
    average_stats = build_average_stats(
        days_to_consider=DaysToConsider,
        cards_per_min="{:.01f}".format(speed),
    )
    txtCardsMin = tr.statistics_cards_per_min(average_stats["cards_per_min"])

    buf = generate_style() + """
        <div style='display:table;padding-top:1.5em;'>
            <div style='display:table-cell;'>
                {}
                <hr>
                &nbsp;{}:&nbsp; <b class='{}'> {}</b>
                &nbsp;{}:&nbsp; <b class='{}'> {}</b>
                &nbsp;{}:&nbsp; <b class='{}'> {}</b>
                &nbsp;{}:&nbsp; <b class='{}'> {}</b>
                &nbsp;{}:&nbsp; <b class='{}'> {}</b>
                &nbsp;{}:&nbsp; <b class='{}'> {}</b>
            </div>
            <div style='display:table-cell;vertical-align:middle;padding-left:2em;'>
                {}: <br> {}
            </div>
        </div>
    """.format(
        _old(self),
        stat_rows[0][0],
        stat_rows[0][1],
        stat_rows[0][2],
        stat_rows[1][0],
        stat_rows[1][1],
        stat_rows[1][2],
        stat_rows[2][0],
        stat_rows[2][1],
        stat_rows[2][2],
        stat_rows[3][0],
        stat_rows[3][1],
        stat_rows[3][2],
        stat_rows[4][0],
        stat_rows[4][1],
        stat_rows[4][2],
        stat_rows[5][0],
        stat_rows[5][1],
        stat_rows[5][2],
        txtAverage,
        txtCardsMin,
    )
    # """.format(_old(self), _("New"), new, _("Learn"), lrn, _("To Review"), due, _("Due"), lrn+due, _("Total"), totalDisplay, _("Average"), speed, _("Cards"), _("Minutes").replace("s", ""), str(ngettext("%s minute.", "%s minutes.", minutes) % minutes).replace(".", ""), _("More").lower())
    
    return buf

aqt.deckbrowser.DeckBrowser._renderStats = anki.hooks.wrap(
    aqt.deckbrowser.DeckBrowser._renderStats, renderStats, 'around')
