# -*- coding: utf-8 -*-

""" Example 1

More detailed description.
"""

from gis_tools.raster import RasterMap
from gis_tools.layer import PolygonLayer

# __all__ = []
# __version__ = '0.1'
__author__ = 'Benjamin Pillot'
__copyright__ = 'Copyright 2017, Benjamin Pillot'
__email__ = 'benjaminpillot@riseup.net'


# Create a digital elevation model from SRTM DEM of French Guiana
biomass = RasterMap("biomasse_ressource.tif", no_data_value=-9999)

# Import a geographical layer made of 6 large polygons from a shapefile
layer = PolygonLayer("enp_pn_s_973.shp")

# Convert DEM to layer's coordinate reference system
biomass = biomass.to_crs(layer.crs)

# Create ZonalStatistics instance from biomass and layer. 
zonal_stat = ZonalStatistics(biomass, layer, is_surface_weighted=False, all_touched=True)

# Compute slope average within each polygon
avg = zonal_stat.mean()
print(avg)