
class LiquidCalc:
	def __init__(self, vol1, temp1, vol2, temp2) -> None:
		self._vol1 = vol1
		self._temp1 = temp1
		self._vol2 = vol2
		self._temp2 = temp2
		self._resVol = None
		self._resTemp = None
		self._calc()

	def _calc(self) -> None:
		self._resVol = self._vol1 + self._vol2
		if self._resVol == 0:
			self._resTemp = 0
		else:
			self._resTemp = (self._vol1 * self._temp1 + self._vol2 * self._temp2) / self._resVol

	def getResultVolume(self) -> int:
		return self._resVol

	def getResultTemperature(self) -> int:
		return self._resTemp
