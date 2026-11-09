---
title: 'From Procedures to Permissions: Learning Precise Subagent Authorization from
  Agent Skills'
title_zh: 从流程到权限：基于Agent技能的精准子代理授权学习方法
authors:
- Wenkai Yu
- Ning Ding
- Wentao Zhang
- Yehui Tang
affiliations:
- Peking University
- Samsung Research, Beijing
arxiv_id: '2611.08905'
url: https://arxiv.org/abs/2611.08905
pdf_url: https://arxiv.org/pdf/2611.08905
published: '2026-11-06'
collected: '2026-11-09'
category: MultiAgent
direction: 多Agent协作 · 子代理授权优化
tags:
- MultiAgent
- Agent Skill
- Authorization
- Synthetic Data
- SFT
one_liner: 基于Agent技能的程序性知识生成带授权监督的训练数据，提升多Agent子代理授权精度
practical_value: '- 电商多Agent系统（客服、运营、商品审核等分工场景）可复用「基于Agent技能SOP推导最小授权范围」思路，避免子代理越权访问用户隐私、商品敏感数据，同时降低权限不足导致的任务失败

  - 训练自定义Agent时，可借鉴技能驱动的合成数据范式：先从技能定义生成任务与SOP，再执行生成轨迹，经独立LLM校验后做SFT，比仅用执行轨迹的监督信号更精准，尤其适合权限边界、操作规范类任务训练

  - 涉及Agent权限管控的业务场景（广告投放、商家运营Agent等）可复用其四维度校验逻辑，从「交付物正确性、无权限违规、轨迹自然度、技能正确使用」做Agent行为审计，降低业务风险'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多Agent系统执行复杂任务时需要将子任务委派给专用子代理，主代理不仅要决定子代理的执行内容，还要分配合理的工具、工作空间资源权限；现有方案仅依靠任务结果、执行轨迹做监督，只能知晓子代理访问了什么资源，无法确定其实际需要的最小权限范围，容易出现权限过度授予或不足的问题，既影响任务成功率也带来数据安全风险。

### 方法关键点
- 利用Agent Skills封装的程序性知识，合成具体任务与对应分步执行SOP，明确每个子任务步骤需要的工具、资源范围
- SOP仅在轨迹合成阶段提供给教师Agent，生成包含子代理授权范围、执行过程的轨迹，不会出现在最终训练数据中，避免模型推理时依赖SOP
- 引入独立LLM做轨迹校验，从交付物正确性、无权限违规、轨迹自然度、技能正确使用四个维度筛选合格轨迹，用于SFT训练

### 关键实验
在ClawArena-Team多Agent编排基准上，对比Base、Chain-of-Agents、ToolMind等基线，Qwen3.5-35B-A3B版本工具权限精度提升13.4pp，工作空间权限精度提升24.1pp，整体任务成功率提升11.6pp；在Terminal-Bench 2.1、SkillsBench上性能也保持行业竞争力。

最值得记住的结论：Agent技能的程序性知识可提供任务结果无法覆盖的细粒度授权监督，是提升多Agent编排可靠性的核心信号来源。
