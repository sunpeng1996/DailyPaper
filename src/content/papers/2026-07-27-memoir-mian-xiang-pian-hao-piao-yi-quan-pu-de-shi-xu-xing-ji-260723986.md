---
title: 'MEMOIR: Temporal Behavioral Memory for Recommendation Across the Preference-Drift
  Spectrum'
title_zh: MEMOIR：面向偏好漂移全谱的时序行为记忆推荐框架
authors:
- Younggue Bae
affiliations:
- Independent Researcher, Vancouver, Canada
arxiv_id: '2607.23986'
url: https://arxiv.org/abs/2607.23986
pdf_url: https://arxiv.org/pdf/2607.23986
published: '2026-07-27'
collected: '2026-07-28'
category: RecSys
direction: 时序推荐 · 用户偏好漂移建模
tags:
- Sequential Recommendation
- Preference Drift
- Contrastive Learning
- LLM
- User Modeling
one_liner: 将用户交互历史按时段编码建模偏好演化轨迹，在高低偏好漂移用户上排序性能更优
practical_value: '- 对用户分偏好漂移层级优化策略：高低漂移用户优先用MEMOIR类演化建模方案提升排序精度，中漂移用户用UniSRec类方案兼顾召回广度，适配电商新用户冷启动、品类跃迁运营等场景

  - 语义特征对齐trick：引入behavioral consistency loss锚定LLM生成的用户语义表征和item embedding空间，避免纯语义特征与行为协同信号错位导致的效果下降

  - 工程优化方案：可预计算冻结LLM的时序窗口embedding并缓存，仅训练轻量聚合层，推理时延与ID基线相当，可直接嵌入现有推荐召回/粗排链路

  - 偏好漂移分层评估方法：可复用文中的分类JSD、评分方差、新颖率三维漂移分群方法，定位不同用户群的效果短板，避免全局指标掩盖分层效果差异'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有时序推荐和LLM增强推荐要么将用户偏好视为静态表征，要么仅把LLM作为离线预处理辅助工具，未对偏好演化轨迹做一阶建模；实测Amazon平台92.2%的用户月度交互物品均为全新物品，偏好漂移是普遍现象，静态表征无法区分相同当前偏好但演化路径完全不同的用户，导致极端漂移用户的推荐效果劣化。

### 方法关键点
- 时序切分：将用户交互历史按自然月拆分为多个窗口，每个窗口序列化为自然语言行为描述，用LoRA微调的TinyLlama编码为语义记忆embedding
- 演化保留对比损失：包含时序平滑项（相邻窗口为正对的InfoNCE损失）和方向一致性项（约束连续演化方向向量的余弦相似度高于阈值），学习偏好演化规律
- 演化感知聚合：用GRU建模记忆序列预测下一个窗口的embedding，融合当前状态（近期窗口加权平均）、演化方向、预测未来三个信号生成最终用户表征
- 一致性正则：加入行为一致性损失，锚定用户表征和目标item embedding空间，避免语义空间与行为空间错位

### 关键实验
在Amazon Reviews 2023的Electronics、服饰鞋包两个类目上测试，对比SASRec、UniSRec等7个基线，全局NDCG@10为0.0643与最强基线UniSRec（0.0641）统计持平，相对ID基线SASRec提升18%；分层来看，高/低偏好漂移用户的NDCG@10、MRR显著优于UniSRec，中漂移用户和召回类指标HR@10/20弱于UniSRec。

### 核心结论
LLM在推荐中的收益不是自动的，必须有明确的机制对齐语义空间和行为协同信号，且偏好演化建模的收益集中在高低漂移的极端用户群，而非全局普适。
