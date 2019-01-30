from fakeit.exceptions import AdditionalRequirementError

try:
    import django
except ModuleNotFoundError as e:
    raise AdditionalRequirementError(e)

raise NotImplementedError