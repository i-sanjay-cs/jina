from typing import Iterable, TYPE_CHECKING

__all__ = ['DocGroundtruthPair']

if TYPE_CHECKING:
    from . import Document


class DocGroundtruthPair:
    """
    Helper class to expose common interface to the traversal logic of the BaseExecutable Driver.
    It is important to note that it checks the matching structure of `docs` and `groundtruths`. It is important while
    traversing to ensure that then the driver can be applied at a comparable level of granularity and adjacency.
    This does not imply that you can't compare at the end a document with 10 matches with a groundtruth with 20 matches

    :param doc: Target `Document`.
    :param groundtruth: The :class:`Document` with desired state.
    """

    def __init__(self, doc: 'Document', groundtruth: 'Document'):
        """Set constructor method.

        :param doc: actual Document
        :param groundtruth: groundtruth Document
        """
        self.doc = doc
        self.groundtruth = groundtruth

    @property
    def matches(self) -> Iterable['DocGroundtruthPair']:
        """Get the pairs between matches and Groundtruth.

        :yields: DocGroundtruthPair object
        """
        assert len(self.doc.matches) == len(self.groundtruth.matches)
        for doc, groundtruth in zip(self.doc.matches, self.groundtruth.matches):
            yield DocGroundtruthPair(doc, groundtruth)

    @property
    def chunks(self) -> Iterable['DocGroundtruthPair']:
        """Get the pairs between chunks and Groundtruth.

        :yields: DocGroundtruthPair object
        """
        assert len(self.doc.chunks) == len(self.groundtruth.chunks)
        for doc, groundtruth in zip(self.doc.chunks, self.groundtruth.chunks):
            yield DocGroundtruthPair(doc, groundtruth)
