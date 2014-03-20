# -*- coding: utf-8 -*-

from Products.ATContentTypes.interfaces import IATDocument
from ftw.pdfgenerator.interfaces import IBuilder
from ftw.pdfgenerator.interfaces import ICustomizableLayout
from ftw.pdfgenerator.layout.customizable import CustomizableLayout
from zope.component import adapts
from zope.interface import Interface
from zope.interface import implements

class SessionLayout(CustomizableLayout):
    adapts(IATDocument, Interface, IBuilder)
    implements(ICustomizableLayout)

    template_directories = ['session_templates']
    template_name = 'layout.tex'

    def before_render_hook(self):
        self.use_babel()
        self.use_package('inputenc', options='utf8')
        self.use_package('fontenc', options='T1')

