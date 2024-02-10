import yaml

from rss_reader import read_yaml_data
from rss_generator import generate_rss_xml, write_rss_to_file


if __name__ == "__main__":
    yaml_data = read_yaml_data('feed.yaml')  # Ensure 'data.yaml' contains your YAML data
    rss_xml = generate_rss_xml(yaml_data)
    write_rss_to_file(rss_xml)