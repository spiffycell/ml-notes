class AutoEncoder(NeuralNetwork):
	"""
	Simple autoencoder object.

	The simplest design is a feed-forward \
	architecture
	- Structure like a single-layer perceptron
		- Used in multi-layer perceptrons

	Single-layer perceptrons:
	https://medium.com/dataprophet/a-comprehensive-guide-to-single-layer-perceptrons-in-artificial-intelligence-7e0b071c88b5

	In our design, we need to pay attention \
	to a four different model hyperparameters:
	- code size
	- layer number
	- nodes per layer
	- loss function
	"""
	
	def __init__(self):
		""" Initialize autoencoder."""
		self.input_layers = []
		self.output_layers = []
		return

	def compress(data):
		"""
		Compress data into a latent state \
		representation.

		The purpose of this is to generate \
		a new representation of data with \
		reduced dimensionality.
		"""

		# Latent space:
		# https://towardsdatascience.com/understanding-latent-space-in-machine-learning-de5a7c687d8d?gi=ab2c88f13ae8
		#
		# Latent space Tutorial with TensorFlow
		# https://medium.com/mlearning-ai/latent-space-representation-a-hands-on-tutorial-on-autoencoders-in-tensorflow-57735a1c0f3f
		return data

	def encoder(data):
		"""
		The input portion.
		Compress input data.
		This is a feedforward densely-connected \
		network.
		"""
		comp_data = compress(data)
		return comp_data

	def is_relevant(feature):
		"""
		Determine if feature is relevant \
		to the data representation.

		Perform element-wise activation on \
		the network weights and biases.
		"""
		if relevant:
			return True
		return False

	def bottleneck(compressed_data):
		"""
		Bottleneck portion.
		Determine most important features \
		for data reconstruction; which data \
		features must be preserved, which can \
		be discarded.
		"""

		# we need to consider representation size.
		size = len(compressed_data)

		# perform element-wise activation on \
		# the weights and biases of the network
		for feature in compressed_data:
			if is_relevant(feature):
				compressed_data.preserve(feature)
			else:
				compressed_data.discard(feature)
		
		return bot_data

	def decoder(encoded_data):
		"""
		The output portion.
		Reconstruct encoded data.
		"""
		dec = encoded_data
		return dec_data

	def run(data):
		"""
		Run autoencoder operations.
		Through this process, the autoencoder \
		learns the important features of the data.
		"""
		# first, we compress the data
		comp_data = encoder(data)
		
		# then we handle the encoded data
		bot_data = bottleneck(comp_data)
		
		# finally we reconstruct it
		dec_data = decoder(bot_data)
		
		return dec_data
