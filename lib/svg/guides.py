import simpletransform

from ..utils import string_to_floats, Point, cache
from .tags import SODIPODI_NAMEDVIEW, SODIPODI_GUIDE, INKSCAPE_LABEL
from .units import get_doc_size, get_viewbox_transform


class InkscapeGuide(object):
    def __init__(self, node):
        self.node = node
        self.svg = node.getroottree().getroot()

        self._parse()

    def _parse(self):
        self.label = self.node.get(INKSCAPE_LABEL, "")

        doc_size = list(get_doc_size(self.svg))

        # convert the size from viewbox-relative to real-world pixels
        viewbox_transform = get_viewbox_transform(self.svg)
        simpletransform.applyTransformToPoint(simpletransform.invertTransform(viewbox_transform), doc_size)

        self.position = Point(*string_to_floats(self.node.get('position')))

        # inkscape's Y axis is reversed from SVG's, and the guide is in inkscape coordinates
        self.position.y = doc_size[1] - self.position.y

        # This one baffles me.  I think inkscape might have gotten the order of
        # their vector wrong?
        parts = string_to_floats(self.node.get('orientation'))
        self.direction = Point(parts[1], parts[0])


@cache
def get_guides(svg):
    """Find all Inkscape guides and return as InkscapeGuide instances."""

    namedview = svg.find(SODIPODI_NAMEDVIEW)
    if namedview is None:
        return []

    return [InkscapeGuide(node) for node in namedview.findall(SODIPODI_GUIDE)]
