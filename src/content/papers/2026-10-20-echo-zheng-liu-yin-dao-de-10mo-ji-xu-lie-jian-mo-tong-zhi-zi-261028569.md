---
title: 'ECHO: Efficient Cascade with Homogeneous Operators for Distillation-Guided
  100K-Sequence Modeling'
title_zh: ECHO：蒸馏引导的10万级序列建模同质算子高效级联框架
authors:
- Wenhao Li
- Qinglin Jia
- Chenghou Jin
- Zihong Xian
- Jiezhou Ji
- Yanzhi Liu
- Zezheng Wang
- Ruiming Tang
- Chaoyi Ma
- Zhaojie Liu
affiliations:
- Kuaishou Technology
arxiv_id: '2610.28569'
url: https://arxiv.org/abs/2610.28569
pdf_url: https://arxiv.org/pdf/2610.28569
published: '2026-10-20'
collected: '2026-10-21'
category: RecSys
direction: 推荐系统 · 10万级超长行为序列建模
tags:
- Long-Sequence Modeling
- Knowledge Distillation
- CTR Prediction
- Efficient Recommendation
- User Behavior Modeling
one_liner: 采用级联蒸馏选择+目标感知检索实现10万级用户序列高效建模降本提效
practical_value: '- 架构可直接复用：采用"用户级预筛选+候选级细检索"的两级级联范式，先离线/实时预蒸馏出K条原始行为记录跨请求复用，在线仅需对K条做候选感知计算，可直接把超长序列建模的在线成本从O(L)降到O(K)，L为原始序列长度

  - 蒸馏trick可迁移：蒸馏监督除了常规分布匹配，新增边界辅助loss，强制老师模型高relevance的行为尽可能落在预筛选集合里，解决用户级无候选感知选择的信息损失问题，可复用至所有预筛选类长序列方案

  - 工程优化直接落地：三个部署优化可直接照搬：同用户样本批次共享特征降低GPU显存占用、紧凑编码存储预筛选记录降存储成本、key侧投影吸收省去投影key缓存，实测单用户存储降33%，在线计算进一步优化

  - 收益可预期：在已经用了TWIN、SequenceO1等成熟长序列方案的生产基线之上，仍能拿到0.1%+的GAUC提升和0.6%+的APP使用时长提升，对活跃用户占比高的内容/电商推荐场景落地价值明确'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐场景中10万级超长用户行为序列可捕捉长期稳定偏好、周期性兴趣和长尾需求，但现有方案存在明显缺陷：检索类方法需为每个候选扫描全量序列，计算成本随序列长度线性增长；压缩类方法将行为聚合为隐向量，丢失原始行为的可寻址性，无法支撑细粒度目标匹配和可解释性溯源，急需兼顾效果、效率和可解释性的方案。
### 方法关键点
- 两级级联架构：首先由仅依赖用户特征的Distilled Selector（DS）从全量10万条序列中筛选出1万条原始行为记录，保留item ID、侧特征、时间戳全部信息，预存后跨请求、跨候选复用；再由Target-aware Fine-grained Retriever（TFR）针对每个候选从1万条中检索100条做目标感知注意力聚合，在线计算完全与原始序列长度解耦。
- 蒸馏对齐策略：用全量历史训练的候选感知老师模型做监督，除匹配soft relevance分布外，新增边界辅助loss，强制老师高评分的行为尽量落入DS的选择集，解决用户级预筛选无候选感知的偏差问题。
- 全链路参数共享：TFR和后续的目标注意力打分模块共享老师模型的Q/K相关性参数，保证级联各阶段的相关性判断一致，减少级联带来的信息损失。
### 关键实验
在KuaiRand-1K公开数据集和快手4亿DAU的工业短视频数据集上，对比DIN、SIM、TWIN、SequenceO1等SOTA基线，8个预测任务GAUC相对提升0.113%~1.520%；10万序列长度下在线序列分支FLOPs相比端到端模型降低160倍；线上A/B测试相比成熟生产基线，APP总使用时长提升0.613%。
### 核心结论
超长序列建模的核心是平衡候选相关精细匹配成本与原始行为可寻址性，通过蒸馏预筛选+参数对齐可在几乎不损失效果的前提下将在线计算量降低两个数量级。
