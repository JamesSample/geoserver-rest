import os
import gdal

def raster_value(path):
    file = os.path.basename(path)
    file_format = file.split('.')[-1]
    file_name = file.split('.')[0]

    if file_format == 'tif':
        gtif = gdal.Open(path)
        srcband = gtif.GetRasterBand(1)
        srcband.ComputeStatistics(0)
        N = srcband.GetMaximum()- srcband.GetMinimum() + 1
        N = int(N)
        min = int(srcband.GetMinimum())
        result = {'N': N, 'min':min, 'file_name':file_name}
        return result

    else:
        print('sorry, file format is incorrect')


