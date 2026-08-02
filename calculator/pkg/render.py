# calculator/pkg/render.py

import json
import math


def format_json_output(expression: str, result: float, indent: int = 2) -> str:
    if isinstance(result, float) and not math.isfinite(result):
        raise ValueError(f"result is not a finite number: {result}")

    if isinstance(result, float) and result.is_integer():
        result_to_dump = int(result)
    else:
        result_to_dump = result

    output_data = {
        "expression": expression,
        "result": result_to_dump,
    }
    return json.dumps(output_data, indent=indent)
