---
title: On the Off-Policy Teacher in On-Policy Distillation
title_zh: SCOUT：解决On-Policy蒸馏中教师分布偏移问题的协同训练框架
authors:
- Langlin Huang
- Hao Liu
- Mononito Goswami
- Xinyu Li
- Prithwith Jana
- Nikos Kanakaris
- Patrick Blöbaum
- Purak Jain
affiliations:
- Washington University in St. Louis
- AWS AI Labs
- Carnegie Mellon University
- Georgia Institute of Technology
arxiv_id: '2609.38360'
url: https://arxiv.org/abs/2609.38360
pdf_url: https://arxiv.org/pdf/2609.38360
published: '2026-09-28'
collected: '2026-10-01'
category: Training
direction: LLM训练 · On-Policy蒸馏优化
tags:
- On-Policy Distillation
- Knowledge Distillation
- GRPO
- Teacher Adaptation
- LLM Training
one_liner: 提出SCOUT协同训练框架，通过适配教师到学生生成前缀解决On-Policy蒸馏的教师分布偏移问题
practical_value: '- 做垂直场景小模型蒸馏（如电商文案生成、推荐系统端侧个性化推理小模型、Agent轻量化部署）时，若拥有可验证的结果Reward，可直接复用SCOUT框架替换传统On-Policy蒸馏，无需改动学生侧训练逻辑，即可获得1~3个点的效果提升，泛化性优于截断/剪枝类OPD优化方案

  - 可复用「线性增加学生前缀长度」的课程式训练技巧，在蒸馏、RLHF等场景中降低分布偏移带来的训练不稳定问题，无需额外算力开销即可获得稳定收益

  - SCOUT与损失层OPD优化方法（如OPTR）完全互补，现有基于OPD的训练pipeline可同时接入两种优化，进一步提升蒸馏效果，无需重构训练流程'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
On-Policy蒸馏（OPD）是近年LLM post-training的主流范式，学生基于自身生成的轨迹学习，可解决传统off-policy蒸馏的暴露偏差问题，广泛用于小模型轻量化、推理能力蒸馏等场景。但OPD存在固有不对称缺陷：学生生成的前缀对教师是off-policy的，随着前缀长度增加，教师续写准确率会下降20%以上、不确定性持续升高，导致监督信号不可靠，现有方案均为固定教师、调整学生侧对监督信号的使用，未从根源解决教师侧分布偏移问题。
### 方法关键点
- 提出SCOUT协同训练框架，保留标准OPD的学生侧训练流程完全不变，新增教师侧周期性RL更新分支，两者耦合迭代
- 每次学生生成完整轨迹后，截取指定长度的前缀作为教师输入，教师生成续写后用可验证的结果Reward通过GRPO更新，梯度仅回传到教师生成的续写token
- 训练策略上，教师每10步OPD更新一次，训练过程中线性增加学生前缀占比，通过课程式学习降低训练难度
### 关键结果
在数学推理、代码生成两个域跨3种师生模型对、不同规模、不同模型家族测试：SCOUT比标准OPD数学推理准确率提升1.2~2.6个点，代码生成平均得分从56.6提升至59.7，效果优于ESR、Prune-OPD、Relay-OPD等现有OPD变种；与损失层优化方法OPTR互补，叠加后可再获得1.2~2.5个点的效果提升。
**最值得记住的一句话**：On-Policy蒸馏的效果瓶颈不仅来自学生学习能力，也来自教师对学生生成分布的不匹配，适配教师比单纯优化学生侧的监督信号使用泛化性更强
