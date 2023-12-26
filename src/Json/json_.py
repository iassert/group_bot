import os
import json

from typing import Any

from Log.log import Log


class Json_:	
    def path(name: str, ex: str = "json") -> str:
        return os.path.abspath(__file__).replace(os.path.basename(__file__), f"{name}.{ex}")

    def read(name: str, default: Any = None) -> Any | None:
        path = Json_.path(name)

        if os.path.exists(path):
            try:
                with open(path, "r", encoding = "utf8") as f:
                    return json.load(f)
            except Exception as ex:
                Log("json").error(ex)
        return default

    def write(name: str, data: Any) -> None:
        path = Json_.path(name)

        try:
            with open(path, "w", encoding = "utf8") as f:
                json.dump(data, f, indent = 4, ensure_ascii = False)
        except Exception as ex:
                Log("json").error(ex)
