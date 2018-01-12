"""Classes for melon orders."""

from random import randint


class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        """Sets base price for melon order."""

        return randint(5, 9)

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == 'christmas':
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price, including tax, and intl order fee."""

        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3

        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order, exempt from tax, must be inspected"""

    order_type = "government"
    tax = 0

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Updates the attribute passed_inspection"""

        self.passed_inspection = passed
