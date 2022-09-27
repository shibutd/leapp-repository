from leapp.actors import Actor
from leapp.libraries.actor import scanvendorrepofiles
from leapp.models import CustomTargetRepository, CustomTargetRepositoryFile, ActiveVendorList
from leapp.tags import FactsPhaseTag, IPUWorkflowTag
from leapp.libraries.stdlib import api


class ScanVendorRepofiles(Actor):
    """
    Load and produce custom repository data from vendor-provided files.
    Only those vendors whose source system repoids were found on the system will be included.
    """

    name = "scan_vendor_repofiles"
    consumes = (ActiveVendorList)
    produces = (CustomTargetRepository, CustomTargetRepositoryFile)
    tags = (FactsPhaseTag, IPUWorkflowTag)

    def process(self):
        scanvendorrepofiles.process()