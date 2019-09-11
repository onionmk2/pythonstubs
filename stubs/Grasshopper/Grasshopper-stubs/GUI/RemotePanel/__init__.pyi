from typing import Tuple, Set, Iterable, List


class RcpLayoutKind:
    #None = 0
    Generic = 1
    ItemAdded = 2
    ItemRemoved = 3
    ItemMoved = 4
    ItemChanged = 5
    GroupAdded = 6
    GroupRemoved = 7
    GroupMoved = 8


class RcpLayoutEventArgs:
    def __init__(self, layout: RcpLayout, kind: RcpLayoutKind): ...
    @property
    def Layout(self) -> RcpLayout: ...
    @property
    def Kind(self) -> RcpLayoutKind: ...


class RcpLayout:
    @overload
    def __init__(self, document: GH_Document): ...
    @overload
    def __init__(self, document: GH_Document, groups: Iterable[RcpGroup]): ...
    def add_LayoutChanged(self, obj: LayoutChangedEventHandler) -> None: ...
    def remove_LayoutChanged(self, obj: LayoutChangedEventHandler) -> None: ...
    @overload
    def OnLayoutChanged(self) -> None: ...
    @overload
    def OnLayoutChanged(self, kind: RcpLayoutKind) -> None: ...
    @property
    def Document(self) -> GH_Document: ...
    @property
    def Count(self) -> int: ...
    @property
    def Group(self, index: int) -> RcpGroup: ...
    @Group.setter
    def Group(self, index: int, Value: RcpGroup) -> None: ...
    def EnsureGroup(self) -> RcpGroup: ...
    def Add(self, group: RcpGroup) -> None: ...
    def Remove(self, group: RcpGroup) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    def Write(self, writer: GH_IWriter) -> bool: ...
    def Read(self, reader: GH_IReader) -> bool: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def GetEnumeratorNotTypeSafe(self) -> IEnumerator: ...


class RcpGroup(RcpItem):
    def __init__(self): ...
    @property
    def Name(self) -> str: ...
    @Name.setter
    def Name(self, AutoPropertyValue: str) -> None: ...
    @property
    def Colour(self) -> Color: ...
    @Colour.setter
    def Colour(self, AutoPropertyValue: Color) -> None: ...
    @property
    def TitleRectangle(self) -> Rectangle: ...
    @property
    def IconRectangle(self) -> Rectangle: ...
    @property
    def NameRectangle(self) -> Rectangle: ...
    @property
    def ContentRectangle(self) -> Rectangle: ...
    @property
    def ItemLayoutRectangle(self) -> Rectangle: ...
    @property
    def ItemCount(self) -> int: ...
    @property
    def Items(self) -> Iterable[IRcpItem]: ...
    @overload
    def AddItem(self, item: IRcpItem) -> None: ...
    @overload
    def AddItem(self, item: IRcpItem, index: int) -> None: ...
    @overload
    def RemoveItem(self, item: IRcpItem) -> None: ...
    @overload
    def RemoveItem(self, index: int) -> None: ...
    def ReplaceItem(self, item: IRcpItem) -> bool: ...
    def RemovePlaceHolders(self) -> None: ...
    def IndexAt(self, pt: Point) -> int: ...
    def ItemAt(self, pt: Point) -> IRcpItem: ...
    def ImpliedInsertionIndex(self, pt: Point) -> Tuple[bool, float, int]: ...
    def OnDelete(self) -> None: ...
    def Toggle(self) -> None: ...
    def Expand(self) -> None: ...
    def Collapse(self) -> None: ...
    @property
    def Expanded(self) -> bool: ...
    @property
    def Collapsed(self) -> bool: ...
    @property
    def DesiredHeight(self) -> int: ...
    def LayoutItems(self) -> None: ...
    def Render(self, graphics: Graphics) -> None: ...
    def Write(self, writer: GH_IWriter) -> bool: ...
    def Read(self, reader: GH_IReader) -> bool: ...


class RcpIndex:
    def __init__(self, groupIndex: int, itemIndex: int): ...
    @property
    def Group(self) -> int: ...
    @property
    def Item(self) -> int: ...


