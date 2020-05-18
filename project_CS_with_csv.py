import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import *
from PyQt5.Qt import QStandardItemModel, QStandardItem
import csv
import mexicoSoup
import canadaSoup
import usaSoup
import newsSoup

mexicoCovData = []
canadaCovData = []
usaCovData = []

class StandardItem(QStandardItem):
    def __init__(self, text='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        font = QFont('Courier New', font_size)
        font.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(font)
        self.setText(text)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('PROJECT CODE SCRAPPERS')
        self.setGeometry(100,100, 2020, 1300)

        hbox = QHBoxLayout()

        # Create Canada Tree View
        treeView = QTreeView(self)
        treeView.setHeaderHidden(True)
        treeView.setFixedWidth(380)
        treeView.setFixedHeight(850)
        treeView.move(10, 5)
        treeView.setStyleSheet('QTreeView {\
                          background-color:#FFFAFA;\
                          border-style: solid;\
                          border-width: 2px;\
                          border-radius: 10px;\
                          border-color: #A0A0A0;\
                          padding: 6px;}')

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()
      
        # Canada Data
        canada = StandardItem('Canada', 14, set_bold=True, color=QColor(255, 0, 0))

        nl = StandardItem(canadaCovData[2][0], set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(nl)
        case = StandardItem("cases: " + canadaCovData[2][1])
        death = StandardItem("deaths: " + canadaCovData[2][2])
        nl.appendRow(case)
        nl.appendRow(death)

        pe = StandardItem(canadaCovData[3][0], set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(pe)
        case = StandardItem("cases: " + canadaCovData[3][1])
        death = StandardItem("deaths: " + canadaCovData[3][2])
        pe.appendRow(case)
        pe.appendRow(death)

        ns = StandardItem(canadaCovData[4][0],set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(ns)
        case = StandardItem("cases: " + canadaCovData[4][1])
        death = StandardItem("deaths: " + canadaCovData[4][2])
        ns.appendRow(case)
        ns.appendRow(death)

        nb = StandardItem(canadaCovData[5][0], set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(nb)
        case = StandardItem("cases: " + canadaCovData[5][1])
        death = StandardItem("deaths: " + canadaCovData[5][2])
        nb.appendRow(case)
        nb.appendRow(death)

        quebec = StandardItem(canadaCovData[6][0], set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(quebec)
        case = StandardItem("cases: " + canadaCovData[6][1])
        death = StandardItem("deaths: " + canadaCovData[6][2])
        quebec.appendRow(case)
        quebec.appendRow(death)

        ontario = StandardItem(canadaCovData[7][0], set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(ontario)
        case = StandardItem("cases: " + canadaCovData[7][1])
        death = StandardItem("deaths: " + canadaCovData[7][2])
        ontario.appendRow(case)
        ontario.appendRow(death)

        manitoba = StandardItem(canadaCovData[8][0], set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(manitoba)
        case = StandardItem("cases: " + canadaCovData[8][1])
        death = StandardItem("deaths: " + canadaCovData[8][2])
        manitoba.appendRow(case)
        manitoba.appendRow(death)

        saskatchewan = StandardItem(canadaCovData[9][0], set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(saskatchewan)
        case = StandardItem("cases: " + canadaCovData[9][1])
        death = StandardItem("deaths: " + canadaCovData[9][2])
        saskatchewan.appendRow(case)
        saskatchewan.appendRow(death)

        alberta = StandardItem(canadaCovData[10][0], set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(alberta)
        case = StandardItem("cases: " + canadaCovData[10][1])
        death = StandardItem("deaths: " + canadaCovData[10][2])
        alberta.appendRow(case)
        alberta.appendRow(death)

        bc = StandardItem(canadaCovData[11][0], set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(bc)
        case = StandardItem("cases: " + canadaCovData[11][1])
        death = StandardItem("deaths: " + canadaCovData[11][2])
        bc.appendRow(case)
        bc.appendRow(death)

        yukon = StandardItem(canadaCovData[12][0], set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(yukon)
        case = StandardItem("cases: " + canadaCovData[12][1])
        death = StandardItem("deaths: " + canadaCovData[12][2])
        yukon.appendRow(case)
        yukon.appendRow(death)

        nt = StandardItem(canadaCovData[13][0], set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(nt)
        case = StandardItem("cases: " + canadaCovData[13][1])
        death = StandardItem("deaths: " + canadaCovData[13][2])
        nt.appendRow(case)
        nt.appendRow(death)

        nunavut = StandardItem(canadaCovData[14][0], set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(nunavut)
        case = StandardItem("cases: " + canadaCovData[14][1])
        death = StandardItem("deaths: " + canadaCovData[14][2])
        nunavut.appendRow(case)
        nunavut.appendRow(death)

        # Add canada data to rootnode and set the tree model for tree view
        rootNode.appendRow(canada)
        treeView.setModel(treeModel)

        # Create USA Tree View
        treeViewUS = QTreeView(self)
        treeViewUS.setHeaderHidden(True)
        treeViewUS.setFixedWidth(380)
        treeViewUS.setFixedHeight(850)
        treeViewUS.move(380, 5)
        treeViewUS.setStyleSheet('QTreeView {\
                          margin: left;\
                          background-color:#F0F8FF;\
                          border-style: solid;\
                          border-width: 2px;\
                          border-radius: 10px;\
                          border-color: #A0A0A0;\
                          padding: 6px;\
                          }')

        treeModelUS = QStandardItemModel()
        rootNodeUS = treeModelUS.invisibleRootItem()

        # USA Data
        usa = StandardItem('USA', 14, set_bold=True, color=QColor(0, 0, 204))

        al = StandardItem(usaCovData[1][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(al)
        case = StandardItem("cases: " + usaCovData[1][1])
        death = StandardItem("deaths: " + usaCovData[1][2])
        al.appendRow(case)
        al.appendRow(death)

        ak = StandardItem(usaCovData[2][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ak)
        case = StandardItem("cases: " + usaCovData[2][1])
        death = StandardItem("deaths: " + usaCovData[2][2])
        ak.appendRow(case)
        ak.appendRow(death)

        am = StandardItem(usaCovData[3][0],set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(am)
        case = StandardItem("cases: " + usaCovData[3][1])
        death = StandardItem("deaths: " + usaCovData[3][2])
        am.appendRow(case)
        am.appendRow(death)

        az = StandardItem(usaCovData[4][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(az)
        case = StandardItem("cases: " + usaCovData[4][1])
        death = StandardItem("deaths: " + usaCovData[4][2])
        az.appendRow(case)
        az.appendRow(death)

        ar = StandardItem(usaCovData[5][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ar)
        case = StandardItem("cases: " + usaCovData[5][1])
        death = StandardItem("deaths: " + usaCovData[5][2])
        ar.appendRow(case)
        ar.appendRow(death)

        ca = StandardItem(usaCovData[6][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ca)
        case = StandardItem("cases: " + usaCovData[6][1])
        death = StandardItem("deaths: " + usaCovData[6][2])
        ca.appendRow(case)
        ca.appendRow(death)

        co = StandardItem(usaCovData[7][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(co)
        case = StandardItem("cases: " + usaCovData[7][1])
        death = StandardItem("deaths: " + usaCovData[7][2])
        co.appendRow(case)
        co.appendRow(death)

        ct = StandardItem(usaCovData[8][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ct)
        case = StandardItem("cases: " + usaCovData[8][1])
        death = StandardItem("deaths: " + usaCovData[8][2])
        ct.appendRow(case)
        ct.appendRow(death)

        de = StandardItem(usaCovData[9][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(de)
        case = StandardItem("cases: " + usaCovData[9][1])
        death = StandardItem("deaths: " + usaCovData[9][2])
        de.appendRow(case)
        de.appendRow(death)

        dc = StandardItem(usaCovData[10][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(dc)
        case = StandardItem("cases: " + usaCovData[10][1])
        death = StandardItem("deaths: " + usaCovData[10][2])
        dc.appendRow(case)
        dc.appendRow(death)

        fl = StandardItem(usaCovData[11][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(fl)
        case = StandardItem("cases: " + usaCovData[11][1])
        death = StandardItem("deaths: " + usaCovData[11][2])
        fl.appendRow(case)
        fl.appendRow(death)

        ga = StandardItem(usaCovData[12][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ga)
        case = StandardItem("cases: " + usaCovData[12][1])
        death = StandardItem("deaths: " + usaCovData[12][2])
        ga.appendRow(case)
        ga.appendRow(death)

        gm = StandardItem(usaCovData[13][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(gm)
        case = StandardItem("cases: " + usaCovData[13][1])
        death = StandardItem("deaths: " + usaCovData[13][2])
        gm.appendRow(case)
        gm.appendRow(death)

        hi = StandardItem(usaCovData[14][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(hi)
        case = StandardItem("cases: " + usaCovData[14][1])
        death = StandardItem("deaths: " + usaCovData[14][2])
        hi.appendRow(case)
        hi.appendRow(death)

        ido = StandardItem(usaCovData[15][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ido)
        case = StandardItem("cases: " + usaCovData[15][1])
        death = StandardItem("deaths: " + usaCovData[15][2])
        ido.appendRow(case)
        ido.appendRow(death)

        il = StandardItem(usaCovData[16][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(il)
        case = StandardItem("cases: " + usaCovData[16][1])
        death = StandardItem("deaths: " + usaCovData[16][2])
        il.appendRow(case)
        il.appendRow(death)

        ina = StandardItem(usaCovData[17][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ina)
        case = StandardItem("cases: " + usaCovData[17][1])
        death = StandardItem("deaths: " + usaCovData[17][2])
        ina.appendRow(case)
        ina.appendRow(death)

        ia = StandardItem(usaCovData[18][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ia)
        case = StandardItem("cases: " + usaCovData[18][1])
        death = StandardItem("deaths: " + usaCovData[18][2])
        ia.appendRow(case)
        ia.appendRow(death)

        ks = StandardItem(usaCovData[19][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ks)
        case = StandardItem("cases: " + usaCovData[19][1])
        death = StandardItem("deaths: " + usaCovData[19][2])
        ks.appendRow(case)
        ks.appendRow(death)

        ky = StandardItem(usaCovData[20][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ky)
        case = StandardItem("cases: " + usaCovData[20][1])
        death = StandardItem("deaths: " + usaCovData[20][2])
        ky.appendRow(case)
        ky.appendRow(death)

        la = StandardItem(usaCovData[21][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(la)
        case = StandardItem("cases: " + usaCovData[21][1])
        death = StandardItem("deaths: " + usaCovData[20][2])
        la.appendRow(case)
        la.appendRow(death)

        me = StandardItem(usaCovData[22][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(me)
        case = StandardItem("cases: " + usaCovData[22][1])
        death = StandardItem("deaths: " + usaCovData[22][2])
        me.appendRow(case)
        me.appendRow(death)

        md = StandardItem(usaCovData[23][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(md)
        case = StandardItem("cases: " + usaCovData[23][1])
        death = StandardItem("deaths: " + usaCovData[23][2])
        md.appendRow(case)
        md.appendRow(death)

        ma = StandardItem(usaCovData[24][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ma)
        case = StandardItem("cases: " + usaCovData[24][1])
        death = StandardItem("deaths: " + usaCovData[24][2])
        ma.appendRow(case)
        ma.appendRow(death)

        mi = StandardItem(usaCovData[25][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(mi)
        case = StandardItem("cases: " + usaCovData[25][1])
        death = StandardItem("deaths: " + usaCovData[25][2])
        mi.appendRow(case)
        mi.appendRow(death)

        mn = StandardItem(usaCovData[26][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(mn)
        case = StandardItem("cases: " + usaCovData[26][1])
        death = StandardItem("deaths: " + usaCovData[26][2])
        mn.appendRow(case)
        mn.appendRow(death)

        ms = StandardItem(usaCovData[27][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ms)
        case = StandardItem("cases: " + usaCovData[27][1])
        death = StandardItem("deaths: " + usaCovData[27][2])
        ms.appendRow(case)
        ms.appendRow(death)

        mo = StandardItem(usaCovData[28][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(mo)
        case = StandardItem("cases: " + usaCovData[28][1])
        death = StandardItem("deaths: " + usaCovData[28][2])
        mo.appendRow(case)
        mo.appendRow(death)

        mt = StandardItem(usaCovData[29][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(mt)
        case = StandardItem("cases: " + usaCovData[29][1])
        death = StandardItem("deaths: " + usaCovData[29][2])
        mt.appendRow(case)
        mt.appendRow(death)

        ne = StandardItem(usaCovData[30][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ne)
        case = StandardItem("cases: " + usaCovData[30][1])
        death = StandardItem("deaths: " + usaCovData[30][2])
        ne.appendRow(case)
        ne.appendRow(death)

        nv = StandardItem(usaCovData[31][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(nv)
        case = StandardItem("cases: " + usaCovData[31][1])
        death = StandardItem("deaths: " + usaCovData[31][2])
        nv.appendRow(case)
        nv.appendRow(death)

        nh = StandardItem(usaCovData[32][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(nh)
        case = StandardItem("cases: " + usaCovData[32][1])
        death = StandardItem("deaths: " + usaCovData[32][2])
        nh.appendRow(case)
        nh.appendRow(death)

        nj = StandardItem(usaCovData[33][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(nj)
        case = StandardItem("cases: " + usaCovData[33][1])
        death = StandardItem("deaths: " + usaCovData[33][2])
        nj.appendRow(case)
        nj.appendRow(death)

        nm = StandardItem(usaCovData[34][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(nm)
        case = StandardItem("cases: " + usaCovData[34][1])
        death = StandardItem("deaths: " + usaCovData[34][2])
        nm.appendRow(case)
        nm.appendRow(death)

        ny = StandardItem(usaCovData[35][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ny)
        case = StandardItem("cases: " + usaCovData[35][1])
        death = StandardItem("deaths: " + usaCovData[35][2])
        ny.appendRow(case)
        ny.appendRow(death)

        nc = StandardItem(usaCovData[36][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(nc)
        case = StandardItem("cases: " + usaCovData[36][1])
        death = StandardItem("deaths: " + usaCovData[36][2])
        nc.appendRow(case)
        nc.appendRow(death)

        nk = StandardItem(usaCovData[37][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(nk)
        case = StandardItem("cases: " + usaCovData[37][1])
        death = StandardItem("deaths: " + usaCovData[37][2])
        nk.appendRow(case)
        nk.appendRow(death)

        nmi = StandardItem(usaCovData[38][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(nmi)
        case = StandardItem("cases: " + usaCovData[38][1])
        death = StandardItem("deaths: " + usaCovData[38][2])
        nmi.appendRow(case)
        nmi.appendRow(death)

        oh = StandardItem(usaCovData[39][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(oh)
        case = StandardItem("cases: " + usaCovData[39][1])
        death = StandardItem("deaths: " + usaCovData[39][2])
        oh.appendRow(case)
        oh.appendRow(death)
        
        ok = StandardItem(usaCovData[40][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ok)
        case = StandardItem("cases: " + usaCovData[40][1])
        death = StandardItem("deaths: " + usaCovData[40][2])
        ok.appendRow(case)
        ok.appendRow(death)

        ore = StandardItem(usaCovData[41][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ore)
        case = StandardItem("cases: " + usaCovData[41][1])
        death = StandardItem("deaths: " + usaCovData[41][2])
        ore.appendRow(case)
        ore.appendRow(death)

        pa = StandardItem(usaCovData[42][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(pa)
        case = StandardItem("cases: " + usaCovData[42][1])
        death = StandardItem("deaths: " + usaCovData[42][2])
        pa.appendRow(case)
        pa.appendRow(death)

        pr = StandardItem(usaCovData[43][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(pr)
        case = StandardItem("cases: " + usaCovData[43][1])
        death = StandardItem("deaths: " + usaCovData[43][2])
        pr.appendRow(case)
        pr.appendRow(death)

        ri = StandardItem(usaCovData[44][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ri)
        case = StandardItem("cases: " + usaCovData[44][1])
        death = StandardItem("deaths: " + usaCovData[44][2])
        ri.appendRow(case)
        ri.appendRow(death)

        sc= StandardItem(usaCovData[45][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(sc)
        case = StandardItem("cases: " + usaCovData[45][1])
        death = StandardItem("deaths: " + usaCovData[45][2])
        sc.appendRow(case)
        sc.appendRow(death)

        sd = StandardItem(usaCovData[46][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(sd)
        case = StandardItem("cases: " + usaCovData[46][1])
        death = StandardItem("deaths: " + usaCovData[46][2])
        sd.appendRow(case)
        sd.appendRow(death)
        
        tn = StandardItem(usaCovData[47][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(tn)
        case = StandardItem("cases: " + usaCovData[47][1])
        death = StandardItem("deaths: " + usaCovData[47][2])
        tn.appendRow(case)
        tn.appendRow(death)

        tx = StandardItem(usaCovData[48][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(tx)
        case = StandardItem("cases: " + usaCovData[48][1])
        death = StandardItem("deaths: " + usaCovData[48][2])
        tx.appendRow(case)
        tx.appendRow(death)

        ut = StandardItem(usaCovData[49][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ut)
        case = StandardItem("cases: " + usaCovData[49][1])
        death = StandardItem("deaths: " + usaCovData[49][2])
        ut.appendRow(case)
        ut.appendRow(death)

        vi = StandardItem(usaCovData[50][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(vi)
        case = StandardItem("cases: " + usaCovData[50][1])
        death = StandardItem("deaths: " + usaCovData[50][2])
        vi.appendRow(case)
        vi.appendRow(death)

        vt = StandardItem(usaCovData[51][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(vt)
        case = StandardItem("cases: " + usaCovData[51][1])
        death = StandardItem("deaths: " + usaCovData[51][2])
        vt.appendRow(case)
        vt.appendRow(death)

        va = StandardItem(usaCovData[52][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(va)
        case = StandardItem("cases: " + usaCovData[52][1])
        death = StandardItem("deaths: " + usaCovData[52][2])
        va.appendRow(case)
        va.appendRow(death)

        wa = StandardItem(usaCovData[53][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(wa)
        case = StandardItem("cases: " + usaCovData[53][1])
        death = StandardItem("deaths: " + usaCovData[53][2])
        wa.appendRow(case)
        wa.appendRow(death)

        wv = StandardItem(usaCovData[54][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(wv)
        case = StandardItem("cases: " + usaCovData[54][1])
        death = StandardItem("deaths: " + usaCovData[54][2])
        wv.appendRow(case)
        wv.appendRow(death)

        wi = StandardItem(usaCovData[55][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(wi)
        case = StandardItem("cases: " + usaCovData[55][1])
        death = StandardItem("deaths: " + usaCovData[55][2])
        wi.appendRow(case)
        wi.appendRow(death)

        wy = StandardItem(usaCovData[56][0], set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(wa)
        case = StandardItem("cases: " + usaCovData[56][1])
        death = StandardItem("deaths: " + usaCovData[56][2])
        wy.appendRow(case)
        wa.appendRow(death)
       
        # Add usa data to rootnode and set the tree model for tree view
        rootNodeUS.appendRow(usa)
        treeViewUS.setModel(treeModelUS)

        # Create Mexico Tree View
        treeViewMx = QTreeView(self)
        treeViewMx.setHeaderHidden(True)
        treeViewMx.setFixedWidth(380)
        treeViewMx.setFixedHeight(850)
        treeViewMx.move(750, 5)
       
        treeViewMx.setStyleSheet('QTreeView {\
                          margin: left;\
                          background-color: #F5FFFA;\
                          border-style: solid;\
                          border-width: 2px;\
                          border-radius: 10px;\
                          border-color: #A0A0A0;\
                          padding: 6px;\
                          }')

        treeModelMx = QStandardItemModel()
        rootNodeMx = treeModelMx.invisibleRootItem()

        # Mexico Data        
        mexico = StandardItem('Mexico', 14, set_bold=True, color=QColor(0, 153, 0))

        mc = StandardItem(mexicoCovData[1][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(mc)
        case = StandardItem("cases: " + str(mexicoCovData[1][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[1][2]))
        mc.appendRow(case)
        mc.appendRow(death)

        sm = StandardItem(mexicoCovData[2][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(sm)
        case = StandardItem("cases: " + str(mexicoCovData[2][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[2][2]))
        sm.appendRow(case)
        sm.appendRow(death)

        bc = StandardItem(mexicoCovData[3][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(bc)
        case = StandardItem("cases: " + str(mexicoCovData[3][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[3][2]))
        bc.appendRow(case)
        bc.appendRow(death)

        to = StandardItem(mexicoCovData[4][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(to)
        case = StandardItem("cases: " + str(mexicoCovData[4][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[4][2]))
        to.appendRow(case)
        to.appendRow(death)

        sa = StandardItem(mexicoCovData[5][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(sa)
        case = StandardItem("cases: " + str(mexicoCovData[5][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[5][2]))
        sa.appendRow(case)
        sa.appendRow(death)

        qr = StandardItem(mexicoCovData[6][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(qr)
        case = StandardItem("cases: " + str(mexicoCovData[6][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[6][2]))
        qr.appendRow(case)
        qr.appendRow(death)

        pu = StandardItem(mexicoCovData[7][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(pu)
        case = StandardItem("cases: " + str(mexicoCovData[7][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[7][2]))
        pu.appendRow(case)
        pu.appendRow(death)
        
        vz = StandardItem(mexicoCovData[8][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(vz)
        case = StandardItem("cases: " + str(mexicoCovData[8][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[8][2]))
        vz.appendRow(case)
        vz.appendRow(death)

        coa = StandardItem(mexicoCovData[9][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(coa)
        case = StandardItem("cases: " + str(mexicoCovData[9][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[9][2]))
        coa.appendRow(case)
        coa.appendRow(death)

        yu = StandardItem(mexicoCovData[10][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(yu)
        case = StandardItem("cases: " + str(mexicoCovData[10][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[10][2]))
        yu.appendRow(case)
        yu.appendRow(death)

        jo = StandardItem(mexicoCovData[11][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(jo)
        case = StandardItem("cases: " + str(mexicoCovData[11][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[11][2]))
        jo.appendRow(case)
        jo.appendRow(death)

        ts = StandardItem(mexicoCovData[12][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(ts)
        case = StandardItem("cases: " + str(mexicoCovData[12][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[12][2]))
        ts.appendRow(case)
        ts.appendRow(death)

        bjs = StandardItem(mexicoCovData[13][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(bjs)
        case = StandardItem("cases: " + str(mexicoCovData[13][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[13][2]))
        bjs.appendRow(case)
        bjs.appendRow(death)

        nl = StandardItem(mexicoCovData[14][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(nl)
        case = StandardItem("cases: " + str(mexicoCovData[14][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[14][2]))
        nl.appendRow(case)
        nl.appendRow(death)

        chi = StandardItem(mexicoCovData[15][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(chi)
        case = StandardItem("cases: " + str(mexicoCovData[15][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[15][2]))
        chi.appendRow(case)
        chi.appendRow(death)

        gu = StandardItem(mexicoCovData[16][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(gu)
        case = StandardItem("cases: " + str(mexicoCovData[16][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[16][2]))
        gu.appendRow(case)
        gu.appendRow(death)

        gue = StandardItem(mexicoCovData[17][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(gue)
        case = StandardItem("cases: " + str(mexicoCovData[17][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[17][2]))
        gue.appendRow(case)
        gue.appendRow(death)

        mic = StandardItem(mexicoCovData[18][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(mic)
        case = StandardItem("cases: " + str(mexicoCovData[18][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[18][2]))
        mic.appendRow(case)
        mic.appendRow(death)
        
        mor = StandardItem(mexicoCovData[19][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(mor)
        case = StandardItem("cases: " + str(mexicoCovData[19][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[19][2]))
        mor.appendRow(case)
        mor.appendRow(death)

        hid = StandardItem(mexicoCovData[20][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(hid)
        case = StandardItem("cases: " + str(mexicoCovData[20][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[20][2]))
        hid.appendRow(case)
        hid.appendRow(death)

        so = StandardItem(mexicoCovData[21][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(so)
        case = StandardItem("cases: " + str(mexicoCovData[21][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[21][2]))
        so.appendRow(case)
        so.appendRow(death)

        ag = StandardItem(mexicoCovData[22][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(ag)
        case = StandardItem("cases: " + str(mexicoCovData[22][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[22][2]))
        ag.appendRow(case)
        ag.appendRow(death)
        
        tl = StandardItem(mexicoCovData[23][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(tl)
        case = StandardItem("cases: " + str(mexicoCovData[23][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[23][2]))
        tl.appendRow(case)
        tl.appendRow(death)

        cs = StandardItem(mexicoCovData[24][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(cs)
        case = StandardItem("cases: " + str(mexicoCovData[24][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[24][2]))
        cs.appendRow(case)
        cs.appendRow(death)

        qo = StandardItem(mexicoCovData[25][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(qo)
        case = StandardItem("cases: " + str(mexicoCovData[25][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[25][2]))
        qo.appendRow(case)
        qo.appendRow(death)

        oa = StandardItem(mexicoCovData[26][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(oa)
        case = StandardItem("cases: " + str(mexicoCovData[26][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[26][2]))
        oa.appendRow(case)
        oa.appendRow(death)

        slp = StandardItem(mexicoCovData[27][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(slp)
        case = StandardItem("cases: " + str(mexicoCovData[27][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[27][2]))
        slp.appendRow(case)
        slp.appendRow(death)

        ce = StandardItem(mexicoCovData[28][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(ce)
        case = StandardItem("cases: " + str(mexicoCovData[28][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[28][2]))
        ce.appendRow(case)
        ce.appendRow(death)

        zs = StandardItem(mexicoCovData[29][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(zs)
        case = StandardItem("cases: " + str(mexicoCovData[29][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[29][2]))
        zs.appendRow(case)
        zs.appendRow(death)

        nt = StandardItem(mexicoCovData[30][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(nt)
        case = StandardItem("cases: " + str(mexicoCovData[30][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[30][2]))
        nt.appendRow(case)
        nt.appendRow(death)

        do = StandardItem(mexicoCovData[31][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(do)
        case = StandardItem("cases: " + str(mexicoCovData[31][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[31][2]))
        do.appendRow(case)
        do.appendRow(death)

        col = StandardItem(mexicoCovData[32][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(col)
        case = StandardItem("cases: " + str(mexicoCovData[32][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[32][2]))
        col.appendRow(case)
        col.appendRow(death)

        # Add mexico data to rootnode and set the tree model for tree view
        rootNodeMx.appendRow(mexico)
        treeViewMx.setModel(treeModelMx)

        # North America Map
        mapNA = QFrame(self)
        mapNA.setFixedWidth(830)
        mapNA.setFixedHeight(850)
        mapNA.move(1130, 20)
        mapNA.setStyleSheet('QFrame {\
                              background-color:#F5F5F5;\
                              border: 6px gray solid;\
                              }')

        # Source Button
        source = QPushButton('Source', self)
        source.setStyleSheet('QPushButton {\
                          margin: left;\
                          font: bold 16px;\
                          background-color:#FFB266;\
                          color:white;\
                          border-style: inset;\
                          border-width: 2px;\
                          border-radius: 10px;\
                          border-corlor: beige;\
                          padding: 6px;\
                          }')

        source.setFixedWidth(230)
        source.setFixedHeight(100)
        source.move(100, 930)
        source.clicked.connect(self.onSourceClicked)
        
        # Devs Button
        devs = QPushButton('Developers', self)
        devs.setStyleSheet('QPushButton {\
                          margin: left;\
                          font: bold 16px;\
                          background-color: lightblue;\
                          color:white;\
                          border-style: inset;\
                          border-width: 2px;\
                          border-radius: 10px;\
                          border-corlor: beige;\
                          padding: 6px;\
                          }')

        devs.setFixedWidth(230)
        devs.setFixedHeight(100)                            
        devs.move(400, 930)
        devs.clicked.connect(self.onDevsClicked)
        
        # Quit Button
        quitButton = QPushButton('Quit', self)
        quitButton.setStyleSheet('QPushButton {\
                          margin: left;\
                          font: bold 16px;\
                          background-color: gray;\
                          color:white;\
                          border-style: inset;\
                          border-width: 2px;\
                          border-radius: 10px;\
                          border-corlor: beige;\
                          padding: 6px;\
                          }')
        quitButton.setFixedWidth(230)
        quitButton.setFixedHeight(100)                            
        quitButton.move(700, 930)
        quitButton.clicked.connect(self.onQuitClicked)
        
        # Trending News Section
        news = QPlainTextEdit(self)
        news.setFixedWidth(980)
        news.setFixedHeight(250)
        news.move(1000, 930)
        news.setStyleSheet('QTextEdit {\
                          font: bold 16px;\
                          font-family: georgia;\
                          color: #000080;\
                          border-style: dot-dash;\
                          border-width: 1px;\
                          border-radius: 10px;\
                          border-color: darkblue;\
                          padding: 3px;\
                          }')
        news.setText(newsSource)
        
        # Layout settings
        hbox.addWidget(source)
        hbox.addWidget(devs)
        hbox.addWidget(news)
                   
        self.setLayout(hbox)
        self.show()

    def onRefreshClicked(self):
        refMsg = QMessageBox(self)

    def onSourceClicked(self, source):

        source = ("https://realpython.com/beautiful-soup-web-scraper-python \n" + \
                  "https://realpython.com/openpyxl-excel-spreadsheets-python \n" + \
                  "https://doc.qt.io/qt-5/stylesheet-reference.html \n" + \
                  "https://doc.qt.io/qtforpython/PySide2/QtGui/QFont.html#more \n" + \
                  "https://doc.qt.io/qtforpython/PySide2/QtWidgets/QTreeView.html \n" + \
                  "https://docs.python.org/3/howto/urllib2.html")
              
        sourceMsg = QMessageBox(self)
        sourceMsg.setWindowTitle('References:')
        sourceMsg.move(100, 1000)
        sourceMsg.setText(source)
        sourceMsg.setStyleSheet('QMessageBox {\
                              font: 15px;\
                              font-family: georgia;\
                              background-color:#FFE5CC;\
                              padding: 6px;\
                              }')
        sourceMsg.exec_()

    def onDevsClicked(self, developers):
        developers = (" Eldon Hayes          \n" +
                      " Cindy Nguyen         \n" +
                      " Carlan Nguyen        \n")
                  
        devsMsg = QMessageBox(self)
        devsMsg.setWindowTitle('Developers')
        devsMsg.move(400, 1000)
        devsMsg.setText(developers)
        devsMsg.setStyleSheet('QMessageBox {\
                              font-size: 18px;\
                              font-family: georgia;\
                              color: #000066;\
                              font-weight: bold;\
                              background-color:#CCE5FF;\
                              padding: 6px;\
                              }')
        devsMsg.exec_()

    def onQuitClicked(self):
        sys.exit(app.exec_())
    
def getCanadaData():
    canadaProvinces = canadaSoup.scrapeCanada()
    for row in canadaProvinces:
        canadaCovData.append([row[0], row[1], row[2]])
            
def getUsaData():
    usaStates = usaSoup.scrapeUSA()
    for row in usaStates:
        usaCovData.append([row[0], row[1], row[2]])
        
def getMexicoData():
    mexicoStates = mexicoSoup.scrapeMexico()
    for row in mexicoStates:
        mexicoCovData.append([row[0], row[1], row[2]])
        
def getNewsData():
    newsList = newsSoup.scrapeNews()
   
    newsStrOne = ''.join(newsList[0]) + ", " + ''.join(newsList[1]) + ", " +\
                 ''.join(newsList[2]) + "\n"
    newsStrTwo = ''.join(newsList[3]) + ", " + ''.join(newsList[4]) + ", " +\
                 ''.join(newsList[5]) + "\n"
    newsStrThree = ''.join(newsList[6]) + ", " + ''.join(newsList[7]) + ", " +\
                 ''.join(newsList[8]) + "\n"
    newsStrFour = ''.join(newsList[9]) + ", " + ''.join(newsList[10]) + ", " +\
                 ''.join(newsList[11]) + "\n"
    newsStrFive = ''.join(newsList[12]) + ", " + ''.join(newsList[13]) + ", " +\
                 ''.join(newsList[14])

    newsSource = "Trending News: \n" + "\n" +\
                 newsStrOne + "\n" +\
                 newsStrTwo + "\n" +\
                 newsStrThree + "\n" +\
                 newsStrFour + "\n" +\
                 newsStrFive 
    return newsSource
   
if __name__ == '__main__':
    getUsaData()
    getMexicoData()
    getCanadaData()
    newsSource = getNewsData()
    app = QApplication(sys.argv)
    codeScraper = MainWindow()
    sys.exit(app.exec_())


    
