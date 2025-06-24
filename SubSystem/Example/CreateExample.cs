using AK.WaapiNet.ObjectModel;
using Newtonsoft.Json.Linq;

using AK.WappiNet.Function;
using AK.Wwise.Waapi;
using Newtonsoft.Json.Linq;

namespace AK.Wwise.Example
{
   public static class WaapiUIExample
   {
      public static  async Task CreateRTPC(this JsonClient client)
      {
         var createArgs = new JObject
         {
            ["parent"] = WwiseUtilities.GameSyncsGameParameter,
            ["type"] = GameSyncsType.GameParameter,
            ["name"] = "PlayerHealth"
         };
         await client.ObjectCreateGameSync(createArgs);
      }
   }
}