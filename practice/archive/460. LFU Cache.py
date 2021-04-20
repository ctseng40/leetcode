# Approach: 2 hashmap + double linked list
# Reference: https://leetcode.com/problems/lfu-cache/discuss/1126650/Python-super-clear-code-with-comments-2-hashmap-%2B-double-linked-list

class LFUNode:
    def __init__(self, key=0, value=0, freq=1, prev=None, succ=None):
        """
        LFU Cache node structure
        :param key: The key use to retrieve the value
        :param value: Value of the node saved.
        :param freq: The frequency of the node in the cache, default to 1
        :param prev: Previous node in the frequency map.
        :param succ: Successor node in the frequency map
        """
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = prev
        self.succ = succ

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keyMap = dict() # key: LFUNode
        self.freqMap = dict() # freq: (dummy_head, dummy_tail)
        self.capacity = capacity
        self.curMinFreq = 1 # Maintenance current minimum frequency, use to knock out from cache
        self.curSize = 0 # current size of cache

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.capacity == 0:
            return -1
        if key in self.keyMap: # key already in the map, update the value and frequency, size no change, data map not change
            node = self.keyMap[key]
            self._delNodeFreqLinkMap(node, self.freqMap)
            if node.freq not in self.freqMap and node.freq == self.curMinFreq: # the node is the last one and is the minimum frequency
                self.curMinFreq += 1
            node.freq += 1
            self._addNodeFreqLinkMap(node, self.freqMap) # Add node to new frequency link
            return node.value
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return -1
        if key in self.keyMap: # key already in the map, update the value and frequency, size no change, data map not change
            node = self.keyMap[key]
            self._delNodeFreqLinkMap(node, self.freqMap) # Delete node from current frequency link
            if node.freq not in self.freqMap and node.freq == self.curMinFreq: # the node is the last one and is the minimum frequency
                self.curMinFreq += 1
            node.freq += 1
            node.value = value
            self._addNodeFreqLinkMap(node, self.freqMap)
        else: # add a new node, freq=1
            node = LFUNode(key, value)
            if self.curSize == self.capacity:  # cache is full, knock out a node from current minimum frequency
                dummy_tail = self.freqMap[self.curMinFreq][1]
                delNode = dummy_tail.prev  # node to be deleted
                prev_node = delNode.prev
                prev_node.succ = dummy_tail
                dummy_tail.prev = prev_node
                if prev_node.prev is None:
                    self.freqMap.pop(delNode.freq)
                self.keyMap.pop(delNode.key)
                self.curSize -= 1

            self._addNodeFreqLinkMap(node, self.freqMap)

            self.keyMap[key] = node  # update key map
            self.curMinFreq = 1  # the minimum value is 1
            self.curSize += 1

    def _addNodeFreqLinkMap(self, node, freqMap):  # add a node to frequency map
        if node.freq in freqMap:  # add after dummy_head
            head = freqMap[node.freq][0]
            follow = head.succ
            head.succ = node
            node.prev = head
            follow.prev = node
            node.succ = follow
        else:  # new node
            dummy_head = LFUNode(succ=node)
            node.prev = dummy_head
            dummy_tail = LFUNode(prev=node)
            node.succ = dummy_tail
            self.freqMap[node.freq] = (dummy_head, dummy_tail)

    def _delNodeFreqLinkMap(self, node, freqMap):  # delete a node from frequency map
        prev_node = node.prev
        succ_node = node.succ
        prev_node.succ = succ_node
        succ_node.prev = prev_node
        if prev_node.prev is None and succ_node.succ is None:  # empty link list
            freqMap.pop(node.freq)
            


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
