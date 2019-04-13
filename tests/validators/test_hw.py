# ========================================================================== #
#                                                                            #
#    KVMD - The main Pi-KVM daemon.                                          #
#                                                                            #
#    Copyright (C) 2018  Maxim Devaev <mdevaev@gmail.com>                    #
#                                                                            #
#    This program is free software: you can redistribute it and/or modify    #
#    it under the terms of the GNU General Public License as published by    #
#    the Free Software Foundation, either version 3 of the License, or       #
#    (at your option) any later version.                                     #
#                                                                            #
#    This program is distributed in the hope that it will be useful,         #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#    GNU General Public License for more details.                            #
#                                                                            #
#    You should have received a copy of the GNU General Public License       #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.  #
#                                                                            #
# ========================================================================== #


from typing import Any

import pytest

from kvmd.validators import ValidatorError
from kvmd.validators.hw import valid_tty_speed
from kvmd.validators.hw import valid_gpio_pin
from kvmd.validators.hw import valid_gpio_pin_optional


# =====
@pytest.mark.parametrize("arg", ["1200 ", 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200])
def test_ok__valid_tty_speed(arg: Any) -> None:
    value = valid_tty_speed(arg)
    assert type(value) == int  # pylint: disable=unidiomatic-typecheck
    assert value == int(str(arg).strip())


@pytest.mark.parametrize("arg", ["test", "", None, 0, 1200.1])
def test_fail__valid_tty_speed(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        print(valid_tty_speed(arg))


# =====
@pytest.mark.parametrize("arg", ["0 ", 0, 1, 13])
def test_ok__valid_gpio_pin(arg: Any) -> None:
    value = valid_gpio_pin(arg)
    assert type(value) == int  # pylint: disable=unidiomatic-typecheck
    assert value == int(str(arg).strip())


@pytest.mark.parametrize("arg", ["test", "", None, -1, -13, 1.1])
def test_fail__valid_gpio_pin(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        print(valid_gpio_pin(arg))


# =====
@pytest.mark.parametrize("arg", ["0 ", -1, 0, 1, 13])
def test_ok__valid_gpio_pin_optional(arg: Any) -> None:
    value = valid_gpio_pin_optional(arg)
    assert type(value) == int  # pylint: disable=unidiomatic-typecheck
    assert value == int(str(arg).strip())


@pytest.mark.parametrize("arg", ["test", "", None, -2, -13, 1.1])
def test_fail__valid_gpio_pin_optional(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        print(valid_gpio_pin_optional(arg))