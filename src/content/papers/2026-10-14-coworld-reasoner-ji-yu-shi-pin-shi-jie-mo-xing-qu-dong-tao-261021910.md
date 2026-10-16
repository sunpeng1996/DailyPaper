---
title: 'CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World
  Model-Driven Harness'
title_zh: CoWorld Reasoner：基于视频世界模型驱动套件的智能体多模态推理框架
authors:
- Dongjie Cheng
- Ruifeng Yuan
- Ran Wei
- Ning Song
- Yongqi Li
- Wenjie Li
affiliations:
- The Hong Kong Polytechnic University
- Hangzhou Diagens Biotechnology Co., Ltd
arxiv_id: '2610.21910'
url: https://arxiv.org/abs/2610.21910
pdf_url: https://arxiv.org/pdf/2610.21910
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: 多模态Agent · VLM与VWM协同进化
tags:
- VLM
- Video World Model
- Multimodal Reasoning
- Agent Evolution
- Tool Use
one_liner: 固定VLM/VWM权重，通过工具化封装与协同进化提升多模态推理精度
practical_value: '- 可复用「大模型+生成模型工具化封装+权重固定协同进化」范式，将电商场景的文生图/文生视频/3D生成模型封装为Agent可调用工具，通过迭代优化prompt、调用逻辑、结果解释规则提升效果，无需微调大模型降低成本

  - 电商AR试穿/试摆效果预判、商品空间关系推理、多模态内容审核场景可直接复用4种VWM操作封装：视角切换、帧间插值、动作延续、干预模拟，覆盖绝大多数动态视觉推理需求

  - Agent四阶段执行框架（能力边界评估→工具请求→结果解读→证据整合）可直接复用，分阶段迭代优化每个环节的规则，比端到端调优的可解释性和迭代效率更高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前VLM做时空因果推理（如视角切换判断、动作结果预判、中间状态补全）时仅靠输入静态图像证据不足，现有Video World Model（VWM）调用均为固定流水线，仅支持预设的新视角合成，无法适配多样化推理任务，且需微调模型才能提效，成本高。

### 方法关键点
- 设计VWM驱动套件：将VWM能力封装为4种标准化工具（视角切换、帧间插值、动作延续、干预模拟），沉淀3类可复用技能（跨视图推理、时序推理、因果干预推理），指导Agent自主判断是否调用工具、构造生成请求、解读生成的视频证据。
- 提出VLM-VWM套件协同进化机制：完全固定VLM和VWM权重，基于执行反馈分四阶段（能力边界评估→工具请求→视频解读→证据整合）迭代优化工具定义、技能逻辑、执行代码，对齐两类模型的交互逻辑。

### 关键实验
在7个多模态推理基准（MMSI、SAT、ERQA等）上测试，最强版本（GPT-5.6 + MiniMax H3）相比同VLM直接推理，MMSI相对精度提升11.8%，ERQA相对提升13.0%，在5个基准上超过5个同基座进化Agent基线；进化后的套件可迁移到Grok-4.5等其他VLM，迁移后整体精度提升6.92个百分点。

最值得记住的一句话：固定大模型权重，通过工具封装、交互逻辑协同进化提升多模态推理效果的范式，成本远低于微调，且可迁移性更强。
