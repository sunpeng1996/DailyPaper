---
title: 'Everything in Moderation: Per-Domain Coverage Optima and Alignment-Resistant
  Domain Gaps in Multi-Domain Mid-Training'
title_zh: 多域中间训练的单域覆盖率最优值与对齐无法消除的域差距
authors:
- Yunpeng Xu
- Kun Zheng
arxiv_id: '2609.09081'
url: https://arxiv.org/abs/2609.09081
pdf_url: https://arxiv.org/pdf/2609.09081
published: '2026-09-08'
collected: '2026-09-09'
category: Training
direction: LLM多域中间训练数据分配优化
tags:
- Mid-Training
- Data Mixture
- Domain Alignment
- SFT
- LLM Training
one_liner: 通过受控实验证明多域中间训练单域最优覆盖率为10-40%，固定预算对齐无法消除其带来的域差距
practical_value: '- 电商/广告多域中间训练阶段可将单域数据占比控制在10-40%区间，避免过高/过低占比导致的域效果下降

  - 不要寄希望于后续SFT/RL对齐修复中间训练的域配比失衡问题，需在中间训练阶段前置优化域数据配比

  - 若需提升特定域效果，优先调整中间训练的该域数据占比，固定预算下仅增加后续对齐阶段的该域权重几乎无法消弭域差距'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM多阶段训练范式中，介于预训练与对齐之间的中间训练（mid-training）的域数据配比通常由数据可得性而非原则化设计决定，行业普遍默认后续SFT/RL对齐可修复中间训练的域分配偏差，但该假设从未经过系统验证，且现有数据混合优化方法仅面向整体困惑度优化，未揭示单域效果随覆盖率变化的规律。
### 方法关键点
- 以Qwen3-8B-Base为基础模型，基于语义规则完全不相交的KOR-Bench 5个逻辑推理域开展受控实验，中间训练总token预算固定为1.5B，后续SFT/RL流程完全固定；
- 设计24组覆盖五域配比单纯形的实验组+6组预留验证组，每组5个随机种子，对比失衡配比、等比例配比、拟合最优区间得到的探索性θ*配比三类配置；
- 增设补偿性SFT（向低覆盖率域倾斜数据）、均匀SFT两组对照，测试域间隙的可修复性。
### 关键结果数字
- 5个域的覆盖率-准确率均呈倒U型，最优占比落在10-40%的中等区间（P≈0.01），单域拟合峰值在9.9%-35.1%之间；
- 固定预算补偿性SFT平均提升准确率4.32pp，但5pp差距阈值下0/240个域对的间隙被完全弥合，10%比例阈值下仅30/240个被弥合，与均匀SFT效果无显著差异；
- 最优θ*配比全流程效果比无中间训练的SFT+RL基线高4.36pp，比等比例配比高3.56pp。

最值得记住的结论：多域中间训练的域数据配比是后续对齐阶段无法修复的前置约束，单域中等占比的效果远好于极端占比。
