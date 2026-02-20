import sys


def func(x):
    return x * x


def calc_func(function, x_min, x_max, point_count):
    x = []
    y = []
    y_min = sys.float_info.max
    y_max = -sys.float_info.max
    dx = (x_max - x_min) / point_count
    for point_counter in range(point_count + 1):
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


def print_plot(function, x_min, x_max, point_count, screen_width=25, screen_height=20):
    func_values = calc_func(function, x_min, x_max, point_count)
    scaled_x = []
    scaled_y = []

    for point_index in range(point_count + 1):
        scaled_x.append(
            round(
                (func_values['x_values'][point_index] - func_values['x_limits'][0]) * screen_width
                / (func_values['x_limits'][1] - func_values['x_limits'][0])
            )
        )
        scaled_y.append(
            round(
                (func_values['y_values'][point_index] - func_values['y_limits'][0]) * screen_height
                / (func_values['y_limits'][1] - func_values['y_limits'][0])
            )
        )

    print(scaled_x)
    print(scaled_y)
    plot = []
    for row_index in range(screen_height + 1):
        row = []
        for col_index in range(screen_width + 1):
            y_indices = []
            if row_index in scaled_y:
                for y_index in range(len(scaled_y)):
                    if row_index == scaled_y[y_index]:
                        y_indices.append(y_index)
                for i in range(len(y_indices)):
                    y_index = y_indices[i]
                    x_column = scaled_x[y_index]
                    if col_index == x_column:
                        row.append('⏺')
                    elif i % len(y_indices):
                        row.append('·')
                
            else:
                row.append('·')
        plot.append(row)
    
    plot.reverse()
    for row_index in range(screen_height):
        print(" ".join(plot[row_index]))


print_plot(function=func, x_min=0, x_max=10, point_count=10)
