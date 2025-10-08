from fastapi import APIRouter, Query
from datetime import datetime, timedelta
from . import services, schemas

router = APIRouter(prefix="/stats", tags=["Statistics"])

def default_range(days=7):
    now = datetime.utcnow()
    return now - timedelta(days=days), now


@router.get("/avg-delays", response_model=schemas.AvgDelaysResponse)
def avg_delays(from_: datetime | None = Query(None), to: datetime | None = Query(None)):
    if not from_ or not to:
        from_, to = default_range(7)
    return services.calculate_avg_delays(from_, to)


@router.get("/revenue", response_model=schemas.RevenueResponse)
def revenue(from_: datetime | None = Query(None), to: datetime | None = Query(None)):
    if not from_ or not to:
        from_, to = default_range(30)
    return services.calculate_revenue(from_, to)
