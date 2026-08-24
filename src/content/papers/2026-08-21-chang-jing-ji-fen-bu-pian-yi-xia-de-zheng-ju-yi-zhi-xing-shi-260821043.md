---
title: Evidence-Consistent Generative Detection under Scenario-Level Distribution
  Shift
title_zh: 场景级分布偏移下的证据一致性生成式检测方法
authors:
- San Kim
- JinYeong Bak
affiliations:
- Sungkyunkwan University
arxiv_id: '2608.21043'
url: https://arxiv.org/abs/2608.21043
pdf_url: https://arxiv.org/pdf/2608.21043
published: '2026-08-21'
collected: '2026-08-24'
category: Other
direction: OOD泛化 · 生成式检测
tags:
- OOD Generalization
- Generative Detection
- Evidence Supervision
- Consistency Regularization
- Fraud Detection
one_liner: 针对场景级OOD检测的场景记忆问题，提出ECoG框架提升生成式检测器跨未知场景的鲁棒性
practical_value: '- 电商恶意内容/欺诈交易/广告违规审核场景，可复用证据跨度监督+理据标签一致性正则，缓解黑产换话术/场景的OOD问题，提升模型鲁棒性

  - 所有生成式分类任务，可引入预测结果与生成理据的一致性校验，降低模型依赖表面特征过拟合的风险，提升未知场景下的准确率

  - 评估模型业务表现时，可构造场景级OOD测试集，避免分布内评估高估真实能力，更贴合黑产不断迭代变异的实际业务场景'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统分布内评估依赖任务特定表面特征易高估模型鲁棒性，社交工程欺诈场景下攻击者会更换场景、伪装实体或话术但保留恶意意图，模型易出现场景记忆，依赖特定场景的词汇/实体线索而非核心决策证据，未知攻击场景下性能暴跌。
### 方法关键点
提出ECoG证据一致性生成式框架，训练阶段同时引入**证据跨度监督**、**理据-标签一致性正则**两个约束，引导模型基于真正的决策证据输出判断，而非记忆表面场景特征。
### 关键结果
0.5B参数量解码器上，相比无一致性正则的同基线：
- OOD困难样本Macro-F1提升3.22个点
- 生成理据与预测标签相反的样本占比下降4.22个点
- 与参考证据跨度的token级重叠度提升8.38个点
上述理据与预测不一致性的优化效果在4个不同解码器backbone上均稳定生效。
