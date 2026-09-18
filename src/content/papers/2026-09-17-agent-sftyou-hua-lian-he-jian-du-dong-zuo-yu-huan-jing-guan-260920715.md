---
title: 'Don''t Mask the Environment: Observation Supervision Changes How Agents Explore
  Under RL'
title_zh: Agent SFT优化：联合监督动作与环境观测提升下游RL探索效果
authors:
- Juzheng Zhang
- Disha Makhija
- Manoj Ghuhan Arivazhagan
- Vinayshekhar Bannihatti Kumar
- Rashmi Gangadharaiah
affiliations:
- University of Maryland
- AWS AI Labs
arxiv_id: '2609.20715'
url: https://arxiv.org/abs/2609.20715
pdf_url: https://arxiv.org/pdf/2609.20715
published: '2026-09-17'
collected: '2026-09-18'
category: Agent
direction: Agent · RL训练初始化优化
tags:
- Agent
- SFT
- RL
- GRPO
- Exploration
one_liner: SFT阶段同时监督动作和环境观测token，无需额外成本即可提升下游RL性能与跨域迁移能力
practical_value: '- 电商导购/客服Agent的SFT训练可直接复用该trick：无需新增数据，仅修改loss mask，将用户反馈/环境返回结果也加入预测目标，即可提升后续RL效果，零额外训练成本。

  - 适配多采样兜底的业务场景（如Agent多轮重试、推荐top-k召回）：可调整观测损失权重λ，牺牲少量单次成功率换取多采样下的整体效果，匹配业务重试机制。

  - 跨域Agent迁移场景（如通用导购迁移到品类专属导购）优先采用ActObs做SFT初始化，能保留更高模型熵、更小RL偏移，跨域效果提升更明显。

  - 现有GRPO等RL流程无需修改，仅替换ActObs的SFT checkpoint即可获得增益，改造成本极低。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
常规Agent SFT仅对Agent输出的动作token计算损失，环境观测仅作为上下文不参与监督，该默认做法从未被验证是否适合作为RL的前置初始化，会导致模型丢失动作-后果的建模能力，RL阶段探索空间被压缩，多采样下的成功率提升受限。

### 方法关键点
- 提出ActObs方法，仅修改SFT阶段的损失mask，同时对轨迹中的动作token、环境观测token计算LM损失，用λ控制观测损失权重，默认λ=1，无需新增数据、参数、前向计算步骤。
- 观测监督仅在SFT阶段开启，后续GRPO、ECHO等RL流程完全不需要修改，无额外落地复杂度。
- 对比顺序先训练观测再训练动作的Obs→Act基线，证明只有动作与观测的联合监督才能带来下游增益。

### 关键结果
在Terminal-Bench 2.0终端任务集、aider-polyglot跨域代码编辑任务集上对比标准ActionSFT基线：Qwen3-4B规模下，ActObs初始化的GRPO在Terminal-Bench pass@1相对提升29%，跨域代码任务pass@1相对提升43%；Qwen3-8B规模下pass@16提升3.4pp，多解决3个独有任务，且RL阶段模型熵更高、相对于SFT初始化的偏移量更小。

**最值得记住的一句话**：Agent SFT的核心目标不只是模仿专家动作，更要保留对动作后果的建模能力，才能为后续RL探索留出足够空间。
