# NowFormatterNode

一个为 ComfyUI 设计的自定义节点，允许用户根据指定的格式获取当前日期和时间。

[English Documentation (README.md)](README.md)

## 概述

`NowFormatterNode` 类提供了一种通过自定义格式获取当前日期和时间的方式。用户可以指定格式模式，该模式将被转换为 `strftime` 格式，以生成当前日期和时间的格式化字符串。

## 使用说明

### 输入

- `format`（字符串）：所需的日期和时间格式。默认为 `"yyyy-MM-dd-hhmmss"`。
    - 使用以下符号：
        - `yyyy`：完整年份（如 2024）
        - `YY`：年份（如 24）
        - `MM`：月份（01 到 12）
        - `dd`：日期（01 到 31）
        - `hh`：24 小时制小时数（00 到 23）
        - `mm`：分钟（00 到 59）
        - `ss`：秒数（00 到 59）

### 输出

- `formatted_datetime`（字符串）：根据指定输入格式的当前日期和时间。

## 示例

将当前日期和时间格式化为 `"2024-11-03-142530"` 的示例：
1. 将 `format` 设置为 `"yyyy-MM-dd-hhmmss"`。
2. 输出将根据当前日期和时间进行格式化。

## 代码结构

该节点使用 `strftime` 函数生成格式化的日期和时间。若格式指定有误，将抛出带有详细信息的 `ValueError` 错误。

## 开发

### 类结构

- **`INPUT_TYPES`**：指定 `format` 输入。
- **`RETURN_TYPES` 和 `RETURN_NAMES`**：定义输出类型和名称为 `formatted_datetime`。
- **`format_datetime` 方法**：格式化日期和时间的主函数。
- **`IS_CHANGED` 方法**：返回 NaN 表示此节点没有状态，不会触发更改。

## 错误处理

若 `format` 模式无效，将抛出 `ValueError` 以指出问题。

如需英文说明，请参考 [English Documentation (README.md)](README.md)。

---

