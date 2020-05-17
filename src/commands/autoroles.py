from resources.structures.Bloxlink import Bloxlink # pylint: disable=import-error
from resources.constants import DEFAULTS

@Bloxlink.command
class AutoRolesCommand(Bloxlink.Module):
    """completely update members that join the server. by default, this is ENABLED."""

    def __init__(self):
        self.permissions = Bloxlink.Permissions().build("BLOXLINK_MANAGER")
        self.category = "Administration"
        self.hidden = True

    async def __main__(self, CommandArgs):
        response = CommandArgs.response
        guild_data = CommandArgs.guild_data

        toggle = not guild_data.get("autoRoles", DEFAULTS.get("autoRoles"))

        guild_data["autoRoles"] = toggle

        await self.r.db("canary").table("guilds").insert(guild_data, conflict="update").run()

        if toggle:
            await response.success("Successfully **enabled** Auto-Roles!")
        else:
            await response.success("Successfully **disabled** Auto-Roles!")