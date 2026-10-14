---
title: Hybrid Reasoning Agents
title_zh: 混合推理智能体HybridAgent：结合隐空间推理与文本交互的高效架构
authors:
- Jiaru Zou
- Yunzhe Qi
- Sirui Chen
- Federico Bianchi
- Shang Zhu
- Pan Lu
- Jingrui He
- James Zou
affiliations:
- Stanford University
- Together AI
- UIUC
- Meta
arxiv_id: '2610.18861'
url: https://arxiv.org/abs/2610.18861
pdf_url: https://arxiv.org/pdf/2610.18861
published: '2026-10-13'
collected: '2026-10-14'
category: Agent
direction: Agent 混合推理架构与效率优化
tags:
- LLM Agent
- Latent Reasoning
- Hybrid Generation
- Tool Use
- Reinforcement Learning
one_liner: 动态切换隐空间推理与文本交互，兼顾Agent工具能力、推理效率与可解释性
practical_value: '- 可复用HybridLink轻量残差适配器设计，无需改动现有LLM主干，仅新增~10M参数即可为电商导购、搜索Agent接入隐式推理能力，降低token生成成本

  - HybridSFT双通自监督训练范式可直接迁移到工具调用类Agent微调，解决隐式推理和显式文本/API调用的模态对齐问题，避免训练推理不一致

  - 连续KV工作记忆跨轮复用机制可落地到多轮会话推荐、搜索会话Agent的上下文管理，无需每轮重新编码全量文本，可提升推理速度1.5倍以上

  - HybridRL的混合策略因式分解方法可用于Agent决策路由：内部候选排序、需求理解走隐式推理，用户回复、工具调用走显式文本，平衡效率和交互体验'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有文本驱动的LLM Agent所有中间推理步骤都要生成显式token，推理成本高、速度慢，无法适配电商/搜索等需要高吞吐的业务场景；而纯隐空间推理方法无法原生对接工具、推理过程不可审计，难以落地需要可控、可解释的交互类Agent场景，两者能力割裂，亟需统一架构兼顾两端优势。
### 方法关键点
- 轻量**HybridLink**残差适配器：将Transformer最后一层隐状态映射回输入嵌入空间，实现文本/隐式推理模式的无缝切换，仅新增~2d_h²参数（4B模型约10M），无需改动主干模型
- 连续KV工作记忆：跨轮累积文本、隐向量、工具返回结果的KV缓存，完整保留混合上下文，无需每轮重建token序列重新编码
- **HybridSFT**两阶段微调：先做格式激活教模型生成<latent>等模式切换特殊token，再用双通自监督训练对齐主干与HybridLink，解决训练推理不一致问题
- **HybridRL**强化学习：通过混合策略因式分解，仅对文本采样位置做策略优化，让模型自适应选择推理模式，无需预设隐式推理长度
### 关键结果
基于4B/8B/14B Qwen3 backbone，在11个覆盖数学、医疗、知识搜索、Agent推理的基准上对比文本Agent、隐式推理方法、前沿商用Agent：平均性能提升10.4%，token用量减少35.5%~54.7%，推理速度提升1.8~2.6倍，计算成本降低2.7~3.7倍。
### 核心洞察
Agent不需要把所有内部思考都转化为显式文本输出，内部推理走隐空间、对外交互/工具调用/审计留文本，是兼顾效果、效率、可控性的可行路径。
