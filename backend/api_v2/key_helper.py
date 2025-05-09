import logging

from django.core.exceptions import ValidationError
from pipeline_v2.models import Pipeline
from rest_framework.request import Request
from workflow_manager.workflow_v2.workflow_helper import WorkflowHelper

from api_v2.exceptions import UnauthorizedKey
from api_v2.models import APIDeployment, APIKey
from api_v2.serializers import APIKeySerializer

logger = logging.getLogger(__name__)


class KeyHelper:
    @staticmethod
    def validate_api_key(api_key: str, instance: APIDeployment | Pipeline) -> None:
        """Validate api key.

        Args:
            api_key (str): api key from request
            instance (Union[APIDeployment, Pipeline]): api or pipeline instance

        Raises:
            UnauthorizedKey: if not valid
        """
        try:
            api_key_instance: APIKey = APIKey.objects.get(api_key=api_key)
            if not KeyHelper.has_access(api_key_instance, instance):
                raise UnauthorizedKey()
        except (APIKey.DoesNotExist, ValidationError):
            raise UnauthorizedKey()

    @staticmethod
    def list_api_keys_of_api(api_instance: APIDeployment) -> list[APIKey]:
        api_keys: list[APIKey] = APIKey.objects.filter(api=api_instance).all()
        return api_keys

    @staticmethod
    def list_api_keys_of_pipeline(pipeline_instance: Pipeline) -> list[APIKey]:
        api_keys: list[APIKey] = APIKey.objects.filter(pipeline=pipeline_instance).all()
        return api_keys

    @staticmethod
    def has_access(api_key: APIKey, instance: APIDeployment | Pipeline) -> bool:
        """Check if the provided API key has access to the specified API
        instance.

        Args:
            api_key (APIKey): api key associated with  the instance
            instance (Union[APIDeployment, Pipeline]): api or pipeline instance

        Returns:
            bool: True if allowed to execute, False otherwise
        """
        if not api_key.is_active:
            return False
        if isinstance(instance, APIDeployment):
            return api_key.api == instance
        if isinstance(instance, Pipeline):
            return api_key.pipeline == instance
        return False

    @staticmethod
    def validate_workflow_exists(workflow_id: str) -> None:
        """Validate that the specified workflow_id exists in the Workflow
        model.
        """
        WorkflowHelper.get_workflow_by_id(workflow_id)

    @staticmethod
    def create_api_key(deployment: APIDeployment | Pipeline, request: Request) -> APIKey:
        """Create an APIKey entity using the data from the provided
        APIDeployment or Pipeline instance.
        """
        api_key_serializer = APIKeySerializer(
            data=deployment.api_key_data,
            context={"deployment": deployment, "request": request},
        )
        api_key_serializer.is_valid(raise_exception=True)
        api_key: APIKey = api_key_serializer.save()
        return api_key
