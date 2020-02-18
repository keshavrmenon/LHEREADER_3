from lhereader import readLHEF
from ROOT import TFile, TCanvas, TH1F, TLegend, TLatex, TLorentzVector

c=TCanvas()

data1=readLHEF('../LHE/NMSSM/m300.lhe')
events1=data1.events
data2=readLHEF('../LHE/NMSSM/m600.lhe')
events2=data2.events
data3=readLHEF('../LHE/NMSSM/m1000.lhe')
events3=data3.events

hpt_h_300=TH1F("pt_h_300", "M_{X}=300", 100, 0, 500)
hpt_h_600=TH1F("pt_h_600", "M_{X}=600", 100, 0, 500)
hpt_h_1000=TH1F("pt_h_1000", "M_{X}=1000", 100, 0, 500)

for e in events1:
    higgs=e.getParticlesByIDs([25])
    for h in higgs:
        hpt_h_300.Fill(h.pt)

for e in events2:
    higgs=e.getParticlesByIDs([25])
    for h in higgs:
        hpt_h_600.Fill(h.pt)

for e in events3:
    higgs=e.getParticlesByIDs([25])
    for h in higgs:
        hpt_h_1000.Fill(h.pt)

hpt_h_300.SetLineColor(600)
hpt_h_600.SetLineColor(418)
hpt_h_1000.SetLineColor(625)
hpt_h_300.SetLineWidth(1)
hpt_h_600.SetLineWidth(1)
hpt_h_1000.SetLineWidth(1)
hpt_h_300.Scale(1/hpt_h_300.GetEntries())
hpt_h_600.Scale(1/hpt_h_600.GetEntries())
hpt_h_1000.Scale(1/hpt_h_1000.GetEntries())
hpt_h_300.Draw("hist")
hpt_h_600.Draw("hist&same")
hpt_h_1000.Draw("hist&same")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
hpt_h_300.SetTitle("p_{T} [in GeV] of Higgs in NMSSM for different masses of X")
c.SaveAs("./comparison/h_pt_compare.root")