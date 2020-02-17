from lhereader import readLHEF
from ROOT import TFile, TCanvas, TH1F, TLegend, TLatex, TLorentzVector
#import CommonSetup1

f=TFile('basic_kin_m300.root', 'RECREATE')
c=TCanvas()

#Getting event data from LHE File for mass point X=300 GeV
data1=readLHEF('../LHE/spin0/m300.lhe')
events1=data1.events
data2=readLHEF('../LHE/spin2/m300.lhe')
events2=data2.events
data3=readLHEF('../LHE/NMSSM/m300.lhe')
events3=data3.events

#defining histogams for photon and diphoton

#Radion Model
hpt_photon0=TH1F("pt_photon_radion","Radion", 50, 0., 100.)
heta_photon0=TH1F("eta_photon_radion","Radion", 50, -5, 5)
hphi_photon0=TH1F("phi_photon_radion","Radion", 50, -5,5)
hpt_diphoton0=TH1F("pt_diphoton_radion","Radion", 50, 0., 100.)
heta_diphoton0=TH1F("eta_diphoton_radion","Radion", 50, -5, 5)
hphi_diphoton0=TH1F("phi_diphoton_radion","Radion", 50, -5,5)
hm_diphoton0=TH1F("m_diphoton_radion","Radion", 1000, 124.9, 125.1)

#Graviton Model
hpt_photon2=TH1F("pt_photon_graviton","Graviton", 50, 0., 100.)
heta_photon2=TH1F("eta_photon_graviton","Graviton", 50, -5., 5.)
hphi_photon2=TH1F("phi_photon_graviton","Graviton", 50, -5,5)
hpt_diphoton2=TH1F("pt_diphoton_graviton","Graviton", 50, 0., 100.)
heta_diphoton2=TH1F("eta_diphoton_graviton","Graviton", 50, -5., 5.)
hphi_diphoton2=TH1F("phi_diphoton_graviton","Graviton", 50, -5,5)
hm_diphoton2=TH1F("m_diphoton_graviton","Graviton", 1000, 124.9, 125.1)

#NMSSM
hpt_photon_nmssm=TH1F("pt_photon_nmssm","NMSSM", 50, 0., 100.)
heta_photon_nmssm=TH1F("eta_photon_nmssm","NMSSM", 50,-5., 5.)
hphi_photon_nmssm=TH1F("phi_photon_nmssm","NMSSM", 50, -5,5)
hpt_diphoton_nmssm=TH1F("pt_diphoton_nmssm","NMSSM",75,0.,150.)
heta_diphoton_nmssm=TH1F("eta_diphoton_nmssm","NMSSM", 50, -5., 5.)
hphi_diphoton_nmssm=TH1F("phi_diphoton_nmssm","NMSSM", 50, -5.,5.)
hm_diphoton_nmssm=TH1F("m_diphoton_nmssm","NMSSM", 1000, 124.9, 125.1)


#defining hists for b and bb

#Radion
hpt_b0=TH1F("pt_b_radion","Radion", 50, 0., 100.)
heta_b0=TH1F("eta_b_radion","Radion", 50, -5., 5.)
hphi_b0=TH1F("phi_b_radion","Radion", 50, -5., 5.)
heta_bb0=TH1F("eta_bb_radion","Radion", 50, -5., 5.)
hpt_bb0=TH1F("pt_bb_radion","Radion", 50, 0., 100.)
hphi_bb0=TH1F("phi_bb_radion","Radion", 50, -5., 5.)
hm_bb0=TH1F("m_bb_radion","Radion", 1000, 124.9, 125.1)

#Graviton
hpt_b2=TH1F("pt_b_graviton","Graviton", 50, 0., 100.)
heta_b2=TH1F("eta_b_graviton","Graviton", 50, -5., 5.)
hphi_b2=TH1F("phi_b_graviton","Graviton", 50, -5., 5.)
heta_bb2=TH1F("eta_bb_graviton","Graviton", 50, -5., 5.)
hpt_bb2=TH1F("pt_bb_graviton","Graviton", 50, 0., 100.)
hphi_bb2=TH1F("phi_bb_graviton","Graviton", 50, -5., 5.)
hm_bb2=TH1F("m_bb_graviton","Graviton", 1000, 124.9, 125.1)

