from dataclasses import dataclass
from datetime import date

@dataclass
class Entry:

    entry_date: date
    upload_date: date
    owner: str
    sub_county: str
    description: str
    floors: int
    issues: str
    assigned: str
    date_moved: date
    days_left: int
    last_follow_up: date
    status: str
    remarks: str
