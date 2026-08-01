class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, PriorityQueue<String>> graph = new HashMap<>();

        for(List<String> ticket: tickets){
            String from  = ticket.get(0);
            String to = ticket.get(1);
            graph.putIfAbsent(from,new PriorityQueue<>());
            graph.get(from).offer(to);
        }

        List<String> result = new ArrayList<>();
        dfs("JFK",graph,result);
        Collections.reverse(result);
        return result;
    }
    private void dfs(String airport, Map<String,PriorityQueue<String>> graph, List<String> result){
        PriorityQueue<String> pq = graph.get(airport);

        while(pq!=null && !pq.isEmpty()){
            String next = pq.poll();
            dfs(next,graph,result);
        }
        result.add(airport);
    }
}
