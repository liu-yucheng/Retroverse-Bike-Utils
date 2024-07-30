"""
(Private) no operation utilities.
"""

# Copyright (C) 2024 Yucheng Liu. Under the GNU AGPL 3.0 License.
# GNU AGPL 3.0 License available at: https://www.gnu.org/licenses/agpl-3.0.txt


class NoOpClass:
    """
    Defines no operation.
    """
    def __add__(self, other: any) -> any:
        return self

    def __sub__(self, other: any) -> any:
        return self

    def __mul__(self, other: any) -> any:
        return self

    def __pow__(self, other: any) -> any:
        return self

    def __truediv__(self, other: any) -> any:
        return self

    def __floordiv__(self, other: any) -> any:
        return self

    def __mod__(self, other: any) -> any:
        return self

    def __lshift__(self, other: any) -> any:
        return self

    def __rshift__(self, other: any) -> any:
        return self

    def __and__(self, other: any) -> any:
        return self

    def __or__(self, other: any) -> any:
        return self

    def __xor__(self, other: any) -> any:
        return self

    def __invert__(self) -> any:
        return self

    def __bool__(self) -> bool:
        return False

    def __int__(self) -> int:
        return 0

    def __float__(self) -> float:
        return 0.0

    def __list__(self) -> list:
        return []


no_op_obj = NoOpClass()
"""
No operation object.
"""
