---
title: 'Mara Chain: Rethinking Failure as a Stepping Stone for AI System Auto-Evolution'
title_zh: Mara Chain：将失败候选作为垫脚石的AI系统自动进化方法
authors:
- Yubin Lyu
- Fu Li
- Jiawei Fei
- Yang Zhao
- Weixing Mei
- Yinan Wu
affiliations:
- Ant Group
- Beijing Intelligent Game and Decision Lab
- Beijing Defense Innovation Institute
arxiv_id: '2609.35855'
url: https://arxiv.org/abs/2609.35855
pdf_url: https://arxiv.org/pdf/2609.35855
published: '2026-09-24'
collected: '2026-10-10'
category: Agent
direction: Agent 自进化 · 失败候选迭代优化
tags:
- Agent
- Self-Optimization
- Auto-Evolution
- Artifact Optimization
- LLM
one_liner: 保留并迭代优化被拒绝的候选配置，大幅提升AI系统artifact优化的性能与样本效率
practical_value: '- 优化电商场景的prompt、Agent技能、检索pipeline时，不要直接丢弃未达验收阈值的候选，保留其运行日志、错误分析、修改历史，基于历史迭代可大幅降低试错成本，适配搜索query改写、推荐prompt调优、RAG
  pipeline优化等场景

  - 候选池管理可复用Pareto过滤+Top-N截断方案，既保留不同子任务上表现优异的互补候选，又避免候选池无限膨胀，平衡探索效率与资源开销

  - 多维度领导权重的父候选采样策略，可直接用于多目标优化场景（如电商推荐同时优化点击率、转化率、客单价），避免单指标排序丢失优质候选'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前部署态AI系统的优化大多是修改prompt、技能、配置、代码等artifact而非模型权重，现有propose-evaluate-select流程会直接丢弃未达验收阈值的候选，导致后续优化重复触发相同失败模式，样本效率极低，甚至长期卡在性能瓶颈无法突破。
### 方法关键点
- 反射优化触发：新候选未达验收标准时，启动Mara Chain流程，保留该候选的运行轨迹、残留错误、结构化分析、修改历史，基于累计上下文迭代生成下一代候选
- 成本边界控制：每条优化链设置固定深度，若全程未产出达标候选则直接丢弃整条链，避免无限制消耗资源
- 候选池两级筛选：先通过Pareto过滤剔除被支配的候选，再保留平均验证分最高的Top-N个候选，既保留互补性优质解，又控制池规模
- 父代加权采样：按候选在各维度的领先次数加权采样，优先选择在不同子任务上表现突出的候选作为父代
### 关键结果
在三类场景验证：AppWorld技能优化，相对GEPA等基线性能最高提升20.5%，达标所需rollout减少65.5%；TerminalBench 2.1 Agent harness优化，通过率比AHE、Meta-Harness分别高20.2、22.5个百分点；MuSiQue检索管道优化，比手工基线nDCG@10提升0.104、Recall@10提升0.131。
### 核心结论
被丢弃的失败候选从来不是无效成本，而是突破性能瓶颈的核心垫脚石。
