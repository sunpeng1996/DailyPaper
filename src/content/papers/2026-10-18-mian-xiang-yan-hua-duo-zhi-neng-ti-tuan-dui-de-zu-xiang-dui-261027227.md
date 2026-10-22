---
title: Which Agent's Skill Should Change? Group-Relative Credit Assignment for Evolving
  Multi-Agent Teams
title_zh: 面向演化多智能体团队的组相对技能信用分配方法GRSE
authors:
- Yanan Ma
- Yang Wang
- David Le
- Chenhan Yuan
- Yizheng Sun
- Guangwei Zhang
- Chenghao Xiao
- Chenghua Lin
- Imon Banerjee
affiliations:
- Mayo Clinic
- University of Manchester
- Alibaba Group
- Shanghai University of Finance and Economics
arxiv_id: '2610.27227'
url: https://arxiv.org/abs/2610.27227
pdf_url: https://arxiv.org/pdf/2610.27227
published: '2026-10-18'
collected: '2026-10-22'
category: MultiAgent
direction: 多智能体协作 · 技能演化信用分配
tags:
- Multi-Agent
- Credit Assignment
- Skill Evolution
- GRPO
- LLM Agent
one_liner: 基于同问题多轮执行对比实现多智能体技能精准归因，训练免参数更新，多跳问答F1较SOTA最高提升6.7
practical_value: '- 电商多智能体链路（比如检索+选品+文案生成多Agent协作）可复用GRSE的组对比归因方案，精准定位链路中需要优化的Agent与技能，无需全链路重训

  - 可直接复用结构化故障诊断+验证门设计：预设8种故障类型、关联执行步骤、编辑动作，每次技能更新前先做小流量验证，避免负向效果

  - 多跳任务（复杂query理解、多轮导购对话）的技能演化可参考同问题多轮采样对比思路，避免将成功/失败归因为无关技能，降低负向优化概率

  - 预算有限场景可优先用G=4的组采样，复用GRPO归一化方法生成相对优势，仅增加1.3-1.8倍训练耗时，归因精度远高于单轨迹方案'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多智能体技能演化方法基于单轨迹做信用分配，常把仅在成功轨迹中出现但实际有害的技能错判为正向，无法精准定位链路中真正需要优化的Agent和技能，尤其是上下游依赖的多跳任务，错误容易被传导（比如检索缺失正确数据，推理Agent反而被判错）。大模型微调成本高，固定参数仅优化技能的方案亟需更精准的归因能力。

### 方法关键点
- 分组滚动：同问题、固定技能库下采样G=4次完整团队执行轨迹，参考GRPO计算每组内的相对优势，消除环境和问题本身的干扰
- 组相对批评家：跨轨迹对比每个Agent的行为和上下游传递信息，给Agent-技能对分配信用，附带结构化故障诊断（预设8种故障类型、关联失败/成功步骤、编辑动作），并做归因校验，排除无证据的归因
- 跨问题聚合：按故障模式聚合多问题的归因结果，避免单轮采样的偶然性
- 验证门：每个技能更新后先在验证集测试，只有不低于原有效果才保留，避免负向更新

### 关键实验
在HotpotQA、LoCoMo两个问答数据集上测试，对比SOTA方法MASkills：HotpotQA上Qwen3.8作为基座时F1提升3.1；LoCoMo多跳任务下Qwen3.8基座F1提6.7、Gemma4基座提3.2；含植入有害技能的脏库修复场景，GRSE恢复到干净库水平（+6.3F1），MASkills反而比初始分低2.2F1。

最值得记住的一句话：多智能体系统的信用分配不要只看单轨迹的技能出现与否，同任务多轮执行的行为对比才是精准定位责任的核心
