from typing import Tuple, Set, Iterable, List

class Fonts:
    def __init__(self): ...
    def GetUiFont (style : Style, size : Size) -> Font: ...
    @property
    def NormalFont () -> Font: ...
    @property
    def HeadingFont () -> Font: ...
    @property
    def BoldHeadingFont () -> Font: ...
    @property
    def TitleFont () -> Font: ...
    @property
    def SmallFont () -> Font: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class ShowPanelReason:
    Show = 0
    Hide = 1
    HideOnDeactivate = 2
    ShowOnDeactivate = 3
class CursorStyle:
    Default = 0
    Wait = 1
    CrossHair = 2
    Hand = 3
    Rotate = 4
    Magnify = 5
    ArrowCopy = 6
    CrosshairCopy = 7
class OptionPageButtons:
    None = 0
    DefaultButton = 1
    ApplyButton = 2
class PropertyPageType:
    Material = 0
    Light = 1
    Custom = 2
    ObjectProperties = 3
    Dimension = 4
    Leader = 5
    Text = 6
    Hatch = 7
    Dot = 8
    TextureMapping = 9
    Detail = 10
    ClippingPlane = 11
    NamedView = 12
    Decal = 13
    View = 14
    PageCount = 15
class RhinoPlotWidthType:
    ByLayer = 0
    ByParent = 1
    Hairline = 2
    Default = 3
    None = 4
    Varies = 5
    Width = 6
class RhinoPlotWidthValue:
    Default = 0
    Varies = -20
    ByParent = -15
    ByLayer = -10
    None = -1
class RhinoGetPlotWidthArgs:
    NoArgs = 0
    ByLayer = 1
    ByParent = 2
    HairLine = 4
    Default = 8
    None = 32
    All = 268435455
class RhinoPageInterop:
    def NewPropertiesPanelPagePointer (page : ObjectPropertiesPage, rhinoDocRuntimeSn : UInt32) -> IntPtr: ...
    def StackedDialogPageFromUnmanagedPointer (pointer : IntPtr) -> StackedDialogPage: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class PanelType:
    PerDoc = 0
    System = 1
class IPanelsService:
    def SupportedType (self, type : Type) -> Tuple[bool, str]: ...
    def DestroyNativeWindow (self, host : Object, nativeObject : Object, disposeOfNativeObject : bool) -> None: ...
    def SetF1Hook (self, nativeObject : Object, hook : EventHandler) -> None: ...
class PanelIds:
    @property
    def Materials () -> Guid: ...
    @property
    def Environment () -> Guid: ...
    @property
    def Texture () -> Guid: ...
    @property
    def LightManager () -> Guid: ...
    @property
    def Sun () -> Guid: ...
    @property
    def GroundPlane () -> Guid: ...
    @property
    def Layers () -> Guid: ...
    @property
    def ObjectProperties () -> Guid: ...
    @property
    def Display () -> Guid: ...
    @property
    def ContextHelp () -> Guid: ...
    @property
    def Notes () -> Guid: ...
    @property
    def Rendering () -> Guid: ...
    @property
    def Libraries () -> Guid: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class IPanel:
    def PanelShown (self, documentSerialNumber : UInt32, reason : ShowPanelReason) -> None: ...
    def PanelHidden (self, documentSerialNumber : UInt32, reason : ShowPanelReason) -> None: ...
    def PanelClosing (self, documentSerialNumber : UInt32, onCloseDocument : bool) -> None: ...
