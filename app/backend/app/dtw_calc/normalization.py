import numpy as np

def mini_max_angles(data, ang):    
    for i in ang:
        data[i] = data[i]/360
        max = np.max(data[i])
        min = np.min(data[i])

        data[i] =(data[i] - min) / (max - min)

def zscore_angles(data, ang):
    from scipy.stats import zscore
    for i in ang:
        data[i] = zscore(data[i])


def normalize_angles(data, ang, mode = "minmax"):
    if mode == "minmax":
        return mini_max_angles(data, ang)
    elif mode == "zscore":
        return zscore_angles(data, ang)
    else:
        for i in ang:
            data[i] = data[i]/360

# Coords
def get_positions(body):
    positions = []
    for i in body:
        positions.append(i + "_x")
        positions.append(i + "_y")
    return positions

def get_positions_x(body):
    positions = []
    for i in body:
        positions.append(i + "_x")
    return positions

def get_positions_y(body):
    positions = []
    for i in body:
        positions.append(i + "_y")
    return positions

def bounding_box(row, body):

    min_x = 1000000
    min_y = 1000000
    max_x = -1000000
    max_y = -1000000

    for i in body:
        coord_x = row[i + "_x"]
        coord_y = row[i + "_y"]
        if coord_x < min_x:
            min_x = coord_x

        if coord_x > max_x:
            max_x = coord_x

        if coord_y < min_y:
            min_y = coord_y

        if coord_y > max_y:
            max_y = coord_y
    return [(int(min_x),int(min_y)),(int(max_x),int(min_y)),(int(max_x),int(max_y)),(int(min_x),int(max_y))]

def normalize_positions(data, body):
    data[get_positions(body)] = data[get_positions(body)].astype(float)
    selected_columns = data[get_positions(body)]
    for index, row in selected_columns.iterrows():
        coords = bounding_box(row, body)
        for i in body:
            x = i + "_x"
            y = i + "_y"
            data.loc[index, x] = np.float64(row[x] - coords[0][0])
            data.loc[index, y] = np.float64(row[y] - coords[0][1])
    for i in body:
        columns = data[[i + "_x", i + "_y"]]
        data[[i + "_x", i + "_y"]] = columns/np.linalg.norm(columns)
