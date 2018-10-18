import java.io.*;
import java.util.*;

public class ReadNodes {
	public static void main(String[] args) throws Exception {
		if (args.length != 3) {
			System.out.println("usage: java ReadNodes <relations-anon.txt> <list_of_starting_nodes.txt> <output.txt>");
			return;
		}
		// uncomment if you need a pause for attaching a debugger
		// System.out.println("hit enter");
		// System.in.read();
		System.out.println("Loading start nodes");
		List<Integer> startNodes = loadStartNodes(new File(args[1]));
		System.out.println("Loading edges");
		Map<Integer, List<Integer>> graphEdges = loadEdges(new File(args[0]));
		System.out.println("Flooding");
		List<Integer> flooded = floodFillDown(graphEdges, startNodes);
		System.out.println("Flooded " + flooded.size());
		Collections.sort(flooded);
		System.out.println("Sorted");
		PrintStream out = new PrintStream(new File(args[2]));
		for (Integer outInt: flooded) {
			out.println(outInt.toString());
		}
	}

	public static List<Integer> loadStartNodes(File file) throws Exception {
		List<Integer> startNodes = new ArrayList<>();
		BufferedReader reader = new BufferedReader(new FileReader(file));
		while (true) {
			String line = reader.readLine();
			if (line == null) break;
			startNodes.add(Integer.valueOf(line, 10));
		}
		reader.close();
		return startNodes;
	}

	public static List<Integer> floodFillDown(Map<Integer, List<Integer>> graphEdges, List<Integer> startNodes) {
		// a modified flood fill (using bfs)
		// open list
		Deque<Integer> queue = new ArrayDeque<>();
		queue.addAll(startNodes);
		HashSet<Integer> closed = new HashSet<>();
		List<Integer> outputNodes = new ArrayList<>();
		Integer newNode;
		while ((newNode = queue.poll()) != null) {
			if (closed.contains(newNode)) continue;
			outputNodes.add(newNode);
			closed.add(newNode);
			List<Integer> edges = graphEdges.get(newNode);
			if (edges == null) continue;
			for (Integer nextNode: edges) {
				if (closed.contains(nextNode)) continue;
				// fixme: might be faster if we check if already in open list, like Wikipedia's example
				queue.add(nextNode);
			}
		}
		return outputNodes;
	}
		

	public static Map<Integer, List<Integer>> loadEdges(File file) throws Exception {
		BufferedReader reader = new BufferedReader(new FileReader(file));
		// skip first line
		reader.readLine();
		Map<Integer, List<Integer>> graphEdges = new HashMap<>();
		while (true) {
			String line = reader.readLine();
			if (line == null) break;
			int splitIndex = line.indexOf("\t");
			Integer srcNode = Integer.valueOf(line.substring(0, splitIndex), 10);
			Integer destNode = Integer.valueOf(line.substring(splitIndex + 1), 10);
			List<Integer> targetList = graphEdges.get(srcNode);
			if (targetList == null) {
				targetList = new ArrayList<Integer>();
				graphEdges.put(srcNode, targetList);
			}
			targetList.add(destNode);
		}
		reader.close();
		return graphEdges;
	}
}
