from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ReadUpdateViewSet(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    pass


class CreateViewSet(GenericViewSet,
                    mixins.CreateModelMixin):
    pass
