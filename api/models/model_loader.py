from . import orders, order_details, recipes, resources, payment, promotions, account, menu_item, feedback

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    account.Base.metadata.create_all(engine)
    menu_item.Base.metadata.create_all(engine)
    feedback.Base.metadata.create_all(engine)
