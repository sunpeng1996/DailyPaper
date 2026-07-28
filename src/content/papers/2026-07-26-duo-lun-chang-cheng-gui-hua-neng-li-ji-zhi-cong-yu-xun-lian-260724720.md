---
title: 'The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training
  via Single- and Multi-Teacher On-Policy Agentic Distillation'
title_zh: 多轮长程规划能力机制：从预训练到单/多教师On-Policy智能体蒸馏全阶段研究
authors:
- Tianyi Men
- Zhuoran Jin
- Kang Liu
- Jun Zhao
affiliations:
- 中国科学院自动化研究所
- 中国科学院大学
arxiv_id: '2607.24720'
url: https://arxiv.org/abs/2607.24720
pdf_url: https://arxiv.org/pdf/2607.24720
published: '2026-07-26'
collected: '2026-07-28'
category: Agent
direction: Agent 长程规划能力全阶段优化
tags:
- Long-Horizon Planning
- Agentic Distillation
- GRPO
- OPD
- MOPD
- World Model
one_liner: 系统揭示多轮长程规划能力在预训练、后训练、多教师整合全阶段的形成规律与优化边界
practical_value: '- 做电商导购、任务型Agent时，预训练仅需混入5%左右的长交互轨迹数据，即可大幅提升长程任务成功率，无需采集大量长轨迹降低成本

  - 长程Agent后训练阶段，若预训练数据质量差、任务交互轮次多，优先选择OPD而非GRPO，其梯度方向更一致，有效优化边界更宽

  - Agent推理阶段，强制在CoT中显式建模状态转移（世界模型），比直接输出动作的长任务准确率提升40%以上，可通过prompt工程快速落地

  - 多场景Agent能力整合时，优先对齐不同场景的通用规划模式，完全冲突的策略蒸馏会导致严重的灾难性遗忘，需提前过滤冲突规划逻辑'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前大模型Agent的多轮长程规划能力表现较差，现有训练流程依赖不可控的互联网公开数据，无法明确规划能力的获取、塑形、整合机制，不同训练阶段的优化边界不清晰，导致长交互类Agent落地难度高。

### 方法关键点
- 构建可控多轮规划仿真环境，覆盖奇幻炼金、畜牧养殖、电子装配3个领域共1500+合成规则，可精准控制任务长度、数据质量、规划知识/模式，兼容SFT与RL范式
- 分三阶段系统研究：预训练阶段的能力获取规律、单教师后训练的能力塑形边界、多教师后训练的能力整合机制
- 基于互信息区分通用规划模式（跨任务共享，低互信息）与任务专属规划知识（场景特定，高互信息），分别分析优化逻辑

### 关键结果
- 预训练阶段：显式建模世界模型的长任务pass@8比直接输出动作高42.9%；仅用短任务训练时长任务准确率接近0，加入5%长轨迹后长任务pass@8提升至11.46%；混入2:1次优轨迹后长任务准确率暴跌至接近0
- 后训练阶段：预训练数据质量低、任务轮次长时，OPD相对GRPO的效果提升超过5%；跨知识蒸馏会损害原有域的世界建模，域内性能下降12.9%

### 核心结论
长程规划能力无法通过原子技能自动组合获得，少量高质量长轨迹+显式世界模型建模是性价比最高的优化手段
