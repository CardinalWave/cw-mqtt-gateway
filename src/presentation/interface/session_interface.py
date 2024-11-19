#pylint: disable=unnecessary-pass
from abc import ABC, abstractmethod

class SessionInterface(ABC):
    """Interface for sessions."""

    @abstractmethod
    def package(self) -> any:
        """Package the session data.

        This method should be implemented by subclasses to package the session
        data into a suitable format for storage or transmission.

        Returns:
            Session Object in String Format
        """
        pass
