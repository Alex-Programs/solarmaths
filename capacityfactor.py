import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def generate_norm_sunlight_intensity():
    # normal distribution
    SUNLIGHT_INTENSITY_NORM = []
    HOURS_PROGRESS = []
    mean = 12
    std = 2.9

    for i in range(0, 3600):  # 0..23
        value_at_pos = stats.norm.pdf(i / 60, mean, std)

        HOURS_PROGRESS.append(i / 60)

        SUNLIGHT_INTENSITY_NORM.append(value_at_pos)

    # Normalise to 0-1
    SUNLIGHT_INTENSITY_NORM = np.array(SUNLIGHT_INTENSITY_NORM)
    SUNLIGHT_INTENSITY_NORM = SUNLIGHT_INTENSITY_NORM / np.max(SUNLIGHT_INTENSITY_NORM)

    return SUNLIGHT_INTENSITY_NORM, HOURS_PROGRESS


def generate_sin_sunlight_intensity():
    # sin distribution
    SUNLIGHT_INTENSITY_SIN = []
    HOURS_PROGRESS = []

    for i in range(0, 3600):
        # https://www.desmos.com/calculator/z0hqgdzzsi
        value_at_pos = math.sin((i + 1560) / 290)

        HOURS_PROGRESS.append(i / 60)

        SUNLIGHT_INTENSITY_SIN.append(value_at_pos)

    # Normalise to 0-1
    SUNLIGHT_INTENSITY_SIN = np.array(SUNLIGHT_INTENSITY_SIN)
    SUNLIGHT_INTENSITY_SIN = SUNLIGHT_INTENSITY_SIN / np.max(SUNLIGHT_INTENSITY_SIN)

    return SUNLIGHT_INTENSITY_SIN, HOURS_PROGRESS


SUNLIGHT_INTENSITY_BY_MINUTE, HOURS_PROGRESS = generate_sin_sunlight_intensity()

print(len(SUNLIGHT_INTENSITY_BY_MINUTE))

plt.figure(0)

ax = plt.subplot(111)
ax.set_ylim(0, 1.2)
ax.set_xlim(0, 24)

plt.plot(HOURS_PROGRESS, SUNLIGHT_INTENSITY_BY_MINUTE)
plt.savefig("sunlight_intensity.png")

# derive empirically
SHADOW_FACTOR = []


def generate_seasonal_adjustment():
    # normal distribution
    SEASONAL_ADJUSTMENT = []
    mean = 365 / 2
    std = 365 / 2.6

    for i in range(0, 365):
        value_at_pos = stats.norm.pdf(i + 0.5, mean, std)

        SEASONAL_ADJUSTMENT.append(value_at_pos)

    # Normalise to 0-1
    SEASONAL_ADJUSTMENT = np.array(SEASONAL_ADJUSTMENT)
    SEASONAL_ADJUSTMENT = SEASONAL_ADJUSTMENT / np.max(SEASONAL_ADJUSTMENT)

    return SEASONAL_ADJUSTMENT


SEASONAL_ADJUSTMENT_BY_DAY = generate_seasonal_adjustment()

print(SEASONAL_ADJUSTMENT_BY_DAY)

plt.figure(1)

ax = plt.subplot(111)
ax.set_ylim(0, 1.2)
ax.set_xlim(0, 365)

plt.plot(SEASONAL_ADJUSTMENT_BY_DAY)
plt.savefig("seasonal_adjustment.png")

UK_MULTIPLIER = 0.8
INEFFICIENT_ANGLE_MULTIPLIER = 0.8
