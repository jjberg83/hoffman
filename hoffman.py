import operator

# theInput = input("Write your message: ")
theInput = "bccabbddaeccbbaeddcc"
#theInput = "BCAADDDCCACACAC"
# test comment

# Create sorted dictionary with all the symbols from the input above
# and counts of each symbol 
countedSymbols = { }

for symbol in theInput:
	if symbol not in countedSymbols:
		countedSymbols[symbol] = 1
	else:
		countedSymbols[symbol] += 1

# Sort the dictionary based on values, technique found here
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
countedSymbols = {k: v for k, v in sorted(countedSymbols.items(), key=lambda item: item[1])}

print(countedSymbols)

# Create nodes based on info from the sorted dictionary
# and build a tree from them, starting at the bottom

class Node:
	def __init__(self, symbol=None, count=None, leftChild=None, rightChild=None):
		self.symbol = symbol
		self.count = count
		self.leftChild = leftChild
		self.rightChild = rightChild 

	def children(self):
		return self.leftChild, self.rightChild

	def printTree(self):
		if self.leftChild is not None:
			self.leftChild.printTree()
		print(self.symbol, self.count),
		if self.rightChild is not None:
			self.rightChild.printTree()

	# this method prints out a dictionary with all the codes
	# for all the symbols used in the input
	# found (but updated) it from:
	# https://favtutor.com/blogs/huffman-coding
	def symbolCodes(self, binString=''):
		if type(self.symbol) is str:
			return {self.symbol: binString}
		(l, r) = self.children()
		d = dict()
		d.update(l.symbolCodes(binString + '0'))
		d.update(r.symbolCodes(binString + '1'))
		return d
	
# the initial list, starting with the nodes from the dictionary
buildingBlocksForTree = []


# filling this list with nodes based on entries in dictionary
for symbol, count in countedSymbols.items():
	node = Node(symbol, count)
	buildingBlocksForTree.append(node)


# This is where the tree is built using the Hoffman technique
while (len(buildingBlocksForTree) > 1):
	parentCount = buildingBlocksForTree[0].count + buildingBlocksForTree[1].count
	parentNode = Node(None, parentCount, buildingBlocksForTree[0], buildingBlocksForTree[1])
	buildingBlocksForTree = buildingBlocksForTree[2:]
	buildingBlocksForTree.append(parentNode)
	buildingBlocksForTree.sort(key=operator.attrgetter('count'))


print(buildingBlocksForTree[0].symbolCodes())

