# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # def test_foo(self):
    #     items = [Item("foo", 0, 0)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEquals("fixme", items[0].name)
    
    def test_vest_item_should_decrease_after_one_day(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(51, items[0].quality)

    def test_aged_brie_quality_increases_over_time(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        for _ in range(3):
            gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(5, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
    

    def test_backstage_passes_quality_changes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(51, items[0].quality) 


if __name__ == '__main__':
    unittest.main()
