import komand
from .schema import GetUsersInput, GetUsersOutput, Input, Output, Component
# Custom imports below


class GetUsers(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_users',
                description=Component.DESCRIPTION,
                input=GetUsersInput(),
                output=GetUsersOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
