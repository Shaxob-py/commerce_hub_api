from starlette_admin.contrib.sqla import ModelView


class ProductModelView(ModelView):
    fields = [
        "id",
        "name",
        "description",
        "views",
        "user_id",

    ]
    label = 'Trip'
    identity = 'Trip'
