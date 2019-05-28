from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TLegend
import CommonSetup1

c=TCanvas()
c.SetLogy()
c.cd()
csetup=CommonSetup1.CommonSetup()
csetup.style()

data1=readLHEF('cmsgrid_final_MG261.lhe')
parts1=data1.getParticlesByIDs([5,-5])
print(len(parts1))
hist1=TH1F("pT", "p_{T} of b [GeV]",10,0,500)
#_1=[hist1.Fill(p.pt) for p in parts1]
hist1.SetLineColor(633)
for p in parts1:
    #if(p.mother == [4,4]):
        hist1.Fill(p.pt)
hist1.SetLineWidth(4)
hist1.SetXTitle("p_{T} GeV");
hist1.SetYTitle("Events");
hist1.Draw()

c.Update()
data2=readLHEF('cmsgrid_final_MG260.lhe')
parts2=data2.getParticlesByIDs([5,-5])
print(len(parts2))
hist2=TH1F("pT", "p_{T} of b [GeV]",10,0,500)
#_2=[hist.Fill(p.pt) for p in parts2]
hist2.SetLineColor(600)
for p in parts2:
    #if(p.mother == [1,2]):
        hist2.Fill(p.pt)
hist2.SetLineWidth(2)
hist2.Draw("same")
"""
c.Update()
data3=readLHEF('/Users/latapanwar/Documents/cmsgrid_2000_10.lhe')
parts3=data3.getParticlesByIDs([5])
print(len(parts3))
hist3=TH1F("eta", "#eta of VBF",50,-5,5)
#_1=[hist1.Fill(p.pt) for p in parts1]
hist3.SetLineColor(413)
for p in parts3:
    #if(p.mother == [1,2]):
        hist3.Fill(p.eta)
hist3.SetLineWidth(3)
hist3.SetXTitle("#eta");
hist3.SetYTitle("Events");
hist3.Draw("same")

c.Update()
data4=readLHEF('/Users/latapanwar/Documents/cmsgrid_2000_20.lhe')
parts4=data4.getParticlesByIDs([5])
print(len(parts4))
hist4=TH1F("eta", "eta of b",50,-5,5)
#_2=[hist.Fill(p.pt) for p in parts2]
hist4.SetLineColor(425)
for p in parts4:
    #if(p.mother == [1,2]):
        hist4.Fill(p.eta)
hist4.SetLineWidth(3)
hist4.Draw("same")

c.Update()
data5=readLHEF('/Users/latapanwar/Documents/cmsgrid_2500_10.lhe')
parts5=data5.getParticlesByIDs([5])
print(len(parts5))
hist5=TH1F("eta", "#eta of VBF",50,-5,5)
#_1=[hist1.Fill(p.pt) for p in parts1]
hist5.SetLineColor(597)
for p in parts5:
    #  if(p.mother == [1,2]):
        hist5.Fill(p.eta)
hist5.SetLineWidth(3)
hist5.Draw("same")

c.Update()
data6=readLHEF('/Users/latapanwar/Documents/cmsgrid_2500_20.lhe')
parts6=data6.getParticlesByIDs([5])
print(len(parts6))
hist6=TH1F("eta", "eta of b",50,-5,5)
#_2=[hist.Fill(p.pt) for p in parts2]
hist6.SetLineColor(593)
for p in parts6:
    # if(p.mother == [1,2]):
        hist6.Fill(p.eta)
hist6.SetLineWidth(3)
hist6.Draw("same")

c.Update()
data7=readLHEF('/Users/latapanwar/Documents/cmsgrid_3000_10.lhe')
parts7=data7.getParticlesByIDs([5])
print(len(parts7))
hist7=TH1F("eta", "eta of b",50,-5,5)
#_2=[hist.Fill(p.pt) for p in parts2]
hist7.SetLineColor(613)
for p in parts7:
    # if(p.mother == [1,2]):
        hist7.Fill(p.eta)
hist7.SetLineWidth(3)
hist7.Draw("same")


c.Update()
data8=readLHEF('/Users/latapanwar/Documents/cmsgrid_3000_20.lhe')
parts8=data8.getParticlesByIDs([5])
print(len(parts8))
hist8=TH1F("eta", "eta of b",50,-5,5)
#_2=[hist.Fill(p.pt) for p in parts2]
hist8.SetLineColor(615)
for p in parts8:
    #  if(p.mother == [1,2]):
        hist8.Fill(p.eta)
hist8.SetLineWidth(3)
hist8.Draw("same")




c.Update()
data3=readLHEF('MGr1000_20.lhe')
parts3=data3.getParticlesByIDs([5])
print(len(parts3))
hist3=TH1F("eta", "eta",50,-5,5)
#_3=[hist.Fill(p.pt) for p in parts3]
hist3.SetLineColor(601)
for p in parts3:
    hist3.Fill(p.eta)
hist3.SetLineWidth(3)
hist3.Draw("same")

"""
#c.Update()
l = TLegend(.75,.70,1.0,.90)
"""l.AddEntry(hist1, "1500_10")
l.AddEntry(hist2, "1500_20")
l.AddEntry(hist3, "2000_10")
l.AddEntry(hist4, "2000_20")
l.AddEntry(hist5, "2500_10")
l.AddEntry(hist6, "2500_20")"""
l.AddEntry(hist2, "MG_260")
l.AddEntry(hist1, "MG_261")

l.Draw()


c.SaveAs("pT_b_log.png")
c.SaveAs("pT_b_log.pdf")


