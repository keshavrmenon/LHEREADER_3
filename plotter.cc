#include<TH1.h>
#include<TFile.h>
#include<TLatex.h>
#include<TLegend.h>
#include<stdio.h>

void plotter(){
  char s[50]="eta_photon";
  char s1[50];
  strcpy(s1,s);
  TFile *f1 = new TFile("basic_kin_m300.root");
  //TFile *f2 = new TFile("basic_kin_m600.root");
  //TFile *f3 = new TFile("basic_kin_m900.root");
  
  TH1F *h1 = (TH1F*) f1->Get(strcat(s,"_nmssm"));
  strcpy(s,s1);
  TH1F *h2 = (TH1F*) f1->Get(strcat(s,"_radion"));
  strcpy(s,s1);
  TH1F *h3 = (TH1F*) f1->Get(strcat(s,"_graviton"));
  strcpy(s,s1);
  TH1F *h4 = (TH1F*) f1->Get(strcat(s,"_sm"));
  h1->SetTitle("NMSSM");
  h2->SetTitle("Radion");
  h3->SetTitle("Graviton");
  h4->SetTitle("SM");
  
  TCanvas *c = new TCanvas();
  TLegend *l;

  h1->SetLineColor(600);
  h2->SetLineColor(418);
  h3->SetLineColor(625);
  h4->SetLineColor(800);
  h1->SetLineWidth(1);
  h2->SetLineWidth(1);
  h3->SetLineWidth(1);
  h4->SetLineWidth(1);
  h1->Scale(1/(h1->GetEntries()));
  h2->Scale(1/(h2->GetEntries()));
  h3->Scale(1/(h3->GetEntries()));
  h4->Scale(1/(h4->GetEntries()));
  h1->SetMaximum(1.2*h4->GetMaximum());
  h1->Draw("hist");
  h2->Draw("hist&same");
  h3->Draw("hist&same");
  h4->Draw("hist&same");
  l=c->BuildLegend(0.75, 0.4, 0.9, 0.5);
}
