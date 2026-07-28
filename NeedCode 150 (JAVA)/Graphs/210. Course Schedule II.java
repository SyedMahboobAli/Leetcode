class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        int[] indegree = new int[numCourses];
        
        for(int i = 0; i<numCourses ; i++){
            graph.add(new ArrayList<>());
        }

        for(int[] p: prerequisites){
            int course = p[0];
            int prereq = p[1];

            graph.get(prereq).add(course);
            indegree[course]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for(int i =0;i<numCourses;i++){
            if(indegree[i] == 0)
                queue.offer(i);
        }
        int idx = 0;
        int[] res = new int[numCourses];

        while(!queue.isEmpty()){
            int curr = queue.poll();
            res[idx++] = curr; //idx incrementing in place

            for(int next : graph.get(curr)){
                indegree[next]--;
                if(indegree[next] == 0)
                    queue.offer(next);
            }
        }
        return idx == numCourses ? res : new int[0]; //here as well you need a new object for []
    }
}
