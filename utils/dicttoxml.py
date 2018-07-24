
def get_node(key, value):
    """Take in two args and returns them in xml format."""
    return "<{key}> {value} </{key}>".format(key=key, value=value)


def dict_to_xml(obj, element_name):
    """Transform Objects key and value pair into xml format."""
    output = []
    for key in obj.keys():
        output.append(get_node(key, obj[key]))
        xml_string = "".join(output)
    return get_node(element_name, xml_string)


def list_to_xml(data, root_name="root", element_name="element"):
    """Return xml data.

    Loop through a list of objects and wrap each obj
    with an element name and finally wraps the list with a root name
    """
    output = []
    for obj in data:
        output.append(dict_to_xml(obj, element_name))
        xml_string = "".join(output)

    return '<?xml version="1.0" encoding="UTF-8"?>\n' + get_node(root_name, xml_string)