class RcpPlaceHolder(RcpItem):
    def __init__(self, bounds: Rectangle): ...
    @property
    def DesiredHeight(self) -> int: ...
    def Render(self, G: Graphics) -> None: ...


class RcpLabelItem(RcpItem):
    def __init__(self, text: str): ...
    @property
    def Text(self) -> str: ...
    @Text.setter
    def Text(self, AutoPropertyValue: str) -> None: ...
    @property
    def DesiredHeight(self) -> int: ...
    @property
    def OwnerInstanceId(self) -> Guid: ...
    def Render(self, graphics: Graphics) -> None: ...


class RcpSeparatorItem(RcpItem):
    def __init__(self): ...
    @property
    def DesiredHeight(self) -> int: ...
    @property
    def OwnerInstanceId(self) -> Guid: ...
    def Render(self, graphics: Graphics) -> None: ...


class RcpDeadItem(RcpItem):
    def __init__(self, id: Guid): ...
    @property
    def DesiredHeight(self) -> int: ...
    @property
    def OwnerInstanceId(self) -> Guid: ...
    def Render(self, graphics: Graphics) -> None: ...


class IRcpItem:
    @property
    def DesiredHeight(self) -> int: ...
    @property
    def Bounds(self) -> Rectangle: ...
    @Bounds.setter
    def Bounds(self, Value: Rectangle) -> None: ...
    @property
    def OwnerInstanceId(self) -> Guid: ...
    def OnDelete(self) -> None: ...
    def Render(self, graphics: Graphics) -> None: ...
    def MouseDoubleClick(self, e: MouseEventArgs) -> GH_ObjectResponse: ...
    def MouseClick(self, e: MouseEventArgs) -> GH_ObjectResponse: ...
    def MouseDown(self, e: MouseEventArgs) -> GH_ObjectResponse: ...
    def MouseMove(self, e: MouseEventArgs) -> GH_ObjectResponse: ...
    def MouseUp(self, e: MouseEventArgs) -> GH_ObjectResponse: ...


class RcpItem:
    @property
    def Bounds(self) -> Rectangle: ...
    @Bounds.setter
    def Bounds(self, AutoPropertyValue: Rectangle) -> None: ...
    @property
    def DesiredHeight(self) -> int: ...
    @property
    def OwnerInstanceId(self) -> Guid: ...
    def MouseClick(self, e: MouseEventArgs) -> GH_ObjectResponse: ...
    def MouseDoubleClick(self, e: MouseEventArgs) -> GH_ObjectResponse: ...
    def MouseDown(self, e: MouseEventArgs) -> GH_ObjectResponse: ...
    def MouseMove(self, e: MouseEventArgs) -> GH_ObjectResponse: ...
    def MouseUp(self, e: MouseEventArgs) -> GH_ObjectResponse: ...
    def OnDelete(self) -> None: ...
    def Render(self, graphics: Graphics) -> None: ...




class RemoteControlPanel:
    def __init__(self): ...
    @property
    def Document(self) -> GH_Document: ...
    @Document.setter
    def Document(self, Value: GH_Document) -> None: ...


class RcpLayoutControl(GH_DoubleBufferedPanel):
    def __init__(self): ...
    @property
    def ScrollBar(self) -> GH_VerticalScrollBar: ...
    def add_EditModeChanged(self, obj: EditModeChangedEventHandler) -> None: ...
    def remove_EditModeChanged(self, obj: EditModeChangedEventHandler) -> None: ...
    @property
    def EditMode(self) -> bool: ...
    @EditMode.setter
    def EditMode(self, Value: bool) -> None: ...
    @property
    def RcpLayout(self) -> RcpLayout: ...
    @RcpLayout.setter
    def RcpLayout(self, Value: RcpLayout) -> None: ...
    @property
    def BottomMostGroup(self) -> RcpGroup: ...
    def LayoutGroups(self) -> None: ...


class LayoutChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, sender: Object, e: RcpLayoutEventArgs, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self, sender: Object, e: RcpLayoutEventArgs) -> None: ...


class EditModeChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, sender: Object, e: EventArgs, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self, sender: Object, e: EventArgs) -> None: ...
