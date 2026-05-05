from xml.etree import ElementTree
import os

class PlantItem:
    def __init__(self, xml_source):
        self.id = xml_source.get('id')
        self.scientific_name = xml_source.find('scientific_name').text
        self.common_name = xml_source.find('common_name').text
        self.icon_source = xml_source.find('image_path').text
        
        self.maintenance = []
        self.tips = []

        for item in xml_source.find('maintenance'):
            self.maintenance.append(item.text)

        for item in xml_source.find('tips'):
            self.tips.append(item.text)


class PlantDataModel:
    def __init__(self, path):
        self.LoadPlantData(path)

    def LoadPlantData(self, path):
        tree = ElementTree.parse(path)
        xml_source = tree.getroot()
        
        self.__data = {}

        for plant in xml_source.findall('plant'):
            plant_item = PlantItem(plant)
            self.__data[plant_item.id] = plant_item

    def ListAllPlants(self):
        return list(self.__data.values())
    
    def ListPlantsWithCommonName(self, filter):
        if filter == '':
            return self.ListAllPlants()
        
        result = []
        for plant in self.__data.values():
            if filter.lower() in plant.common_name.lower():
                result.append(plant)
        return result
    
    def GetPlantByID(self, id):
        return self.__data[id]
        
     
if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))

    stripped_path = path[:-5]
    stripped_path += "resources\\data\\plants.xml"

    print(stripped_path)

    model = PlantDataModel(stripped_path)

    result = model.GetPlantByID('1003')

    print(result)