class Panels:
    def IsShowing (reason : ShowPanelReason) -> bool: ...
    def IsHiding (reason : ShowPanelReason) -> bool: ...
    def RegisterPanel (plugIn : PlugIn, type : Type, caption : str, icon : Icon, panelType : PanelType) -> None: ...
    def RegisterPanel (plugin : PlugIn, panelType : Type, caption : str, icon : Icon) -> None: ...
    @property
    def IconSize () -> Size: ...
    @property
    def ScaledIconSize () -> Size: ...
    def ChangePanelIcon (panelType : Type, icon : Icon) -> None: ...
    def GetPanel (panelId : Guid) -> Object: ...
    def GetPanel () -> T: ...
    def GetPanel (panelId : Guid, documentSerialNumber : UInt32) -> Object: ...
    def GetPanel (documentSerialNumber : UInt32) -> T: ...
    def GetPanel (panelId : Guid, rhinoDoc : RhinoDoc) -> Object: ...
    def GetPanel (rhinoDoc : RhinoDoc) -> T: ...
    def GetPanels (panelId : Guid, doc : RhinoDoc) -> Set(Object): ...
    def GetPanels (panelId : Guid, documentRuntimeSerialNumber : UInt32) -> Set(Object): ...
    def GetPanels (documentRuntimeSerialNumber : UInt32) -> Set(T): ...
    def GetPanels (doc : RhinoDoc) -> Set(T): ...
    def IsPanelVisible (panelId : Guid, isSelectedTab : bool) -> bool: ...
    def IsPanelVisible (panelType : Type, isSelectedTab : bool) -> bool: ...
    def IsPanelVisible (panelId : Guid) -> bool: ...
    def IsPanelVisible (panelType : Type) -> bool: ...
    def OpenPanelAsSibling (panelId : Guid, siblingPanelId : Guid) -> bool: ...
    def OpenPanelAsSibling (panelId : Guid, siblingPanelId : Guid, makeSelectedPanel : bool) -> bool: ...
    def OpenPanel (panelId : Guid) -> None: ...
    def OpenPanel (panelId : Guid, makeSelectedPanel : bool) -> None: ...
    def OpenPanel (panelType : Type) -> None: ...
    def OpenPanel (panelType : Type, makeSelectedPanel : bool) -> None: ...
    def OpenPanel (dockBarId : Guid, panelId : Guid) -> Guid: ...
    def OpenPanel (dockBarId : Guid, panelId : Guid, makeSelectedPanel : bool) -> Guid: ...
    def OpenPanel (dockBarId : Guid, panelType : Type) -> Guid: ...
    def OpenPanel (dockBarId : Guid, panelType : Type, makeSelectedPanel : bool) -> Guid: ...
    def FloatPanel (panelType : Type, mode : FloatPanelMode) -> bool: ...
    def FloatPanel (panelTypeId : Guid, mode : FloatPanelMode) -> bool: ...
    def PanelDockBars (panelId : Guid) -> Set(Guid): ...
    def PanelDockBar (panelId : Guid) -> Guid: ...
    def PanelDockBar (panelType : Type) -> Guid: ...
    def ClosePanel (panelId : Guid) -> None: ...
    def ClosePanel (panelType : Type) -> None: ...
    def GetOpenPanelIds () -> Set(Guid): ...
    def OnShowPanel (panelId : Guid, documentSerialNumber : UInt32, show : bool) -> None: ...
    def add_Show (value : EventHandler) -> None: ...
    def remove_Show (value : EventHandler) -> None: ...
    def OnClosePanel (panelId : Guid, documentSerialNumber : UInt32) -> None: ...
    def add_Closed (value : EventHandler) -> None: ...
    def remove_Closed (value : EventHandler) -> None: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class PanelEventArgs:
    def __init__(self, panelId : Guid, documentSerialNumber : UInt32): ...
    @property
    def PanelId (self) -> Guid: ...
    @property
    def DocumentSerialNumber (self) -> UInt32: ...
    @property
    def Document (self) -> RhinoDoc: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class ShowPanelEventArgs:
    def __init__(self, panelId : Guid, documentSerialNumber : UInt32, show : bool): ...
    @property
    def Show (self) -> bool: ...
    @property
    def PanelId (self) -> Guid: ...
    @property
    def DocumentSerialNumber (self) -> UInt32: ...
    @property
    def Document (self) -> RhinoDoc: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class MouseButton:
    None = 0
    Left = 1
    Right = 2
    Middle = 4
class ModifierKey:
    None = 0
    Control = 1
    Shift = 2
