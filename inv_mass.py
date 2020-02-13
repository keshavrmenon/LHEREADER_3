from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TLegend
import CommonSetup1

c=TCanvas()
#c.SetLogy()
c.cd()
csetup=CommonSetup1.CommonSetup()
csetup.style()

data7=readLHEF('cmsgrid_final.lhe')
parts7=data7.getParticlesByIDs([35])
print(len(parts7))
hist7=TH1F("inv_mass", "inv_mass of Gr",100,0,200)
_7=[hist7.Fill(p.invariantMass) for p in parts7]
hist7.SetLineColor(625)
hist7.SetLineWidth(3)
hist7.SetXTitle("M_{HH} in GeV");
hist7.SetYTitle("Events");
hist7.Draw()

c.Update()
"""data6=readLHEF('M1500.lhe')
parts6=data6.getParticlesByIDs([39])
print(len(parts6))
hist6=TH1F("inv_mass", "inv_mass of Gr",100,0,6000)
_6=[hist6.Fill(p.invariantMass) for p in parts6]
hist6.SetLineColor(413)
#hist6.SetLineStyle(2)
hist6.SetLineWidth(3)
hist6.SetXTitle("Inv_Mass_{Gr} in GeV");
hist6.SetYTitle("Events");
hist6.Draw("same")
"""
"""c.Update()
data5=readLHEF('1500_01.lhe')
parts5=data5.getParticlesByIDs([39])
print(len(parts5))
hist5=TH1F("inv_mass", "inv_mass of Graviton",100,0,6000)
_5=[hist5.Fill(p.invariantMass) for p in parts5]
hist5.SetLineWidth(3)
hist5.SetLineColor(425)
hist5.Draw("same")"""


"""c.Update()
data3=readLHEF('../LHE/1500_05.lhe')
parts3=data3.getParticlesByIDs([39])
print(len(parts3))
hist3=TH1F("inv_mass", "inv_mass of Graviton",100,0,6000)
#_3=[hist.Fill(p.pt) for p in parts3]
hist3.SetLineColor(600)
for p in parts3:
    hist3.Fill(p.invariantMass)
hist3.SetLineWidth(3)
hist3.Draw("same")
"""
"""c.Update()
data4=readLHEF('../LHE/1500_05.lhe')
parts4=data4.getParticlesByIDs([39])
print(len(parts3))
hist4=TH1F("inv_mass", "inv_mass of Graviton",100,0,6000)
#_3=[hist.Fill(p.pt) for p in parts3]
hist4.SetLineColor(625)
for p in parts4:
    hist4.Fill(p.invariantMass)
hist4.SetLineWidth(3)
hist4.Draw("same")

c.Update()
data1=readLHEF('1500_30.lhe')
parts1=data1.getParticlesByIDs([39])
print(len(parts1))
hist1=TH1F("inv_mass", "inv_mass of Graviton",100,0,6000)
#_3=[hist.Fill(p.pt) for p in parts3]

for p in parts1:
    hist1.Fill(p.invariantMass)
hist1.SetLineWidth(5)
hist1.SetLineStyle(2)
hist1.Draw("same")
"""


c.Update()
l = TLegend(.75,.70,1.0,.90)
#l.AddEntry(hist1, "MG_M1500_W30_10k")
#l.AddEntry(hist6, "M1500_W30")
#l.AddEntry(hist5, "M1500_W01")
#l.AddEntry(hist3, "M1500_W05")
#l.AddEntry(hist4, "M1500_W20_5k")
l.AddEntry(hist7, "M1500_W01")
l.Draw()


c.SaveAs("mass_p4_linear.jpg")




