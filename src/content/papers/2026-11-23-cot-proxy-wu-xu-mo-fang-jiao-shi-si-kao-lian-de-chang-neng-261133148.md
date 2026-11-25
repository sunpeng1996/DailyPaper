---
title: 'CoT-Proxy: Cross-Format Transfer for Distilling Long-Horizon Policies'
title_zh: CoT-Proxy：无需模仿教师思考链的长Horizon智能体策略蒸馏方法
authors:
- Dawid J. Kopiczko
- Tijmen Blankevoort
- Yuki M. Asano
affiliations:
- University of Technology Nuremberg
- NVIDIA
arxiv_id: '2611.33148'
url: https://arxiv.org/abs/2611.33148
pdf_url: https://arxiv.org/pdf/2611.33148
published: '2026-11-23'
collected: '2026-11-25'
category: Agent
direction: 长Horizon智能体 · 闭源模型策略蒸馏
tags:
- Agent-Distillation
- Chain-of-Thought
- Closed-LLM
- Long-Horizon
- LoRA
- KL-Regularization
one_liner: 无需访问闭源模型隐藏思考链，仅用动作和摘要即可蒸馏小模型长序列智能体能力
practical_value: '- 闭源大模型蒸馏业务Agent的落地方案：无需获取GPT等闭源模型的内部隐藏CoT，仅用API返回的可见动作+公开推理摘要即可完成小模型蒸馏，规避服务条款风险同时降低数据成本，可直接用于电商智能导购、客服等多轮交互Agent的能力迁移

  - 跨格式迁移训练trick：训练时填充空<think>块仅监督动作，推理时打开思考开关让小模型用原生推理逻辑执行策略，无需强制对齐大模型思考范式，小模型在业务场景的适配性更强

  - 能力留存正则方案：蒸馏时加入15%比例的跨领域重放样本，用KL loss锚定初始模型的通用能力，避免特定业务任务微调后通用推理能力滑坡，适合多场景复用的业务Agent微调

  - 低工程成本架构：整套方案基于LoRA微调实现，无需全量参数更新，可快速迁移到商品运营、售后处理等长序列业务Agent的能力迭代'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前小模型落地长Horizon智能体任务的主流方案是蒸馏大教师模型的完整CoT轨迹，但最强的闭源模型（如GPT系列）的CoT被加密隐藏无法获取；同时小模型直接模仿大模型思考链的适配性差，容易丢失自身原有推理能力，蒸馏效果受限。

### 方法关键点
- 提出3种训练范式：传统全CoT监督、仅动作监督（训练时<think>块填空，仅监督后续动作）、CoT-Proxy（空<think>块后增加教师推理摘要作为额外监督信号，摘要无需来自原始CoT，可直接用闭源API返回的公开摘要）
- 跨领域重放正则：训练时每个batch混合15%的初始模型在非目标域生成的样本，用KL loss约束微调后模型与初始模型的分布差异，避免能力漂移
- 训练推理跨格式：推理时统一打开<think>开关，让小模型用自身原生逻辑生成思考内容，无需输出训练阶段的摘要块

### 关键结果
实验在AppWorld（168个APP操作任务）、SWE-bench Verified（500个代码修复任务）两个长Horizon基准上验证：
- 仅用动作蒸馏即可把Qwen3-4B的AppWorld任务成功率从7%提升到35%，效果接近全CoT蒸馏
- 采用CoT-Proxy蒸馏闭源GPT-5.6 Luna时，Qwen3-4B的AppWorld成功率进一步提升到48%，SWE-bench成功率从3%提升到28%，同时保留98%以上的初始单轮推理能力

### 核心结论
蒸馏长序列智能体策略时，不需要强制小模型模仿大模型的思考过程，仅对齐动作决策就能实现有效迁移，还能保留小模型自身的推理能力