class MouseCallbackEventArgs:
    @property
    def View (self) -> RhinoView: ...
    @property
    def MouseButton (self) -> MouseButton: ...
    @property
    def Button (self) -> MouseButtons: ...
    @property
    def ShiftKeyDown (self) -> bool: ...
    @property
    def CtrlKeyDown (self) -> bool: ...
    @property
    def ViewportPoint (self) -> Point: ...
    @property
    def Cancel (self) -> bool: ...
    @Cancel.setter
    def Cancel (self, value : bool) -> None: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class MouseCallback:
    @property
    def Enabled (self) -> bool: ...
    @Enabled.setter
    def Enabled (self, value : bool) -> None: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class ObjectPropertiesPageEventArgs:
    def __init__(self, page : ObjectPropertiesPage): ...
    @property
    def Page (self) -> ObjectPropertiesPage: ...
    @property
    def Objects (self) -> Set(RhinoObject): ...
    def IncludesObjectsType (self) -> bool: ...
    def IncludesObjectsType (self, allMustMatch : bool) -> bool: ...
    def IncludesObjectsType (self, objectTypes : ObjectType) -> bool: ...
    def IncludesObjectsType (self, objectTypes : ObjectType, allMustMatch : bool) -> bool: ...
    def GetObjects (self) -> Set(T): ...
    def GetObjects (self, filter : ObjectType) -> Set(RhinoObject): ...
    @property
    def ObjectCount (self) -> int: ...
    @property
    def ObjectTypes (self) -> UInt32: ...
    @property
    def View (self) -> RhinoView: ...
    @property
    def Viewport (self) -> RhinoViewport: ...
    @property
    def DocRuntimeSerialNumber (self) -> UInt32: ...
    @property
    def Document (self) -> RhinoDoc: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class ObjectPropertiesPage:
    def PageIcon (self, sizeInPixels : Size) -> Icon: ...
    @property
    def Icon (self) -> Icon: ...
    @property
    def PageControl (self) -> Object: ...
    @property
    def EnglishPageTitle (self) -> str: ...
    @property
    def SupportedTypes (self) -> ObjectType: ...
    @property
    def AllObjectsMustBeSupported (self) -> bool: ...
    def OnCreateParent (self, hwndParent : IntPtr) -> None: ...
    def OnSizeParent (self, width : int, height : int) -> None: ...
    def OnActivate (self, active : bool) -> bool: ...
    def OnHelp (self) -> None: ...
    def ShouldDisplay (self, rhObj : RhinoObject) -> bool: ...
    def ShouldDisplay (self, e : ObjectPropertiesPageEventArgs) -> bool: ...
    def InitializeControls (self, rhObj : RhinoObject) -> None: ...
    def UpdatePage (self, e : ObjectPropertiesPageEventArgs) -> None: ...
    def ModifyPage (self, callbackAction : Action) -> None: ...
    @property
    def SupportsSubObjects (self) -> bool: ...
    @property
    def LocalPageTitle (self) -> str: ...
    @property
    def PageType (self) -> PropertyPageType: ...
    @property
    def PageIconEmbeddedResourceString (self) -> str: ...
    def RunScript (self, doc : RhinoDoc, objectList : Set(RhinoObject)) -> Result: ...
    def RunScript (self, e : ObjectPropertiesPageEventArgs) -> Result: ...
    @property
    def SelectedObjects (self) -> Set(RhinoObject): ...
    def AnySelectedObject (self) -> bool: ...
    def AnySelectedObject (self, allMustMatch : bool) -> bool: ...
    def GetSelectedObjects (self) -> Set(T): ...
    def GetSelectedObjects (self, filter : ObjectType) -> Set(RhinoObject): ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class OptionsDialogPage:
    def RunScript (self, doc : RhinoDoc, mode : RunMode) -> Result: ...
    @property
    def Children (self) -> List: ...
    @property
    def HasChildren (self) -> bool: ...
    def AddChildPage (self, pageToAdd : StackedDialogPage) -> None: ...
    @property
    def Modified (self) -> bool: ...
    @Modified.setter
    def Modified (self, value : bool) -> None: ...
    @property
    def Handle (self) -> IntPtr: ...
    def RemovePage (self) -> None: ...
    def MakeActivePage (self) -> None: ...
    @property
    def PageControl (self) -> Object: ...
    def OnCreateParent (self, hwndParent : IntPtr) -> None: ...
    def OnSizeParent (self, width : int, height : int) -> None: ...
    def SetEnglishPageTitle (self, newPageTile : str) -> None: ...
    @property
    def EnglishPageTitle (self) -> str: ...
    @property
    def LocalPageTitle (self) -> str: ...
    @property
    def PageImage (self) -> Image: ...
    def OnApply (self) -> bool: ...
    def OnCancel (self) -> None: ...
    def OnActivate (self, active : bool) -> bool: ...
    @property
    def ShowDefaultsButton (self) -> bool: ...
    @property
    def ShowApplyButton (self) -> bool: ...
    def OnDefaults (self) -> None: ...
    def OnHelp (self) -> None: ...
    @property
    def NavigationTextIsBold (self) -> bool: ...
    @NavigationTextIsBold.setter
    def NavigationTextIsBold (self, value : bool) -> None: ...
    @property
    def NavigationTextColor (self) -> Color: ...
    @NavigationTextColor.setter
    def NavigationTextColor (self, value : Color) -> None: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class MouseCursor:
    def SetToolTip (tooltip : str) -> None: ...
    @property
    def Location () -> Point2d: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class StatusBar:
    def SetDistancePane (distance : float) -> None: ...
    def SetNumberPane (number : float) -> None: ...
    def SetPointPane (point : Point3d) -> None: ...
    def SetMessagePane (message : str) -> None: ...
    def ClearMessagePane () -> None: ...
    def ShowProgressMeter (lowerLimit : int, upperLimit : int, label : str, embedLabel : bool, showPercentComplete : bool) -> int: ...
    def ShowProgressMeter (docSerialNumber : UInt32, lowerLimit : int, upperLimit : int, label : str, embedLabel : bool, showPercentComplete : bool) -> int: ...
    def UpdateProgressMeter (position : int, absolute : bool) -> int: ...
    def UpdateProgressMeter (docSerialNumber : UInt32, position : int, absolute : bool) -> int: ...
    def HideProgressMeter () -> None: ...
    def HideProgressMeter (docSerialNumber : UInt32) -> None: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class OpenFileDialog:
    def __init__(self): ...
    @property
    def DefaultExt (self) -> str: ...
    @DefaultExt.setter
    def DefaultExt (self, value : str) -> None: ...
    @property
    def FileName (self) -> str: ...
    @FileName.setter
    def FileName (self, value : str) -> None: ...
    @property
    def Title (self) -> str: ...
    @Title.setter
    def Title (self, value : str) -> None: ...
    @property
    def Filter (self) -> str: ...
    @Filter.setter
    def Filter (self, value : str) -> None: ...
    @property
    def InitialDirectory (self) -> str: ...
    @InitialDirectory.setter
    def InitialDirectory (self, value : str) -> None: ...
    @property
    def MultiSelect (self) -> bool: ...
    @MultiSelect.setter
    def MultiSelect (self, value : bool) -> None: ...
    @property
    def FileNames (self) -> Set(str): ...
    def ShowOpenDialog (self) -> bool: ...
    def ShowDialog (self) -> DialogResult: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class SaveFileDialog:
    def __init__(self): ...
    @property
    def DefaultExt (self) -> str: ...
    @DefaultExt.setter
    def DefaultExt (self, value : str) -> None: ...
    @property
    def FileName (self) -> str: ...
    @FileName.setter
    def FileName (self, value : str) -> None: ...
    @property
    def Title (self) -> str: ...
    @Title.setter
    def Title (self, value : str) -> None: ...
    @property
    def Filter (self) -> str: ...
    @Filter.setter
    def Filter (self, value : str) -> None: ...
    @property
    def InitialDirectory (self) -> str: ...
    @InitialDirectory.setter
    def InitialDirectory (self, value : str) -> None: ...
    def ShowDialog (self) -> DialogResult: ...
    def ShowSaveDialog (self) -> bool: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class IStackedDialogPageService:
    def GetImageHandle (self, image : Image, canBeNull : bool) -> IntPtr: ...
    def GetImageHandle (self, icon : Icon, canBeNull : bool) -> IntPtr: ...
    def GetNativePageWindow (self, nativeWindowObject : Object) -> Tuple[IntPtr, Object]: ...
    def GetNativePageWindow (self, pageObject : Object) -> Tuple[IntPtr, Object, Object]: ...
    def RedrawPageControl (self, pageControl : Object) -> None: ...
    def TryGetControlMinimumSize (self, controlObject : Object) -> Tuple[bool, SizeF]: ...
