from math import sin, cos, acos, pi, atan2
 
#############################################################################
def dms2dd(d, m, s):
    """Convertit un angle "degrés minutes secondes" en "degrés décimaux"
    """
    return d + m/60 + s/3600
 
#############################################################################
def dd2dms(dd):
    """Convertit un angle "degrés décimaux" en "degrés minutes secondes"
    """
    d = int(dd)
    x = (dd-d)*60
    m = int(x)
    s = (x-m)*60
    return d, m, s
 
#############################################################################
def deg2rad(dd):
    """Convertit un angle "degrés décimaux" en "radians"
    """
    return dd/180*pi
 
#############################################################################
def rad2deg(rd):
    """Convertit un angle "radians" en "degrés décimaux"
    """
    return rd/pi*180
 
#############################################################################
def distanceGPS(latA, longA, latB, longB):
    """Retourne la distance en mètres entre les 2 points A et B connus grâce à
       leurs coordonnées GPS (en radians).
    """
    # Rayon de la terre en mètres (sphère IAG-GRS80)
    RT = 6378137
    # angle en radians entre les 2 points
    S = acos(sin(latA)*sin(latB) + cos(latA)*cos(latB)*cos(abs(longB-longA)))
    # distance entre les 2 points, comptée sur un arc de grand cercle
    return S*RT
 
#############################################################################
def bearingGPS(latA, longA, latB, longB):
    x = cos(latB)*sin(abs(latA-latB))
    y = cos(latA)*sin(latB)-sin(latA)*cos(latB)*cos(abs(latA-latB))
    bearing = atan2(x, y)
    return bearing

if __name__ == "__main__":
 
    # cooordonnées GPS en radians du 1er point (ici, mairie de Tours)
    latA = deg2rad(47.13333333333333) # Nord
    longA = deg2rad(-1.7483333333333333) # Est
 
    # cooordonnées GPS en radians du 2ème point (ici, mairie de Limoges)
    latB = deg2rad(47.190555555555555) # Nord
    longB = deg2rad(-1.5686111111111112) # Est
 
    dist = distanceGPS(latA, longA, latB, longB)
    print(int(dist))