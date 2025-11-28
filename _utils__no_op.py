"""
(Private) no operation utilities.
"""

# Copyright (C) 2024-2025 Yucheng Liu. Under the GNU AGPL 3.0 License.
# GNU AGPL 3.0 License available at: https://www.gnu.org/licenses/agpl-3.0.txt .


class NoOp_Class:
    """A class with no operation."""
    def __add__(self, other: any) -> any:
        return self
    # end def

    def __sub__(self, other: any) -> any:
        return self
    # end def

    def __mul__(self, other: any) -> any:
        return self
    # end def

    def __pow__(self, other: any) -> any:
        return self
    # end def

    def __truediv__(self, other: any) -> any:
        return self
    # end def

    def __floordiv__(self, other: any) -> any:
        return self
    # end def

    def __mod__(self, other: any) -> any:
        return self
    # end def

    def __lshift__(self, other: any) -> any:
        return self
    # end def

    def __rshift__(self, other: any) -> any:
        return self
    # end def

    def __and__(self, other: any) -> any:
        return self
    # end def

    def __or__(self, other: any) -> any:
        return self
    # end def

    def __xor__(self, other: any) -> any:
        return self
    # end def

    def __invert__(self) -> any:
        return self
    # end def

    def __bool__(self) -> bool:
        return False
    # end def

    def __int__(self) -> int:
        return 0
    # end def

    def __float__(self) -> float:
        return 0.0
    # end def

    def __list__(self) -> list:
        return []
    # end def


no_op_obj = NoOp_Class()
"""A no operation object."""
