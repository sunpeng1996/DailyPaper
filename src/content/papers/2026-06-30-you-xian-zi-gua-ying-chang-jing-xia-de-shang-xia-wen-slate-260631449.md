---
title: Contextual Slate GLM Bandits with Limited Adaptivity
title_zh: 有限自适应场景下的上下文Slate GLM赌博机算法
authors:
- Tanmay Goyal
- Sukruta Prakash Midigeshi
- Gaurav Sinha
affiliations:
- Microsoft Research India
arxiv_id: '2606.31449'
url: https://arxiv.org/abs/2606.31449
pdf_url: https://arxiv.org/pdf/2606.31449
published: '2026-06-30'
collected: '2026-07-01'
category: RecSys
direction: 推荐系统 · 低开销在线探索算法
tags:
- Slate Bandit
- Online Learning
- GLM
- Limited Adaptivity
- Recommendation
one_liner: 提出两种低更新频次的slate GLM bandit算法，有限自适应约束下接近全自适应SOTA性能
practical_value: '- 电商广告创意组合、landing page组件优化等slate类决策场景，可直接复用B-SlateGLinCB的O(log
  log T)批次更新架构，大幅降低线上模型更新频次和运维成本，同时保持探索效果接近全自适应算法。

  - LLM in-context exemplar选择、Agent工具链组合等多slot决策任务，可直接复用B-SlateGLinCB+的批次探索方案，仅需极少参数更新即可达到和全自适应算法相当的效果，适合高并发线上场景。

  - 落地GLM类bandit时，可复用论文提出的scaling-slate设计消除非线性参数κ对regret的影响，避免高非线性场景下探索效果大幅下降。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有全自适应slate GLM bandit算法需要每轮更新参数，无法适配Web级推荐、广告场景对低更新频次、高并发、可并行的要求；而现有有限自适应bandit算法无法直接扩展到组合空间极大的slate决策场景，且regret常受GLM非线性参数κ的制约导致性能不稳定。

### 方法关键点
- 提出两种有限自适应算法：批次版B-SlateGLinCB将时间窗划分为O(log log T)个批次，每批次仅用前序批次数据更新策略，支持批次内请求全并行；少切换版RS-SlateGLinCB通过行列式阈值自适应触发更新，总更新次数仅O(Nd log T)。
- 核心优化：通过slot级独立选品+G最优设计采样，将per轮复杂度从指数级降到poly(N)，解决slate组合爆炸问题；引入scaling-slate构造缩放设计矩阵，消除regret上界对GLM非线性参数κ的依赖。
- 提出改进版B-SlateGLinCB+，简化多轮剪枝逻辑，大幅降低推理耗时的同时进一步提升效果。

### 关键实验
合成实验在2组不同κ、slate规模的配置下，两种算法均大幅超过SoftBatch、RS-GLinCB等有限自适应基线，RS-SlateGLinCB和全自适应SOTA Slate-GLM-OFU的regret差距小于15%，B-SlateGLinCB+的regret几乎和SOTA持平；真实场景实验用SST-2数据集做LLM in-context exemplar选择，B-SlateGLinCB+仅O(log log T)次更新，准确率和全自适应SOTA相当，比随机选样例高12%以上。

有限自适应slate bandit算法可在仅损失极少探索效果的前提下，大幅降低线上运维开销，完全满足Web级业务的性能要求。
