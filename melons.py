"""Classes for melon orders."""

import random

from datetime import datetime

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    order_type = None
    tax = 0

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
    
    def get_base_price(self):
        """Generate base price randomly from 5-9"""

        self.base_price = random.randint(5,9)

        current_hour = datetime.now().hour
        current_weekday = datetime.now().weekday()

        if current_weekday < 5 and current_hour in range(8, 12):
            self.base_price = self.base_price + 4

    def get_total(self):
        """Calculate price, including tax."""

        total = (1 + self.tax) * self.qty * self.base_price

        if "Christmas" in self.species:
            total = (1 + self.tax) * self.qty * (1.5 * self.base_price)

        if self.order_type == "international" and self.qty <10:
          total =+ 3
        
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
 
        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):

    order_type = "government"
    tax = 0.00

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
 
        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection_passed(self, passed):
        """Record whether an order has passed inspection"""

        if passed == True:
            self.passed_inspection = True

        return self.passed_inspection 






