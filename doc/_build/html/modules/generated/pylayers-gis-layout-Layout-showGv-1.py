from pylayers.gis.Layout import *
L = Layout()
L.loadstr('exemple.str')
L.buildGt()
L.buildGr()
L.buildGv()
fig,ax=L.showGs()
L.showGv(fig=fig,ax=ax)
plt.axis('off')
plt.show()
