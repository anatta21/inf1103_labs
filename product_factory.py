
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


# Registry for supported product types.
_REGISTRY = {
    PhysicalProduct.TYPE: lambda data: PhysicalProduct(
        data["product_id"],
        data["name"],
        data["price"],
        data["stock_quantity"],
        data.get("weight", 0.0)
    ),

    DigitalProduct.TYPE: lambda data: DigitalProduct(
        data["product_id"],
        data["name"],
        data["price"],
        data["stock_quantity"],
        data["download_size"]
    ),
}


def product_from_dict(data):
    """Reconstruct a product object from dictionary data."""

    try:
        # Support both old and new JSON field names.
        product_id = data.get("product_id", data.get("id"))
        stock_quantity = data.get(
            "stock_quantity", data.get("stock")
        )

        if product_id is None:
            raise ValueError("Missing product ID.")

        if stock_quantity is None:
            raise ValueError("Missing stock quantity.")

        # Standardise data types.
        product_data = {
            "product_id": str(product_id),
            "name": str(data["name"]),
            "price": float(data["price"]),
            "stock_quantity": int(stock_quantity),
            "weight": float(data.get("weight", 0.0)),
        }

        product_type = data.get("type", PhysicalProduct.TYPE)

        if product_type == DigitalProduct.TYPE:
            product_data["download_size"] = float(
                data["download_size"]
            )

        return _REGISTRY[product_type](product_data)

    except KeyError as error:
        raise ValueError(
            f"Cannot build product: missing field {error}"
        ) from error

    except (TypeError, ValueError) as error:
        raise ValueError(
            f"Invalid product data: {error}"
        ) from error
