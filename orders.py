from bot.client import get_client
import logging

client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        response = client.futures_create_order(**params)

        logging.info(f"Order Response: {response}")

        return response

    except Exception as e:
        logging.error(f"Error placing order: {e}")
        return None
