---
title: Contribution-Aware Bandwidth Allocation for Multimodal Split Learning
title_zh: 面向多模态拆分学习的贡献感知带宽分配方法
authors:
- Iason Ofeidis
- Leandros Tassiulas
affiliations:
- Yale University
arxiv_id: '2609.01406'
url: https://arxiv.org/abs/2609.01406
pdf_url: https://arxiv.org/pdf/2609.01406
published: '2026-09-01'
collected: '2026-09-03'
category: Training
direction: 多模态拆分学习 · 通信效率优化
tags:
- Split Learning
- Multimodal
- Shapley Value
- Bandwidth Allocation
- Edge Computing
one_liner: 提出基于Shapley贡献值的多模态拆分学习带宽分配器ModalShare，等传输载荷下显著提升模型精度
practical_value: '- 多模态召回/排序任务可复用Shapley值量化各模态贡献，动态分配特征传输、存储、计算预算，无需人工预设模态权重

  - 端云协同的多模态Agent推理/训练场景，可借鉴模态间资源分配逻辑，在固定带宽/算力约束下提升整体效果

  - 边缘侧多模态数据处理pipeline可集成该无额外开销的贡献评估方法，自动适配不同模态组合的资源需求'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
多模态模型边缘训练受端侧算力限制无法部署全量编码器，拆分学习将浅层放端侧、深层放云端实现可行训练，但现有压缩方案按模态激活维度均分上行带宽，未关联各模态对最终预测的贡献，资源分配效率极低。
### 方法关键点
提出模态间显式带宽分配器ModalShare，由云端基于已接收的多模态激活集合计算各模态的Shapley贡献分，动态设置各模态激活的保留率；该过程无额外上行流量开销、无需端侧新增计算、无需模态属性先验知识。
### 关键结果
5倍压缩、相同传输载荷下，在CREMA-D、MVSA数据集上精度比等保留率方案分别高15.4、12.4个百分点，适配3种压缩器、3个数据集、4种带宽预算，可补全现有压缩方案在多模态场景的效果损失。
