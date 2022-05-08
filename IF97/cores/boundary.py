from math import sqrt, log
from ..coefficients import nb23, InBoundT3


class Boundary23:
    """Class for boundary equations between region 2 and 3

    classmethod
    -------------
    getPress(cls, t)
        return pressure at boundary line between region 2 and region 3
    getTemp(cls, p)
        return temperature at boundary line betweeen region 2 and region 3
    """

    _n = nb23

    @classmethod
    def getPress(cls, t):
        """Get pressure at boundary line between region 2 and region 3


        Parameters
        ----------
        t: float
            temperature (K)


        Returns
        -------
        ans: float or None
            return presssure (KPa) or if value of t not in range or exceed range of validity return None instead


        Range of validity
        -----------------
        623.15 K <= t <= 863.15 K or 350 C <= t <= 800 C
        """

        if 623.15 <= t <= 863.15:
            _n = nb23
            theta = t/1
            ans = cls._n[0] + cls._n[1]*theta + cls._n[2]*(theta**2)
            return ans*1000
        else:
            return None

    @classmethod
    def getTemp(cls, p):
        """Get temperature at boundary line between region 2 and region 3


        Parameters
        ----------
        p: float
            presssure (KPa)


        Returns
        -------
        ans: float or None
            return temperature (K) or if value of p is not in range or exceed range of validity return None instead


        Range of validity
        -----------------
        16.5291643e3 KPa <= p <= 1e5 KPa or 16.5291643 MPa <= p <= 100 MPa
        """

        if 16.5291643e3 <= p <= 1e5:
            pi = p/1000
            ans = cls._n[3] + sqrt((pi - cls._n[4])/cls._n[2])
            return ans*1
        else:
            return None


def temp3(p, desc=""):
    """Boundary eequations for subregion 3


    Parameters
    ----------
    p: float
        presssure (KPa)
    desc: str
        one of input keys, see below


    Returns
    -------
    t: float or None
        return temperature (K) or if value of desc is wrong return None instead


    Input keys
    ----------
    "3ab": Represent the boundary equation between subregion 3a and 3d

    "3cd": Represent the boundary equation between subregion 3d, 3g, 3l, 3q, or 3s and subregion 3c

    "3gh": Represent the boundary equation between subregion 3h or 3m and subregion 3g or 3l

    "3ij": Represent the boundary equation between subregion 3j and subregion 3i or 3p

    "3jk":

    "3mn":

    "3op":

    "3qu":

    "3rx":

    "3uv":

    "3wx":

    For further details see http://www.iapws.org/relguide/Supp-VPT3-2016.pdf
    """

    pi = p/1e3

    if desc and desc.lower() in InBoundT3.keys():
        if desc.lower() != "3ab" and desc.lower() != "3ef" and desc.lower() != "3op" and desc.lower() != "3wx":
            koef = InBoundT3[desc.lower()]

            theta = 0.
            for ni, Ii in zip(koef["n"], koef["I"]):
                theta += ni*(pi**Ii)

            t = theta*1
            return t
        elif desc.lower() == "3ab" or desc.lower() == "3op" or desc.lower() == "3wx":
            koef = InBoundT3[desc.lower()]

            theta = 0.
            for ni, Ii in zip(koef["n"], koef["I"]):
                theta += ni*(log(pi)**Ii)

            t = theta*1
            return t
    elif desc and desc.lower() == "3ef":
        t = 3.727888004*(pi-22.064)+647.096
        return t
    else:
        return None