class Encoder:
    """ The first portion of the Autoencoder network."""
    def __init__(self):
        """ Initialize the Encoder object."""
        return

	def compress(self, data):
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

	def run(self, data):
		"""
		The input portion.
		Compress input data.
		This is a feedforward densely-connected \
		network.
		"""
		comp_data = compress(data)
		return comp_data


class AutoEncoder(NeuralNetwork):
	"""
	Simple autoencoder object.

	The simplest design is a feed-forward \
	architecture
	- Structure like a single-layer perceptron
	    - https://medium.com/dataprophet/a-comprehensive-guide-to-single-layer-perceptrons-in-artificial-intelligence-7e0b071c88b5
		- Used in multi-layer perceptrons

    The auto-encoder is trained via backpropagation.
    https://www.askpython.com/python/examples/backpropagation-in-python

    It doesn't need labels
    - With enough data, we can get high performance on __specific__ input data
        - This is data-specificity
            - It can only compres data highly similar to previously-used data

    Due to the compression stage, autoencoders are lossy:
    - Output data is degraded in relation to the input data

	In our design, we need to pay attention \
	to a four different model hyperparameters:
	- code size
        - How many nodes begin the bottleneck()?
            - fewer nodes -> higher compression
                encoder goes on.
	- layer number
	- nodes per layer
        - For encoders, we want to decrease nodes per layer
        - For decoders, we wnt to increase nodes per layer
	- loss function
        - either
            - binary cross-entropy 
                - appropriate for instances where input_values in range(0, 1)
                - https://pythonguides.com/binary-cross-entropy-tensorflow/
                - https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-visual-explanation-a3ac6025181a?gi=de3df99d9a42
            - mean square error
	"""
	
	def __init__(self):
		""" Initialize autoencoder."""
		self.input_layers = []
		self.output_layers = []
        self.architectures = {
                # https://medium.com/@syoya/what-happens-in-sparse-autencoder-b9a5a69da5c6 
                "sparse": {}, 
                # https://deepai.org/machine-learning-glossary-and-terms/contractive-autoencoder 
                "contractive": {}, 
                # https://towardsdatascience.com/convolutional-autoencoders-for-image-noise-reduction-32fce9fc1763
                "convolutional": {}, 
                # https://towardsdatascience.com/denoising-autoencoders-explained-dbb82467fc2 
                "denoising": {}, 
                # https://www.topbots.com/variational-autoencoders-explained/ 
                "variational": {}}
		return

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
        # we start with the encoder segment
        encoder = Encoder()
        encoder.run(data)

		# then we handle the encoded data
		bot_data = bottleneck(comp_data)
		
		# finally we reconstruct it
		dec_data = decoder(bot_data)
		
		return dec_data
