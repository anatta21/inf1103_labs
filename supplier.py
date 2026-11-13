class Supplier:
    """Represents a supplier associated with a product."""

    def __init__(self, supplier_id, name, contact_email):
        self._supplier_id = supplier_id
        self._name = name
        self._contact_email = contact_email

    @property
    def supplier_id(self):
        return self._supplier_id

    @property
    def name(self):
        return self._name

    @property
    def contact_email(self):
        return self._contact_email

    def display_information(self):
        """Display supplier information."""
        print(
            f"Supplier ID: {self._supplier_id} | "
            f"Name: {self._name} | "
            f"Email: {self._contact_email}"
        )

    def to_dict(self):
        """Convert supplier information into a dictionary."""
        return {
            "supplier_id": self._supplier_id,
            "name": self._name,
            "contact_email": self._contact_email
        }
