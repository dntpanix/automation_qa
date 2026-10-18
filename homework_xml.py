
import logging
import xml.etree.ElementTree as ET
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

xml_file = Path("ideas_for_test/work_with_xml/groups.xml")


def get_incoming_by_group_number(group_number):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")

        if number is not None and number.text == str(group_number):
            incoming = group.find("timingExbytes/incoming")

            if incoming is not None:
                logging.info(
                    "Group %s: incoming = %s",
                    group_number,
                    incoming.text
                )
                return incoming.text

            logging.info(
                "Group %s does not have an incoming value",
                group_number
            )
            return None

    logging.info("Group %s was not found", group_number)
    return None


group_number = input("Enter group number: ")
get_incoming_by_group_number(group_number)
