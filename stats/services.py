from datetime import datetime
from sqlalchemy import text
from src.db import SessionLocal   # zakładam, że masz taki plik od bazy

def calculate_avg_delays(from_: datetime, to: datetime):
    sql_dep = text("""
        SELECT AVG((strftime('%s', COALESCE(actual_dep, scheduled_dep))
                    - strftime('%s', scheduled_dep)))/60.0 AS avg_dep_delay_min
        FROM flights
        WHERE scheduled_dep BETWEEN :from AND :to
          AND status IN ('SCHEDULED','COMPLETED')
    """)
    sql_arr = text("""
        SELECT AVG((strftime('%s', COALESCE(actual_arr, scheduled_arr))
                    - strftime('%s', scheduled_arr)))/60.0 AS avg_arr_delay_min
        FROM flights
        WHERE scheduled_dep BETWEEN :from AND :to
          AND status IN ('SCHEDULED','COMPLETED')
    """)

    with SessionLocal() as db:
        dep = db.execute(sql_dep, {"from": from_, "to": to}).scalar()
        arr = db.execute(sql_arr, {"from": from_, "to": to}).scalar()

    return {"avg_dep_delay_min": dep or 0.0, "avg_arr_delay_min": arr or 0.0}


def calculate_revenue(from_: datetime, to: datetime):
    sql = text("""
        SELECT SUM(t.price) AS revenue
        FROM tickets t
        JOIN flights f ON f.id = t.flight_id
        WHERE t.status='CONFIRMED'
          AND f.scheduled_dep BETWEEN :from AND :to
    """)
    with SessionLocal() as db:
        revenue = db.execute(sql, {"from": from_, "to": to}).scalar()
    return {"revenue": revenue or 0.0}
