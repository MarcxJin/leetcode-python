class Solution:
    def convertStringToComplex(self, string):
        string = string[:-1].split("+")
        return (int(string[0]), int(string[1]))
        
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = self.convertStringToComplex(a)
        b = self.convertStringToComplex(b)
        real = a[0]*b[0]-a[1]*b[1]
        image = a[0]*b[1]+a[1]*b[0]
        return str(real)+"+"+str(image)+"i"