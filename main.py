import ifcopenshell

from .rules import windowRule
from .rules import doorRule

model = ifcopenshell.open('C:/Users/friis/OneDrive - Danmarks Tekniske Universitet/DTU/41934 - Advanced BIM/IFC/CES_BLD_24_06_STR.ifc')

windowResult = windowRule.checkRule(model)
doorResult = doorRule.checkRule(model)

print("Window result:", windowResult)
print("Door result:", doorResult)