#NMSSM
hpt_b_nmssm=TH1F("pt_b_nmssm","NMSSM", 50, 0., 100.)
heta_b_nmssm=TH1F("eta_b_nmssm","NMSSM", 50, -5., 5.)
hphi_b_nmssm=TH1F("phi_b_nmssm","NMSSM", 50, -5., 5.)
heta_bb_nmssm=TH1F("eta_bb_nmssm","NMSSM", 50, -5., 5.)
hpt_bb_nmssm=TH1F("pt_bb_nmssm","NMSSM", 50, 0., 100.)
hphi_bb_nmssm=TH1F("phi_bb_nmssm","NMSSM", 50, -5., 5.)
hm_bb_nmssm=TH1F("m_bb_nmssm","NMSSM", 1000, 124.9, 125.1)

#defining Hists for Higgs, Y, HY, and X

#Radion
hpt_h0=TH1F("pt_h_radion","Radion", 50, 0., 100.)
heta_h0=TH1F("eta_h_radion","Radion", 50, -5., 5.)
hphi_h0=TH1F("phi_h_radion","Radion", 50, -5., 5.)
hpt_hh0=TH1F("pt_hh_radion","Radion", 100, 0., 200.)
heta_hh0=TH1F("eta_hh_radion","Radion", 50, -5., 5.)
hphi_hh0=TH1F("phi_hh_radion","Radion", 50, -5., 5.)
hm_hh0=TH1F("m_hh_radion", "Radion", 1000, 290, 310)

#Graviton
hpt_h2=TH1F("pt_h_graviton","Graviton", 50, 0., 100.)
heta_h2=TH1F("eta_h_graviton", "Graviton", 50, -5., 5.)
hphi_h2=TH1F("phi_h_graviton", "Graviton", 50, -5., 5.)
hpt_hh2=TH1F("pt_hh_graviton","Graviton", 100, 0., 200.)
heta_hh2=TH1F("eta_hh_graviton", "Graviton", 50, -5., 5.)
hphi_hh2=TH1F("phi_hh_graviton", "Graviton", 50, -5., 5.)
hm_hh2=TH1F("m_hh_graviton", "Graviton", 1000, 290, 310)

#NMSSM
hpt_h_nmssm=TH1F("pt_h_nmssm","NMSSM", 50, 0., 100.)
heta_h_nmssm=TH1F("eta_h_nmssm", "NMSSM", 50, -5., 5.)
hphi_h_nmssm=TH1F("phi_h_nmssm", "NMSSM", 50, -5., 5.)
hpt_y_nmssm=TH1F("pt_y_nmssm","NMSSM", 50, 0., 100.)
heta_y_nmssm=TH1F("eta_y_nmssm", "NMSSM", 50, -5., 5.)
hphi_y_nmssm=TH1F("phi_y_nmssm", "NMSSM", 50, -5., 5.)
hpt_hy_nmssm=TH1F("pt_hy_nmssm","NMSSM", 100, 0., 200.)
heta_hy_nmssm=TH1F("eta_hy_nmssm", "NMSSM", 50, -5., 5.)
hphi_hy_nmssm=TH1F("phi_hy_nmssm", "NMSSM", 50, -5., 5.)
hm_hy_nmssm=TH1F("m_hy_nmssm", "NMSSM", 1000, 290, 310)

