from dataclasses import dataclass
from typing import Optional

@dataclass
class House:
    title: str
    price: Optional[int] = None
    date: Optional[str] = None
    location_site: str = None
    category_site: str = None
    area: Optional[int] = None
    post_type: str = None
    room_count: Optional[int] = None
    parking: Optional[bool] = None
    mortgage: Optional[int] = None
    rent: Optional[int] = None
    elevator: Optional[bool] = None
    warehouse: Optional[bool] = None
    age: Optional[int] = None
