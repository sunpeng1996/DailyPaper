---
title: Preserving Utility in Continual LLM Unlearning via Orthogonal Projections
title_zh: 基于正交投影的大语言模型持续遗忘效用保留方法
authors:
- Juan Belieni
- Ana Carolina Erthal
- Eliezer de Souza da Silva
- Diego Mesquita
affiliations:
- Getulio Vargas Foundation
- University of Coimbra
arxiv_id: '2610.40483'
url: https://arxiv.org/abs/2610.40483
pdf_url: https://arxiv.org/pdf/2610.40483
published: '2026-10-29'
collected: '2026-10-30'
category: Training
direction: LLM持续遗忘 · 正交梯度投影
tags:
- LLM-unlearning
- continual-training
- gradient-projection
- orthogonal-projection
- model-editing
one_liner: 提出可插拔的持续正交投影COP，解决多轮LLM遗忘的效用衰减与遗忘回退问题
practical_value: '- 业务侧需要对部署LLM做持续内容擦除（如侵权商品描述、违规话术、过时活动信息）时，可直接将COP作为插件接入现有基于梯度的微调/遗忘流程，无需修改原有损失函数，即可避免多轮擦除后模型通用能力崩溃

  - 梯度投影到历史激活子空间正交补的思路可迁移到推荐系统持续迭代场景：每次更新召回/排序策略时，投影梯度避开历史优质样本的激活子空间，避免新策略破坏历史有效效果，缓解灾难性遗忘

  - 低秩激活子空间缓存的工程trick存储开销远低于存历史梯度/数据，单轮仅新增最多rmax（如256）个方向每层，内存可控，适合在线持续训练落地'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM遗忘方法大多针对单次删除请求设计，多轮连续遗忘时更新会互相干扰，要么已删除内容恢复，要么模型通用效用骤降，而全量重训成本过高，无法满足部署后持续的合规擦除（版权内容、用户隐私、违规信息）需求。

### 方法关键点
- 提出轻量可插拔的持续正交投影（COP）组件，无需修改原有遗忘损失，仅对每轮梯度做投影：将当前梯度投影到历史所有遗忘集激活子空间的正交补空间，保证每轮更新不会干扰之前的遗忘效果
- 每轮遗忘完成后，仅缓存当前遗忘集激活的低秩正交基（保留τ比例激活能量，单轮每层最多新增rmax个方向），无需存储历史梯度、历史遗忘数据，内存开销极低
- 理论上保证一阶无干扰，对激活子空间覆盖的样本，后续更新完全不会改变模型输出

### 关键结果
在TOFU（虚构实体遗忘）、RWKU（真实知识遗忘）两个标准基准上测试，对比GA、NPO等基础遗忘方法，以及O3、ALKN等持续遗忘基线：
- 5轮连续遗忘后，COP加持的方法比原生方法效用MU最高提升300%（原生GA的MU跌到0.159，GA+COP保持0.461），同时遗忘效果几乎无下降
- 比O3基线遗忘效果提升40%以上，比ALKN基线效用提升2个数量级

最值得记住的一句话：多轮迭代场景的更新干扰问题，用「梯度投影到历史关键激活子空间正交补」的方案，比拆分参数、加正则的方法效用保留效果好得多，且工程落地成本极低
