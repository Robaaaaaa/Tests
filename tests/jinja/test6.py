import jinja2

template = env.from_string("""
Book titles are:
{% for book in books -%}
-{{book}}
{% endfor %}
""")

print(template.render(books = ["Diary of a Wimpy Kid", "Lord of Light"]))
