---
title: 'OxygenREC-v2: Internalizing Discrimination into Generative Recommendation'
title_zh: OxygenREC-v2：将行为判别信号内化进生成式推荐系统
authors:
- Guo Tang
- Hanye Wu
- Changjiang Han
- Qingyang Li
- Ming Zhang
- Xiangyu Qian
- Yanchen Qiao
- Huanjie Wang
- Zhi Ma
- Zhen Li
affiliations:
- JD.COM
arxiv_id: '2607.24255'
url: https://arxiv.org/abs/2607.24255
pdf_url: https://arxiv.org/pdf/2607.24255
published: '2026-07-27'
collected: '2026-07-28'
category: GenRec
direction: 生成式推荐 · 行为信号内化优化
tags:
- Generative Recommendation
- Semantic ID
- MoE
- Self-Distillation
- Behavior Modeling
one_liner: 将用户行为判别信号内置于生成推荐全训练流程，无需外部Reward Model，工业落地提升显著
practical_value: '- 预训练阶段可在Decoder前缀加入业务目标对应的行为指令（点击/加购/下单），无需额外模块即可让生成候选匹配不同场景的转化目标

  - 后训练阶段可直接用用户未来交互行为作为特权信息做自蒸馏，无需单独训练Reward Model即可完成RL优化，避免Reward Hacking同时降低训练成本

  - 蒸馏时增加熵感知门控，仅在教师模型熵低的位置做偏好蒸馏，高熵位置用正向KL保留多样性，相比全量蒸馏效果更好且节省算力

  - 工业落地可采用3B参数量、1B激活的MoE架构，兼顾效果和推理成本，直接替换现有生成推荐基线即可拿到转化和GMV提升'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐通常将用户点击、加购、下单等行为信号作为外部重排序或RL Reward输入，存在两个核心问题：一是外部Reward Model对生成的OOD候选打分不准，易出现Reward Hacking；二是生成器本身行为无感，无法从生成源头适配不同场景的业务目标（如首页要点击率、结算页要下单率），只能事后重排序，候选集质量存在明显瓶颈。

### 方法关键点
- 预训练阶段：将目标行为（点击/加购/下单）编码为行为指令Ib拼接至Decoder前缀，让每一步生成都受行为目标约束，同时训练时按行为价值加权损失，高价值的下单行为权重更高。
- 后训练阶段：提出EA-TOSD熵感知轨迹优化自蒸馏框架，无需外部Reward Model：用生成序列与真实交互的匹配度作为可验证Reward做轨迹优化；用加入用户未来交互前缀的同backbone模型作为特权教师做自蒸馏；增加熵感知门控，低熵位置蒸馏教师偏好，高熵位置用正向KL保留多样性，避免特权偏差。
- 全程仅用一个统一Backbone，推理时无需额外模块，仅修改Ib即可适配不同场景的业务目标。

### 关键实验
基于京东大规模电商交互数据训练，对比基线包括无后训练的OxygenREC-v1、采用外部Reward Model的Proxy-RM，离线HR@1从4.62%提升到5.64%，HR@512从43.24%提升到44.14%；部署为3B参数1B激活的MoE模型后，多场景线上A/B测UCTCVR提升1.6%~4.4%，GMV提升2.8%~6.8%。

### 核心结论
行为信号是生成式推荐的一等训练目标而非事后重排序信号，从生成源头适配业务目标的收益远高于事后调整。
