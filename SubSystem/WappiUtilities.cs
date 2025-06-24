using AK.Wwise.Waapi;
using Newtonsoft.Json.Linq;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using AK.WappiNet.Function;

namespace AK.WappiNet.Utilities
{
    public static class SelectUtils
    {
        /// <summary>
        /// 获取当前选择的Wwise对象（异步扩展方法）
        /// </summary>
        /// <param name="client">JsonClient实例</param>
        /// <param name="filterTypes">要过滤的类型数组（可选）</param>
        /// <param name="returnFields">要返回的字段数组（可选，默认返回id/name/type/path）</param>
        /// <returns>选择的对象列表</returns>
        public static async Task<List<JObject>> GetSelectedObjectsAsync(this JsonClient client,
            string[] filterTypes = null,
            string[] returnFields = null)
        {
            try
            {
                // 设置默认返回字段
                var fields = returnFields ?? new[] { "id", "name", "type", "path" };
            
                // 调用扩展方法获取选择对象
                var result = await client.GetSelectedObjects(
                    selectArgs: null, 
                    selectOptions: new JObject { ["return"] = new JArray(fields) });
                
                if (result == null || result["objects"] == null)
                    return new List<JObject>();

                // 转换为JObject列表
                var objects = (result["objects"] as JArray)?
                    .Select(o => (JObject)o)
                    .ToList() ?? new List<JObject>();
            
                // 类型过滤
                if (filterTypes != null && filterTypes.Length > 0)
                {
                    objects = objects
                        .Where(o => filterTypes.Contains(o["type"]?.ToString()))
                        .ToList();
                }

                return objects;
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"获取选择失败: {ex.Message}");
                return new List<JObject>();
            }
        }
    }
}