from ....models.models import Vote
from ...generics.delete import DeleteAction
from ...util.default_schema import DefaultSchema
from ...util.register import register_action


@register_action("vote.delete")
class VoteDelete(DeleteAction):
    """
    Action to delete votes.
    """

    model = Vote()
    schema = DefaultSchema(Vote()).get_delete_schema()
