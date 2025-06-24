using System.Linq;
using System.Threading.Tasks;

namespace AK.Wwise.Waapi.SubSystem
{

    public class ClientSubSystem:Singleton<ClientSubSystem>
    {
        private AK.Wwise.Waapi.JsonClient client;
        public AK.Wwise.Waapi.JsonClient Client => client;
        
        
        public async Task Initialize(JsonClient jsonClient)
        {
            this.client = jsonClient;
            SubscribeDisconnected(()=> System.Console.WriteLine("Log Temp We lost connection! "));
            await ConnectWwise();
        }
        
        // Try to connect to running instance of Wwise on localhost, default port
        public async Task ConnectWwise() => await Client.Connect();
        public void SubscribeDisconnected(Wamp.DisconnectedHandler handler)
            => Client.Disconnected += handler;

    }
}