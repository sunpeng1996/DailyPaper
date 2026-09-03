---
title: 'GenCAR: Generative Counterfactual Alignment with Risk-Controlled Selection
  for Out-of-Distribution Recommendation'
title_zh: 面向分布外推荐的生成式反事实对齐与风险控制框架GenCAR
authors:
- Qianqian Wang
- Yunshan Li
- Jiawen Zeng
- Wenwu Gong
- Lili Yang
affiliations:
- Southern University of Science and Technology
- University of Pennsylvania
arxiv_id: '2609.02162'
url: https://arxiv.org/abs/2609.02162
pdf_url: https://arxiv.org/pdf/2609.02162
published: '2026-09-02'
collected: '2026-09-03'
category: RecSys
direction: 分布外推荐 · 反事实对齐风险控制
tags:
- OOD-Recommendation
- Counterfactual-Reasoning
- Conformal-Prediction
- FDR-Control
- LLM4Rec
one_liner: 结合LLM离线反事实监督与共形选择，实现分布外推荐下FDR可控的候选召回
practical_value: '- 离线LLM生成反事实训练样本的范式可复用：固定用户稳定偏好表示、干预环境因子，再通过偏好锚点+信任半径过滤无效生成样本，大幅降低LLM生成噪声对排序模型的负面影响

  - 共形预测+BH/BY选择的风险控制方案可直接迁移到推荐bad case管控场景：通过离线校准集计算conformal p值，可在无需在线LLM的前提下，将推荐池的错配FDR控制在预设阈值α内

  - 线上完全卸载LLM的架构适配高吞吐推荐场景：所有LLM调用、标注都放在离线阶段，线上仅需常规embedding匹配+轻量校准计算，Coat数据集上单用户推理延迟<1ms，远低于在线LLM
  rerank的5.4s'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有分布外（OOD）推荐方法大多仅优化排序效果或生成反事实候选，无法控制服务集的代理标签错误发现率（FDR），盲目扩大候选池提升召回的同时会引入大量低质量内容，无法平衡效用和风险。

### 方法关键点
- 两阶段无在线LLM架构：离线完成所有LLM调用、样本构造和校准，线上仅用训练好的排序模型和校准规则
- 偏好锚定的反事实样本生成：固定用户稳定偏好表示$z_c$，干预环境因子$z_e$，将$z_c$映射为TopK偏好锚点物品喂给LLM生成候选，再通过与$z_c$的余弦距离阈值（信任半径）过滤无效样本，用有效样本微调排序模型的item embedding
- FDR可控的候选选择：用离线LLM输出的对齐分数作为代理标签训练对齐预测器，基于独立校准集的代理负样本计算每个候选的conformal p值，采用BH/BY算法选择候选集，保证整体FDR低于预设α

### 关键实验
在MovieLens-100K（时间偏移）、Coat（曝光偏移）、Amazon-Book（流行度偏移）三个基准数据集上对比IPS-CN、DICE、InvCF等OOD推荐基线，以及在线LLM rerank的TallRec：
- 相对CausalVAE基线，Recall@10分别提升11.0%、19.1%、43.5%
- 在α=0.3的预设FDR阈值下，所有测试集的实际FDP均低于0.2，满足风险控制要求
- 线上单用户推理延迟<1ms，仅为在线LLM rerank方案的1/5400

最值得记住的一句话：离线LLM生成反事实监督+轻量共形风险控制的范式，可在完全不增加线上推理负担的前提下，同时提升OOD推荐效果和风险可控性
