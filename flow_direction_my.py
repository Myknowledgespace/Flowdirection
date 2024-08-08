from ad8_algorithm import ad8_flow_directions
import rasterio
import numpy as np


def process_dem_and_save_flow_directions(dem_tiff_path, output_tiff_path, output_tiff_path2):
    # Read the DEM data from the GeoTIFF file
    with rasterio.open(dem_tiff_path) as src:
        dem_data = src.read(1)
        cellsize = src.transform[0]

    # Call the flow direction function with the DEM data
    result_directions = ad8_flow_directions(dem_data, cellsize)

    # Save the results as a new GeoTIFF file with numeric values
    with rasterio.open(output_tiff_path, 'w', driver='GTiff', height=result_directions[0].shape[0],
                       width=result_directions[0].shape[1], count=1, dtype=np.uint8,
                       crs=src.crs, transform=src.transform,nodata=0) as dst:
        dst.write(result_directions[0], 1)
    #
    with rasterio.open(output_tiff_path2, 'w', driver='GTiff', height=result_directions[0].shape[0],
                       width=result_directions[0].shape[1], count=1, dtype=np.uint8,
                       crs=src.crs, transform=src.transform) as dst:
        dst.write(result_directions[1], 1)


# Replace 'your_dem_file.tif' with the actual path to your DEM GeoTIFF file

# input_tiff_path = "P:/PhD/Pavan_phd/data/tordera/new_methodology/DATA/dem/tordera_dem.tif"
# input_tiff_path = "P:/PhD/Pavan_phd/data/tordera/new_methodology/DATA/dem/tordera_dem_fill_pits.tif"
input_tiff_path = "P:/PhD/Pavan_phd/data/tordera/new_methodology/DATA/dem/tordera_dem_filled_sinks.tif"

# output_tiff_path = 'P:/PhD/Pavan_phd/data/tordera/new_methodology/DATA/flow_direction/flow_direction_v2.tif'
output_tiff_path = 'P:/PhD/Pavan_phd/data/tordera/new_methodology/DATA/flow_direction/flow_direction_v3.tif'

output_tiff_path2 = 'P:/PhD/Pavan_phd/data/tordera/new_methodology/DATA/flow_direction/slope_v2.tif'
process_dem_and_save_flow_directions(input_tiff_path, output_tiff_path, output_tiff_path2)
