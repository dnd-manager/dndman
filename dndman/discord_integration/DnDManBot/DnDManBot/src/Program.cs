// using System;
// using System.Threading.Tasks;
// using Discord;
// using Discord.WebSocket;

using System;

namespace DnDManBot
{
    // public class Program
    // {
    //     public static void Main()
    //     {
    //         MainAsync().GetAwaiter().GetResult();
    //     }
    //
    //     public static DiscordSocketClient Client;
    //
    //     private static async Task MainAsync()
    //     {
    //         Client = new DiscordSocketClient();
    //         Client.Log += Log;
    //
    //         await Client.LoginAsync(TokenType.Bot, "");
    //         await Client.StartAsync();
    //         
    //         await Task.Delay(-1);
    //     }
    //
    //     private static Task Log(LogMessage logMessage)
    //     {
    //         Console.WriteLine(logMessage.Message);
    //         return Task.CompletedTask;
    //     }
    // }
    
    public class Test {
        public void Print()
        {
            Console.WriteLine("Wow");
        }

        public int Add(int a, int b)
        {
            return a + b;
        }
    }
}