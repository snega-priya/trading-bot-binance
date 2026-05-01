from bot.client import get_client
import logging
from bot.logging_config import setup_logger

# initialize logger
setup_logger()

def place_market_order(symbol, side, quantity):
    client = get_client()

    try:
        logging.info(f"Placing MARKET order: {symbol} {side} {quantity}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        print("Order placed successfully ✅")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))

        logging.info(f"Order Response: {order}")

    except Exception as e:
        print("Error placing order ❌")
        print(e)
        logging.error(f"Error: {str(e)}")


def place_limit_order(symbol, side, quantity, price):
    client = get_client()

    try:
        logging.info(f"Placing LIMIT order: {symbol} {side} {quantity} @ {price}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        print("Limit order placed successfully ✅")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))

        logging.info(f"Order Response: {order}")

    except Exception as e:
        print("Error placing limit order ❌")
        print(e)
        logging.error(f"Error: {str(e)}")