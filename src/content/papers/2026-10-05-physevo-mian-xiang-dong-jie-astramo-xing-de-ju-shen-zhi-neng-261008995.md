---
title: 'PhysEvo: Astra Can Act, Let It'
title_zh: PhysEvo：面向冻结Astra模型的具身智能递归自进化框架
authors:
- Wenqing Tian
- Zeyu Zhang
- Zhaocheng Liu
- Fengwei Liu
- Qiang Liu
- Liang Wang
affiliations:
- University of Chinese Academy of Sciences
- Institute of Automation, Chinese Academy of Sciences
- Tsinghua University
- Independent Researcher
arxiv_id: '2610.08995'
url: https://arxiv.org/abs/2610.08995
pdf_url: https://arxiv.org/pdf/2610.08995
published: '2026-10-05'
collected: '2026-10-08'
category: Agent
direction: 具身Agent · 递归自优化
tags:
- Embodied Agent
- Recursive Self-Improvement
- Frozen LLM
- Meta Agent
- Robot Manipulation
one_liner: 围绕冻结Astra模型构建双Agent递归自进化框架，无需权重更新即可大幅提升具身任务性能
practical_value: '- 双Agent（任务执行+Meta优化）自迭代架构可复用在推荐策略调优场景：任务Agent跑线上流量，Meta Agent自动分析bad
  case迭代召回/排序规则，无需频繁重训基座模型

  - 冻结大模型+工具/技能迭代的思路可降低LLM4Rec部署成本：无需反复做LoRA微调，仅通过优化Prompt模板、检索工具链即可持续提升推荐效果

  - 基于执行轨迹的闭环迭代验证机制可迁移到电商大促策略调优：修订后的规则先在模拟环境验证效果再放量，降低线上业务风险'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有基于大模型的具身Agent要么依赖模型权重更新、额外训练专用策略，迭代成本极高；要么直接调用大模型的零/少样本方案在复杂操纵任务上成功率极低，无法落地。
### 方法关键点
1. 双Agent递归自进化架构：任务Agent基于当前工具集执行机器人任务，Meta Agent基于执行轨迹诊断失败原因、修订工具与技能、验证修正效果，还可迭代自身的诊断工具
2. 全程冻结基座Astra模型权重，无需额外训练动作策略，所有优化沉淀为可复用的工具、技能与规则
### 关键结果
- 42个RoboDojo任务平均得分68.14/100，成功率62.00%，比SOTA的RoboDawn 1-shot Astra高出14.83个百分点
- 8项Astra直接调用困难的操纵任务成功率从1.25%提升至55.00%
- 真实世界5项任务25次试验平均得分90.60/100，成功率达84.00%
