---
title: 'GARP: Real-Time Generative Agents on Local Hardware in a Game Engine'
title_zh: GARP：运行于本地硬件游戏引擎的实时生成式智能体平台
authors:
- Piero Molino
- Patrick John Chia
- Federico Bianchi
- Jonathan P. Chen
- Paul Szerlip
affiliations:
- Studio Atelico
- Together AI
arxiv_id: '2611.11064'
url: https://arxiv.org/abs/2611.11064
pdf_url: https://arxiv.org/pdf/2611.11064
published: '2026-11-08'
collected: '2026-11-10'
category: Agent
direction: 生成式智能体 · 本地实时部署优化
tags:
- Generative Agent
- Local Inference
- LLM
- Real-time Simulation
- Prompt Engineering
one_liner: 在Godot引擎上实现3B小模型全本地部署的实时生成式智能体系统，支持多智能体自主行为模拟
practical_value: '- 小模型Agent部署可复用分层优化策略：可调时钟预决策、多层级缓存、异步执行、前置候选过滤，有效解决小模型高延迟问题，适配端侧/边缘侧推荐Agent、导购Agent场景

  - 多维度用户建模可参考人格-需求-情绪-关系联动框架：把人格特质同时映射为prompt文本和系统参数，解决小模型人格一致性差的问题，可迁移到用户画像、个性化内容推荐、智能客服场景

  - Agent记忆系统可复用四因子检索+艾宾浩斯Consolidation方案：加入情绪显著性、记忆稳定性权重，提升记忆召回相关性，适合长周期用户行为记忆建模、用户兴趣动态捕捉

  - 线上高可用LLM服务可复用JSON Schema强制约束+分级fallback机制，避免LLM输出异常导致服务中断，适配生成式推荐、智能文案生成等高可靠业务要求'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
原斯坦福生成式智能体依赖云侧大模型、离散时间模拟，无法嵌入游戏等实时交互场景，且云调用成本高、延迟不可控、数据隐私风险高，亟需适配本地硬件的低延迟、低成本、高可用生成式智能体架构。

### 方法关键点
- 三层架构：Godot游戏层+认知管理层+Rust原生引擎层，支持本地/云推理无缝切换，所有LLM调用采用JSON Schema约束+降级fallback，确保输出可靠性
- 智能体认知框架：融合6维度需求模型、4维度大五人格映射（同时作用于prompt和模拟参数）、4维度情绪系统（含对话情绪传染）、显式pairwise关系模型、四因子（重要性/相关性/新鲜度/情绪显著性）记忆检索+艾宾浩斯遗忘机制
- 本地优化策略：前置affordance过滤把50+候选动作压缩到3-8个，配合可调时间缩放、提前预决策、多层缓存、异步非阻塞执行，掩盖小模型推理延迟

### 关键结果
9个场景共27次运行，25次通过日志校验，通过率92.6%；仅生日派对场景2次失败，原因是单智能体未把派对纳入当日计划；本地部署采用Llama 3.2 3B 4-bit量化模型，可支持20个智能体同时运行，对比原云部署推理成本降为0。

### 核心结论
小模型Agent的行为一致性不能仅靠prompt引导，必须把人格、需求等特质同时映射为系统层面的数值参数，才能稳定控制行为输出。
