import numpy as np
a = np.array()

def change_last_bit(width, height, pix, bin_massage, draw):
    count_channels = len(pix[0, 0])
    index = 0
    for x in range(width):
        for y in range(height):
            for z in range(count_channels):

                if index == len(bin_massage):
                    return pix

                bit = int(bin_massage[index])
                channel = pix[x, y][z]

                if (bit == 0b0):
                    channel &= ~0b1
                else:
                    channel |= 0b1

                channels = list(pix[x, y])
                channels[z] = channel
                channels = tuple(channels)

                draw.point((x, y), channels)
                index += 1
