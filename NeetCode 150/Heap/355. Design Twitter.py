class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) # userId -> list of (time, tweetId)
        self.following = defaultdict(set) # userId -> set of followees
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time -= 1 # decreasing time ensures newer tweets come first

    def getNewsFeed(self, userId: int) -> List[int]:
        res =[]
        heap = []

         # user should follow himself
        self.following[userId].add(userId)
        # push latest tweet of each followed user
        for followee in self.following[userId]:
            if self.tweets[followee]:
                time , tweetID = self.tweets[followee][-1]
                idx = len(self.tweets[followee]) - 1
                heapq.heappush(heap,(time, tweetID, followee, idx))   

        # get 10 most recent tweets
        while heap and len(res) < 10:
            time, tweetid, user, idx = heapq.heappop(heap)
            res.append(tweetid) 

            # move to previous tweet of same user
            if idx > 0:
                next_time,next_tweetid = self.tweets[user][idx -1]
                heapq.heappush(heap,(next_time,next_tweetid,user,idx-1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)
            #does not throw error if key not present else remove throws error
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
