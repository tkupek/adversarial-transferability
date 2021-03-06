import os

from tensorflow.keras.models import load_model

from data import get_prepare_dataset
from taboo import taboo_tools

TEST_SIZE = 10000


def print_profile(profile, key):
    result = ""
    for i in range(len(profile)):
        result += " " + str(profile[i][key])

    print(str.replace(result, ".", ","))


if __name__ == "__main__":

    (train_images, train_labels), (test_images, test_labels) = get_prepare_dataset.load_fashion_mnist(None)
    test_images = test_images[:TEST_SIZE]
    test_labels = test_labels[:TEST_SIZE]

    model = load_model(os.path.join('tmp', 'sideeffect-3.h5'))

    # profiled_layers = [layer.output for layer in model.layers if layer.name.startswith('activation')]
    profiled_layers = [model.layers[5].output]
    profile = taboo_tools.profile_model(model, test_images, profiled_layers, 32)
    print(profile)

    print_profile(profile, '5_percentile')
    print_profile(profile, '10_percentile')
    print_profile(profile, '90_percentile')
    print_profile(profile, '99_percentile')
    print_profile(profile, '995_percentile')
    print_profile(profile, 'max')