#iterating over events
for e in events1:
    photons=e.getParticlesByIDs([22])
    bb=e.getParticlesByIDs([5,-5])
    hh=e.getParticlesByIDs([25])
    p_phot=TLorentzVector(0,0,0,0)         #defining Lorentz-Vector for diphoton
    p_bb=TLorentzVector(0,0,0,0)           #defining Lorentz-Vector for bb
    p_hh=TLorentzVector(0,0,0,0)
    for p in photons:
        if p.mother==[4,4]:
            p_phot+=p.p4                   #Adding 4-vectors for photons in event
            hpt_photon0.Fill(p.pt)
            heta_photon0.Fill(p.eta)
            hphi_photon0.Fill(p.phi)
    hpt_diphoton0.Fill(p_phot.Pt())
    heta_diphoton0.Fill(p_phot.Eta())
    hphi_diphoton0.Fill(p_phot.Phi())
    hm_diphoton0.Fill(p_phot.M())
    for j in bb:
        p_bb+=j.p4
        hpt_b0.Fill(j.pt)
        heta_b0.Fill(j.eta)
        hphi_b0.Fill(j.phi)
    hpt_bb0.Fill(p_bb.Pt())
    heta_bb0.Fill(p_bb.Eta())
    hphi_bb0.Fill(p_bb.Phi())
    hm_bb0.Fill(p_bb.M())
    for h in hh:
        p_hh+=h.p4
        hpt_h0.Fill(h.pt)
        heta_h0.Fill(h.eta)
        hphi_h0.Fill(h.phi)
    hpt_hh0.Fill(p_hh.Pt())
    heta_hh0.Fill(p_hh.Eta())
    hphi_hh0.Fill(p_hh.Phi())
    hm_hh0.Fill(p_hh.M())
        
for e in events2:
    photons=e.getParticlesByIDs([22])
    bb=e.getParticlesByIDs([5,-5])
    hh=e.getParticlesByIDs([25])
    p_phot=TLorentzVector(0,0,0,0)
    p_bb=TLorentzVector(0,0,0,0)
    p_hh=TLorentzVector(0,0,0,0)
    for p in photons:
        if p.mother==[4,4]:
            p_phot+=p.p4
            hpt_photon2.Fill(p.pt)
            heta_photon2.Fill(p.eta)
            hphi_photon2.Fill(p.phi)
    hpt_diphoton2.Fill(p_phot.Pt())
    heta_diphoton2.Fill(p_phot.Eta())
    hphi_diphoton2.Fill(p_phot.Phi())
    hm_diphoton2.Fill(p_phot.M())
    for j in bb:
        if j.mother==[5,5]:
            p_bb+=j.p4
            hpt_b2.Fill(j.pt)
            heta_b2.Fill(j.eta)
            hphi_b2.Fill(j.phi)
    hpt_bb2.Fill(p_bb.Pt())
    heta_bb2.Fill(p_bb.Eta())
    hphi_bb2.Fill(p_bb.Phi())
    hm_bb2.Fill(p_bb.M())
    for h in hh:
        p_hh+=h.p4
        hpt_h2.Fill(h.pt)
        heta_h2.Fill(h.eta)
        hphi_h2.Fill(h.phi)
    hpt_hh2.Fill(p_hh.Pt())
    heta_hh2.Fill(p_hh.Eta())
    hphi_hh2.Fill(p_hh.Phi())
    hm_hh2.Fill(p_hh.M())

