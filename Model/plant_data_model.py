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
        pass # remove this when method is implemented
        # Hint: use the "values" method on the data dictionary
        # and return the list to complete this method.
    
    def ListPlantsWithCommonName(self, filter):
        pass # remove this when the method is completed.
        # 1. If the filter is an empty string, return all plants by callind
        #    ListAllPlants
        
        # 2. Otherwise, create an empty list and loop through the plant data.
        # 
            # 2-a. If the filter string is a substring of this plant,
            # then append it to the result list.
            # note that it should be case-INsensitive (meaning upper-case and 
            # lower-case shouldn't matter).

        # Return the filtered result
    
    def GetPlantByID(self, id):
        pass # remove this when method is implemented.
        # Get the plant from the dictionary using the plant data 
        
     
if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))

    stripped_path = path[:-5]
    stripped_path += "resources\\data\\plants.xml"

    print(stripped_path)

    model = PlantDataModel(stripped_path)

    result = model.GetPlantByID('1003')

    print(result)


