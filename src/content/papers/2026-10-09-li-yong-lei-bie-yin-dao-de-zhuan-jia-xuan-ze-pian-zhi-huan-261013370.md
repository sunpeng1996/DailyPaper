---
title: Overcoming Data Imbalances with Expert Selection Biases
title_zh: 利用类别引导的专家选择偏置缓解MoE模型数据不平衡问题
authors:
- Ayush K. Tarun
- Clara Meister
- Antoine Bosselut
affiliations:
- EPFL
arxiv_id: '2610.13370'
url: https://arxiv.org/abs/2610.13370
pdf_url: https://arxiv.org/pdf/2610.13370
published: '2026-10-09'
collected: '2026-10-12'
category: Training
direction: MoE预训练 · 低资源类别容量优化
tags:
- MoE
- Expert Routing
- Low-resource Learning
- Pretraining
- Data Imbalance
one_liner: 提出COAX轻量方法，通过类别引导的路由偏置为MoE低资源类别分配超额专家容量，推理无额外开销
practical_value: '- 若业务侧使用MoE架构搭建多域/多模态/多语言推荐大模型，可直接复用COAX的偏置路由策略，给低流量域/小众类目分配超出其数据占比的专家配额，长尾效果提升的同时不增加推理成本

  - 推理阶段可直接移除偏置，无需改造现有MoE推理栈，也不需要提前识别输入的类别标签，工程落地成本极低，10B规模MoE训练 overhead 仅1.3%，性价比突出

  - 无需为每个低资源类目单独分配独立专家组，粗粒度的「主流类/长尾类」二分专家分组即可拿到大部分收益，大幅降低配置成本，适配电商海量长尾类目场景

  - 可与常规的数据上采样策略叠加使用，进一步提升长尾类目/低资源域的模型效果，无需改动现有数据处理 pipeline'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
MoE是当前前沿大模型的主流架构，理论上可实现专家按域/语言/模态专业化，但训练数据不平衡时，低资源类别易出现路由集中导致专家饱和、或分散路由导致容量利用率低的问题，现有专家专业化方法要么需要硬分专家组，要么推理需改造逻辑，落地成本高。

### 方法关键点
- 提出COAX（Category-Oriented Allocation of eXperts），预训练阶段给每个类别的指定专家子集的路由得分加固定正偏置α，软引导同类别token路由到对应专家组，允许高置信度路由结果覆盖偏置，保留跨类别知识共享能力
- 支持为低资源类别设置超出其训练token占比的专家配额（相对专家份额r_c>1），单token激活专家数K不变，不增加推理计算量
- 偏置仅在预训练阶段生效，推理可直接移除，无需修改标准MoE推理栈，也不需要输入的类别标签

### 关键结果
在多语言、多模态、多领域3个场景下345M~10.6B参数的MoE模型上验证：345M规模效果等价于增加18.5%训练token，10.6B规模等价于增加2.7%训练token，训练 overhead 仅1.3%；多语言场景下占训练数据0.85%的斯瓦希里语损失最高降0.59%，多模态场景下图像任务损失最高降0.76%，主流类别效果几乎无损失；对比硬路由、EDL等方法，8语言混合场景下7个小语种平均损失降幅达0.286%，显著优于基线。

### 核心结论
MoE路由偏置不止可用于负载均衡，还可作为轻量的类别级专家容量调控工具，以极低的成本解决长尾数据训练容量不足的问题