for e in events3:
    photons=e.getParticlesByIDs([22])
    bb=e.getParticlesByIDs([5,-5])
    higgs=e.getParticlesByIDs([25])
    y=e.getParticlesByIDs([35])
    hy=higgs+y
    p_phot=TLorentzVector(0,0,0,0)
    p_bb=TLorentzVector(0,0,0,0)
    p_hy=TLorentzVector(0,0,0,0)
    for p in photons:
      p_phot+=p.p4
      hpt_photon_nmssm.Fill(p.pt)
      heta_photon_nmssm.Fill(p.eta)
      hphi_photon_nmssm.Fill(p.phi)
    hpt_diphoton_nmssm.Fill(p_phot.Pt())
    heta_diphoton_nmssm.Fill(p_phot.Eta())
    hphi_diphoton_nmssm.Fill(p_phot.Phi())
    hm_diphoton_nmssm.Fill(p_phot.M())
    for j in bb:
        p_bb+=j.p4
        hpt_b_nmssm.Fill(j.pt)
        heta_b_nmssm.Fill(j.eta)
        hphi_b_nmssm.Fill(j.phi)
    for i in hy:
        p_hy+=i.p4
    hpt_bb_nmssm.Fill(p_bb.Pt())
    heta_bb_nmssm.Fill(p_bb.Eta())
    hphi_bb_nmssm.Fill(p_bb.Phi())
    hm_bb_nmssm.Fill(p_bb.M())
    for h in higgs:
        hpt_h_nmssm.Fill(h.pt)
        heta_h_nmssm.Fill(h.eta)
        hphi_h_nmssm.Fill(h.phi)
    for i in y:
        hpt_y_nmssm.Fill(i.pt)
        heta_y_nmssm.Fill(i.eta)
        hphi_y_nmssm.Fill(i.phi)
    hpt_hy_nmssm.Fill(p_hy.Pt())
    heta_hy_nmssm.Fill(p_hy.Eta())
    hphi_hy_nmssm.Fill(p_hy.Phi())    
    
#Draw Histograms
c.Update()
hpt_photon0.SetLineColor(600)
hpt_photon0.SetLineWidth(1)
hpt_photon2.SetLineColor(418)
hpt_photon2.SetLineWidth(1)
hpt_photon_nmssm.SetLineColor(625)
hpt_photon_nmssm.SetLineWidth(1)
hpt_photon_nmssm.Scale(1/hpt_photon_nmssm.GetEntries())
hpt_photon0.Scale(1/hpt_photon0.GetEntries())
hpt_photon2.Scale(1/hpt_photon2.GetEntries())
hpt_photon0.SetMaximum(1.2*hpt_photon0.GetMaximum())
hpt_photon0.Draw("hist")
hpt_photon_nmssm.Draw("hist&sames")
hpt_photon2.Draw("hist&sames")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
hpt_photon0.SetTitle("p_{T}(#gamma) [GeV] at M_{X}=300GeV")
c.SaveAs("photon_pt.root")

heta_photon0.SetLineColor(600)
heta_photon0.SetLineWidth(1)
heta_photon2.SetLineColor(418)
heta_photon2.SetLineWidth(1)
heta_photon_nmssm.SetLineColor(625)
heta_photon_nmssm.SetLineWidth(1)
heta_photon_nmssm.Scale(1/heta_photon_nmssm.GetEntries())
heta_photon0.Scale(1/heta_photon0.GetEntries())
heta_photon2.Scale(1/heta_photon2.GetEntries())
heta_photon_nmssm.SetMaximum(1.2*heta_photon_nmssm.GetMaximum())
heta_photon_nmssm.Draw("hist")
heta_photon0.Draw("hist&sames")
heta_photon2.Draw("hist&sames")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
heta_photon_nmssm.SetTitle("#eta(#gamma) at M_{X}=300GeV")
c.SaveAs("photon_eta.root")

hphi_photon0.SetLineColor(600)
hphi_photon0.SetLineWidth(1)
hphi_photon2.SetLineColor(418)
hphi_photon2.SetLineWidth(1)
hphi_photon_nmssm.SetLineColor(625)
hphi_photon_nmssm.SetLineWidth(1)
hphi_photon_nmssm.Scale(1/hphi_photon_nmssm.GetEntries())
hphi_photon0.Scale(1/hphi_photon0.GetEntries())
hphi_photon2.Scale(1/hphi_photon2.GetEntries())
hphi_photon_nmssm.SetMaximum(1.2*hphi_photon_nmssm.GetMaximum())
hphi_photon_nmssm.Draw("hist")
hphi_photon2.Draw("hist&same")
hphi_photon0.Draw("hist&same")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
hphi_photon_nmssm.SetTitle("#phi(#gamma) at M_{X}=300GeV")
c.SaveAs("photon_phi.root")

