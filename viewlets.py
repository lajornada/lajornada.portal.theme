from plone.app.layout.viewlets import common as base

class LikeViewlet(base.ViewletBase):
	""" A Viewlet.
	"""

	def name(self):
		return "Plone"


class AddMultimediaButtonViewlet(base.ViewletBase):
	""" Agrega el boton "agregar video" alos nitf
	"""