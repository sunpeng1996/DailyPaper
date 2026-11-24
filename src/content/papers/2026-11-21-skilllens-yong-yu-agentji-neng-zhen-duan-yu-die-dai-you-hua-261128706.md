---
title: 'SkillLens: An Interactive Human-LLM System for Diagnosing and Refining Agent
  Skills'
title_zh: SkillLens：用于Agent技能诊断与迭代优化的交互式人-LLM协同系统
authors:
- Shuo Yan
- Rui Sheng
- Xiaoyan Gu
- Lian Lian
- Chengran Xu
- Yifang Wang
affiliations:
- Florida State University
- The Hong Kong University of Science and Technology
- Washington University in St. Louis
- University of Wisconsin–Madison
- Zhejiang University
arxiv_id: '2611.28706'
url: https://arxiv.org/abs/2611.28706
pdf_url: https://arxiv.org/pdf/2611.28706
published: '2026-11-21'
collected: '2026-11-24'
category: Agent
direction: Agent 技能迭代与人机协同优化
tags:
- LLM Agent
- Skill Refinement
- Human-in-the-loop
- Interactive System
- Agent Debugging
one_liner: 打通Agent技能版本、执行证据、人在回路验证链路，实现可解释可追溯的技能迭代优化
practical_value: '- 电商/导购Agent的技能库迭代可直接复用这套链路架构：打通技能版本、benchmark case执行轨迹、效果指标的关联，解决「改了一处技能逻辑，不知道影响哪些场景」的盲调问题，大幅降低回归风险

  - 技能迭代的分层验证流程可直接落地：先小批量Sample Run验证改动效果，再全量Full Run评估，大幅降低大技能库迭代的计算成本和业务风险

  - 多团队维护公共Agent技能库时，可复用全链路留痕设计：所有修改假设、验证结果、决策依据全部可追溯，避免迭代时重复踩历史踩过的坑'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
LLM Agent 依赖的可复用技能迭代目前存在两类痛点：人工调试需要跨日志、版本、测试case多源翻找信息，效率极低；全自动技能优化方法为黑盒，极易出现改对单场景却导致大量旧case回归的问题，开发者无法快速将效果波动与技能修改、执行链路关联，技能库规模扩大后维护难度陡增。

### 方法关键点
- 设计4个联动视图：Performance View 展示跨版本指标变化、case流转分布（如正确→错误、错误→正确的case数量）；Summary View 关联错误模式与技能调用序列，快速定位问题技能；Context View 下钻单case的技能diff、执行轨迹、输出对比，还原根因；Refinement View 支持生成优化假设、分层What-if验证，全链路留痕
- 所有LLM生成的解释、优化建议仅作为参考，最终修改、决策权限完全交给开发者，避免过度依赖LLM的错误结论
- 支持分层验证机制：Sample Run 小批量验证改动效果，Full Run 全量评估，Multiple Runs 排除单次采样波动，平衡迭代速度与可靠性

### 关键实验
基于FRAMES数据集的100个多跳问答case、8个版本的web搜索技能库开展对照实验，对比基线（人工查看原始日志+通用Chat工具链），20名受试者中两组任务完成率均为90%；SkillLens组完成任务的平均耗时24.7分钟，比基线组的32.2分钟快23%；70%的SkillLens受试者提交的证据质量得满分（2/2），比基线组高10个百分点。

### 核心结论
Agent技能迭代的核心不是追求全自动黑盒优化，而是给开发者提供可追溯的证据链路，让人的决策基于真实执行数据而非主观猜测。
