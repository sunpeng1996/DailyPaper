---
title: 'Ask Before You Optimize: Dynamic Pre-Formulation Clarification for Interactive
  Optimization'
title_zh: 优化前先提问：交互式优化的动态预建模澄清机制
authors:
- Sihan Ge
- Yichen Lin
- Chenyu Zhou
- Jianghao Lin
- Tao Yao
- Dongdong Ge
affiliations:
- Cardinal Operations
- Shanghai Jiao Tong University
arxiv_id: '2609.05258'
url: https://arxiv.org/abs/2609.05258
pdf_url: https://arxiv.org/pdf/2609.05258
published: '2026-09-03'
collected: '2026-09-07'
category: Agent
direction: Agent 交互式需求澄清优化
tags:
- LLM Agent
- Interactive Optimization
- Clarification
- Benchmark
- Stopping Strategy
one_liner: 提出OR-Clarify澄清基准与双阶段InterOPT框架，实现优化建模前的需求主动澄清与停止决策
practical_value: '- 做需求对齐类Agent（如电商运营需求转推荐策略、广告投放优化需求建模）时，可复用「gap跟踪+动作选择」双阶段架构，先识别对结果有决定性影响的核心信息缺口，再针对性提问，避免无效交互

  - 交互Agent的停止决策可借鉴分级槽位方案：明确划定「必须澄清的高优先级缺口」（对应论文P0/P1槽位），仅当所有高优缺口补齐后才允许停止，可大幅降低静默假设导致的业务错误

  - 用户意图澄清场景（如搜索Query歧义消解、个性化推荐需求澄清）可借鉴Choice式交互设计，给用户提供选项而非开放提问，既提升澄清准确率，又降低用户交互负担

  - 做Agent能力评测时，可复用OR-Clarify的「隐藏槽位+模拟用户+事后判分」框架，不需要人工实时介入就能量化交互澄清的准确率、交互成本、停止合理性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM驱动的优化建模方案默认输入需求完整，但真实业务场景（如电商供应链优化、广告投放预算分配）的用户需求常缺失关键约束、目标或业务规则，直接建模会产生完全错误的结果。现有评测体系普遍假设需求完备，忽视了「何时需要澄清」的决策能力，也没有专门基准衡量预建模阶段的澄清效果。
### 方法关键点
- 构建OR-Clarify基准：从已标注的完整运筹优化任务中，掩码约半数会改变建模结构的核心事实作为隐藏槽位（分P0阻断级、P1核心级、P2次要级三个优先级），支持开放提问、选项式提问两种交互模式，评测指标覆盖槽位恢复率、停止行为合理性、静默假设数量、交互成本4个维度。
- 提出InterOPT双阶段框架：第一阶段Dynamic Gap Search跨轮次跟踪未解决的建模核心缺口，从目标权衡、决策范围、运营约束、时间边界等6个维度识别未明确的业务条件；第二阶段Gap-Guided Action Search基于当前缺口决定提问内容或停止，提问优先绑定已识别的核心缺口，避免无效交互。
### 关键实验
基于OR-Clarify的100个案例共178个隐藏槽位验证，对比FreeQA、ORPilot、GATE等基线：选项式场景下InterOPT的Core Exact（核心槽位完全恢复率）达67.5%，比MC-D基线高16.9个百分点，单次运行静默假设数降至0.366；开放提问场景下InterOPT Core Exact达53.8%，和现有SOTA基线性能相当。
### 核心结论
优化类Agent的能力不仅体现在建模求解的准确性，更要在建模前先判断「现有信息是否足够支撑正确建模」，需澄清时主动提问，信息完备时及时停止。
