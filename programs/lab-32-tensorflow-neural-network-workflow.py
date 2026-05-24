# TensorFlow / Neural Network Workflow
try:
    import tensorflow as tf
    model = tf.keras.Sequential([tf.keras.layers.Dense(8, activation="relu", input_shape=(2,)), tf.keras.layers.Dense(1, activation="sigmoid")])
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    model.summary()
except ImportError:
    print("Install TensorFlow: pip install tensorflow")
