import json
import logging
import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def render_index(template_dir, data, output_file):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("base.html")

    with open(data, "r", encoding="utf-8") as f:
        cards = json.load(f)

    rendered_html = template.render(
        cards=cards,
        apps=cards,
        year=datetime.now().year
    )

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(rendered_html)
    logging.info(f"> Rendered {output_file} with data from {data}")


if __name__ == "__main__":
    render_index(
        template_dir="templates",
        data=os.path.join("data", "data.json"),
        output_file="index.html",
    )
