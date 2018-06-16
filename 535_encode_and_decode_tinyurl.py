class Codec:
    def __init__(self):
        self.url_dict = {}
        self.cnter = 0
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.url_dict[self.cnter] = longUrl
        self.cnter += 1
        return "http://tinyurl.com/"+str(self.cnter-1)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.url_dict[int(shortUrl[shortUrl.index(".")+5:])]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))