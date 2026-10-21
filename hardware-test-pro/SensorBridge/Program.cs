using System.Text.Json;
using LibreHardwareMonitor.Hardware;

internal static class Program
{
    private static readonly JsonSerializerOptions JsonOptions = new()
    {
        PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
        WriteIndented = false
    };

    private static int Main(string[] args)
    {
        var started = DateTimeOffset.UtcNow;
        var sensors = new List<Dictionary<string, object?>>();
        var errors = new List<string>();
        Computer? computer = null;
        try
        {
            computer = new Computer
            {
                IsCpuEnabled = true,
                IsGpuEnabled = true,
                IsMemoryEnabled = true,
                IsMotherboardEnabled = true,
                IsControllerEnabled = true,
                IsStorageEnabled = true,
                IsNetworkEnabled = true
            };
            computer.Open();
            foreach (var hardware in computer.Hardware)
                ReadHardware(hardware, sensors, errors);
            var result = new
            {
                ok = sensors.Any(x => x["value"] is not null),
                timestampUtc = DateTimeOffset.UtcNow,
                startedAtUtc = started,
                sensorCount = sensors.Count,
                valueCount = sensors.Count(x => x["value"] is not null),
                sensors,
                errors = errors.Take(30).ToArray(),
                provider = "LibreHardwareMonitorLib 0.9.6"
            };
            Console.Out.WriteLine(JsonSerializer.Serialize(result, JsonOptions));
            return sensors.Any(x => x["value"] is not null) ? 0 : 2;
        }
        catch (Exception ex)
        {
            var result = new
            {
                ok = false,
                timestampUtc = DateTimeOffset.UtcNow,
                startedAtUtc = started,
                sensorCount = sensors.Count,
                valueCount = sensors.Count(x => x["value"] is not null),
                sensors,
                errors = errors.Append(ex.GetType().Name + ": " + ex.Message).Take(30).ToArray(),
                provider = "LibreHardwareMonitorLib 0.9.6"
            };
            Console.Out.WriteLine(JsonSerializer.Serialize(result, JsonOptions));
            return 2;
        }
        finally
        {
            try { computer?.Close(); } catch { }
        }
    }

    private static void ReadHardware(IHardware hardware, List<Dictionary<string, object?>> sensors, List<string> errors)
    {
        try
        {
            hardware.Update();
            foreach (var sensor in hardware.Sensors)
            {
                var type = sensor.SensorType.ToString();
                double? value = sensor.Value.HasValue && float.IsFinite(sensor.Value.Value)
                    ? Math.Round((double)sensor.Value.Value, 3)
                    : null;
                sensors.Add(new Dictionary<string, object?>
                {
                    ["hardware"] = hardware.Name,
                    ["hardwareType"] = hardware.HardwareType.ToString(),
                    ["hardwareId"] = hardware.Identifier.ToString(),
                    ["sensor"] = sensor.Name,
                    ["sensorType"] = type,
                    ["value"] = value,
                    ["valueAvailable"] = value.HasValue,
                    ["unit"] = UnitFor(type),
                    ["identifier"] = sensor.Identifier.ToString()
                });
            }
        }
        catch (Exception ex)
        {
            errors.Add(hardware.Name + ": " + ex.GetType().Name + ": " + ex.Message);
        }

        foreach (var sub in hardware.SubHardware)
            ReadHardware(sub, sensors, errors);
    }

    private static string UnitFor(string type) => type switch
    {
        "Temperature" => "°C",
        "Fan" => "RPM",
        "Clock" => "MHz",
        "Load" => "%",
        "Voltage" => "V",
        "Power" => "W",
        "Data" => "GB",
        "SmallData" => "MB",
        "Throughput" => "B/s",
        "Energy" => "mWh",
        "TimeSpan" => "s",
        "Level" => "%",
        _ => ""
    };
}
