---
title: 'MDSKILL: Learning to Internalize Skill Memory through Multi-View Distillation
  for Efficient Dynamic Agent Self-Evolution'
title_zh: MDSKILL：基于多视图蒸馏的Agent技能记忆内化自进化框架
authors:
- Dian Jin
- Jinluan Yang
- Kairong Han
- Baohong Li
- Zijing Hu
- Yi He
- Wenlin Zhong
- Yunze Tong
- Minqin Zhu
- Linchuan Li
affiliations:
- Zhejiang University
- Kuaishou Technology
arxiv_id: '2611.05313'
url: https://arxiv.org/abs/2611.05313
pdf_url: https://arxiv.org/pdf/2611.05313
published: '2026-11-03'
collected: '2026-11-04'
category: Agent
direction: Agent自进化 · 多视图技能蒸馏
tags:
- SkillMemory
- SelfDistillation
- SelfEvolution
- MultiViewLearning
- LLMAgent
one_liner: 通过多视图蒸馏拆解技能记忆功能，无额外开销提升Agent自进化性能
practical_value: '- 技能库构建可参考三功能视图拆分逻辑，把电商导购Agent的经验拆分为场景感知、路径规划、执行纠偏三类，降低技能纠缠带来的蒸馏噪声

  - 动态技能筛选的Reliability+Advantage双指标+汤普森采样方案可直接复用在推荐系统的历史策略召回阶段，平衡探索利用的同时过滤过时无效策略

  - 蒸馏门控自适应方案（小模型用严格门控、大模型用宽松门控）可迁移到生成式推荐蒸馏任务中，根据基座规模调整监督阈值避免噪声传导

  - 正向/反向/跨视图的多向蒸馏范式可用于Agent+推荐混合系统，实现规则策略、RAG策略、原生模型能力的双向知识迁移'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有On-Policy Self-Distillation（OPSD）可将Agent技能记忆内化到模型参数，无需持续依赖外部检索，但自生成的技能记忆存在噪声、功能纠缠、冗余冲突等问题，直接蒸馏会干扰知识内化甚至降低性能，小模型受限于固有知识储备，该问题尤为突出。

### 方法关键点
- 动态技能筛选：维护Reliability（任务成功率）、Advantage（相对无技能轨迹的性能增益）两个动态指标，通过带时间衰减的Beta分布建模技能价值，结合汤普森采样筛选高价值技能，过滤过时/无效经验
- 三功能视图拆分：将技能记忆拆解为状态感知（场景信息校验）、行动规划（子目标拆解排序）、执行控制（错误检测恢复）三类互补视图，搭配无技能分支、综合视图分支并行探索，降低知识纠缠
- 多向蒸馏机制：基于轨迹成功率匹配蒸馏对，实现技能视图→无技能视图的正向知识迁移、无技能视图→技能视图的反向错误校正、不同技能视图间的跨视图互补知识传递，统一token级蒸馏损失与RL损失联合优化

### 关键实验
在ALFWorld、WebShop、Search-QA三个Agent基准测试，对比GRPO、GiGPO、UCOB等SOTA基线，在Qwen3-1.7B基座上ALFWorld成功率较SOTA提升7.1%，WebShop成功率提升8.1%，无额外推理开销；小模型性能增益远高于大模型，可有效弥补小模型的知识劣势。

最值得记住的一句话：技能记忆内化的核心瓶颈不是知识不足，而是噪声与功能纠缠导致的监督不稳定，通过功能拆分与outcome驱动的自适应蒸馏可以大幅提升知识迁移效率。
