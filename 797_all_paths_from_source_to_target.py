class Solution:
    def pathFromNode(self, node, graph, length, memo):
        if node == length:
            return [[node]]
        else:
            retval = []
            for curr_node in graph[node]:
                path_after_node = self.pathFromNode(curr_node,graph,length, memo) if node not in memo \
                                  else memo[node]
                for path in self.pathFromNode(curr_node, graph, length, memo):
                    retval.append([node] + path)
                memo[node] = path_after_node
            return retval
        
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        length = len(graph) - 1
        memo = dict()
        return self.pathFromNode(0, graph, length, memo)