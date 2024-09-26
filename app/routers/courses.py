from fastapi import APIRouter

from app.models.course import Recommendation
from app.resources.course_resource import RecommendationResource
from app.services.service_factory import ServiceFactory

router = APIRouter()


@router.get("/recommendations/{professor_id}", tags=["users"])
async def get_courses(professor_id: str) -> list[Recommendation]:

    # TODO Do lifecycle management for singleton resource
    res = ServiceFactory.get_service("RecommendationResource")
    result = res.get_by_key(professor_id)
    return result