class StackedDialogPage:
    @property
    def Children (self) -> List: ...
    @property
    def HasChildren (self) -> bool: ...
    def AddChildPage (self, pageToAdd : StackedDialogPage) -> None: ...
    @property
    def Modified (self) -> bool: ...
    @Modified.setter
    def Modified (self, value : bool) -> None: ...
    @property
    def Handle (self) -> IntPtr: ...
    def RemovePage (self) -> None: ...
    def MakeActivePage (self) -> None: ...
    @property
    def PageControl (self) -> Object: ...
    def OnCreateParent (self, hwndParent : IntPtr) -> None: ...
    def OnSizeParent (self, width : int, height : int) -> None: ...
    def SetEnglishPageTitle (self, newPageTile : str) -> None: ...
    @property
    def EnglishPageTitle (self) -> str: ...
    @property
    def LocalPageTitle (self) -> str: ...
    @property
    def PageImage (self) -> Image: ...
    def OnApply (self) -> bool: ...
    def OnCancel (self) -> None: ...
    def OnActivate (self, active : bool) -> bool: ...
    @property
    def ShowDefaultsButton (self) -> bool: ...
    @property
    def ShowApplyButton (self) -> bool: ...
    def OnDefaults (self) -> None: ...
    def OnHelp (self) -> None: ...
    @property
    def NavigationTextIsBold (self) -> bool: ...
    @NavigationTextIsBold.setter
    def NavigationTextIsBold (self, value : bool) -> None: ...
    @property
    def NavigationTextColor (self) -> Color: ...
    @NavigationTextColor.setter
    def NavigationTextColor (self, value : Color) -> None: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class ToolbarFile:
    @property
    def Id (self) -> Guid: ...
    @property
    def Path (self) -> str: ...
    @property
    def Name (self) -> str: ...
    def Close (self, prompt : bool) -> bool: ...
    def Save (self) -> bool: ...
    def SaveAs (self, path : str) -> bool: ...
    @property
    def GroupCount (self) -> int: ...
    @property
    def ToolbarCount (self) -> int: ...
    def GetToolbar (self, index : int) -> Toolbar: ...
    def GetGroup (self, index : int) -> ToolbarGroup: ...
    def GetGroup (self, name : str) -> ToolbarGroup: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class Toolbar:
    @property
    def Id (self) -> Guid: ...
    @property
    def Name (self) -> str: ...
    @property
    def BitmapSize () -> Size: ...
    @BitmapSize.setter
    def BitmapSize (value : Size) -> None: ...
    @property
    def TabSize () -> Size: ...
    @TabSize.setter
    def TabSize (value : Size) -> None: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class ToolbarGroup:
    @property
    def Id (self) -> Guid: ...
    @property
    def Name (self) -> str: ...
    @property
    def Visible (self) -> bool: ...
    @Visible.setter
    def Visible (self, value : bool) -> None: ...
    @property
    def IsDocked (self) -> bool: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class ToolbarFileCollection:
    @property
    def Count (self) -> int: ...
    @property
    def Item (self, index : int) -> ToolbarFile: ...
    def FindByName (self, name : str, ignoreCase : bool) -> ToolbarFile: ...
    def FindByPath (self, path : str) -> ToolbarFile: ...
    def Open (self, path : str) -> ToolbarFile: ...
    def GetEnumerator (self) -> IEnumerator: ...
    @property
    def SidebarIsVisible () -> bool: ...
    @SidebarIsVisible.setter
    def SidebarIsVisible (value : bool) -> None: ...
    @property
    def MruSidebarIsVisible () -> bool: ...
    @MruSidebarIsVisible.setter
    def MruSidebarIsVisible (value : bool) -> None: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class RuiUpdateUi:
    @Enabled.setter
    def Enabled (self, value : bool) -> None: ...
    @property
    def Enabled (self) -> bool: ...
    @Checked.setter
    def Checked (self, value : bool) -> None: ...
    @property
    def Checked (self) -> bool: ...
    @RadioChecked.setter
    def RadioChecked (self, value : bool) -> None: ...
    @property
    def RadioChecked (self) -> bool: ...
    @Text.setter
    def Text (self, value : str) -> None: ...
    @property
    def Text (self) -> str: ...
    @property
    def FileId (self) -> Guid: ...
    @property
    def MenuId (self) -> Guid: ...
    @property
    def MenuItemId (self) -> Guid: ...
    @property
    def MenuHandle (self) -> IntPtr: ...
    @property
    def MenuIndex (self) -> int: ...
    @property
    def WindowsMenuItemId (self) -> UInt32: ...
    def RegisterMenuItem (file : Guid, menu : Guid, item : Guid, callBack : UpdateMenuItemEventHandler) -> bool: ...
    def RegisterMenuItem (fileId : str, menuId : str, itemId : str, callBack : UpdateMenuItemEventHandler) -> bool: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class DrawingUtilities:
    def IconFromResource (resourceName : str, assembly : Assembly) -> Icon: ...
    def IconFromResource (resourceName : str, size : Size, assembly : Assembly) -> Icon: ...
    def BitmapFromIconResource (resourceName : str, assembly : Assembly) -> Bitmap: ...
    def BitmapFromIconResource (resourceName : str, bitmapSize : Size, assembly : Assembly) -> Bitmap: ...
    def ImageFromResource (resourceName : str, assembly : Assembly) -> Image: ...
    def LoadBitmapWithScaleDown (iconName : str, sizeDesired : int, assembly : Assembly) -> Bitmap: ...
    def LoadIconWithScaleDown (iconName : str, sizeDesired : int, assembly : Assembly) -> Icon: ...
    def CreateMeshPreviewImage (mesh : Mesh, color : Color, size : Size) -> Bitmap: ...
    def CreateMeshPreviewImage (meshes : Iterable[Mesh], colors : Iterable[Color], size : Size) -> Bitmap: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class IHelp:
    @property
    def HelpUrl (self) -> str: ...
