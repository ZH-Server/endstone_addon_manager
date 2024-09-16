from endstone.command import Command, CommandSender
from endstone.plugin import Plugin

#from .addon_command import 

class AddonManager(Plugin):
    api_version = "0.5"

    def on_load(self) -> None:
        self.logger.info("Addon Manager has been loaded!")
    
    def on_enable(self) -> None:
        self.logger.info("Addon Manager has been enabled!")
    
    def on_disable(self) -> None:
        self.logger.info("Addon Manager has been disabled!")

    commands = {
        "addon": {
            "description": "Manage the resource and behavior packs",
            "usages": ["/addon (list|info|install|uninstall|enable|disable)<action: ManageAddon>"],
            "aliass": ["am"],
            "permissions": ["addon_manager.command.addon"],
        }
    }

    permissions = {
        "addon_manager.command.addon": {
            "description": "Allow server console and operators use /addon command",
            "default": "op",
        }
    }

    def on_command(self, sender: CommandSender, command: Command, args: list[str]) -> bool:
        if command.name == "addon":
            if args[0] == "list":
                pass
            if args[0] == "info":
                pass
            if args[0] == "install":
                pass
            if args[0] == "uninstall":
                pass
            if args[0] == "enable":
                pass
            if args[0] == "disable":
                pass
        return True
