from .datetime_formatter_node import NowFormatterNode

NODE_CLASS_MAPPINGS = {
    "DateTimeFormatterNode": NowFormatterNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DateTimeFormatterNode": "DateTime Formatter"
}

__all__ = ["NODE_CLASS_MAPPINGS"]