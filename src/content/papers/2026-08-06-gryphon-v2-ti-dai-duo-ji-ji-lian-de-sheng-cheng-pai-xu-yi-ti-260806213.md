---
title: 'Gryphon-v2: One Model in Place of a Cascade - Generate-and-Rank Recommender
  with Rollout Distillation'
title_zh: Gryphon-v2：替代多级级联的生成排序一体化推荐系统
authors:
- Anna Lipkina
- Daria Tikhonovich
- Viktor Yanush
- Mariia Ulianova
- Oleg Sorokin
- Vladislav Dodonov
- Ilya Murzin
- Denis Burshtein
- Nikolay Savushkin
affiliations:
- Yandex
arxiv_id: '2608.06213'
url: https://arxiv.org/abs/2608.06213
pdf_url: https://arxiv.org/pdf/2608.06213
published: '2026-08-06'
collected: '2026-08-07'
category: GenRec
direction: 生成式推荐 · 端到端生成排序一体化
tags:
- Generative Recommendation
- Semantic ID
- Knowledge Distillation
- End-to-End RecSys
- Rollout Distillation
one_liner: 单一生成排序模型替代15+路召回级联，在线效果优于生产推荐系统
practical_value: '- 架构层面可复用「共享用户历史编码器+Semantic ID生成候选+轻量排序模块」设计，用户历史仅编码一次，大幅降低推理延迟，同时避免多级级联的特征链路维护成本

  - 蒸馏训练可采用Rollout Distillation思路：将训练时当前解码器生成的候选、线上历史曝光候选同时送给大参数量教师排序模型打标，蒸馏到轻量学生模块，既覆盖线上曝光分布，又适配推理时的生成候选分布，效果远好于仅用曝光数据

  - 工业落地时可将无法在线部署的大精排模型作为教师蒸馏，仅用学生模型在线服务，在不增加 latency 的前提下承接大模型的排序效果，该方案可替代15+路召回级联且效果更优

  - 离线评估可新增TeacherRecall指标，衡量学生对教师排序偏好的拟合程度，配合传统召回率、排序准确率指标，更全面评估蒸馏效果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级推荐系统普遍采用多路召回+预排+精排的多级级联架构，效果稳定但存在用户历史重复编码、特征链路复杂、多模块维护成本高的问题；基于Semantic ID的生成式召回能简化链路，但仅做next-item预测无法对齐生产精排的多目标细粒度偏好，难以直接替代全链路级联。

### 方法关键点
- 架构：采用共享用户历史编码器的一体化设计，用户历史仅编码一次，输出状态同时供Semantic ID自回归解码器生成候选、轻量排序模块打分复用，候选通过目录trie约束的beam search生成，解决Semantic ID合法性问题
- 训练：提出Rollout Distillation，用训练阶段专属、无法在线部署的大参数量教师排序模型的打分作为监督，蒸馏候选同时来自两部分：当前解码器生成的rollout候选（和推理逻辑一致，占90%+ distinct候选）、线上历史曝光候选，蒸馏损失用MAE，和next-token预测损失联合训练
- 推理：生成的Semantic ID解析为物品后直接用排序模块打分排序，无后续精排链路

### 关键结果
在Yandex音乐场景做线上A/B实验，单模型直接替代15+路召回+预排+精排的生产级联，活跃用户数提升1.41%，总收听时长提升1.62%，端到端延迟和原级联持平；离线层面教师Top10召回对齐度从0.04提升到0.56，加权排序准确率WPA达0.5892，比普通生成式推荐高6.6%。

**最值得记住的一句话**：基于蒸馏的生成排序一体化模型已经可以在工业级大流量场景下完全替代传统多级级联推荐架构，在效果和效率上同时具备竞争力。
