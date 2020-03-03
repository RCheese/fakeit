from fakeit.exceptions import AdditionalRequirementError

try:
    pass
except ModuleNotFoundError as e:
    raise AdditionalRequirementError(e)

raise NotImplementedError
