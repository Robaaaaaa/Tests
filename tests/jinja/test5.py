import jinja2
env = jinja2.Environment()
template = env.from_string("""
My favorite fruits are:
{% for fruit in fruits -%}
- {{ fruit }}
{% endfor %}
""")

print(template.render(fruits=["mangoes", "bananas"]))

