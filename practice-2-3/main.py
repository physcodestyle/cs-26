import sys


def func(x):
    return x * x


def calc_func(function, x_min, x_max, point_count):
    x = []
    y = []
    y_min = sys.float_info.max
    y_max = -sys.float_info.max
    dx = (x_max - x_min) / (point_count - 1)
    for point_counter in range(point_count):
        x.append(x_min + dx * point_counter)
        y.append(function(x[len(x) - 1]))
        y_min = y[len(y) - 1] if y[len(y) - 1] < y_min else y_min
        y_max = y[len(y) - 1] if y[len(y) - 1] > y_max else y_max
    return {
        "x_values": x,
        "y_values": y,
        "x_limits": (x_min, x_max),
        "y_limits": (y_min, y_max),
    }


def print_values(function, x_min, x_max, point_count):
    func_values = calc_func(function, x_min, x_max, point_count)
    for point_index in range(point_count + 1):
        print(f"{func_values['x_values'][point_index]:10.4f}\t{func_values['y_values'][point_index]:10.4f}\t")


def get_origin_index(values, axe, screen_size):
    key = f"{axe}_limits"
    if round(values[key][0]) == 0:
        return 0
    elif round(values[key][1]) == 0:
        return screen_size
    elif values[key][0] < 0 and values[key][1] > 0:
        return round(
            -1 * values[key][0] * screen_size
            /  (values[key][1] - values[key][0])
        )
    return -1


def get_value_indices(values, axe, screen_size, point_count):
    value_key = f"{axe}_values"
    limits_key = f"{axe}_limits"
    scaled_values = []
    for point_index in range(point_count):
        scaled_values.append(
            round(
                (values[value_key][point_index] - values[limits_key][0]) * screen_size
                / (values[limits_key][1] - values[limits_key][0])
            )
        )
    return scaled_values


def print_plot(function, x_min, x_max, point_count, screen_width=20, screen_height=20):
    func_values = calc_func(function, x_min, x_max, point_count)
    scaled_x = get_value_indices(func_values, "x", screen_width, point_count)
    scaled_y = get_value_indices(func_values, "y", screen_height, point_count)
    scaled_x_origin = get_origin_index(func_values, "x", screen_width)
    scaled_y_origin = get_origin_index(func_values, "y", screen_height)
    plot = []
    for row_index in range(screen_height + 1):
        row = []
        x_indices = []
        if row_index in scaled_y:
            for y_index in range(len(scaled_y)):
                if row_index == scaled_y[y_index]:
                    x_indices.append(scaled_x[y_index])
        for col_index in range(screen_width + 1):
            if col_index in x_indices:
                row.append("⏺")
            elif row_index == scaled_y_origin and col_index == scaled_x_origin:
                row.append("+")
            elif col_index == scaled_x_origin:
                row.append("|")
            elif row_index == scaled_y_origin:
                row.append("—")
            else:
                row.append("·")
        plot.append(row)
    plot.reverse()
    for row_index in range(screen_height + 1):
        print(" ".join(plot[row_index]))


print_plot(function=func, x_min=-5, x_max=5, point_count=10, screen_width=40, screen_height=20)
