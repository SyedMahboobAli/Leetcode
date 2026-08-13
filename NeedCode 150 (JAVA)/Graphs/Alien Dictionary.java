import java.util.*;

class Solution {
    public String alienOrder(String[] words) {

        // Character -> characters that must come after it
        Map<Character, Set<Character>> graph = new HashMap<>();

        // Character -> number of incoming edges
        Map<Character, Integer> indegree = new HashMap<>();

        // Initialize every character
        for (String word : words) {
            for (char c : word.toCharArray()) {
                graph.putIfAbsent(c, new HashSet<>());
                indegree.putIfAbsent(c, 0);
            }
        }

        // Build graph from adjacent words
        for (int i = 0; i < words.length - 1; i++) {

            String word1 = words[i];
            String word2 = words[i + 1];

            int minLen = Math.min(word1.length(), word2.length());

            boolean foundDifference = false;

            for (int j = 0; j < minLen; j++) {

                char c1 = word1.charAt(j);
                char c2 = word2.charAt(j);

                if (c1 != c2) {

                    // c1 must come before c2
                    // Add edge only if it doesn't already exist
                    if (graph.get(c1).add(c2)) {
                        indegree.put(c2, indegree.get(c2) + 1);
                    }

                    foundDifference = true;
                    break;
                }
            }

            // Invalid case:
            // ["abc", "ab"]
            if (!foundDifference && word1.length() > word2.length()) {
                return "";
            }
        }

        // Topological sort using Kahn's algorithm
        Queue<Character> queue = new LinkedList<>();

        for (char c : indegree.keySet()) {
            if (indegree.get(c) == 0) {
                queue.offer(c);
            }
        }

        StringBuilder result = new StringBuilder();

        while (!queue.isEmpty()) {

            char curr = queue.poll();
            result.append(curr);

            for (char next : graph.get(curr)) {

                indegree.put(next, indegree.get(next) - 1);

                if (indegree.get(next) == 0) {
                    queue.offer(next);
                }
            }
        }

        // If not all characters were processed, there is a cycle
        if (result.length() != indegree.size()) {
            return "";
        }

        return result.toString();
    }
}
