import math


class Vect:

    __slots__ = ("x", "y")

    # Constructors

    def __init__(self, x=None, y=None):
        """
        If y is not filled in, it takes the value of x.
        And if neither of them is filled in, then it is a null vector.
        """

        if y is None:
            if x is None:
                x = y = 0
            else:
                y = x
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x = x
            self.y = y
        else:
            raise TypeError

    @classmethod
    def from_polar(cls, norm, angle):
        if isinstance(norm, (int, float)) and isinstance(angle, (int, float)):
            return norm * cls(math.cos(angle), math.sin(angle))
        raise TypeError

    # Properties

    @property
    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)

    @property
    def angle(self):
        if self.x == 0:
            if self.y > 0:
                return math.pi / 2
            elif self.y < 0:
                return - math.pi / 2
            else:
                return 0
        return math.atan(self.y / self.x)

    @property
    def center(self):
        return self / 2

    # Methods

    def normalize(self):
        self.x /= self.norm
        self.y /= self.norm

    # Containers

    def __getitem__(self, key):
        if key in (0, "x"):
            return self.x
        elif key in (1, "y"):
            return self.y
        raise KeyError(key)

    def __setitem__(self, key, value):
        if isinstance(value, (int, float)):
            if key in (0, "x"):
                self.x = value
            elif key in (1, "y"):
                self.y = value
            else:
                raise KeyError(key)
        raise TypeError

    def __contains__(self, value):
        return value in (self.x, self.y)

    def __len__(self):
        return self.norm

    # Comparisons

    def __eq__(self, other):
        if isinstance(other, Vect):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Vect):
            return self.norm < other.norm
        return False

    def __le__(self, other):
        if isinstance(other, Vect):
            return self.norm <= other.norm
        return False

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    # Sign

    def __pos__(self):
        return self

    def __neg__(self):
        return Vect(-self.x, -self.y)

    def __abs__(self):
        return Vect(abs(self.x), abs(self.y))

    # Operations

    def dot(self, other):
        if isinstance(other, Vect):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Vect):
            return Vect(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vect(self.x + other, self.y + other)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(-other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, Vect):
            return Vect(self.x * other.x, self.y * other.y)
        elif isinstance(other, (int, float)):
            return Vect(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Vect):
            return Vect(self.x / other.x, self.y / other.y)
        elif isinstance(other, (int, float)):
            return self * (1 / other)
        return NotImplemented

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __floordiv__(self, other):
        if isinstance(other, Vect):
            return Vect(self.x // other.x, self.y // other.y)
        elif isinstance(other, (int, float)):
            return Vect(self.x // other, self.y // other)
        return NotImplemented

    def __rfloordiv__(self, other):
        return self.__floordiv__(other)

    def __ifloordiv__(self, other):
        return self.__floordiv__(other)

    def __mod__(self, other):
        if isinstance(other, Vect):
            return Vect(self.x % other.x, self.y % other.y)
        elif isinstance(other, (int, float)):
            return Vect(self.x % other, self.y % other)
        return NotImplemented

    def __rmod__(self, other):
        return self.__mod__(other)

    def __imod__(self, other):
        return self.__mod__(other)

    def __pow__(self, power, modulo=None):
        if isinstance(power, (int, float)):
            return Vect(self.x ** power, self.y ** power)
        return NotImplemented

    def __ipow__(self, other):
        return self.__pow__(other)

    # Conversions

    def __str__(self):
        return self.__repr__()

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __round__(self, n=None):
        return Vect(round(self.x, n), round(self.y, n))

    def list(self):
        return [self.x, self.y]

    def tuple(self):
        return (self.x, self.y)

    # Other

    def __repr__(self):
        return f"Vect({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def copy(self):
        return Vect(self.x, self.y)