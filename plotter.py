from ROOT import TH1F, TFile, TLatex, TLegend, TCanvas
import CommonSetup
c=TCanvas()
c.cd()
csetup=CommonSetup.CommonSetup()
csetup.style()

s='pt_photon'
c.SetName(s)
f1=TFile.Open('basic_kin_m300.root')

h1=f1.Get(s+'_nmssm')
h1.SetXTitle("p_{T}(b) [GeV]")
h1.SetYTitle("Events")
h1.SetTitle('NMSSM')
h1.SetLineColor(600)
h1.Draw('hist')
c.Update()

h2=f1.Get(s+'_radion')
h2.SetXTitle("p_{T}(b) [GeV]")
h2.SetYTitle("Event")
h2.SetTitle('NMSSM')
h2.SetLineColor(418)
h2.Draw('hist&same')
c.Update()

h3=f1.Get(s+'_graviton')
h3.SetXTitle("p_{T}(b) [GeV]")
h3.SetYTitle("Events")
h3.SetTitle('graviton')
h3.SetLineColor(625)
h3.Draw('hist&same')
c.Update()

l=c.BuildLegend(0.75,0.4,0.9,0.5)
c.Update()
f=TFile.Open('plots.root', 'UPDATE')
c.Write()
