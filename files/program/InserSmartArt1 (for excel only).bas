Attribute VB_Name = "InserSmartArt1"
Sub Macro1()
'Taken from: https://www.excel-downloads.com/threads/creation-smartart-vba.20023716/
Dim oSALayout As SmartArtLayout
Set oSALayout = Application.SmartArtLayouts(44)
Dim oShp  As Shape
Set oShp = ActiveWorkbook.ActiveSheet.Shapes.AddSmartArt(oSALayout)

Dim QNodes As SmartArtNodes
Dim QNode As SmartArtNode
Set QNodes = oShp.SmartArt.AllNodes

For i = 1 To QNodes.Count  'supprime toutes les nodes de base
    oShp.SmartArt.AllNodes(1).Delete
Next

  ' Créer 5 Fléches comme dans l'exemple
    For i = 1 To 5
        Set QNode = oShp.SmartArt.AllNodes.Add 'ajoute une node
        Dim cpt As Integer
        cpt = cpt + 1
        QNode.TextFrame2.TextRange.text = "Texte " & cpt 'ecris le texte
        Call Créer_Fils(QNode, cpt)
    Next i
End Sub

Sub Créer_Fils(Parent As SmartArtNode, cpt As Integer)
Dim FNode1 As SmartArtNode
Dim FNode2 As SmartArtNode
'va créer deux fils à mon parent
Set FNode1 = Parent.AddNode(msoSmartArtNodeBelow)
FNode1.TextFrame2.TextRange.text = "Eric " & cpt
End Sub
