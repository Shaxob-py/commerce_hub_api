from starlette_admin.contrib.sqla import Admin
from admin.auth import UsernameAndPasswordProvider
from admin.product import ProductModelView
from admin.user import UserModelView, AdminModelView, SupportMessageAdmin
from database import User, Product, SupportMessage
from database.base import db

admin = Admin(
    engine=db.engine,
    title="Trip",

    # templates_dir="templates",
    auth_provider=UsernameAndPasswordProvider()
)

admin.add_view(AdminModelView(User))
admin.add_view(ProductModelView(Product))
admin.add_view(UserModelView(User))
admin.add_view(SupportMessageAdmin(SupportMessage))
