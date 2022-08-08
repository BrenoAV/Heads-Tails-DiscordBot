import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from heads_or_tails import HeadsOrTails
import time

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


class MyBot(commands.Bot):
    def __init__(self, command_prefix) -> None:
        commands.Bot.__init__(self, command_prefix=command_prefix)
        self.game = HeadsOrTails()
        self.message_on_ready = "Bot is ready!!"
        self.chose_one = False # Variable to control if the first play is already played or not

        self.add_commands()
    
    async def on_ready(self):
        print(self.message_on_ready)

    def add_commands(self):
        @self.command(name="newgame")
        async def newgame(ctx):
            """Command to reset the game
            """
            self.game.new_game()
            self.chose_one = False
            await ctx.channel.send("A new game has created! Please, type your guesses.")

        @self.command(name='heads')
        async def heads(ctx):
            """Command to bet your guess in "heads". If you are the first player or if you are the second player"""
            if self.game.get_player1() == (None, None) and not self.chose_one:
                name = ctx.author.name
                guess = HeadsOrTails.GUESSES[0]
                self.game.set_player1(name=name, guess=guess)
                await ctx.channel.send(f'The **Player 1** "{name}" chose **"{guess}/Cara"**. Good Luck!')
                self.chose_one = True

            elif self.game.get_player2() == (None, None) and self.game.get_player1()[1] != HeadsOrTails.GUESSES[0] and \
                self.game.get_player1()[0] != ctx.author.name:

                name = ctx.author.name
                guess = HeadsOrTails.GUESSES[0]
                self.game.set_player2(name=name, guess=guess)
                await ctx.channel.send(f'The **Player 2** "{name}" chose **"{guess}/Cara"**. Good Luck!')
                result = self.game.play()
                time.sleep(2)
                await ctx.channel.send(f'\n#####################\n**THE RESULT IS...{result[0].upper()}**\n#####################')
                if result[1] == 1:
                    await ctx.channel.send(result[2])
                elif result[1] == 2:
                    await ctx.channel.send(result[2])
                self.chose_one = False
                self.game.new_game() # Reset the game

        @self.command(name='tails')
        async def tails(ctx):
            """Command to bet your guess in "tails". If you are the first player or if you are the second player"""
            if self.game.get_player1() == (None, None) and not self.chose_one:
                name = ctx.author.name
                guess = HeadsOrTails.GUESSES[1]
                self.game.set_player1(name=name, guess=guess)
                await ctx.channel.send(f'The **Player 1** "{name}" chose **"{guess}/Coroa"**. Good Luck!')
                self.chose_one = True

            elif self.game.get_player2() == (None, None) and self.game.get_player1()[1] != HeadsOrTails.GUESSES[1] and \
                self.game.get_player1()[0] != ctx.author.name:

                name = ctx.author.name
                guess = HeadsOrTails.GUESSES[1]
                self.game.set_player2(name=name, guess=guess)
                await ctx.channel.send(f'The **Player 2** "{name}" chose **"{guess}/Coroa"**. Good Luck!')
                result = self.game.play()
                time.sleep(2)
                await ctx.channel.send(f'\n#####################\n**THE RESULT IS... {result[0].upper()}**\n#####################')
                if result[1] == 1:
                    await ctx.channel.send(result[2])
                elif result[1] == 2:
                    await ctx.channel.send(result[2])
                self.chose_one = False
                self.game.new_game() # Reset the game


if __name__== "__main__":
    bot = MyBot(command_prefix=".")
    bot.run(TOKEN)