hpt_diphoton_nmssm.Scale(1/hpt_diphoton_nmssm.GetEntries())
hpt_diphoton0.Scale(1/hpt_diphoton0.GetEntries())
hpt_diphoton2.Scale(1/hpt_diphoton2.GetEntries())
hpt_diphoton0.SetLineColor(600)
hpt_diphoton0.SetLineWidth(1)
hpt_diphoton0.SetMaximum(1.2*hpt_diphoton2.GetMaximum())
hpt_diphoton0.Draw("hist")
hpt_diphoton2.SetLineColor(418)
hpt_diphoton2.SetLineWidth(1)
hpt_diphoton2.Draw("hist&same")
hpt_diphoton_nmssm.SetLineColor(625)
hpt_diphoton_nmssm.SetLineWidth(1)
hpt_diphoton_nmssm.Draw("hist&same")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
hpt_diphoton0.SetTitle("Diphoton p_{T}(#gamma #gamma) [GeV] at M_{X}=300GeV")
c.SaveAs("diphoton_pt.root")

heta_diphoton0.SetLineColor(600)
heta_diphoton0.SetLineWidth(1)
heta_diphoton2.SetLineColor(418)
heta_diphoton2.SetLineWidth(1)
heta_diphoton_nmssm.SetLineColor(625)
heta_diphoton_nmssm.SetLineWidth(1)
heta_diphoton_nmssm.Scale(1/heta_diphoton_nmssm.GetEntries())
heta_diphoton0.Scale(1/heta_diphoton0.GetEntries())
heta_diphoton2.Scale(1/heta_diphoton2.GetEntries())
heta_diphoton_nmssm.SetMaximum(1.2*heta_diphoton_nmssm.GetMaximum())
heta_diphoton_nmssm.Draw("hist")
heta_diphoton0.Draw("hist&same")
heta_diphoton2.Draw("hist&same")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
heta_diphoton_nmssm.SetTitle("#eta(#gamma #gamma) at M_{X}=300GeV")
c.SaveAs("diphoton_eta.root")

hphi_diphoton0.SetLineColor(600)
hphi_diphoton0.SetLineWidth(1)
hphi_diphoton2.SetLineColor(418)
hphi_diphoton2.SetLineWidth(1)
hphi_diphoton_nmssm.SetLineColor(625)
hphi_diphoton_nmssm.SetLineWidth(1)
hphi_diphoton_nmssm.Scale(1/hphi_diphoton_nmssm.GetEntries())
hphi_diphoton0.Scale(1/hphi_diphoton0.GetEntries())
hphi_diphoton2.Scale(1/hphi_diphoton2.GetEntries())
hphi_diphoton_nmssm.SetMaximum(1.2*hphi_diphoton_nmssm.GetMaximum())
hphi_diphoton_nmssm.Draw("hist")
hphi_diphoton0.Draw("hist&same")
hphi_diphoton2.Draw("hist&same")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
hphi_diphoton_nmssm.SetTitle("#phi(#gamma #gamma) [GeV] at M_{X}=300GeV")
c.SaveAs("diphoton_phi.root")

hm_diphoton0.SetLineColor(600)
hm_diphoton0.SetLineWidth(1)
hm_diphoton2.SetLineColor(418)
hm_diphoton2.SetLineWidth(1)
hm_diphoton_nmssm.SetLineColor(625)
hm_diphoton_nmssm.SetLineWidth(1)
hm_diphoton_nmssm.Scale(1/hm_diphoton_nmssm.GetEntries())
hm_diphoton0.Scale(1/hm_diphoton0.GetEntries())
hm_diphoton2.Scale(1/hm_diphoton2.GetEntries())
hm_diphoton_nmssm.SetMaximum(1.2*hm_diphoton_nmssm.GetMaximum())
hm_diphoton_nmssm.Draw("hist")
hm_diphoton0.Draw("hist&same")
hm_diphoton2.Draw("hist&same")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
hm_diphoton_nmssm.SetTitle("m(#gamma #gamma) [GeV] at M_{X}=300GeV")
c.SaveAs("diphoton_mass.root")

