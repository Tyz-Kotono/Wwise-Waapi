using System.Linq;
using System.Threading.Tasks;

using Newtonsoft.Json.Linq;


namespace AK.WappiNet.Function
{
    using Wwise.Waapi;
    public static  class WaapiUILibrary
    {
        public static async Task<JObject> GetSelectedObjects(this JsonClient client,object selectArgs = null, object  selectOptions = null)
            =>await client.Call(ak.wwise.ui.getSelectedObjects, selectArgs, selectOptions);
        
    }
    
    public static  class WaapicoreLibrary
    {
        public static async Task<JObject> GetWwiseInfo(this JsonClient client)
            =>await client.Call(ak.wwise.core.getInfo, null, null);
       
       
        public static async Task<JObject> ObjectCreate(this JsonClient client,object args = null, object options = null)
            =>await client.Call(ak.wwise.core.@object.create, args, options);
       
        public static async Task<JObject> ObjectCreateGameSync(this JsonClient client,object Syncargs = null, object Syncoptions = null)
            =>await client.Call(ak.wwise.core.@object.create, Syncargs, Syncoptions);
    }
}