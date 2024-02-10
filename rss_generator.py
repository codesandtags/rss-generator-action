from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

def generate_rss_xml(data):
    rss = Element('rss')
    rss.set('version', '2.0')
    
    channel = SubElement(rss, 'channel')
    
    title = SubElement(channel, 'title')
    title.text = data['rss_feed']['title']
    
    link = SubElement(channel, 'link')
    link.text = data['rss_feed']['link']
    
    description = SubElement(channel, 'description')
    description.text = data['rss_feed']['description']
    
    language = SubElement(channel, 'language')
    language.text = data['rss_feed']['language']
    
    lastBuildDate = SubElement(channel, 'lastBuildDate')
    lastBuildDate.text = data['rss_feed']['lastBuildDate']
    
    updatePeriod = SubElement(channel, 'updatePeriod')
    updatePeriod.text = data['rss_feed']['updatePeriod']
    
    for article in data['rss_feed']['articles']:
        item = SubElement(channel, 'item')
        
        item_title = SubElement(item, 'title')
        item_title.text = article['title']
        
        item_link = SubElement(item, 'link')
        item_link.text = article['link']
        
        item_description = SubElement(item, 'description')
        item_description.text = article['description']
        
        item_author = SubElement(item, 'author')
        item_author.text = article['author']
        
        item_pubDate = SubElement(item, 'pubDate')
        item_pubDate.text = article['pubDate']
        
        item_category = SubElement(item, 'category')
        item_category.text = article['category']
    
    return parseString(tostring(rss)).toprettyxml(indent="  ")


def write_rss_to_file(xml_content, filename="newsletter.xml"):
    with open(filename, "w") as file:
        file.write(xml_content)