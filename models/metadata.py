from typing import List

from machine_learning.decision_tree.properties import Property

__CLASS_TARGET__ = {
    92: 0,
    88: 1,
    42: 2,
    90: 3,
    65: 4,
    16: 5,
    67: 6,
    95: 7,
    62: 8,
    15: 9,
    52: 10,
    6: 11,
    64: 12,
    53: 13
}


class Metadata():

    def __init__(self, object_id: int, ra: float, decl: float, gal_l: float, gal_b: float, ddf: bool, specz: float,
                 photoz: float, photoz_err: float, distmod: float, mwebv: float, target: int, kaggle_target: int) -> None:
        self.object_id = object_id
        self.ra = ra
        self.decl = decl
        self.gal_l = gal_l
        self.gal_b = gal_b
        self.ddf = ddf
        self.specz = specz
        self.photoz = photoz
        self.photoz_err = photoz_err
        self.distmod = distmod
        self.mwebv = mwebv
        self.target = target
        self.kaggle_target = kaggle_target

    def __repr__(self):
        return '(object_id: {}, ra: {}, decl: {}, gal_l: {}, gal_b: {}, ddf: {}, specz: {}, photoz: {}, photoz_err: {}, distmod: {}, mwebv: {}, target: [{} -> {}])'.format(
            self.object_id,
            self.ra,
            self.decl,
            self.gal_l,
            self.gal_b,
            self.ddf,
            self.specz,
            self.photoz,
            self.photoz_err,
            self.distmod,
            self.mwebv,
            self.kaggle_target,
            self.target
        )

    def __eq__(self, other):
        if type(other) is not Metadata:
            return False
        else:
            return self.object_id == other.object_id

    def __hash__(self):
        return hash(self.object_id)


def from_line(line: List[str]) -> Metadata:
    kaggle_target = int(line[11]) if len(line) == 12 else -1
    target = __CLASS_TARGET__[kaggle_target] if len(line) == 12 else -1
    return Metadata(
        object_id=int(line[0]),
        ra=float(line[1]),
        decl=float(line[2]),
        gal_l=float(line[3]),
        gal_b=float(line[4]),
        ddf=line[5] == '1',
        specz=float(line[6]),
        photoz=float(line[7]),
        photoz_err=float(line[8]),
        distmod=float(line[9]),
        mwebv=float(line[10]),
        target=target,
        kaggle_target=kaggle_target
    )


def features(meta: Metadata) -> List[float]:
    return [meta.ra, meta.decl, meta.gal_l, meta.gal_b, 1.0 if meta.ddf else 0.0, 0.0 if meta.ddf else 1.0, meta.specz,
            meta.photoz, meta.photoz_err, meta.distmod, meta.mwebv]


def label(meta: Metadata) -> float:
    return meta.target
