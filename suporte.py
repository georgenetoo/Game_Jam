import pygame
import os
from csv import reader
from os import walk

import pygame.image

csv_map = os.path.join('map', 'map_FloorBlocks.csv')
csv_grass = os.path.join('map', 'map_Grass.csv')
csv_object = os.path.join('map', 'map_LargeObjects.csv')
grass = os.path.join('graphics', 'grass')
object = os.path.join('graphics', 'objects')


def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_folder(path):
    surface_list = []

    for _,_,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list


