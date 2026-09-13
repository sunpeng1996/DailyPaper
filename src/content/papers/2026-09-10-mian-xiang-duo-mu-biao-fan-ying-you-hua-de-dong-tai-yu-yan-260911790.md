---
title: Dynamic language model representations for multi-objective reaction optimisation
title_zh: 面向多目标反应优化的动态语言模型表示方法
authors:
- Joshua W. Sin
- David Ming Segura
- Bojana Ranković
- Siu Lun Chau
- Marius D. R. Lutz
- Andrea Anelli
- Ryan P. Burwood
- Kurt Püntener
- Maximilian J. Notheis
- Raphael Bigler
affiliations:
- F. Hoffmann-La Roche AG, Basel, Switzerland
- EPFL, Lausanne, Switzerland
- National Centre of Competence in Research (NCCR) Catalysis, EPFL
- Nanyang Technological University, Singapore
arxiv_id: '2609.11790'
url: https://arxiv.org/abs/2609.11790
pdf_url: https://arxiv.org/pdf/2609.11790
published: '2026-09-10'
collected: '2026-09-13'
category: Other
direction: 跨领域多目标优化 · 自适应文本表示学习
tags:
- Representation Learning
- Multi-Objective Optimization
- LM Fine-tuning
- Bayesian Optimization
one_liner: 微调LM与高斯过程联合学习文本动态反应表示，降低多目标反应优化所需实验次数
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 3
source: arxiv-cs.LG
depth: abstract
---

### 动机
化学多目标反应优化（产率、选择性、安全性等）高度依赖反应组分的表示设计，现有表示方法要么信息密度低（如one-hot编码），要么无法跨不同化学组分复用，手动构建适配新反应体系的共享特征成本极高，需针对每个新反应重新设计。

### 方法关键点
1. 跳过手动特征工程步骤，直接从反应条件的文本描述端到端学习动态表示
2. 微调LM与高斯过程代理模型联合训练，在多目标贝叶斯优化循环内生成任务自适应表示。

### 关键结果数字
- 镍、钯催化交叉偶联实验中，收敛所需实验次数显著少于传统描述符库/one-hot编码方法
- 钯催化氰化、不对称氢化两个前瞻性实验中，仅需2轮高通量实验（共192次，占设计空间不足3%），分别实现94%、84%的克级分离产率，后者对映体过量达99.6%
