from fakeit.exceptions import AdditionalRequirementError

try:
    import sqlalchemy
except ModuleNotFoundError as e:
    raise AdditionalRequirementError(e)
