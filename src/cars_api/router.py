from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, and_, cast, Numeric, func, Float
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession as As

from src.cars_api.models import Cars
from src.cars_api.shema import UpdateCar, CreateCar
from src.database import get_async_session

router = APIRouter(
    prefix="/cars",
    tags=["Cars"]
)


async def get_car_by_id(car_id: int, session: As = Depends(get_async_session)):
    car = await session.get(Cars, car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Item not found")
    return car


@router.post("/", response_model=CreateCar)
async def add_car(car: CreateCar, session: As = Depends(get_async_session)):
    try:
        new_car = Cars(**dict(car))
        session.add(new_car)
        await session.commit()
        return new_car
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500,
                            detail={"error": "Ошибка базы данных"})



@router.get("/")
async def get_cars(brand: str | None = None,
                   model: str | None = None,
                   year_min: int = 1900,
                   year_max: int = 2050,
                   fuel_type: str | None = None,
                   gearbox_type: str | None = None,
                   mileage_min: int = 1,
                   mileage_max: int = 1000000,
                   price_min: float = 1,
                   price_max: float = 300000000,

                   session: As = Depends(get_async_session)):
    try:
        if year_min <= 0:
            raise HTTPException(status_code=400,
                                detail="Год выпуска должен быть положительным целым числом")
        if year_max <= 0:
            raise HTTPException(status_code=400,
                                detail="Год выпуска должен быть положительным целым числом")

        if mileage_min <= 0:
            raise HTTPException(status_code=400,
                                detail="Пробег должен быть положительным целым числом")
        if mileage_max <= 0:
            raise HTTPException(status_code=400,
                                detail="Пробег должен быть положительным целым числом")

        if price_min <= 0:
            raise HTTPException(status_code=400,
                                detail="Цена должна быть положительным числом")
        if price_max <= 0:
            raise HTTPException(status_code=400,
                                detail="Цена должна быть положительным числом")

        query = select(Cars)

        if brand:
            query = query.filter(Cars.brand == brand)
        if model:
            query = query.filter(Cars.model == model)
        if year_min and year_max:
            query = query.filter(and_(Cars.year_of_issue >= year_min,
                                      Cars.year_of_issue <= year_max))
        if fuel_type:
            query = query.filter(Cars.fuel_type == fuel_type)

        if gearbox_type:
            query = query.filter(Cars.gearbox_type == gearbox_type)

        if mileage_min and mileage_max:
            query = query.filter(and_(Cars.mileage >= mileage_min,
                                      Cars.mileage <= mileage_max))

        if price_min and price_max:
            price_min = float(price_min)
            price_max = float(price_max)
            query = query.filter(
                func.cast(Cars.price, Float).between(price_min, price_max))

        result = await session.execute(query)
        cars = result.scalars().all()
        return cars
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500,
                            detail={"error": "Ошибка базы данных"})



@router.get("/{car_id:int}")
async def get_car_id(car_id: int, session: As = Depends(get_async_session)):
    try:
        car = await get_car_by_id(car_id, session)
        return car
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500,
                            detail={"error": "Ошибка базы данных"})



@router.delete("/{car_id: int}")
async def delete_car_id(car_id: int, session: As = Depends(get_async_session)):
    result = await session.get(Cars, car_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Car not found")
    await session.delete(result)
    await  session.commit()
    return {"status": "deleted"}


@router.patch("/{car_id: int}", response_model=UpdateCar)
async def patch_car_id(car: UpdateCar, car_id: int,
                       session: As = Depends(get_async_session)):
    result = await get_car_by_id(car_id, session)
    for key, value in car.dict().items():
        if value is not None:
            setattr(result, key, value)

    await session.commit()
    return result
