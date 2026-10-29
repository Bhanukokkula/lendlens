{% macro default_rate(default_column) %}
    round(avg({{ default_column }}) * 100, 2)
{% endmacro %}