class RhinoHelp:
    def Show (helpLink : str) -> bool: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class LOC:
    def STR (english : str) -> str: ...
    def STR (english : str, assemblyOrObject : Object) -> str: ...
    def COMMANDNAME (english : str) -> str: ...
    def CON (english : str) -> LocalizeStringPair: ...
    def CON (english : str, assemblyFromObject : Object) -> LocalizeStringPair: ...
    def COV (english : str) -> LocalizeStringPair: ...
    def COV (english : str, assemblyFromObject : Object) -> LocalizeStringPair: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class DistanceDisplayMode:
    Decimal = 0
    Fractional = 1
    FeetInches = 2
class ILocalizationService:
    def LocalizeCommandName (self, assembly : Assembly, languageId : int, english : str) -> str: ...
    def LocalizeDialogItem (self, assembly : Assembly, languageId : int, key : str, english : str) -> str: ...
    def LocalizeForm (self, assembly : Assembly, languageId : int, formOrUserControl : Object) -> None: ...
    def LocalizeString (self, assembly : Assembly, languageId : int, english : str, contextId : int) -> str: ...
class Localization:
    def UnitSystemName (units : UnitSystem, capitalize : bool, singular : bool, abbreviate : bool) -> str: ...
    def FormatNumber (x : float, units : UnitSystem, mode : DistanceDisplayMode, precision : int, appendUnitSystemName : bool) -> str: ...
    def FormatDistanceAndTolerance (distance : float, units : UnitSystem, dimStyle : DimensionStyle, alternate : bool) -> str: ...
    def LocalizeString (english : str, contextId : int) -> str: ...
    def LocalizeString (english : str, assemblyOrObject : Object, contextId : int) -> str: ...
    def LocalizeDialogItem (assemblyOrObject : Object, key : str, english : str) -> str: ...
    def LocalizeForm (formOrUserControl : Object) -> None: ...
    def LocalizeCommandName (english : str) -> str: ...
    def LocalizeCommandName (english : str, assemblyOrObject : Object) -> str: ...
    def LocalizeCommandOptionName (english : str, contextId : int) -> LocalizeStringPair: ...
    def LocalizeCommandOptionName (english : str, assemblyOrObject : Object, contextId : int) -> LocalizeStringPair: ...
    def LocalizeCommandOptionValue (english : str, contextId : int) -> LocalizeStringPair: ...
    def LocalizeCommandOptionValue (english : str, assemblyOrObject : Object, contextId : int) -> LocalizeStringPair: ...
    @property
    def CurrentLanguageId () -> int: ...
    @property
    def RunningAsEnglish () -> bool: ...
    def SetLanguageId (id : int) -> bool: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class LocalizeStringPair:
    def __init__(self, english : str, local : str): ...
    @property
    def English (self) -> str: ...
    @property
    def Local (self) -> str: ...
    def ToString (self) -> str: ...
    def op_Implicit (lcp : LocalizeStringPair) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class IDialogService:
    def ShowMultiListBox (self, title : str, message : str, items : List[str], defaults : List[str]) -> Set(str): ...
    def WrapAsIWin32Window (self, handle : IntPtr) -> Object: ...
    def ObjectToWindowHandle (self, window : Object, useMainRhinoWindowWhenNull : bool) -> IntPtr: ...
