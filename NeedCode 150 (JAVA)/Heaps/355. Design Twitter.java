class Twitter {
    //why static : The keyword static means Tweet does not need a reference to the enclosing Twitter object to save memory.
    /*
    Conceptually, Java treats it like:

class Tweet {
    Twitter this$0;   // hidden reference
    int id;
    int time;
}
it doesn't need twitter reference here
    */
    private static class Tweet{
        int id;
        int time;

        Tweet(int id, int time){
            this.id = id;
            this.time = time;
        }
    }

    private int time;
    private Map<Integer, Set<Integer>> followMap; //User has a set of followee(whom he follows)
    private Map<Integer, List<Tweet>> tweetMap; //for every id, list of Tweet class

    public Twitter() {
        time = 0;
        followMap = new HashMap<>();
        tweetMap = new HashMap<>();
    }
    
    public void postTweet(int userId, int tweetId) {
        tweetMap.putIfAbsent(userId, new ArrayList<>());
        tweetMap.get(userId).add(new Tweet(tweetId,time++));
    }
    
    public List<Integer> getNewsFeed(int userId) {
        PriorityQueue<Tweet> maxHeap = new PriorityQueue<>((a,b) -> b.time - a.time);

        //own Tweets
        if(tweetMap.containsKey(userId)){
            for(Tweet t : tweetMap.get(userId)){
                maxHeap.offer(t);
            }
        }

        //tweets from followees (whom he follows)
        if(followMap.containsKey(userId)){
            for(int followee: followMap.get(userId)){
                if(tweetMap.containsKey(followee)){
                    for(Tweet t: tweetMap.get(followee)){
                        maxHeap.offer(t);
                    }
                }
            }
        }

        List<Integer> feed = new ArrayList<>();
        while(!maxHeap.isEmpty() && feed.size() < 10){
            feed.add(maxHeap.poll().id);
        }
        
        return feed;
    }
    
    public void follow(int followerId, int followeeId) {
        if (followerId == followeeId) return;

        followMap.putIfAbsent(followerId, new HashSet<>());
        followMap.get(followerId).add(followeeId);
    }
    
    public void unfollow(int followerId, int followeeId) {
        if(followMap.containsKey(followerId))
            followMap.get(followerId).remove(followeeId);
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */
