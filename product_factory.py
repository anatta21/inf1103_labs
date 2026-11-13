from digital_product import DigitalProduct
from physical_product import PhysicalProduct
from supplier import Supplier

# Registry for supported product types.

_REGISTRY = {

    PhysicalProduct.TYPE: lambda data: PhysicalProduct(
        data["product_id"],
        data["name"],
        data["price"],
        data["stock_quantity"],
        data.get("weight", 0.0),
        data["supplier"]
    ),

    DigitalProduct.TYPE: lambda data: DigitalProduct(
        data["product_id"],
        data["name"],
        data["price"],
        data["stock_quantity"],
        data["download_size"],
        data["supplier"]
    ),

}


def product_from_dict(data):
    """Reconstruct a product object from dictionary data."""

    try:
        # Support both old and new product field names.

        product_id = data.get("product_id", data.get("id"))

        stock_quantity = data.get(
            "stock_quantity", data.get("stock")
        )

        if product_id is None:
            raise ValueError("Missing product ID.")

        if stock_quantity is None:
            raise ValueError("Missing stock quantity.")

        # Reconstruct supplier object.

        supplier_data = data["supplier"]

        supplier = Supplier(
            supplier_data["supplier_id"],
            supplier_data["name"],
            supplier_data["contact_email"]
        )

        # Standardise data types.

        product_data = {
            "product_id": str(product_id),
            "name": str(data["name"]),
            "price": float(data["price"]),
            "stock_quantity": int(stock_quantity),
            "weight": float(data.get("weight", 0.0)),
            "supplier": supplier
        }

        product_type = data.get("type", PhysicalProduct.TYPE)

        if product_type == DigitalProduct.TYPE:
            product_data["download_size"] = float(
                data["download_size"]
            )

        if product_type not in _REGISTRY:
            raise ValueError(
                f"Unsupported product type: {product_type}"
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
