---
title: 'Beyond Weight Updates: Evolving Agent Harnesses for Domain Specialization'
title_zh: 不依赖权重更新：面向领域专用化的Agent Harness演化方法
authors:
- BoHao Chen
affiliations:
- Independent Researcher
arxiv_id: '2611.25380'
url: https://arxiv.org/abs/2611.25380
pdf_url: https://arxiv.org/pdf/2611.25380
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: Agent领域专用化 · Harness演化
tags:
- Agent Specialization
- Harness Evolution
- GEPA
- Domain Adaptation
- Reinforcement Learning
one_liner: 提出不更新LLM权重仅优化Agent Harness的GEPA方案，低成本实现领域适配且可与权重训练互补
practical_value: '- 垂直业务Agent快速迭代优先走Harness优化路径，无需GPU训练，仅优化系统prompt、工具schema、技能库即可获得55%~110%的权重训练级收益，适配周期从数天压缩到数小时

  - 多场景Agent部署可采用Harness Adapter架构，不同业务域的适配包独立加载、互不干扰，避免SFT带来的跨场景遗忘、推理链截断问题，兼顾业务效果和通用能力保留

  - Harness优化可与LoRA/RL等权重更新方案组合使用，峰值效果优于单一路径，可先用Harness快速上线验证需求，再用权重训练做深度性能提升'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent领域专用化普遍依赖SFT/RL等权重更新方案，存在GPU成本高、推理链截断/格式鲁棒性下降、跨领域遗忘等问题，而手工设计的Harness（系统prompt、工具、技能库等）作为Agent核心组件，其优化价值未被充分挖掘。

### 方法关键点
- 将Agent领域专用化建模为权重θ和Harness H的联合优化问题，Harness包含系统prompt、工具schema、技能库、上下文策略、规划流程5部分，优化时完全冻结模型权重
- 基于GEPA反射式演化算法优化Harness，以任务成功率、token成本、延迟为帕累托优化目标，通过失败轨迹反思生成prompt/工具/技能的编辑突变，搭配交叉选择保留最优Harness基因型，最终输出可插拔的领域Adapter
- 支持多Adapter组合，重叠字段采用右偏覆盖规则，适配多业务域叠加需求

### 关键实验
在SWE-bench Verified、OfficeBench、Terminal-Bench三个Agent基准上对比4种配置：基线效果分别为0.31、0.28、0.35；仅权重更新（SAO）效果为0.52、0.49、0.55；仅Harness优化（GEPA）效果为0.48、0.51、0.46，获得权重训练55%~110%的收益，GPU训练成本为0，仅需4小时运行时间；二者组合效果最优，分别为0.61、0.63、0.64。同时验证Harness优化不会带来SFT常见的推理截断率上升（SFT从8.8%升至13.2%，Harness优化无变化）、格式鲁棒性下降问题。

### 核心结论
Agent领域专用化不是单纯的权重更新问题，大部分垂直场景下的效果提升来源于模型外围的Harness脚手架优化，可低成本、非破坏性地实现
