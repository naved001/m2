from ims.exception.exception import ISCSIException


class TargetExistsException(ISCSIException):
    """ Should be raised when target already exists """

    @property
    def status_code(self):
        return 500

    def __str__(self):
        return "Target Already Exists"


class TargetDoesntExistException(ISCSIException):
    """ Should be raised when target doesnt exist """

    @property
    def status_code(self):
        return 500

    def __str__(self):
        return "Target Doesnt Exist"


class TargetCreationFailed(ISCSIException):
    """ Should be raised when target creation failed """

    @property
    def status_code(self):
        return 500

    def __init__(self, error):
        self.error = error

    def __str__(self):
        return "Target Creation Failed with error {0}".format(self.error)


class TargetDeletionFailed(ISCSIException):
    """ Should be raised when target deletion failed """

    @property
    def status_code(self):
        return 500

    def __init__(self, error):
        self.error = error

    def __str__(self):
        return "Target Deletion Failed with error {0}".format(self.error)


class ListTargetFailedException(ISCSIException):
    """ Should be raised when listing targets failed """

    @property
    def status_code(self):
        return 500

    def __init__(self, error):
        self.error = error

    def __str__(self):
        return "List Target Failed with error {0}".format(self.error)


class StartFailedException(ISCSIException):
    """ Should be raised when starting iscsi failed """

    @property
    def status_code(self):
        return 500

    def __str__(self):
        return "ISCSI Failed to Start"


class InconsistentTargets(ISCSIException):
    """ Should be raised when checking of iscsi server fails"""

    @property
    def status_code(self):
        return 500

    def __str__(self):
        return "iSCSI targets are not in sync. Tell an admin about it please."


class PSSHException(ISCSIException):
    """Raised when there's an authentication with the pssh module"""

    @property
    def status_code(self):
        return 500

    def __init__(self, error):
        self.error = error

    def __str__(self):
        return "PSSH reports an error {0}".format(self.error)
