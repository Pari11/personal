require(RNetCDF)
require(sp)

# put your working directory here:
setwd("D:/rg")

# read variable and dimensions:
nc_in          <- open.nc("yfin_20141219.nc")
nc_var         <- var.get.nc(nc_in, "yft_adu")
nc_lon         <- var.get.nc(nc_in, "lon")
nc_lat         <- var.get.nc(nc_in, "lat")
close.nc(nc_in)
rm(nc_in)

# assuming a regular grid (which by the way appears not entirely true for this data set):
gt             <- GridTopology(cellcentre.offset = c(nc_lon[1], nc_lat[1]),
                               cellsize = c((tail(nc_lon, 1) - nc_lon[1])/(length(nc_lon) - 1), (tail(nc_lat, 1) - nc_lat[1])/(length(nc_lat) - 1)),
                               cells.dim = c(length(nc_lon), length(nc_lat)))
sg             <- SpatialGrid(gt, CRS("+proj=longlat +datum=WGS84"))
sgdf           <- SpatialGridDataFrame(sg, data.frame(var = as.vector(nc_var[,ncol(nc_var):1])))

# plot your grid:
image(sgdf["var"], col = rainbow(15), breaks = 10^(-15:0))

# load coastal lines of Indonesia:
con <- url("http://biogeo.ucdavis.edu/data/gadm2/R/IDN_adm0.RData")
load(file = con)
close(con)

# plot coastal lines:
plot(gadm, add = T, col = "lightgreen")
