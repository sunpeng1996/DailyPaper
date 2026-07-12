---
title: Federated Deep Learning for Privacy-Preserving Cardiovascular Disease Risk
  Prediction
title_zh: 面向隐私保护的心血管疾病风险预测联邦深度学习方法
authors:
- Hyunho Mo
- Djura Smits
- Mahlet A. Birhanu
- Maarten J. G. Leening
- Daniel Bos
- Pim van der Harst
- Esther E. Bron
affiliations:
- Erasmus MC University Medical Center Rotterdam
- Netherlands eScience Center
- University Medical Center Utrecht
arxiv_id: '2607.08595'
url: https://arxiv.org/abs/2607.08595
pdf_url: https://arxiv.org/pdf/2607.08595
published: '2026-07-09'
collected: '2026-07-12'
category: Other
direction: 联邦学习 · 隐私保护风险预测
tags:
- Federated Learning
- Privacy Preserving
- Deep Survival Model
- Heterogeneous Data
- Risk Prediction
one_liner: 提出跨异质人群队列的联邦深度学习方案，在保护患者隐私的同时提升心血管疾病风险预测性能
practical_value: '- 跨商家/跨业务域的用户建模可参考该联邦学习范式，规避用户隐私数据传输的合规风险

  - 异质数据联邦训练可借鉴其参数聚合逻辑，平衡不同量级、不同特征分布数据集的贡献

  - 跨域联合训练的效果评估可复用其分域验证思路，优先在高数据质量的目标域验证核心效果'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统疾病风险预测模型依赖单机构/中心化数据集，跨机构协作受隐私合规限制，且联邦学习落地面临数据异质性、结局定义差异等问题。
### 方法关键点
采用联邦深度学习框架训练深度生存模型，融合两个特征差异显著的人群队列（14.8万自报结局的Lifelines队列、1万临床结局的Rotterdam队列），无需传输原始用户数据即可完成联合训练。
### 关键结果
在随访质量更高的Rotterdam队列上C统计量从0.728提升至0.739，Lifelines队列从0.783提升至0.787，效果均优于单机构本地训练的模型，且全程保护用户个体数据隐私。
