# def get_queryset(self):
#     if getattr(self, 'swagger_fake_view', False):
#         # queryset just for schema generation metadata
#         return Activity.objects.none()