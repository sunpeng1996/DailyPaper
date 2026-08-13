---
title: Sona Technical Report
title_zh: Yandex Music单模型生成式推荐系统SONA技术报告
authors:
- Sona Team
- Alexandr Udeneev
- Aleksei Krasilnikov
- Alexey Nadtochiy
- Andrey Semenov
- Andrey Tsyrkunov
- Anna Krivonos
- Anna Lipkina
- Artem Matveev
- Daniil Burlakov
affiliations:
- Yandex
arxiv_id: '2608.11015'
url: https://arxiv.org/abs/2608.11015
pdf_url: https://arxiv.org/pdf/2608.11015
published: '2026-08-11'
collected: '2026-08-12'
category: GenRec
direction: 生成式推荐 · 单模型统一召回排序
tags:
- Generative Recommendation
- Semantic ID
- Knowledge Distillation
- Unified RecSys
- Sequence Modeling
one_liner: 用共享编码器的单生成式推荐模型替换全链路级联，大幅提升Yandex音乐核心业务指标
practical_value: '- 可复用Semantic ID生成流程：结合多模态预训练表征+协同信号优化item表征后做残差量化，既解决大sku库生成空间爆炸问题，还能提升新item泛化性，电商大品类场景可直接迁移

  - 单模型统一召回排序架构：共享用户编码器，生成模块出候选+蒸馏自教师排序器的轻量打分模块重排，大幅降低链路冗余，适合中小流量场景快速迭代

  - 训练trick：教师排序器先做next-item prediction预训练再微调排序目标，比直接训排序效果更优；蒸馏同时用模型自生成候选和线上曝光候选，兼顾排序保真度与生产分布适配

  - 工程优化：长用户历史做分段编码，仅对近期历史做深度attention，长期历史做轻量交互，在保留8k长历史效果的同时把推理延迟降一半，时延敏感场景可直接复用'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统生产级推荐链路由十余个召回+预排+精排模型级联构成，依赖大量人工特征，迭代成本高、链路冗余；生成式推荐虽已有落地案例，但很少有全链路替换成熟生产级联的工业级实践，且音乐推荐需平衡用户熟悉曲目留存和新曲探索的特殊需求，现有方案效果未达上线要求。

### 方法关键点
- 架构：共享用户编码器同时供给自回归decoder和排序模块，decoder生成3维Semantic ID映射到音乐候选，排序模块基于共享编码器表征做重排，全程无人工特征
- Semantic ID构建：先用多模态大模型Qwen2.5-Omni编码音乐音频+元数据，再用协同对Transformer优化表征，最后残差量化为3个32k码本的ID，相似音乐共享前缀提升泛化
- 训练：联合next-token prediction生成损失+蒸馏损失，蒸馏源同时用decoder自生成候选和线上曝光候选；教师排序器先做next-item预训练再微调多目标排序，蒸馏后推理无需教师
- 工程优化：8k长用户历史拆分为2k近期+6k长期，仅近期做深度attention，长期做轻量跨attention，推理成本降50%；线上训练流实现事件到模型更新中位数45分钟延迟

### 关键结果
在Yandex Music智能音箱My Vibe场景做线上A/B测试，对比之前最优的Argus模型，SONA带来Active Users +4.53%（是Argus提升的2.35倍）、总收听时长+6.30%、点赞+11.42%，单模型完全替换原有15+召回+预排+精排的全链路级联。

最值得记住的结论：无人工特征的单模型生成式推荐完全可以替代成熟的多阶段推荐级联，同时获得显著的业务指标提升。
