from abc import ABC, abstractmethod
import discord

from typing import Optional, List

from .base import Command
from .config import Config

config = Config()


class Category(ABC):
    """ Template for category classes. """

    name: Optional[str] = None
    prefix: Optional[str] = None
    commands: List[Command] = []

    def __init__(self) -> None:
        """ Initialize the category. """
        self.commands_map: Callable[..., Dict[str, Command]] = lambda: {
            command.name: command for command in self.commands if command.name
        }

        if not self.name:
            raise ValueError("Category name is required")

    @abstractmethod
    def check_permissions(self, message: discord.Message) -> bool:
        raise NotImplementedError("Check permissions method is required")


class FunCategory(Category):
    """ A command category instance. """
    name = "fun"
    prefix = None

    def check_permissions(self, message: discord.Message) -> bool:
        return True


class UtilityCategory(Category):
    """ A command category instance. """
    name = "utility"
    prefix = "utils"

    def check_permissions(self, message: discord.Message) -> bool:
        return True

class DistroCategory(Category):
    """ A command category instance. """
    name = "distroroles"
    prefix = "distro"

    def check_permissions(self, message: discord.Message) -> bool:
        return True


class ModCategory(Category):
    """ A command category instance. """
    name = "mod"
    prefix = "mod"

    def check_permissions(self, message: discord.Message) -> bool:
        # Checking for everyone who are a mod in the server. Usually the server has more mod roles than just one
        for i in message.author.roles:
            if i.id in config.mod_role_id:
                return True

        return False
class RequestCategory(Category):

    name = "request"
    prefix = "req"

    def check_permissions(self, message: discord.Message) -> bool:
        return True


if __name__ == "__main__":
    print("I had a dream where I was fighting Chuck Norris. That day I woke up with scars.")
