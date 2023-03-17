from handlers.handler_commands import HandlerCommands


class HandlerMain:
    def __init__(self, bot):
        self.bot = bot
        self.handler_commands = HandlerCommands(self.bot)

    def handle(self):
        self.handler_commands.handle()
