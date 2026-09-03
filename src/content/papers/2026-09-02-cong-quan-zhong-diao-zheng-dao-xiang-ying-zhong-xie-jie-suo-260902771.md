---
title: 'From Reweighting to Rewriting: Unlocking the Intervention Effects of Influential
  Samples in Training Data Attribution'
title_zh: 从权重调整到响应重写：解锁训练数据归因中高影响样本的干预价值
authors:
- Yuzhang Luo
- Chenpeng Wang
- Jianhui Chen
- Liangming Pan
affiliations:
- Peking University
- YiXin-AILab
- Beijing Academy of Artificial Intelligence
arxiv_id: '2609.02771'
url: https://arxiv.org/abs/2609.02771
pdf_url: https://arxiv.org/pdf/2609.02771
published: '2026-09-02'
collected: '2026-09-03'
category: Training
direction: LLM SFT干预 · 训练数据归因
tags:
- Training Data Attribution
- Influence Functions
- Supervised Fine-Tuning
- Response Rewriting
- LLM Alignment
one_liner: 提出影响力引导的响应重写框架，挖掘高影响训练样本隐藏的行为干预价值
practical_value: '- 做垂直场景LLM对齐（如电商客服合规拒答、导购话术规范）时，可先用IF筛选2.5%左右的高影响SFT样本，仅重写其响应，干预效果远优于传统的样本加权/删除操作，大幅降低对齐成本

  - 做Agent行为管控时，用IF筛选与目标行为（如不泄露隐私、不虚假宣传）关联度最高的样本重写，比随机挑选样本重写的干预效果高60%以上，且不会造成模型通用能力的大面积退化

  - 过往用IF做数据筛选、重加权效果不稳定的场景，可直接替换为响应重写方案，解决传统IF干预效果弱、方向不可控的问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统基于Influence Functions（IF）的训练数据归因方法，选出的高影响样本通过重加权/删除干预时，效果往往和随机样本无明显差异，无法确定是样本本身无干预价值，还是重加权这种干预方式未能释放其潜力，亟需更高效的训练干预方案。
### 方法关键点
- 用IF对SFT训练样本打分，筛选对目标行为影响最高的Top/Bottom样本集；
- 对比两类干预方案：传统的样本加权/删除，以及保留prompt固定、仅重写样本响应的新方案，响应可设置为目标行为对齐/反向的内容；
- 采用EK-FAC近似计算大规模LLM的IF，将归因计算成本控制在可落地范围内。
### 关键结果
在4款1B-7B开源LLM上，覆盖认知拒答、安全拒答两个场景：仅干预2.5%的SFT样本时，响应重写的干预强度是传统重加权的5-10倍；对齐重写可将拒答召回率最高提升0.24，反向重写可最多降低0.3，效果比随机样本重写高60%以上，且干预效果仅集中在目标行为，无明显通用能力退化。
> 高影响训练样本本身具备极强的行为干预杠杆，传统重加权方式严重浪费了这种价值，替换为响应重写可释放数倍的调整效果
