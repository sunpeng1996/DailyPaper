---
title: Training the Whole Agent, Not Just the Model
title_zh: Agent全链路训练：同步优化策略模型与运行支撑套件
authors:
- Lingxiao Tang
- Wei Tao
- Yiwen Guo
- Lingfeng Bao
affiliations:
- Zhejiang University
- LIGHTSPEED
- Independent Researcher
arxiv_id: '2610.28069'
url: https://arxiv.org/abs/2610.28069
pdf_url: https://arxiv.org/pdf/2610.28069
published: '2026-10-19'
collected: '2026-10-22'
category: Agent
direction: Agent训练 · 运行支撑套件协同优化
tags:
- Agent Training
- Reinforcement Learning
- GRPO
- Harness Adaptation
- Coding Agent
one_liner: 提出HarnessAdapt-RL框架，RL训练时同步适配Agent运行支撑套件，显著提升编码Agent效果
practical_value: '- 训练电商/推荐/广告场景Agent（如导购Agent、文案生成Agent、选品Agent）时可复用机制级引导方案：仅输出问题解决逻辑原理，不给出具体答案，训练完成后移除引导也能保留收益，避免训练依赖提示导致推理泛化差的问题

  - Harness适配的双指标验收规则可直接复用：用任务通过率、可用于策略更新的轨迹占比双维度判断是否保留候选套件，任一指标提升且无下降就接受，避免适配只优化短期效果损害训练效率

  - 同场景Agent训练可复用已演化的Harness：训练完成得到的工具、钩子套件无需重新演化，可直接用于同场景新模型的训练，节省演化成本，效果接近全流程演化的结果

  - 多轮交互Agent可参考轨迹驱动的Harness迭代逻辑：从当前策略生成的交互轨迹中发现共性问题，针对性优化工具/反馈逻辑，比预定义固定Harness效果更优'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent训练通常仅更新策略模型，固定运行支撑套件（Harness），但训练过程中轨迹暴露的修复策略缺陷、跨任务交互问题会随策略学习动态变化，固定Harness会严重限制训练效率与最终性能。

### 方法关键点
- 提出HarnessAdapt-RL框架，RL训练阶段同步优化策略模型与Harness：两个独立教师分别处理两类问题：冻结教师针对单任务修复策略缺陷，生成仅讲解逻辑原理、不泄露具体答案的机制级技能引导策略学习；另一教师从跨任务轨迹中识别共性交互问题，提出工具、钩子修改方案
- 双指标验收规则：候选Harness与当前Harness同条件对比，仅当pass rate（任务通过率）或trainable rate（可用于GRPO更新的轨迹占比）提升且无指标下降时，才接受修改
- 部署策略：训练阶段使用机制级技能引导，部署时移除技能，保留演化完成的工具和钩子套件，与训练好的策略配对部署

### 关键实验
基础模型为Qwen3.5-9B，在SWE-bench Verified、Multilingual、Pro三个基准上对比GRPO、OpenHands-GRPO等基线：
1. HarnessAdapt-RL对比GRPO，pass@1分别提升9.8、12.6、6.4个百分点，也优于人工设计的OpenHands套件训练的GRPO
2. 部署时移除演化好的工具和钩子，pass@1最多下降7.7个百分点，说明套件对最终效果至关重要
3. 演化得到的H2套件可直接复用在同场景新模型训练，效果接近全流程演化的结果

### 核心结论
Agent是模型与运行支撑套件是不可分割的整体，训练时同步优化两者才能获得最优性能，而非仅优化模型权重
