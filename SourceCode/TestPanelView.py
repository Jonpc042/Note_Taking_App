import wx


def __init__(self, parent, pixelsPerUnit=20):
    wx.StatusBar.__init__(self, parent, -1)

    self.pixelsPerUnit = pixelsPerUnit
    self.SetMinHeight(16)

    # Dummy panel para encobrir a ScrollBar
    # self.panelDummy = wx.Panel(self)
    # self.panelDummy.SetBackgroundColour('green')
    # self.panelDummy.Show(False)

    self.SetFieldsCount(3)
    self.SetStatusWidths([-3, -1, -1])
    # self.SetStatusText("Aqui vai a legenda dos Logs...", 0)

    self.sb = wx.ScrollBar(self)
    self.sb.show = False
    self.sb.SetScrollbar(0, 10, 100, 10)
    self.Bind(wx.EVT_SIZE, self._OnSize)

    self.sb.Bind(wx.EVT_SCROLL_THUMBTRACK, self._OnScroll)
    self.sb.Bind(wx.EVT_SCROLL_LINEUP, self._OnScroll)
    self.sb.Bind(wx.EVT_SCROLL_PAGEUP, self._OnScroll)
    self.sb.Bind(wx.EVT_SCROLL_LINEDOWN, self._OnScroll)
    self.sb.Bind(wx.EVT_SCROLL_PAGEDOWN, self._OnScroll)

    self.sb.ultimaPosicao = 0
    self.Reposition()

    # self.timer = wx.PyTimer(self.Notify)
    # self.timer.Start(1000)
    # self.Notify()

    self.HideScrollBar()
