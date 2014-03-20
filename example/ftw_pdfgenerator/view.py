# -*- coding: utf-8 -*-

from Products.ATContentTypes.interfaces import IATDocument
from ftw.pdfgenerator.interfaces import ILaTeXLayout
from ftw.pdfgenerator.interfaces import ILaTeXView
from ftw.pdfgenerator.view import MakoLaTeXView
from zope.component import adapts
from zope.interface import Interface
from zope.interface import implements

class SessionLaTeXView(MakoLaTeXView):
    adapts(IATDocument, Interface, ILaTeXLayout)
    implements(ILaTeXView)

    template_directories = ['session_templates']
    template_name = 'view.tex'

    def get_render_arguments(self):
        return {'title': self.convert(self.context.Title()),
                'description': self.convert(self.context.Description()),
                'creators': self.convert(", ".join(self.context.Creators()))}
