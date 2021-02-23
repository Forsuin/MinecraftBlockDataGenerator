import json

blockList = ["DIRT",
             "BEDROCK",
             "GLOWSTONE",
             "STONE",
             "GRANITE",
             "POLISHED_GRANITE",
             "DIORITE",
             "POLISHED_DIORITE",
             "ANDESITE",
             "POLISHED_ANDESITE",
             "GRASS_BLOCK",
             "COARSE_DIRT",
             "PODZOL",
             "SAND",
             "RED_SAND",
             "GRAVEL",
             "GLASS",
             "LAPIS_BLOCK",
             "SANDSTONE",
             "CHISELED_SANDSTONE",
             "CUT_SANDSTONE",
             "WHITE_WOOL",
             "ORANGE_WOOL",
             "MAGENTA_WOOL",
             "LIGHT_BLUE_WOOL",
             "YELLOW_WOOL",
             "LIME_WOOL",
             "PINK_WOOL",
             "GRAY_WOOL",
             "LIGHT_GRAY_WOOL",
             "CYAN_WOOL",
             "PURPLE_WOOL",
             "BLUE_WOOL",
             "BROWN_WOOL",
             "GREEN_WOOL",
             "RED_WOOL",
             "BLACK_WOOL",
             "GOLD_BLOCK",
             "IRON_BLOCK",
             "BRICKS",
             "OBSIDIAN",
             "DIAMOND_BLOCK",
             "ICE",
             "SNOW_BLOCK",
             "CLAY",
             "NETHERRACK",
             "WHITE_STAINED_GLASS",
             "ORANGE_STAINED_GLASS",
             "MAGENTA_STAINED_GLASS",
             "LIGHT_BLUE_STAINED_GLASS",
             "YELLOW_STAINED_GLASS",
             "LIME_STAINED_GLASS",
             "PINK_STAINED_GLASS",
             "GRAY_STAINED_GLASS",
             "LIGHT_GRAY_STAINED_GLASS",
             "CYAN_STAINED_GLASS",
             "PURPLE_STAINED_GLASS",
             "BLUE_STAINED_GLASS",
             "BROWN_STAINED_GLASS",
             "GREEN_STAINED_GLASS",
             "RED_STAINED_GLASS",
             "BLACK_STAINED_GLASS",
             "EMERALD_BLOCK",
             "REDSTONE_BLOCK",
             "WHITE_TERRACOTTA",
             "ORANGE_TERRACOTTA",
             "MAGENTA_TERRACOTTA",
             "LIGHT_BLUE_TERRACOTTA",
             "YELLOW_TERRACOTTA",
             "LIME_TERRACOTTA",
             "PINK_TERRACOTTA",
             "GRAY_TERRACOTTA",
             "LIGHT_GRAY_TERRACOTTA",
             "CYAN_TERRACOTTA",
             "PURPLE_TERRACOTTA",
             "BLUE_TERRACOTTA",
             "BROWN_TERRACOTTA",
             "GREEN_TERRACOTTA",
             "RED_TERRACOTTA",
             "BLACK_TERRACOTTA",
             "SLIME_BLOCK",
             "SEA_LANTERN",
             "TERRACOTTA",
             "COAL_BLOCK",
             "PACKED_ICE",
             "SMOOTH_STONE",
             "FROSTED_ICE",
             "MAGMA_BLOCK",
             "NETHER_WART_BLOCK",
             "BONE_BLOCK",
             "WHITE_GLAZED_TERRACOTTA",
             "ORANGE_GLAZED_TERRACOTTA",
             "MAGENTA_GLAZED_TERRACOTTA",
             "LIGHT_BLUE_GLAZED_TERRACOTTA",
             "YELLOW_GLAZED_TERRACOTTA",
             "LIME_GLAZED_TERRACOTTA",
             "PINK_GLAZED_TERRACOTTA",
             "GRAY_GLAZED_TERRACOTTA",
             "LIGHT_GRAY_GLAZED_TERRACOTTA",
             "CYAN_GLAZED_TERRACOTTA",
             "PURPLE_GLAZED_TERRACOTTA",
             "BLUE_GLAZED_TERRACOTTA",
             "BROWN_GLAZED_TERRACOTTA",
             "GREEN_GLAZED_TERRACOTTA",
             "RED_GLAZED_TERRACOTTA",
             "BLACK_GLAZED_TERRACOTTA",
             "WHITE_CONCRETE",
             "ORANGE_CONCRETE",
             "MAGENTA_CONCRETE",
             "LIGHT_BLUE_CONCRETE",
             "YELLOW_CONCRETE",
             "LIME_CONCRETE",
             "PINK_CONCRETE",
             "GRAY_CONCRETE",
             "LIGHT_GRAY_CONCRETE",
             "CYAN_CONCRETE",
             "PURPLE_CONCRETE",
             "BLUE_CONCRETE",
             "BROWN_CONCRETE",
             "GREEN_CONCRETE",
             "RED_CONCRETE",
             "BLACK_CONCRETE",
             "WHITE_CONCRETE_POWDER",
             "ORANGE_CONCRETE_POWDER",
             "MAGENTA_CONCRETE_POWDER",
             "LIGHT_BLUE_CONCRETE_POWDER",
             "YELLOW_CONCRETE_POWDER",
             "LIME_CONCRETE_POWDER",
             "PINK_CONCRETE_POWDER",
             "GRAY_CONCRETE_POWDER",
             "LIGHT_GRAY_CONCRETE_POWDER",
             "CYAN_CONCRETE_POWDER",
             "PURPLE_CONCRETE_POWDER",
             "BLUE_CONCRETE_POWDER",
             "BROWN_CONCRETE_POWDER",
             "GREEN_CONCRETE_POWDER",
             "RED_CONCRETE_POWDER",
             "BLACK_CONCRETE_POWDER",
             "BLUE_ICE",
             "BAMBOO",
             "HONEY_BLOCK",
             "HONEYCOMB_BLOCK",
             "NETHERITE_BLOCK",
             "ANCIENT_DEBRIS",
             "CRYING_OBSIDIAN",
             "GILDED_BLACKSTONE",
             "CHISELED_NETHER_BRICKS",
             "CRACKED_NETHER_BRICKS",
             "QUARTZ_BRICKS"]

