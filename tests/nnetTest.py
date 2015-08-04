import sys
import unittest
sys.path.append("..")
from NeuralNet import *

class NeuronTest(unittest.TestCase):
	
	def testWeights(self):
		_weights = 10
		Neuron = neuron(_weights)
		self.assertEqual(len(Neuron.weights),_weights+1)
		self.assertEqual(Neuron.numinputs,_weights+1)
		self.assertNotEqual(Neuron.weights,None)

class neuronLayerTest(unittest.TestCase):
	
	def testconstructor(self):
		nrons = 10
		inpts = 3
		nlayer = neuronLayer(nrons,inpts)
		self.assertEqual(nlayer.numNeurons,nrons)
		self.assertEqual(len(nlayer.nhiddenlayer),nrons)
		self.assertNotEqual(nlayer.nhiddenlayer,None)

	def testhiddenlayer(self):
		nrons = 10
		inpts = 3
		nlayer = neuronLayer(nrons,inpts)
		for i in xrange(nrons):
			self.assertTrue(nlayer.gethiddenlayer(i))
	def testnumneurons(self):
		nrons = 10
		inpts = 3
		nlayer = neuronLayer(nrons,inpts)
		self.assertTrue(nlayer.getnumNeurons(),nron)

if __name__ == '__main__':
	unittest.main()