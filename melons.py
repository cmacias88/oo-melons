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

        if qty >= 100:
            raise TooManyMelonsError("Too many melons!")
    
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

class TooManyMelonsError(ValueError):
    
    pass




# ALTERNATE SOLUTION:
# """Classes for melon orders."""
# from itertools import count
# import random
# import datetime

# class AbstractMelonOrder:
#     """An abstract base class that other Melon Orders inherit from."""

#     # the following 2 lines can be included, but are not necessary because 
#     # AbstractMelonOrder should never be instantiated directly

#     order_type = None
#     tax = 0

#     def __init__(self, species, qty, country_code=None):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.shipped = False
#         self.country_code = country_code

#         try:
#             if self.qty > 100:
#                 raise TooManyMelonsError

#         except TooManyMelonsError:          
#             print("TOO MANY MELONS")     


#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = self.get_base_price()

#         if self.species == "christmas":
#             base_price = base_price * 1.5

#         total = (1 + self.tax) * self.qty * base_price

#         return total


#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True


#     def get_base_price(self):

#         random_base_price = random.randint(5, 9)

#         # Returning today's date and time (year, month, day, hour, minute, etc.), store in current_datetime
#         current_datetime = datetime.datetime.now()
#         # Get integer representing weekday of current_date (0 = Mon; 6 = Sun)
#         weekday_number = current_datetime.weekday()
#         # Get current hour by looking at hour attribute of current_datetime
#         current_hour = current_datetime.hour

#         # Check if hour between 8 and 11 + if weekday is Mon (0) - Fri (5)
#         # If yes, add $4 to random_base_price
#         if current_hour in range(8,12) and weekday_number in range(0,5):
#             random_base_price += 4

#         return random_base_price


# class DomesticMelonOrder(AbstractMelonOrder):
#     """A melon order within the USA."""

#     order_type = "domestic"
#     tax = 0.08


# class InternationalMelonOrder(AbstractMelonOrder):
#     """An international (non-US) melon order."""

#     order_type = "international"
#     tax = 0.17

#     def get_total(self):
#         """Check if order qty is less than 10 and add fee"""

#         if self.qty < 10:
#             total = super().get_total() + 3
#         else:
#             total = super().get_total()
        
#         return total

#     def get_country_code(self):
#         """Return the country code."""

#         return self.country_code



# class GovernmentMelonOrder(AbstractMelonOrder):
#     """A U.S. government melon order."""
#     order_type = 'government'
#     tax = 0
#     passed_inspection = False

#     def mark_inspection(self, passed):
    
#         if passed == True:
#             self.passed_inspection = True

# class TooManyMelonsError(ValueError):

#     pass