modelList = []

blockListLight = ["BLUE_ICE", "NETHERITE_BLOCK", "QUARTZ_BRICKS"]

path = r'C:\Users\Ian\Documents\Minecraft Mod Dev\JSON File Maker\\'

file = open(r"C:\Users\Ian\Documents\Minecraft Mod Dev\JSON File Maker\test_stairs.json")
raw_data = file.read()
file.close()


def gen_blockitem_models():
    data = json.loads(raw_data)
    previous_block = "dirt"

    for block in blockList:
        l_block = block.lower()
        data["parent"] = data["parent"].replace(previous_block, l_block)
        previous_block = l_block

        new_name = path + l_block + '_stairs.json'

        file = open(new_name, "x")
        json_data = json.dumps(data)
        file.write(json_data)
        file.close()


def gen_block_state():
    data = json.loads(raw_data)

    previous_block = "dirt"

    for block in blockList:
        l_block = block.lower()
        for key in data:
            top_level = data["variants"]
            for facing in top_level:
                temp = data["variants"][facing]["model"]
                temp2 = temp.replace(previous_block, l_block)
                data["variants"][facing]["model"] = temp2
        previous_block = l_block

        new_name = path + l_block + '_stairs.json'

        file = open(new_name, "x")
        json_data = json.dumps(data)
        file.write(json_data)
        file.close()


def gen_block_model():
    stair_variant_list = ["normal", "inner", "outer"]

    file = open(r"C:\Users\Ian\Documents\Minecraft Mod Dev\JSON File Maker\test_stairs_inner.json")
    raw_data_inner = file.read()
    file.close()

    file = open(r"C:\Users\Ian\Documents\Minecraft Mod Dev\JSON File Maker\test_stairs_outer.json")
    raw_data_outer = file.read()
    file.close()

    for variant in stair_variant_list:
        if variant == "inner":
            data = json.loads(raw_data_inner)
        elif variant == "outer":
            data = json.loads(raw_data_outer)
        else:
            data = json.loads(raw_data)
        for block in blockList:
            l_block = block.lower()
            data["textures"]["bottom"] = "betterbuilding:block/{}".format(l_block)
            data["textures"]["top"] = "betterbuilding:block/{}".format(l_block)
            data["textures"]["side"] = "betterbuilding:block/{}".format(l_block)

        new_name = path + l_block + '_stairs.json'
        new_name_inner = path + l_block + '_stairs_inner.json'
        new_name_outer = path + l_block + '_stairs_outer.json'

        if variant == "inner":
            new_name = new_name_inner

        elif variant == "outer":
            new_name = new_name_outer
        file = open(new_name, "x")
        json_data = json.dumps(data)
        file.write(json_data)
        file.close()


def main():
    gen_blockitem_models()


if __name__ == '__main__':
    main()
