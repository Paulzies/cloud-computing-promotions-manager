from typing import Any

from framework.resources.base_resource import BaseResource

from app.models.course import Promotion
from app.services.service_factory import ServiceFactory


class PromotionsResource(BaseResource):

    def __init__(self, config):
        super().__init__(config)

        # TODO -- Replace with dependency injection.
        #
        self.data_service = ServiceFactory.get_service("PromotionsDataService")
        self.database = "promotions_manager"
        self.collection = "promotions"
        self.key_field="promotion_id"

    def get_by_key(self, key: str) -> list[Promotion]:

        d_service = self.data_service

        result = d_service.get_data_object(
            self.database, self.collection, key_field=self.key_field, key_value=key
        )

        result = [Promotion(**result[i]) for i in range(len(result))]
        return result


