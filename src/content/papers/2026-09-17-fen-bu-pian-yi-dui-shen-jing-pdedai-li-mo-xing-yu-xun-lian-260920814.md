---
title: How Does Distribution Shift Shape Pretraining Gains in Neural PDE Surrogates?
title_zh: 分布偏移对神经PDE代理模型预训练增益的影响机制研究
authors:
- Pochinapeddi Sai Bhargav
- Nithin Somasekharan
- Rohit Sunil Kanchi
- Sicheng He
- Shaowu Pan
affiliations:
- Rensselaer Polytechnic Institute
- University of Tennessee
arxiv_id: '2609.20814'
url: https://arxiv.org/abs/2609.20814
pdf_url: https://arxiv.org/pdf/2609.20814
published: '2026-09-17'
collected: '2026-09-20'
category: Other
direction: 神经PDE代理 · 预训练分布偏移研究
tags:
- PDE Surrogate
- Distribution Shift
- Pretraining
- Fine-tuning
- CFD
one_liner: 量化分布偏移维度、下游数据预算等因素对神经PDE代理预训练增益的影响规律
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 3
source: arxiv-cs.LG
depth: abstract
---

### 动机
神经PDE代理预训练可降低下游新场景CFD数据需求，但分布偏移不同组分对预训练收益的影响机制尚不明确。
### 方法关键点
基于单翼型族254909个RANS解预训练代理模型，在来流范围匹配的两个下游目标场景微调：相同SA湍流模型、SA加$e^N$转捩模型的新翼型族场景，对比不同下游数据量下预训练效果。
### 关键结果数字
- 下游数据量为1000时，预训练模型在同SA场景等效于3.25倍数据量的从零训练模型，转捩模型场景等效倍数为2.58；数据量为5000时规律反转，对应倍数分别为1.56、1.86。
- 1000样本下采样更多不同翼型可降低双场景误差，仅同SA场景增益高于随机波动（3.3倍升至4.0倍）。
- 预训练价值由下游数据预算、覆盖度、源目标物理建模是否一致共同决定。
