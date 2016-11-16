
"""Sample file demonstrating SQLAlchemy joins & relationships."""

from flask_sqlalchemy import SQLAlchemy


# This is the connection to the SQLite database; we're getting this
# through the Flask-SQLAlchemy helper library. On this, we can find
# the `session` object, where we do most of our interactions
# (like committing, etc.)

db = SQLAlchemy()


####################################################################
# Model definitions

class Forecast(db.Model):
    """Forecast."""

    __tablename__ = "forecasts"

    forecast_id = db.Column(db.Integer, primary_key=True)
    zipcode = db.Column(db.Integer, nullable=False, unique=True)
    state = db.Column(db.String(2), nullable=False, default='CA')
    daily_forecast = db.Column(
        db.String(140), nullable=True, default='Unknown')
    outlook_forecast = db.Column(
        db.String(140), nullable=True, default='Unknown')

def example_data():
    """Create some sample data."""

    # In case this example_data function is run more than once,
    # let's delete all the existing forecasts,
    # so we don't have an error when we try to add them.
    Forecast.query.delete()

    forecasts = [
        Forecast(zipcode=94101, state='CA', daily_forecast="Sunny with a high of 70 and a low of 60."),
        Forecast(zipcode=94105, state='CA', daily_forecast="Partly cloudy with a high of 68 and a low of 60."),
        Forecast(zipcode=94122, state='CA', daily_forecast="Mostly cloudy with a high of 65 and a low of 55.")
    ]

    db.session.add_all(forecasts)
    db.session.commit()


def raw_sql_query():
    """Show how to query in raw SQL, bypassing SQLAlchemy ORM.
    Sometimes, there may be questions that are just easier
    to ask using the SQL you know, rather than learning how to
    do it with an ORM.

    We can bypass and use raw SQL directly if that's easier.
    For example, let's ask the question: "show us the counts
    of the number of employees who like orange in each department"
    """

    SQL = """
        SELECT zipcode,
               daily_forecast
        FROM forecasts
        WHERE state='CA'
        ORDER BY zipcode
    """

    results = db.engine.execute(SQL).fetchall()
    return results

    # It would be possible to write this query going through the
    # ORM -- you'd just need to learn a bit more about the ORM
    # to do so. If you're interested, here's how we could
    # write that same query via the ORM:

    # results = (db.session.query(Forecast.zipcode,
    #                             Forecast.state)
    #                      .filter(Forecast.state == 'CA')
    #                      .order_by(Forecast.zipcode)
    #           ).all()
    # return results




####################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emp.db'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

    # Create our tables and some sample data
    db.create_all()
    example_data()


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."

    # grab the employee object with the name 'Cynthia Dueltgen'
    outer_sunset = Forecast.query.filter(Forecast.zipcode == 94122).one()

    # what is today's forecast in the outer sunset?
    print outer_sunset.daily_forecast
