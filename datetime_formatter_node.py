import datetime

class NowFormatterNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "format": ("STRING", {"default": "yyyy-MM-dd-hhmmss"}),  # Default format
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("formatted_datetime",)
    FUNCTION = "format_datetime"
    CATEGORY = "utils"

    def format_datetime(self, format: str) -> tuple[str]:
        # Convert custom format to strftime format
        format = format.replace("yyyy", "%Y").replace("MM", "%m").replace("dd", "%d").replace("hh", "%H").replace("mm", "%M").replace("ss", "%S")
        
        # Get the current time and format it
        try:
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime(format)  # Use the user-provided format directly
            return formatted_time,
        except ValueError as e:
            raise ValueError(f"Invalid format: {str(e)}")

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")
