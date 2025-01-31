from . import account, menu_item, order_details, orders, payment, promotions, recipes, resources, feedback


def load_routes(app):
    app.include_router(account.router)
    app.include_router(menu_item.router)
    app.include_router(order_details.router)
    app.include_router(orders.router)
    app.include_router(payment.router)
    app.include_router(promotions.router)
    app.include_router(recipes.router)
    app.include_router(resources.router)
    app.include_router(feedback.router)
