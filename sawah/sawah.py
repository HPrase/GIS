import mapnik
m = mapnik.Map(900,400)
m.background = mapnik.Color('white')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#FFD700')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('blue'), 1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Heri', s)
ds = mapnik.Shapefile(file="shp sawah/lu_sawah.shp")
layer = mapnik.Layer('sawah')
layer.datasource = ds
layer.styles.append('Heri')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'sawah.png', 'png')
print "rendered image to 'sawah.png'"