class GetColorEventArgs:
    @property
    def InputColor (self) -> Color: ...
    @property
    def SelectedColor (self) -> Color: ...
    @SelectedColor.setter
    def SelectedColor (self, value : Color) -> None: ...
    @property
    def IncludeButtonColors (self) -> bool: ...
    @property
    def Title (self) -> str: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class WaitCursor:
    def __init__(self): ...
    def Set (self) -> None: ...
    def Clear (self) -> None: ...
    def Dispose (self) -> None: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class ShowMessageResult:
    None = 0
    OK = 1
    Cancel = 2
    Abort = 3
    Retry = 4
    Ignore = 5
    Yes = 6
    No = 7
class ShowMessageButton:
    OK = 0
    OKCancel = 1
    AbortRetryIgnore = 2
    YesNoCancel = 3
    YesNo = 4
    RetryCancel = 5
class ShowMessageIcon:
    None = 0
    Error = 16
    Hand = 16
    Stop = 16
    Question = 32
    Exclamation = 48
    Warning = 48
    Information = 64
    Asterisk = 64
class ShowMessageDefaultButton:
    Button1 = 0
    Button2 = 256
    Button3 = 512
class ShowMessageOptions:
    None = 0
    SetForeground = 65536
    DefaultDesktopOnly = 131072
    TopMost = 262144
    RightAlign = 524288
    RtlReading = 1048576
    ServiceNotification = 2097152