c.Update()
hpt_b0.SetLineColor(600)
hpt_b0.SetLineWidth(1)
hpt_b2.SetLineColor(418)
hpt_b2.SetLineWidth(1)
hpt_b_nmssm.SetLineColor(625)
hpt_b_nmssm.SetLineWidth(1)
hpt_b_nmssm.Scale(1/hpt_b_nmssm.GetEntries())
hpt_b0.Scale(1/hpt_b0.GetEntries())
hpt_b2.Scale(1/hpt_b2.GetEntries())
hpt_b0.SetMaximum(1.2*hpt_b0.GetMaximum())
hpt_b0.Draw("hist")
hpt_b_nmssm.Draw("hist&sames")
hpt_b2.Draw("hist&sames")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
hpt_b0.SetTitle("p_{T}(b) [GeV] at M_{X}=300GeV")
c.SaveAs("b_pt.root")

heta_b0.SetLineColor(600)
heta_b0.SetLineWidth(1)
heta_b2.SetLineColor(418)
heta_b2.SetLineWidth(1)
heta_b_nmssm.SetLineColor(625)
heta_b_nmssm.SetLineWidth(1)
heta_b_nmssm.Scale(1/heta_b_nmssm.GetEntries())
heta_b0.Scale(1/heta_b0.GetEntries())
heta_b2.Scale(1/heta_b2.GetEntries())
heta_b_nmssm.SetMaximum(1.2*heta_b_nmssm.GetMaximum())
heta_b_nmssm.Draw("hist")
heta_b0.Draw("hist&sames")
heta_b2.Draw("hist&sames")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
heta_b_nmssm.SetTitle("#eta(b) at M_{X}=300GeV")
c.SaveAs("b_eta.root")

hphi_b0.SetLineColor(600)
hphi_b0.SetLineWidth(1)
hphi_b2.SetLineColor(418)
hphi_b2.SetLineWidth(1)
hphi_b_nmssm.SetLineColor(625)
hphi_b_nmssm.SetLineWidth(1)
hphi_b_nmssm.Scale(1/hphi_b_nmssm.GetEntries())
hphi_b0.Scale(1/hphi_b0.GetEntries())
hphi_b2.Scale(1/hphi_b2.GetEntries())
hphi_b_nmssm.SetMaximum(1.2*hphi_b_nmssm.GetMaximum())
hphi_b_nmssm.Draw("hist")
hphi_b2.Draw("hist&same")
hphi_b0.Draw("hist&same")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
hphi_b_nmssm.SetTitle("#phi(b) at M_{X}=300GeV")
c.SaveAs("b_phi.root")

hpt_bb_nmssm.Scale(1/hpt_bb_nmssm.GetEntries())
hpt_bb0.Scale(1/hpt_bb0.GetEntries())
hpt_bb2.Scale(1/hpt_bb2.GetEntries())
hpt_bb0.SetLineColor(600)
hpt_bb0.SetLineWidth(1)
hpt_bb0.SetMaximum(1.2*hpt_bb2.GetMaximum())
hpt_bb0.Draw("hist")
hpt_bb2.SetLineColor(418)
hpt_bb2.SetLineWidth(1)
hpt_bb2.Draw("hist&same")
hpt_bb_nmssm.SetLineColor(625)
hpt_bb_nmssm.SetLineWidth(1)
hpt_bb_nmssm.Draw("hist&same")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
hpt_bb0.SetTitle("p_{t}(bb) [GeV] at M_{X}=300GeV")
c.SaveAs("bb_pt.root")

