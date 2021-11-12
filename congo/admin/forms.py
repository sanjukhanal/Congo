from flask_wtf import FlaskForm
from wtforms import SelectField


class DateToggle(FlaskForm):
    reports_for = SelectField(
        'View transactions Since:',
        choices=[
            ('all', 'All time'),
            ('yesterday', 'Yesterday'),
            ('this_month', 'This Month'),
            ('last_month', 'Last Month'),
            ('current_year', 'This Year'),
        ]
    )
