
import numpy as np

def ad8_flow_directions(dem, cs):
    # Get the shape of the DEM
    rows, cols = dem.shape
    # Create an array to store flow directions, initially filled with NoData value
    flow_directions = np.full_like(dem, 0, dtype=np.float32)
    slope_data =  np.full_like(dem, np.nan, dtype=np.float32)

    # Define the eight possible neighbors for each cell
    neighbors = [(0, 1, 'e'), (-1, 1, 'ne'), (-1, 0, 'n'),
                 (-1, -1, 'nw'), (0, -1, 'w'),
                 (1, -1, 'sw'), (1, 0, 's'), (1, 1, 'se')]

    # Loop through each cell in the DEM
    for row in range(0, rows - 1):
        for col in range(0, cols - 1):
            # Skip NoData values
            if dem[row, col] == -999:
                continue

            current_elevation = dem[row, col]
            # min_slope = float('inf')
            max_slope = -9999

            min_elevation_diff = float('inf')
            min_direction = np.nan  # Default direction for NoData cells

            # Loop through the eight neighbors
            for dr, dc, direction in neighbors:
                # Get the elevation of the neighbor
                neighbor_elevation = dem[row + dr, col + dc]

                # Skip NoData values
                if neighbor_elevation == -999:
                    continue

                # Calculate horizontal and vertical distances
                if direction in ['e', 'w', 'n', 's']:
                    horizontal_distance = cs
                    vertical_distance = 0
                else:
                    horizontal_distance = cs / np.sqrt(2)
                    vertical_distance = cs / np.sqrt(2)

                # Calculate slope between current cell and neighbor
                distance = np.sqrt(horizontal_distance**2 + vertical_distance**2)
                slope = (current_elevation -neighbor_elevation ) / distance

                # Calculate elevation difference
                elevation_diff = abs(neighbor_elevation - current_elevation)

                if slope > max_slope:
                    max_slope = slope
                    min_direction = neighbors.index((dr, dc, direction)) + 1  # Add 1 to make directions 1 to 8

            # Assign the flow direction to the current cell
            flow_directions[row, col] = min_direction
            slope_data[row,col]= max_slope

    return flow_directions,slope_data