import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

parser = argparse.ArgumentParser(description="Trading Bot CLI")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    # VALIDATION
    validate_symbol(args.symbol)
    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)
    validate_price(args.price)

    # ORDER EXECUTION
    if args.type == "MARKET":
        place_market_order(args.symbol, args.side, args.quantity)

    elif args.type == "LIMIT":
        if args.price is None:
            print("Price required for LIMIT order ❌")
        else:
            place_limit_order(args.symbol, args.side, args.quantity, args.price)

except Exception as e:
    print("Validation Error ❌")
    print(e)