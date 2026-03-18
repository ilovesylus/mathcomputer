# Author: [Your Name]
# Date: [Date of Creation or Last Update]
# Purpose:

class Polynomial:
    """
    Class implementation of a polynomial. The polynomial coefficients are
    represented in a list in descending order of their degrees.
    """
    def __init__(self, coefficients):
        """
        Initialize the Polynomial instance.

        Args:
            coefficients (list): A list of coefficients, starting with the
                                 coefficient of the highest degree term.
        """


    def __add__(self, other):
        """
        Add two polynomials.

        Args:
            other (Polynomial): Another Polynomial instance to add.

        Returns:
            Polynomial: The sum of the two polynomials.
        """


    def __sub__(self, other):
        """
        Subtract one polynomial from another.

        Args:
            other (Polynomial): Another Polynomial instance to subtract.

        Returns:
            Polynomial: The result of the subtraction.
        """


    def __mul__(self, other):
        """
        Multiply two polynomials.

        Args:
            other (Polynomial): Another Polynomial instance to multiply with.

        Returns:
            Polynomial: The product of the two polynomials.
        """


    def __neg__(self):
        """
        Negate the polynomial.

        Returns:
            Polynomial: A new Polynomial instance representing the negation of the current polynomial.
        """


    #### Do not modify the code below ####
    def __str__(self):
        """
        String representation of the polynomial.

        """
        terms = []
        first_term = True

        for i, coeff in enumerate(self._coeff):
            power = len(self._coeff) - i - 1
            if abs(coeff) > 1e-9:
                # Format coefficient and power
                coeff_str = "" if abs(coeff) == 1 and power != 0 else f"{coeff:.4f}".rstrip('0').rstrip('.')
                if power == 0:
                    term = coeff_str
                elif power == 1:
                    term = f"{coeff_str}x"
                else:
                    term = f"{coeff_str}x^{power}"
                # Add sign and format term
                if coeff > 0 and not first_term:
                    term = "+ " + term
                elif coeff < 0:
                    term = "- " + term.lstrip('-')
                terms.append(term)
                first_term = False

        return ' '.join(terms) if terms else "0"

    def __repr__(self):
        """
        Official string representation of the polynomial, for debugging.

        """
        return f"Polynomial({self._coeff})"
    #### Do not modify the code above ####