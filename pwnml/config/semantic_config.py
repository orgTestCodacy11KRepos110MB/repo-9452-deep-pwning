import tensorflow as tf

# source_url = 'http://yann.lecun.com/exdb/mnist/'
# work_directory = 'data'
# train_data_filename = 'train-images-idx3-ubyte.gz'
# train_labels_filename = 'train-labels-idx1-ubyte.gz'
# test_data_filename = 't10k-images-idx3-ubyte.gz'
# test_labels_filename = 't10k-labels-idx1-ubyte.gz'

num_classes = 2

# validation_size = 5000  # size of the validation set.
seed = 66478  # set to none for random seed.
batch_size = 64
num_epochs = 200
eval_batch_size = 64
eval_frequency = 100  # number of steps between evaluations.
checkpoint_path = 'checkpoints/semantic/prototype.ckpt'
data_type = tf.float32

adversarial_perturbation_min = .01
adversarial_perturbation_max = .15
adversarial_perturbation_steps = 15
