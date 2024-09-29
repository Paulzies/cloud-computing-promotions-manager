from fastapi import APIRouter

from app.models.course import Promotion
from app.resources.course_resource import PromotionsResource
from app.services.service_factory import ServiceFactory

router = APIRouter()


@router.get("/promotions/{promotion_id}", tags=["users"])
async def get_courses(promotion_id: str) -> list[Promotion]:

    # TODO Do lifecycle management for singleton resource
    res = ServiceFactory.get_service("PromotionsResource")
    result = res.get_by_key(promotion_id)
    return result

