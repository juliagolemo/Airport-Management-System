from datetime import datetime
from pydantic import BaseModel

class DateRange(BaseModel):
    from_: datetime
    to: datetime

class AvgDelaysResponse(BaseModel):
    avg_dep_delay_min: float
    avg_arr_delay_min: float

class RevenueResponse(BaseModel):
    revenue: float
