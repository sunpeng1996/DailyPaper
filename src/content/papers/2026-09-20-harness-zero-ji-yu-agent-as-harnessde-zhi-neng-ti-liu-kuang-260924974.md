---
title: 'Harness-Zero: Harness Distillation via Agent-as-Harness'
title_zh: Harness-Zero：基于Agent-as-Harness的智能体Harness蒸馏框架
authors:
- Haoran Ye
- Yuxing Lu
- Haonan Dong
- Zhaochen Su
- Guojie Song
affiliations:
- 北京大学
- Google
- 香港科技大学
arxiv_id: '2609.24974'
url: https://arxiv.org/abs/2609.24974
pdf_url: https://arxiv.org/pdf/2609.24974
published: '2026-09-20'
collected: '2026-09-22'
category: Agent
direction: Agent Harness 能力蒸馏 · 无Harness部署
tags:
- LLM Agent
- Harness Distillation
- Agent-as-Harness
- SFT
- Model Optimization
one_liner: 提出Harness蒸馏范式，将专用Harness的诱导行为迁移到模型权重，部署时无需依赖外部Harness
practical_value: '- 可复用Agent-as-Harness范式，将电商/推荐场景的专用Agent脚手架（如用户意图识别规则、商品召回约束、合规校验逻辑）能力蒸馏进小模型，部署时去掉复杂脚手架降低推理延迟和工程开销

  - 业务SFT训练无需直接使用大模型生成轨迹，可引入引导Agent基于业务规则修正小模型原始输出，生成符合目标动作空间的训练数据，蒸馏效果远优于直接用大模型轨迹

  - 多场景Agent部署无需维护多套Harness路由，可将不同场景的专用Harness能力统一蒸馏进同一份基础模型权重，降低运维复杂度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent的性能增益高度依赖外部Harness（工具链、上下文管理、流程控制等脚手架），但不同场景最优Harness差异大：要么使用通用Harness损失专用性能，要么维护多套专用Harness带来路由、调度、资源开销，且Harness优化的增益无法沉淀到模型本身。

### 方法关键点
- 定义Harness蒸馏任务：将专用优化Harness的诱导行为迁移到模型权重，部署时仅用极简固定Harness即可获得原专用Harness的性能增益
- 核心设计Agent-as-Harness：先用训练集演化出场景专用Harness h⋆，再将其适配为供harnessing agent使用的私有参考Harness K；训练阶段harnessing agent用K审查学生模型的每步输出，在目标Harness的动作空间内做最小修正，生成符合要求的交互轨迹
- 对修正后的轨迹做LoRA SFT，将Harness诱导的行为内化到模型参数，部署时移除所有额外组件仅保留基础Harness

### 关键结果
在电子表格知识工作、多应用工具使用、科学推理三个领域验证：
1. 推理阶段Agent-as-Harness比Code-as-Harness平均性能高3pct（81.1% vs 78.1%）
2. 蒸馏后Qwen3.5-9B仅用极简Harness的情况下，宏平均任务成功率从23.3%提升到44.3%，超过原模型挂载专用Harness的41.7%
3. 28种Harness专属行为的平均恢复率达82.3%

### 核心结论
Agent的外部脚手架能力可以通过蒸馏完全内化到模型权重，无需在部署时保留复杂的外部Harness组件