heta_bb0.SetLineColor(600)
heta_bb0.SetLineWidth(1)
heta_bb2.SetLineColor(418)
heta_bb2.SetLineWidth(1)
heta_bb_nmssm.SetLineColor(625)
heta_bb_nmssm.SetLineWidth(1)
heta_bb_nmssm.Scale(1/heta_bb_nmssm.GetEntries())
heta_bb0.Scale(1/heta_bb0.GetEntries())
heta_bb2.Scale(1/heta_bb2.GetEntries())
heta_bb_nmssm.SetMaximum(1.2*heta_bb_nmssm.GetMaximum())
heta_bb_nmssm.Draw("hist")
heta_bb0.Draw("hist&same")
heta_bb2.Draw("hist&same")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
heta_bb_nmssm.SetTitle("#eta(bb) at M_{X}=300GeV")
c.SaveAs("bb_eta.root")

hphi_bb0.SetLineColor(600)
hphi_bb0.SetLineWidth(1)
hphi_bb2.SetLineColor(418)
hphi_bb2.SetLineWidth(1)
hphi_bb_nmssm.SetLineColor(625)
hphi_bb_nmssm.SetLineWidth(1)
hphi_bb_nmssm.Scale(1/hphi_bb_nmssm.GetEntries())
hphi_bb0.Scale(1/hphi_bb0.GetEntries())
hphi_bb2.Scale(1/hphi_bb2.GetEntries())
hphi_bb_nmssm.SetMaximum(1.2*hphi_bb_nmssm.GetMaximum())
hphi_bb_nmssm.Draw("hist")
hphi_bb0.Draw("hist&same")
hphi_bb2.Draw("hist&same")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
hphi_bb_nmssm.SetTitle("#phi(bb) at M_{X}=300GeV")
c.SaveAs("bb_phi.root")

hm_bb0.SetLineColor(600)
hm_bb0.SetLineWidth(1)
hm_bb2.SetLineColor(418)
hm_bb2.SetLineWidth(1)
hm_bb_nmssm.SetLineColor(625)
hm_bb_nmssm.SetLineWidth(1)
hm_bb_nmssm.Scale(1/hm_bb_nmssm.GetEntries())
hm_bb0.Scale(1/hm_bb0.GetEntries())
hm_bb2.Scale(1/hm_bb2.GetEntries())
hm_bb_nmssm.SetMaximum(1.2*hm_bb_nmssm.GetMaximum())
hm_bb_nmssm.Draw("hist")
hm_bb0.Draw("hist&same")
hm_bb2.Draw("hist&same")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
hm_bb_nmssm.SetTitle("m(bb) [GeV] at M_{X}=300GeV")
c.SaveAs("bb_mass.root")

c.Update()
hpt_h0.SetLineColor(600)
hpt_h0.SetLineWidth(1)
hpt_h2.SetLineColor(418)
hpt_h2.SetLineWidth(1)
hpt_h_nmssm.SetLineColor(625)
hpt_h_nmssm.SetLineWidth(1)
hpt_h_nmssm.Scale(1/hpt_h_nmssm.GetEntries())
hpt_h0.Scale(1/hpt_h0.GetEntries())
hpt_h2.Scale(1/hpt_h2.GetEntries())
hpt_h0.SetMaximum(1.2*hpt_h0.GetMaximum())
hpt_h0.Draw("hist")
hpt_h_nmssm.Draw("hist&sames")
hpt_h2.Draw("hist&sames")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
hpt_h0.SetTitle("p_{T}(H) [GeV] at M_{X}=300GeV")
c.SaveAs("h_pt.root")

heta_h0.SetLineColor(600)
heta_h0.SetLineWidth(1)
heta_h2.SetLineColor(418)
heta_h2.SetLineWidth(1)
heta_h_nmssm.SetLineColor(625)
heta_h_nmssm.SetLineWidth(1)
heta_h_nmssm.Scale(1/heta_h_nmssm.GetEntries())
heta_h0.Scale(1/heta_h0.GetEntries())
heta_h2.Scale(1/heta_h2.GetEntries())
heta_h_nmssm.SetMaximum(1.2*heta_h_nmssm.GetMaximum())
heta_h_nmssm.Draw("hist")
heta_h0.Draw("hist&sames")
heta_h2.Draw("hist&sames")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
heta_h_nmssm.SetTitle("#eta(H) at M_{X}=300GeV")
c.SaveAs("h_eta.root")

