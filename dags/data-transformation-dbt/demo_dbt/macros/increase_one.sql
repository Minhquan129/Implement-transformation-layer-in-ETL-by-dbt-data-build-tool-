-- Using macro as if you are writing a function
{% macro increase_one(column_name) %}
    ({{ column_name }} + 1)
{% endmacro %}