---
title: The Price of Scale in Proactive Memory Recall
title_zh: 主动记忆召回的规模代价
authors:
- Yichuan Chen
- Xin Wang
affiliations:
- Zhejiang Sci-Tech University
arxiv_id: '2610.34507'
url: https://arxiv.org/abs/2610.34507
pdf_url: https://arxiv.org/pdf/2610.34507
published: '2026-10-25'
collected: '2026-10-27'
category: Agent
direction: Agent 长时记忆主动召回优化
tags:
- Proactive_Memory_Recall
- Conformal_Prediction
- LLM_Agent
- Memory_Gating
- Long_Term_Memory
one_liner: 揭示主动记忆召回误报率随记忆库规模上升的规律，提出无标注cue-swap共形门控实现有限样本误报率保证
practical_value: '- 做Agent长时主动召回/电商用户记忆主动触达时，不能用固定阈值：语义embedding阈值按√lnN调整，lexical得分阈值按lnN调整，可大幅降低大库下的误报率

  - 相似度得分做per-cue归一化，可在相同误报率下将hit率提升近1倍，该trick可直接复用到推荐召回相似度截断、RAG检索阈值设置场景

  - 可复用cue-swap共形门控设计，用用户同来源历史cue作为参考集做无标注阈值校准，不需要标注数据即可将误报率控制在预设水平，适合落地

  - 长周期主动召回场景下，优先提升embedding区分度、增加LLM对topK候选的二次校验，收益远高于单纯扩大记忆库规模'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前长周期LLM Agent的主动记忆召回缺少规模适应性，固定阈值在记忆库从8增长到2048时误报率会从5%飙升到87%-100%，频繁打扰用户，且此前没有可落地的有限样本误报率控制方案。
### 方法关键点
- 将主动召回决策建模为多重假设检验问题，证明固定误报率α下，单样本误报率约为$-\ln(1-\alpha)/N$，hit率随$N$呈幂律衰减
- 区分语义/lexical两个通道的得分分布规律，分别匹配$\sqrt{\ln N}$、$\ln N$的阈值增长曲线
- 提出cue-swap共形门控，用用户同来源历史cue的得分做参考集计算p值，无需标注即可保证有限样本下的误报率不超过预设值
### 关键结果
在LongMemEval、LoCoMo数据集上测试，对比固定cosine阈值、固定tf-idf阈值、z-score门控等baseline：
- 固定阈值在$N=2048$时误报率达87%-100%，cue-swap门控始终将误报率控制在2.8%-5.9%，hit率和有标注调优的z-score门控差距在3个百分点以内
- per-cue归一化可在相同误报率下将hit率提升近1倍
- $N=2048$时，14B LLM对top5候选做二次校验可将hit率提升到28%，误报率仅4%

> 最值得记住的结论：主动记忆召回的可用规模上限由得分的区分度决定，提升embedding质量、引入候选二次校验比单纯扩大记忆库的收益高得多
