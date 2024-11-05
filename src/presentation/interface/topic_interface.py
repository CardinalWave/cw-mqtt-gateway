#pylint: disable=unnecessary-pass
from abc import ABC, abstractmethod

class TopicInterface(ABC):
    """Interface for topic handling."""

    @abstractmethod
    def handle(self, input_object: any) -> any:
        """Handle topic input.

        This method should be implemented by subclasses to handle input
        related to the topic.

        Args:
            self: Instance of class
            input_object: Object to be manipulated.

        Returns:
            Result of object manipulation by internal services.
        """
        pass