hphi_h0.SetLineColor(600)
hphi_h0.SetLineWidth(1)
hphi_h2.SetLineColor(418)
hphi_h2.SetLineWidth(1)
hphi_h_nmssm.SetLineColor(625)
hphi_h_nmssm.SetLineWidth(1)
hphi_h_nmssm.Scale(1/hphi_h_nmssm.GetEntries())
hphi_h0.Scale(1/hphi_h0.GetEntries())
hphi_h2.Scale(1/hphi_h2.GetEntries())
hphi_h_nmssm.SetMaximum(1.2*hphi_h_nmssm.GetMaximum())
hphi_h_nmssm.Draw("hist")
hphi_h2.Draw("hist&same")
hphi_h0.Draw("hist&same")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
hphi_h_nmssm.SetTitle("#phi(H) at M_{X}=300GeV")
c.SaveAs("h_phi.root")

c.Update()
hpt_hh0.SetLineColor(600)
hpt_hh0.SetLineWidth(1)
hpt_hh2.SetLineColor(418)
hpt_hh2.SetLineWidth(1)
hpt_hy_nmssm.SetLineColor(625)
hpt_hy_nmssm.SetLineWidth(1)
hpt_hy_nmssm.Scale(1/hpt_hy_nmssm.GetEntries())
hpt_hh0.Scale(1/hpt_hh0.GetEntries())
hpt_hh2.Scale(1/hpt_hh2.GetEntries())
hpt_hh0.SetMaximum(1.2*hpt_hh0.GetMaximum())
hpt_hh0.Draw("hist")
hpt_hy_nmssm.Draw("hist&sames")
hpt_hh2.Draw("hist&sames")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
hpt_hh0.SetTitle("p_{T}(HH/HY) [GeV] at M_{X}=300GeV")
c.SaveAs("hy_pt.root")

heta_hh0.SetLineColor(600)
heta_hh0.SetLineWidth(1)
heta_hh2.SetLineColor(418)
heta_hh2.SetLineWidth(1)
heta_hy_nmssm.SetLineColor(625)
heta_hy_nmssm.SetLineWidth(1)
heta_hy_nmssm.Scale(1/heta_hy_nmssm.GetEntries())
heta_hh0.Scale(1/heta_hh0.GetEntries())
heta_hh2.Scale(1/heta_hh2.GetEntries())
heta_hy_nmssm.SetMaximum(1.2*heta_hy_nmssm.GetMaximum())
heta_hy_nmssm.Draw("hist")
heta_hh0.Draw("hist&sames")
heta_hh2.Draw("hist&sames")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
heta_hy_nmssm.SetTitle("#eta(HH/HY) at M_{X}=300GeV")
c.SaveAs("hy_eta.root")

hphi_hh0.SetLineColor(600)
hphi_hh0.SetLineWidth(1)
hphi_hh2.SetLineColor(418)
hphi_hh2.SetLineWidth(1)
hphi_hy_nmssm.SetLineColor(625)
hphi_hy_nmssm.SetLineWidth(1)
hphi_hy_nmssm.Scale(1/hphi_hy_nmssm.GetEntries())
hphi_hh0.Scale(1/hphi_hh0.GetEntries())
hphi_hh2.Scale(1/hphi_hh2.GetEntries())
hphi_hy_nmssm.SetMaximum(1.2*hphi_hy_nmssm.GetMaximum())
hphi_hy_nmssm.Draw("hist")
hphi_hh2.Draw("hist&same")
hphi_hh0.Draw("hist&same")
l=c.BuildLegend(0.75, 0.4, 0.9, 0.5)
hphi_hy_nmssm.SetTitle("#phi(HH/HY) at M_{X}=300GeV")
c.SaveAs("hy_phi.root")

f.Write()