class ShowMessageMode:
    ApplicationModal = 0
    SystemModal = 4096
    TaskModal = 8192
class Dialogs:
    def ShowAboutDialog (forceSimpleDialog : bool) -> None: ...
    def ShowContextMenu (items : Iterable[str], screenPoint : Point, modes : Iterable[int]) -> int: ...
    def SetCustomColorDialog (handler : EventHandler) -> None: ...
    def KillSplash () -> None: ...
    def ShowSemiModal (form : Form) -> DialogResult: ...
    def ShowTextDialog (message : str, title : str) -> None: ...
    def ShowMessageBox (message : str, title : str) -> DialogResult: ...
    def ShowMessageBox (message : str, title : str, buttons : MessageBoxButtons, icon : MessageBoxIcon) -> DialogResult: ...
    def ShowMessage (message : str, title : str) -> ShowMessageResult: ...
    def ShowMessage (message : str, title : str, buttons : ShowMessageButton, icon : ShowMessageIcon) -> ShowMessageResult: ...
    def ShowMessage (parent : Object, message : str, title : str, buttons : ShowMessageButton, icon : ShowMessageIcon, defaultButton : ShowMessageDefaultButton, options : ShowMessageOptions, mode : ShowMessageMode) -> ShowMessageResult: ...
    def ShowColorDialog (color : Color) -> Tuple[bool, Color]: ...
    def ShowColorDialog (color : Color, includeButtonColors : bool, dialogTitle : str) -> Tuple[bool, Color]: ...
    def ShowColorDialog (parent : IWin32Window, color : Color4f, allowAlpha : bool) -> Tuple[bool, Color4f]: ...
    def ShowColorDialog (parent : Object, color : Color4f, allowAlpha : bool) -> Tuple[bool, Color4f]: ...
    def ShowColorDialog (parent : Object, color : Color4f, allowAlpha : bool, colorCallback : OnColorChangedEvent) -> Tuple[bool, Color4f]: ...
    def ShowColorDialog (color : Color4f, allowAlpha : bool) -> Tuple[bool, Color4f]: ...
    def ShowSunDialog (sun : Sun) -> bool: ...
    def ShowSelectLayerDialog (layerIndex : int, dialogTitle : str, showNewLayerButton : bool, showSetCurrentButton : bool, initialSetCurrentState : bool) -> Tuple[bool, int, bool]: ...
    def ShowSelectMultipleLayersDialog (defaultLayerIndices : Iterable[int], dialogTitle : str, showNewLayerButton : bool) -> Tuple[bool, Set(int)]: ...
    def ShowSelectLinetypeDialog (linetypeIndex : int, displayByLayer : bool) -> Tuple[bool, int]: ...
    def ShowComboListBox (title : str, message : str, items : IList) -> Object: ...
    def ShowListBox (title : str, message : str, items : IList) -> Object: ...
    def ShowListBox (title : str, message : str, items : IList, selectedItem : Object) -> Object: ...
    def ShowLineTypes (title : str, message : str, doc : RhinoDoc) -> Object: ...
    def ShowCheckListBox (title : str, message : str, items : IList, checkState : List[bool]) -> Set(bool): ...
    def ShowEditBox (title : str, message : str, defaultText : str, multiline : bool) -> Tuple[bool, str]: ...
    def ShowNumberBox (title : str, message : str, number : float) -> Tuple[bool, float]: ...
    def ShowNumberBox (title : str, message : str, number : float, minimum : float, maximum : float) -> Tuple[bool, float]: ...
    def ShowPropertyListBox (title : str, message : str, items : IList, values : List[str]) -> Set(str): ...
    def ShowMultiListBox (title : str, message : str, items : List[str], defaults : List[str]) -> Set(str): ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class IRhinoUiDialogService:
    def ShowComboListBox (self, title : str, message : str, items : IList) -> Object: ...
    def ShowListBox (self, title : str, message : str, items : IList, selectedItem : Object) -> Object: ...
    def ShowCheckListBox (self, title : str, message : str, items : IList, checkState : List[bool]) -> Set(bool): ...
    def ShowEditBox (self, title : str, message : str, defaultText : str, multiline : bool) -> Tuple[bool, str]: ...
    def ShowNumberBox (self, title : str, message : str, number : float, minimum : float, maximum : float) -> Tuple[bool, float]: ...
    def ShowPopupMenu (self, arrItems : Set(str), arrModes : Set(int), screenPointX : Nullable, screenPointY : Nullable) -> int: ...
    def ShowLineTypes (self, title : str, message : str, doc : RhinoDoc) -> Object: ...
    def ShowMultiListBox (self, items : List[str], message : str, title : str, defaults : List[str]) -> Set(str): ...
