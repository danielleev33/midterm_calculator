from app.calculator_config import CalculatorConfig
from app.exceptions import ValidationError


def validate_number(value):
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"Invalid numeric input: {value}") from exc

    if abs(number) > CalculatorConfig.MAX_INPUT_VALUE:
        raise ValidationError(
            f"Input exceeds maximum allowed value of {CalculatorConfig.MAX_INPUT_VALUE}"
        )

    return number