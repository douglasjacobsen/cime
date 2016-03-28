"""
Interface to the config_component.xml files.  This class inherits from EntryID.py
"""
from standard_module_setup import *

from entry_id import EntryID
from CIME.utils import expect, get_cime_root, get_model

logger = logging.getLogger(__name__)

class Component(EntryID):

    def __init__(self,infile):
        """
        initialize an object
        """
        EntryID.__init__(self,infile)

    def get_value(self, name, attribute={}, resolved=False):
        return EntryID.get_value(self, name, attribute, resolved)

    def get_valid_model_components(self):
        """
        return a list of all possible valid generic (e.g. atm, clm, ...) model components
        from the entries in the model CONFIG_DRV_FILE
        """
        components = []
        comps = self.get_nodes("comp", root=self.get_node("components"))
        for comp in comps:
            components.append(comp.text)
        return components

    def print_values(self):
        """
        print values for help and description in target config_component.xml file
        """
        rootnode = self.get_node("help")
        helptext = rootnode.text

        rootnode = self.get_node("description")
        compsets = {}
        descs = self.get_nodes("desc", root=rootnode)
        for desc in descs:
            attrib = desc.attrib["compset"]
            text = desc.text
            compsets[attrib] = text

        logger.info(" %s" %helptext)
        for v in compsets.iteritems():
            label, definition = v
            logger.info("   %20s : %s" %(label, definition))

