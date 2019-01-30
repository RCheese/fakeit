class BaseFakeItException(Exception):
    message = None

    def __init__(self, message=None):
        if not message:
            message = self.message
        super().__init__(message)


class FakeItException(BaseFakeItException):
    message = "Unknown exception"


class OutOfRangeException(BaseFakeItException):
    message = "Out of range"


class EmptyException(BaseFakeItException):
    message = "Empty value"


class InvalidRange(BaseFakeItException):
    message = "Ivalid range"


class EmptyAlphabet(BaseFakeItException):
    message = "Empty alphabet"


class InvalidValue(BaseFakeItException):
    message = "Invalid value"


class AdditionalRequirementError(BaseFakeItException):
    message = "Install additional requirement for use submodule. ({outer_error})"

    def __init__(self, message=None):
        if not message:
            message = self.message
        message = self.message.format(outer_error=message)
        super().__init__(message)


class FuckIt(BaseFakeItException):
    message = "F*CK"
