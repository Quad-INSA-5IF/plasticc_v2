from typing import List, Callable

from machine_learning.decision_tree.properties import Property
from models.metadata import Metadata
from models.record import Record

import utils.underscore as _


class PropertyBuilder:
    def __init__(self, light_curves_loader: Callable[[Metadata], List[Record]]):
        self.load = light_curves_loader

    def DDF(self) -> Property[Metadata, bool]: return Property('ddf', lambda x: x.ddf)

    def PHOTOZ(self) -> Property[Metadata, float]: return Property('photoz', lambda x: x.photoz)

    def SPECZ(self) -> Property[Metadata, float]: return Property('specz', lambda x: x.specz)

    def MWEBV(self) -> Property[Metadata, float]: return Property('photoz', lambda x: x.mwebv)

    def FLUX_PASSBAND_U(self) -> Property[Metadata, List[float]]:
        return Property("passband u", self._flux_passband_u)

    def FLUX_PASSBAND_G(self) -> Property[Metadata, List[float]]:
        return Property("passband g", self._flux_passband_g)

    def FLUX_PASSBAND_R(self) -> Property[Metadata, List[float]]:
        return Property("passband r", self._flux_passband_r)

    def FLUX_PASSBAND_I(self) -> Property[Metadata, List[float]]:
        return Property("passband i", self._flux_passband_i)

    def FLUX_PASSBAND_Z(self) -> Property[Metadata, List[float]]:
        return Property("passband z", self._flux_passband_z)

    def FLUX_PASSBAND_Y(self) -> Property[Metadata, List[float]]:
        return Property("passband Y", self._flux_passband_Y)

    def FLUX_ERR_PASSBAND_U(self) -> Property[Metadata, List[float]]:
        return Property("passband_err u", self._flux_err_passband_u).memoize()

    def FLUX_ERR_PASSBAND_G(self) -> Property[Metadata, List[float]]:
        return Property("passband_err g", self._flux_err_passband_g).memoize()

    def FLUX_ERR_PASSBAND_R(self) -> Property[Metadata, List[float]]:
        return Property("passband_err r", self._flux_err_passband_r).memoize()

    def FLUX_ERR_PASSBAND_I(self) -> Property[Metadata, List[float]]:
        return Property("passband_err i", self._flux_err_passband_i).memoize()

    def FLUX_ERR_PASSBAND_Z(self) -> Property[Metadata, List[float]]:
        return Property("passband_err z", self._flux_err_passband_z).memoize()

    def FLUX_ERR_PASSBAND_Y(self) -> Property[Metadata, List[float]]:
        return Property("passband_err Y", self._flux_err_passband_Y).memoize()

    def _get_flux(self, records: List[Record]) -> List[float]: return _.map(records, lambda it: it.flux)

    def _get_flux_err(self, records: List[Record]) -> List[float]: return _.map(records, lambda it: it.flux_err)

    def _get_passband(self, star: Metadata, passband: int) -> List[Record]:
        return _.filter(self.load(star), lambda it: it.passband == passband)

    def _passband_u(self, star: Metadata) -> List[Record]: return self._get_passband(star, 0)

    def _passband_g(self, star: Metadata) -> List[Record]: return self._get_passband(star, 1)

    def _passband_r(self, star: Metadata) -> List[Record]: return self._get_passband(star, 2)

    def _passband_i(self, star: Metadata) -> List[Record]: return self._get_passband(star, 3)

    def _passband_z(self, star: Metadata) -> List[Record]: return self._get_passband(star, 4)

    def _passband_Y(self, star: Metadata) -> List[Record]: return self._get_passband(star, 5)

    def _flux_passband_u(self, star: Metadata): return self._get_flux(self._passband_u(star))

    def _flux_passband_g(self, star: Metadata): return self._get_flux(self._passband_g(star))

    def _flux_passband_r(self, star: Metadata): return self._get_flux(self._passband_r(star))

    def _flux_passband_i(self, star: Metadata): return self._get_flux(self._passband_i(star))

    def _flux_passband_z(self, star: Metadata): return self._get_flux(self._passband_z(star))

    def _flux_passband_Y(self, star: Metadata): return self._get_flux(self._passband_Y(star))

    def _flux_err_passband_u(self, star: Metadata): return self._get_flux_err(self._passband_u(star))

    def _flux_err_passband_g(self, star: Metadata): return self._get_flux_err(self._passband_g(star))

    def _flux_err_passband_r(self, star: Metadata): return self._get_flux_err(self._passband_r(star))

    def _flux_err_passband_i(self, star: Metadata): return self._get_flux_err(self._passband_i(star))

    def _flux_err_passband_z(self, star: Metadata): return self._get_flux_err(self._passband_z(star))

    def _flux_err_passband_Y(self, star: Metadata): return self._get_flux_err(self._passband_Y(star))
