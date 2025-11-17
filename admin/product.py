from starlette_admin.contrib.sqla import ModelView


class ProductModelView(ModelView):
    fields = [
        "id",
        "name",
        "days",
        "description",
        "view",
        "user_id",

    ]
    label = 'Trip'
    identity = 'Trip'
