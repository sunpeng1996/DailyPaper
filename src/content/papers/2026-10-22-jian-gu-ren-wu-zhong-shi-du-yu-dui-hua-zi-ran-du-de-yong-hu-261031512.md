---
title: Towards User Simulators That Stay On Task And Still Sound Natural
title_zh: 兼顾任务忠实度与对话自然度的用户模拟器UserLM-2.0
authors:
- Mustafa Omer Gul
- Philippe Laban
- Tanya Goyal
- Jennifer Neville
affiliations:
- Cornell University
- Microsoft Research
arxiv_id: '2610.31512'
url: https://arxiv.org/abs/2610.31512
pdf_url: https://arxiv.org/pdf/2610.31512
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: Agent 用户模拟 · 多轮交互性能优化
tags:
- User Simulator
- Reinforcement Learning
- Adversarial Training
- Multi-turn Conversation
- Reward Design
one_liner: 基于RL+动态对抗判别器的用户模拟器，兼顾任务忠实度与自然度，有效会话率3倍于SOTA
practical_value: '- 智能导购/客服Agent评测场景：可复用该用户模拟器训练范式，基于业务历史对话快速生成高保真模拟用户，降低真实用户交互采样成本，支撑多轮交互效果的离线评测

  - 多目标优化场景：当优化目标存在tradeoff（如生成式推荐的相关性vs自然度、对话系统的任务完成率vs拟人化），可借鉴该多奖励加权+动态判别器的RL设计，规避单一目标的reward
  hacking问题

  - 自然度评测场景：放弃LLM-as-judge做自然度评估，改用基于业务数据fine-tune的轻量判别器，不仅评测准确性更高，推理和训练成本也降低一个数量级以上，可直接复用在生成式文案、query推荐的自然度校验环节'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前多轮交互AI助手的性能会随对话轮次提升严重衰减，急需高保真用户模拟器支撑离线评测与训练优化，但现有方案存在明显tradeoff：prompt驱动的LLM可严格遵循任务意图但对话风格生硬、不符合真实用户行为，SFT训练的专用用户模拟器对话自然但容易偏离任务要求，无法同时满足任务忠实度与自然度要求。

### 方法关键点
- 两阶段训练：先在多轮用户-助手对话数据上做SFT得到初始化模型，再用GRPO算法做多轮RL训练，联合优化质量、意图覆盖率、自然度、终止合理性4个奖励维度，质量不达标时总奖励直接置0，过滤错误样本
- 自然度奖励设计：放弃LLM-as-judge，采用基于ModernBERT的轻量判别器，每25步RL就用最新生成的模拟对话更新一次判别器（GAN式对抗训练），避免模拟器针对固定判别器做reward hacking
- 防奖励泄露设计：给模拟器输入的是抽象版任务意图，给覆盖率判分LLM的是带完整子目标的意图，防止模型直接复述意图骗取高覆盖率分数

### 关键结果
基于WildChat-4.8M的多轮对话子集训练，对比10+基线（包括GPT-5.6系列、SFTUser-14B等），UserLM-2.0的有效会话率（同时满足80%+意图覆盖率、自然度达标、质量合格、正常终止）达46.2%，是此前最优SFTUser-14B（14.1%）的3.28倍；7子目标高复杂度场景下有效率12.6%，是其他基线的12倍以上；单百次有效会话成本仅0.11美元，远低于prompt类方案。

### 核心结论
用LLM judge做自然度评测效果远差于动态训练的轻量判别器，甚至不如不加自然度奖励，平衡多目标的RL训练必须优先规避reward hacking风险。
