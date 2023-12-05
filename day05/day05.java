import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/*
 * Converted from python to Java via ChatGPT to run fast enough
 */
public class day05 {

	public static long mapping(long num, List<long[]> mapping) {
		for (long[] m : mapping) {
			long dest = m[0];
			long source = m[1];
			long range = m[2];
			if (num >= dest && num <= dest + range) {
				return num - dest + source;
			}
		}
		return num;
	}

	public static void main(String[] args) {
		List<Long[]> seeds = new ArrayList<>();
		List<long[]> seedToSoil = new ArrayList<>();
		List<long[]> soilToFertilizer = new ArrayList<>();
		List<long[]> fertilizerToWater = new ArrayList<>();
		List<long[]> waterToLight = new ArrayList<>();
		List<long[]> lightToTemperature = new ArrayList<>();
		List<long[]> temperatureToHumidity = new ArrayList<>();
		List<long[]> humidityToLocation = new ArrayList<>();
		List<List<long[]>> inputMap = List.of(
				seedToSoil, soilToFertilizer, fertilizerToWater,
				waterToLight, lightToTemperature, temperatureToHumidity,
				humidityToLocation);

		List<long[]> currentInput = null;

		try (BufferedReader br = new BufferedReader(new FileReader("input.txt"))) {
			String line;
			while ((line = br.readLine()) != null) {
				if (line.isEmpty()) {
					continue;
				}

				line = line.trim();

				if (line.startsWith("seeds:")) {
					line = line.replace("seeds: ", "");
					String[] seedAndRange = line.split(" ");
					for (int i = 0; i < seedAndRange.length; i += 2) {
						seeds.add(new Long[] { Long.parseLong(seedAndRange[i]), Long.parseLong(seedAndRange[i + 1]) });
					}
				} else if (!Character.isDigit(line.charAt(0))) {
					currentInput = inputMap.get(getInputIndex(line));
				} else {
					String[] parts = line.split(" ");
					long dest = Long.parseLong(parts[0]);
					long source = Long.parseLong(parts[1]);
					long range = Long.parseLong(parts[2]);
					currentInput.add(new long[] { dest, source, range });
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		}

		long loc = 1;
		while (true) {
			long humidity = mapping(loc, humidityToLocation);
			long temperature = mapping(humidity, temperatureToHumidity);
			long light = mapping(temperature, lightToTemperature);
			long water = mapping(light, waterToLight);
			long fertilizer = mapping(water, fertilizerToWater);
			long soil = mapping(fertilizer, soilToFertilizer);
			long seed = mapping(soil, seedToSoil);

			for (Long[] sr : seeds) {
				long s = sr[0];
				long r = sr[1];
				if (seed >= s && seed < s + r) {
					System.out.println(loc);
					System.exit(0);
				}
			}

			loc++;
		}
	}

	private static int getInputIndex(String line) {
		switch (line) {
			case "seed-to-soil map:":
				return 0;
			case "soil-to-fertilizer map:":
				return 1;
			case "fertilizer-to-water map:":
				return 2;
			case "water-to-light map:":
				return 3;
			case "light-to-temperature map:":
				return 4;
			case "temperature-to-humidity map:":
				return 5;
			case "humidity-to-location map:":
				return 6;
			default:
				throw new IllegalArgumentException("Invalid input map: " + line);
		}
	}
}
