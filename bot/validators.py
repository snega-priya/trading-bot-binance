def validate_symbol(symbol):
    if not isinstance(symbol, str):
        raise ValueError("Symbol must be a string")
    
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must end with USDT (e.g., BTCUSDT)")


def validate_side(side):
    if not isinstance(side, str):
        raise ValueError("Side must be a string")
    
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be either BUY or SELL")


def validate_order_type(order_type):
    if not isinstance(order_type, str):
        raise ValueError("Order type must be a string")
    
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")


def validate_quantity(quantity):
    if not isinstance(quantity, (int, float)):
        raise ValueError("Quantity must be a number")
    
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")


def validate_price(price):
    if price is not None:
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")
        
        if price <= 0:
            raise ValueError("Price must be greater than 0")