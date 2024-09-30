
from typing import Optional

from pydantic import BaseModel,Field


class CreateCar(BaseModel):
    brand: str
    model: str
    year_of_issue: int = Field(..., gt=1900, lt=2100)
    fuel_type: str
    gearbox_type: str
    mileage: int
    price: float


class UpdateCar(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None
    year_of_issue: Optional[int] = None
    fuel_type: Optional[str] = None
    gearbox_type: Optional[str] = None
    mileage: Optional[int] = None
    price: Optional[float] = None