class Size:
    Small = 0
    Normal = 1
    Large = 2
    Title = 3
class Style:
    Regular = 0
    Bold = 1
    Italic = 2
    Underline = 4
    Strikeout = 8
class FloatPanelMode:
    Show = 0
    Hide = 1
    Toggle = 2
class UpdateMenuItemEventHandler:
    def __init__(self, object : Object, method : IntPtr): ...
    def Invoke (self, sender : Object, cmdui : RuiUpdateUi) -> None: ...
    def BeginInvoke (self, sender : Object, cmdui : RuiUpdateUi, callback : AsyncCallback, object : Object) -> IAsyncResult: ...
    def EndInvoke (self, result : IAsyncResult) -> None: ...
    def GetObjectData (self, info : SerializationInfo, context : StreamingContext) -> None: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetInvocationList (self) -> Set(Delegate): ...
    def GetHashCode (self) -> int: ...
    def DynamicInvoke (self, args : Set(Object)) -> Object: ...
    @property
    def Method (self) -> MethodInfo: ...
    @property
    def Target (self) -> Object: ...
    def Clone (self) -> Object: ...
    def ToString (self) -> str: ...
    def GetType (self) -> Type: ...
class OnColorChangedEvent:
    def __init__(self, object : Object, method : IntPtr): ...
    def Invoke (self, color : Color4f) -> None: ...
    def BeginInvoke (self, color : Color4f, callback : AsyncCallback, object : Object) -> IAsyncResult: ...
    def EndInvoke (self, result : IAsyncResult) -> None: ...
    def GetObjectData (self, info : SerializationInfo, context : StreamingContext) -> None: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetInvocationList (self) -> Set(Delegate): ...
    def GetHashCode (self) -> int: ...
    def DynamicInvoke (self, args : Set(Object)) -> Object: ...
    @property
    def Method (self) -> MethodInfo: ...
    @property
    def Target (self) -> Object: ...
    def Clone (self) -> Object: ...
    def ToString (self) -> str: ...
    def GetType (self) -> Type: ...