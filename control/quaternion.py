"""Quaternion arithmetic for attitude representation."""
import math
from dataclasses import dataclass

@dataclass
class Quaternion:
    w: float
    x: float
    y: float
    z: float

    def norm(self) -> float:
        return math.sqrt(self.w**2 + self.x**2 + self.y**2 + self.z**2)

    def normalise(self) -> 'Quaternion':
        n = self.norm()
        return Quaternion(self.w/n, self.x/n, self.y/n, self.z/n)

    def conjugate(self) -> 'Quaternion':
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def __mul__(self, other: 'Quaternion') -> 'Quaternion':
        w = self.w*other.w - self.x*other.x - self.y*other.y - self.z*other.z
        x = self.w*other.x + self.x*other.w + self.y*other.z - self.z*other.y
        y = self.w*other.y - self.x*other.z + self.y*other.w + self.z*other.x
        z = self.w*other.z + self.x*other.y - self.y*other.x + self.z*other.w
        return Quaternion(w, x, y, z)
