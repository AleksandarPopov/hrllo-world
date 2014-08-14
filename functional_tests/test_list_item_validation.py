from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
	@skip
	def test_cannot_add_empty_lsit_items(self):
		self.fail('write me!')
