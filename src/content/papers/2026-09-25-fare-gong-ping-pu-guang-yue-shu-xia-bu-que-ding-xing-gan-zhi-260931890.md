---
title: 'FARE: Deep Reinforcement Learning For Fair Exposure Constrained Uncertainty
  Aware Financial Content Personalization'
title_zh: FARE：公平曝光约束下不确定性感知的金融内容个性化重排框架
authors:
- Arundeep Chinta
- Lucas Vinh Tran
- Jay Katukuri
affiliations:
- JPMorgan Chase
arxiv_id: '2609.31890'
url: https://arxiv.org/abs/2609.31890
pdf_url: https://arxiv.org/pdf/2609.31890
published: '2026-09-25'
collected: '2026-09-29'
category: RecSys
direction: 推荐系统公平重排 · 不确定性感知
tags:
- Re-ranking
- Fairness
- Uncertainty-Aware
- Reinforcement Learning
- SOV Constraint
one_liner: 提出无需重训CTR的可插拔不确定性感知重排框架，低损耗满足公平曝光SOV约束
practical_value: '- 可直接复用FARE的可插拔架构，在现有CTR模型下游叠加公平约束层，无需重训上游模型，快速满足业务的商家曝光配额、品类均衡等需求，上线成本极低

  - 直接套用不确定性加权调整trick：对CTR预测不确定性越高的item，公平干预的调整幅度越大，可大幅降低公平约束带来的点击损失，尤其适合新品扶持、中小商家流量倾斜场景

  - 部署选型参考：单公平目标优先选FARE-PC，O(K)推理时延仅需调增益α参数；多目标（公平+多样性等）场景选FARE-ES，稳定性显著优于PPO类策略'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统CTR最优排序易引发「富者越富」马太效应，高CTR内容占据绝大多数曝光，既无法满足业务侧品类/商家公平曝光的合约要求，也不利于用户发现多元内容、挖掘长期价值；现有公平重排方法要么忽略CTR预测不确定性，导致公平干预带来过高点击损失，要么需要重训整个CTR模型，上线成本极高。
### 方法关键点
- 借鉴算法交易的信号-执行解耦架构，FARE作为独立执行层部署在任意黑盒CTR模型下游，仅调整CTR预测均值，不修改预测方差也无需重训上游模型
- 设计三类执行策略：无训练的不确定性加权比例控制器FARE-PC、免梯度学习的进化策略FARE-ES、梯度优化的PPO策略FARE-PPO
- 核心设计：对SOV曝光缺口越大、CTR预测不确定性越高的内容施加更大的排序分数调整，优先在预测置信度低的场景做公平干预，最大化降低点击损耗
### 关键结果
在合成数据和公开KuaiRand-Pure数据集上对比CTR-Only、硬配额Quota-CTR等基线：FARE-PC在合成数据实现90.3%的SOV误差降低，仅带来2.64%的点击损失；在KuaiRand-Pure数据集实现91.8%的SOV误差降低，点击损失仅0.19%，性能显著优于所有基线和学习类策略。
最值得记住的结论：公平干预优先对模型不确定的预测做调整，能以极低的业务损耗满足曝光约束，且可插拔架构的上线成本远低于修改CTR模型损失的方案
