#     Copyright 2021 JSquad AB
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.


from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras import utils
from tensorflow.keras.datasets import mnist


class Digits:

    def __init__(self):
        self.prepareTheTestData()
        self.setupNeuralNetwork()

    def prepareTheTestData(self):
        (self.train_images, self.train_labels), (self.test_images, self.test_labels) = mnist.load_data()

        self.train_images = self.train_images.reshape((60000, 28*28))
        self.train_images = self.train_images.astype('float32')/255

        self.test_images = self.test_images.reshape((10000, 28*28))
        self.test_images = self.test_images.astype('float32')/255

        # Categorically encode the labels
        self.train_labels = utils.to_categorical(self.train_labels)
        self.test_labels = utils.to_categorical(self.test_labels)

    def setupNeuralNetwork(self):
        self.network = models.Sequential()
        self.network.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
        self.network.add(layers.Dense(10, activation='softmax'))

        self.network.compile(optimizer='rmsprop', loss='categorical_crossentropy',metrics=['accuracy'])

    def trainModel(self):
        self.network.fit(self.train_images, self.train_labels, epochs=5, batch_size=128)

    def evaulate(self):
        return self.network.evaluate(self.test_images, self.test_labels)