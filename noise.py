import numpy as np
import argparse
import cv2


def noisy(noise_typ, image):
    # noise type:
    # 'gauss'     Gaussian-distributed additive noise.
    # 'poisson'   Poisson-distributed noise generated from the data.
    # 's&p'       Replaces random pixels with 0 or 1.
    # 'speckle'   Multiplicative noise using out = image + n*image,where
    #             n is uniform noise with specified mean & variance.
    if noise_typ == "gauss":
        row, col, ch = image.shape
        gauss = image + 3 * image.std() * np.random.random(image.shape)
        return gauss

    elif noise_typ == "s&p":
        row, col, ch = image.shape
        s_vs_p = 0.5
        amount = 0.004
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))
                  for i in image.shape]
        out[coords] = 1

        # Pepper mode
        num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
                  for i in image.shape]
        out[coords] = 0
        return out

    elif noise_typ == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / vals
        return noisy

    elif noise_typ == "speckle":
        row, col, ch = image.shape
        noise = np.random.randn(row, col, ch)
        noise = noise.reshape(row, col, ch)
        noisy = image + image * noise
        return noisy


def main():
    # Training settings
    parser = argparse.ArgumentParser(description='Data argumentation - flip')
    parser.add_argument('--noise-type', type=str,
                        default='gauss', help='Noise type(gauss, s&p,\
                             poisson, speckle)')
    args = parser.parse_args()

    image = cv2.imread('data/test.png', 1)
    noisy_image = noisy(args.noise_type, image)
    cv2.imwrite(f"saved/{args.noise_type}_noise.png", (noisy_image))


if __name__ == "__main__":
    main()
