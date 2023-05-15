class MultipleSerializerMixin:
    details_serializer_class = None

    def get_serializer_class(self):
        if self.action == "retrieve" and self.details_serializer_class is not None:
            return self.details_serializer_class

        return super().get_serializer_class()

class EnablePartialUpdateMixin:

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True

        return super().update(request, *args, **kwargs)
