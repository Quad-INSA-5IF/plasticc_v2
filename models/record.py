from typing import List


class Record():
    def __init__(self, object_id: int, mjd: float, passband: int, flux: float, flux_err: float, detected: bool) -> None:
        self.object_id = object_id
        self.mjd = mjd
        self.passband = passband
        self.flux = flux
        self.flux_err = flux_err
        self.detected = detected

    def __repr__(self):
        return "(object_id: {}, mjd: {}, passband: {}, flux: {}, flux_err: {}, detected: {})".format(
            self.object_id,
            self.mjd,
            self.passband,
            self.flux,
            self.flux_err,
            self.detected
        )


def from_line(line: List[str]) -> Record:
    return Record(
        object_id=int(line[0]),
        mjd=int(float(line[1])),
        passband=int(line[2]),
        flux=float(line[3]),
        flux_err=float(line[4]),
        detected=line[5] == '1'
    )