# -*- coding: utf-8 -*-CRISTIAN ############################################################################# Python code generated with wxFormBuilder (version Sep 12 2010)## http://www.wxformbuilder.org/#### PLEASE DO "NOT" EDIT THIS FILE!###########################################################################import wximport wx.animate############################################################################# Class FrameMain###########################################################################class FrameMain ( wx.Frame ):		def __init__( self, parent ):		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Proyecto Investigación LASER", pos = wx.DefaultPosition, size = wx.Size( 1400,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )				self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )				BoxMain = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )				Sizer_titulo = wx.BoxSizer( wx.VERTICAL )				self.m_Bienvenido = wx.StaticText( self, wx.ID_ANY, u"Bienvenidos al proyecto de investigación Modelo híbrido de control  con señales  mioeléctrica y encefalográfica para la identificación de gestos en miembro superior\n", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )		self.m_Bienvenido.Wrap( 800 )		self.m_Bienvenido.SetFont( wx.Font( 36, 70, 90, 90, False, wx.EmptyString ) )		self.m_Bienvenido.SetForegroundColour( wx.Colour( 53, 55, 254 ) )				Sizer_titulo.Add( self.m_Bienvenido, 0, wx.ALL, 5 )				Sizer_imagen = wx.BoxSizer( wx.HORIZONTAL )				self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../../Downloads/bienvenido.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )		Sizer_imagen.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER|wx.ALIGN_BOTTOM, 5 )				Sizer_titulo.Add( Sizer_imagen, 10, wx.ALIGN_CENTER, 5 )				Sizer_botones = wx.BoxSizer( wx.HORIZONTAL )				Sizer_botones.SetMinSize( wx.Size( 300,50 ) ) 		self.button_iniciar = wx.Button( self, wx.ID_ANY, u"Iniciar", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )		self.button_iniciar.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )		self.button_iniciar.SetForegroundColour( wx.Colour( 17, 0, 254 ) )		self.button_iniciar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )				Sizer_botones.Add( self.button_iniciar, 0, wx.ALIGN_CENTER_VERTICAL, 5 )				self.button_salir = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )		self.button_salir.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )				Sizer_botones.Add( self.button_salir, 0, wx.ALIGN_CENTER_VERTICAL, 50 )				Sizer_titulo.Add( Sizer_botones, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL, 0 )				BoxMain.Add( Sizer_titulo, 50, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER, 0 )				self.SetSizer( BoxMain )		self.Layout()				self.Centre( wx.BOTH )				# Connect Events		self.button_iniciar.Bind( wx.EVT_BUTTON, self.OnClickIniciar )		self.button_salir.Bind( wx.EVT_BUTTON, self.OnClickSalir )		def __del__( self ):		pass			# Virtual event handlers, overide them in your derived class	def OnClickIniciar( self, event ):		event.Skip()		def OnClickSalir( self, event ):		event.Skip()	############################################################################# Class FrameObjetivos###########################################################################class FrameObjetivos ( wx.Frame ):		def __init__( self, parent ):		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Objetivos de la investigación", pos = wx.DefaultPosition, size = wx.Size( 1400,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )				self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )				bSizer4 = wx.BoxSizer( wx.VERTICAL )				self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Objetivo General", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText2.Wrap( -1 )		self.m_staticText2.SetFont( wx.Font( 34, 70, 90, 90, False, wx.EmptyString ) )				bSizer4.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL, 10 )				bSizer7 = wx.BoxSizer( wx.VERTICAL )				self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"\n Diseñar un modelo híbrido que relacione las  señales \n mioeléctrica y   las señales encefalográficas para la  \n identificación de gestos  comunes realizados por  un \n miembro superior. \n\n", wx.DefaultPosition, wx.Size( 800,-1 ), 0 )		self.m_staticText3.Wrap( -1 )		self.m_staticText3.SetFont( wx.Font( 26, 70, 90, 90, False, wx.EmptyString ) )				bSizer7.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )				bSizer9 = wx.BoxSizer( wx.VERTICAL )				self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Objetivos Especificos", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText4.Wrap( -1 )		self.m_staticText4.SetFont( wx.Font( 34, 70, 90, 90, False, wx.EmptyString ) )				bSizer9.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )				bSizer10 = wx.BoxSizer( wx.VERTICAL )				self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"\n - Establecer los gestos que serán razón de estudio en el desarrollo del proyecto. \n -Identificar, caracterizar, procesar y analizar las características principales de las  señales mioeléctricas junto a las señales encefalográficas obtenidas en el estudio.  \n - Definir  un modelo conceptual que incluya las señales bioeléctricas relacionadas del miembro  superior.   \n - Realizar un cuadro comparativo donde se compare la efectividad  del modelo relacional ( señales mioeléctricas y  \n encefalográficas) obtenidos  de los gestos estudiados contra un modelo  ya establecido  de gestos obtenidos con \n señales mioeléctricas. \n", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText5.Wrap( -1 )		self.m_staticText5.SetFont( wx.Font( 22, 70, 90, 90, False, wx.EmptyString ) )				bSizer10.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )				bSizer8 = wx.BoxSizer( wx.HORIZONTAL )				bSizer8.SetMinSize( wx.Size( 300,80 ) ) 		self.button_siguiente = wx.Button( self, wx.ID_ANY, u"Siguiente", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )		self.button_siguiente.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )				bSizer8.Add( self.button_siguiente, 0, wx.ALL, 5 )				self.button_salir = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )		self.button_salir.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )				bSizer8.Add( self.button_salir, 0, wx.ALL, 5 )				bSizer10.Add( bSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 50 )				bSizer9.Add( bSizer10, 1, wx.EXPAND, 5 )				bSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )				bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )				self.SetSizer( bSizer4 )		self.Layout()				self.Centre( wx.BOTH )				# Connect Events		self.button_siguiente.Bind( wx.EVT_BUTTON, self.OnClickConcentimiento )		self.button_salir.Bind( wx.EVT_BUTTON, self.OnClickSalir )		def __del__( self ):		pass			# Virtual event handlers, overide them in your derived class	def OnClickConcentimiento( self, event ):		event.Skip()		def OnClickSalir( self, event ):		event.Skip()	############################################################################# Class FrameConsentimiento###########################################################################class FrameConsentimiento ( wx.Frame ):		def __init__( self, parent ):		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Consentimiento de la investigación", pos = wx.DefaultPosition, size = wx.Size( 1400,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )				self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )				bSizer4 = wx.BoxSizer( wx.VERTICAL )				self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Consentimiento informado", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText2.Wrap( -1 )		self.m_staticText2.SetFont( wx.Font( 34, 70, 90, 90, False, wx.EmptyString ) )				bSizer4.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL, 10 )				bSizer7 = wx.BoxSizer( wx.VERTICAL )				self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"\n Para continuar con el desarrollo del experimento es \n necesario  que usted, como participante lea \n cuidadosamente el consentimiento  informado \n previamente entregado por el equipo investigador, si \n tiene alguna duda o no entiende alguna palabra del \n consentiento por favor no dude en realizar todas las \n preguntas pertinente al equipo investigador.\n", wx.DefaultPosition, wx.Size( 700,-1 ), 0 )		self.m_staticText3.Wrap( -1 )		self.m_staticText3.SetFont( wx.Font( 26, 70, 90, 90, False, wx.EmptyString ) )				bSizer7.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )				bSizer9 = wx.BoxSizer( wx.VERTICAL )				bSizer10 = wx.BoxSizer( wx.VERTICAL )				self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"\n \n ¿ Ha leido y comprendido en\n  su totalidad el consentimiento \n informado dado con  anterioridad ? \n", wx.DefaultPosition, wx.Size( 400,-1 ), 0 )		self.m_staticText5.Wrap( -1 )		self.m_staticText5.SetFont( wx.Font( 24, 70, 90, 90, False, wx.EmptyString ) )				bSizer10.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )				bSizer8 = wx.BoxSizer( wx.HORIZONTAL )				bSizer8.SetMinSize( wx.Size( 300,50 ) ) 		self.button_siguiente = wx.Button( self, wx.ID_ANY, u"Siguiente", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )		self.button_siguiente.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )				bSizer8.Add( self.button_siguiente, 0, wx.ALL, 5 )				self.button_salir = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )		self.button_salir.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )				bSizer8.Add( self.button_salir, 0, wx.ALL, 5 )				bSizer10.Add( bSizer8, 2, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 50 )				bSizer9.Add( bSizer10, 1, wx.EXPAND, 5 )				bSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )				bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )				self.SetSizer( bSizer4 )		self.Layout()				self.Centre( wx.BOTH )				# Connect Events		self.button_siguiente.Bind( wx.EVT_BUTTON, self.OnClickConcentimiento )		self.button_salir.Bind( wx.EVT_BUTTON, self.OnClickSalir )		def __del__( self ):		pass			# Virtual event handlers, overide them in your derived class	def OnClickConcentimiento( self, event ):		event.Skip()		def OnClickSalir( self, event ):		event.Skip()	############################################################################# Class FrameCalibracion###########################################################################class FrameCalibracion( wx.Frame ):		def __init__( self, parent ):		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Calibración de herramientas", pos = wx.DefaultPosition, size = wx.Size( 1400,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )				self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )				bSizer4 = wx.BoxSizer( wx.VERTICAL )				self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Calibración de herramientas", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText2.Wrap( -1 )		self.m_staticText2.SetFont( wx.Font( 34, 70, 90, 90, False, wx.EmptyString ) )				bSizer4.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL, 10 )				bSizer7 = wx.BoxSizer( wx.VERTICAL )				self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"\n En esta etapa del proceso el equipo investigador \n procedera a realizar la calibración de la herramienta \n UltraCortex (casco) y la herramienta MYO (brazalete)", wx.DefaultPosition, wx.Size( 700,-1 ), 0 )		self.m_staticText3.Wrap( -1 )		self.m_staticText3.SetFont( wx.Font( 26, 70, 90, 90, False, wx.EmptyString ) )				bSizer7.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )				bSizer9 = wx.BoxSizer( wx.VERTICAL )				bSizer10 = wx.BoxSizer( wx.VERTICAL )				self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"\n \n  \n \n ¿ Las herramientas ya han sido\n  calibradas en su totalidad  por \n el equipo de investigación? \n", wx.DefaultPosition, wx.Size( 400,-1 ), 0 )		self.m_staticText5.Wrap( -1 )		self.m_staticText5.SetFont( wx.Font( 24, 70, 90, 90, False, wx.EmptyString ) )				bSizer10.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )				bSizer8 = wx.BoxSizer( wx.HORIZONTAL )				bSizer8.SetMinSize( wx.Size( 300,50 ) ) 		self.button_siguiente = wx.Button( self, wx.ID_ANY, u"Siguiente", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )		self.button_siguiente.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )				bSizer8.Add( self.button_siguiente, 0, wx.ALL, 5 )				self.button_salir = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )		self.button_salir.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )				bSizer8.Add( self.button_salir, 0, wx.ALL, 5 )				bSizer10.Add( bSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 170 )				bSizer9.Add( bSizer10, 1, wx.EXPAND, 5 )				bSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )				bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )				self.SetSizer( bSizer4 )		self.Layout()				self.Centre( wx.BOTH )				# Connect Events		self.button_siguiente.Bind( wx.EVT_BUTTON, self.OnClickCInstruccion )		self.button_salir.Bind( wx.EVT_BUTTON, self.OnClickSalir )		def __del__( self ):		pass			# Virtual event handlers, overide them in your derived class	def OnClickCInstruccion( self, event ):		event.Skip()		def OnClickSalir( self, event ):		event.Skip()	############################################################################# Class FrameInstrucion###########################################################################class FrameInstrucion ( wx.Frame ):		def __init__( self, parent ):		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Instruciones del proyecto", pos = wx.DefaultPosition, size = wx.Size( 1400,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )				self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )				bSizer4 = wx.BoxSizer( wx.VERTICAL )				self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Instrucciones de toma de señales", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText2.Wrap( -1 )		self.m_staticText2.SetFont( wx.Font( 34, 70, 90, 90, False, wx.EmptyString ) )				bSizer4.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL, 10 )				bSizer7 = wx.BoxSizer( wx.VERTICAL )				self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"\n A continuación usted tendra que realizar una serie de \n gestos con o sin ayuda de elementos que le seran \n brindados por el equipo de investigación, por \n favor lea  con atención y realice el gesto lo mas \n parecido posible  a las imagenes de refencia, tendra \n que realizar los  los gestos las veces definidas y el tiempo que se  le indique el equipo de investigación.", wx.DefaultPosition, wx.Size( 700,-1 ), 0 )		self.m_staticText3.Wrap( -1 )		self.m_staticText3.SetFont( wx.Font( 26, 70, 90, 90, False, wx.EmptyString ) )				bSizer7.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )				bSizer9 = wx.BoxSizer( wx.VERTICAL )				bSizer10 = wx.BoxSizer( wx.VERTICAL )				self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"\n  ¿ Esta de acuerdo con seguir las\n  instruciones definidas por el \n equipo de investigación? \n", wx.DefaultPosition, wx.Size( 400,-1 ), 0 )		self.m_staticText5.Wrap( -1 )		self.m_staticText5.SetFont( wx.Font( 24, 70, 90, 90, False, wx.EmptyString ) )				bSizer10.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )				bSizer8 = wx.BoxSizer( wx.HORIZONTAL )				bSizer8.SetMinSize( wx.Size( 300,50 ) ) 		self.button_siguiente = wx.Button( self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )		self.button_siguiente.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )				bSizer8.Add( self.button_siguiente, 0, wx.ALL, 5 )				self.button_salir = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )		self.button_salir.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )				bSizer8.Add( self.button_salir, 0, wx.ALL, 5 )				bSizer10.Add( bSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 170 )				bSizer9.Add( bSizer10, 1, wx.EXPAND, 5 )				bSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )				bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )				self.SetSizer( bSizer4 )		self.Layout()				self.Centre( wx.BOTH )				# Connect Events		self.button_siguiente.Bind( wx.EVT_BUTTON, self.OnClickConcentimiento )		self.button_salir.Bind( wx.EVT_BUTTON, self.OnClickSalir )		def __del__( self ):		pass			# Virtual event handlers, overide them in your derived class	def OnClickConcentimiento( self, event ):		event.Skip()		def OnClickSalir( self, event ):		event.Skip()	############################################################################# Class FrameGesto1###########################################################################class FrameGesto1 ( wx.Frame ):		def __init__( self, parent ):		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Captura de señales para el gesto 1", pos = wx.DefaultPosition, size = wx.Size( 1400,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )				self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )				bSizer4 = wx.BoxSizer( wx.VERTICAL )				self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Captura de señales para el primer gesto \n", wx.DefaultPosition, wx.Size( 700,-1 ), 0 )		self.m_staticText2.Wrap( -1 )		self.m_staticText2.SetFont( wx.Font( 34, 70, 90, 90, False, wx.EmptyString ) )				bSizer4.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL, 10 )				bSizer49 = wx.BoxSizer( wx.VERTICAL )				bSizer50 = wx.BoxSizer( wx.HORIZONTAL )				bSizer50.SetMinSize( wx.Size( 700,-1 ) ) 		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Para iniciar el experimento por favor observe \n ", wx.DefaultPosition, wx.Size( 1000,-1 ), 0 )		self.m_staticText30.Wrap( -1 )		self.m_staticText30.SetFont( wx.Font( 17, 70, 90, 90, False, wx.EmptyString ) )				bSizer50.Add( self.m_staticText30, 0, wx.ALL, 5 )				bSizer52 = wx.BoxSizer( wx.VERTICAL )				bSizer52.SetMinSize( wx.Size( 90,-1 ) ) 		self.m_button32 = wx.Button( self, wx.ID_ANY, u"Inicio", wx.Point( -1,-1 ), wx.Size( 150,-1 ), 0 )		self.m_button32.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )				bSizer52.Add( self.m_button32, 0, wx.TOP, 10 )				bSizer50.Add( bSizer52, 1, 0, 5 )				self.m_animCtrl1 = wx.animate.AnimationCtrl( self, wx.ID_ANY, wx.animate.NullAnimation, wx.DefaultPosition, wx.Size( -1,-1 ), wx.animate.AC_DEFAULT_STYLE )		self.m_animCtrl1.LoadFile( u"/Users/macfabian/Desktop/manos.gif" )		self.m_animCtrl1.SetMinSize( wx.Size( 200,-1 ) )				bSizer50.Add( self.m_animCtrl1, 0, wx.ALIGN_CENTER, 5 )				bSizer49.Add( bSizer50, 1, 0, 5 )				bSizer51 = wx.BoxSizer( wx.VERTICAL )				self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Señal EMG", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText31.Wrap( -1 )		self.m_staticText31.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )				bSizer51.Add( self.m_staticText31, 0, wx.ALL, 5 )				bSizer57 = wx.BoxSizer( wx.VERTICAL )				bSizer51.Add( bSizer57, 1, wx.EXPAND, 5 )				bSizer49.Add( bSizer51, 1, wx.EXPAND, 5 )				bSizer53 = wx.BoxSizer( wx.VERTICAL )				self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Señal EEG", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText32.Wrap( -1 )		self.m_staticText32.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )				bSizer53.Add( self.m_staticText32, 0, wx.ALL, 5 )				bSizer49.Add( bSizer53, 1, wx.EXPAND, 5 )				bSizer8 = wx.BoxSizer( wx.HORIZONTAL )				self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Tiempo:", wx.DefaultPosition, wx.Size( 550,-1 ), 0 )		self.m_staticText33.Wrap( -1 )		self.m_staticText33.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )				bSizer8.Add( self.m_staticText33, 0, wx.ALL, 5 )				self.button_siguiente = wx.Button( self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )		self.button_siguiente.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )				bSizer8.Add( self.button_siguiente, 0, wx.ALL, 5 )				self.button_salir = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )		self.button_salir.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )				bSizer8.Add( self.button_salir, 0, wx.ALL, 5 )				bSizer49.Add( bSizer8, 0, wx.TOP, 1 )				bSizer4.Add( bSizer49, 1, wx.EXPAND, 5 )				self.SetSizer( bSizer4 )		self.Layout()				self.Centre( wx.BOTH )				# Connect Events		self.m_button32.Bind( wx.EVT_BUTTON, self.OnClickInicio )		self.button_siguiente.Bind( wx.EVT_BUTTON, self.OnClickConcentimiento )		self.button_salir.Bind( wx.EVT_BUTTON, self.OnClickSalir )		def __del__( self ):		pass			# Virtual event handlers, overide them in your derived class	def OnClickInicio( self, event ):		event.Skip()		def OnClickConcentimiento( self, event ):		event.Skip()		def OnClickSalir( self, event ):		event.Skip()	