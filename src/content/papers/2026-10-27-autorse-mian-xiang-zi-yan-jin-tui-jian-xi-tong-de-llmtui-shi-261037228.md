---
title: 'AutoRSE: Evaluating LLM Agents as Recommendation Engineers for Self-Evolving
  Recommender Systems'
title_zh: AutoRSE：面向自演进推荐系统的LLM推荐工程师Agent评估框架
authors:
- Rui Tian
- Yi Fang
- Yejin Hua
- Du Wang
- Yuzhe Wang
- Minxuan Shan
- Zirui Ren
- Xinyu Lin
- Chongming Gao
- Wenjie Wang
affiliations:
- University of Science and Technology of China
- National University of Singapore
arxiv_id: '2610.37228'
url: https://arxiv.org/abs/2610.37228
pdf_url: https://arxiv.org/pdf/2610.37228
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: 推荐系统Agent · 能力评估与边界分析
tags:
- LLM Agent
- Recommender System
- Benchmark
- AutoML
- Self-Evolving
one_liner: 构建统一评估框架benchmark主流RSE-Agent，明确当前Agent能力边界与核心瓶颈
practical_value: '- 可复用AutoRSE的12小时单GPU自动化调优工作流，部署到内部推荐算法迭代场景，替代初级算法工程师的超参调优、模型集成、训练策略调整等重复工作，降低人力成本

  - 业务落地时可优先构建内部推荐算法专利/顶会论文/竞赛方案的idea库，给Agent做前置注入，实测比Agent自主生成创意额外提升性能13.35%

  - 针对新上线的生成式推荐场景（Semantic ID召回、序列生成推荐等）优先用RSE-Agent优化，这类场景基线不饱和，平均相对提效可达29.2%，远高于CTR预测等成熟场景的3.1%

  - 自研RSE-Agent优先选择LLM+原生harness组合（如GPT-5.5+Codex、Claude Opus+Claude Code），相比第三方harness性能提升接近1倍'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前RSE-Agent已可自主迭代推荐算法，但缺乏统一评估框架，能力边界与核心瓶颈不清晰，现有方案多为私有工业pipeline，无法横向对比不同Agent的优化效果。

### 方法关键点
- 搭建AutoRSE评估框架，覆盖6类工业级推荐任务（3类生成式推荐+3类CTR预测），每个任务提供SOTA基线代码、H200单GPU沙箱环境、12小时优化预算，全程禁止联网与访问测试集标签
- 设计轨迹级分析pipeline，将Agent优化动作分为6类：3类工程优化（超参调优、模型集成、训练策略调整）+3类算法创新（特征建模、架构修改、目标函数优化），配套0-4分的算法novelty评估标准
- 开展idea注入实验，对比自主生成创意、注入顶会/专家创意两类场景下的Agent优化效果

### 关键结果
测试3款前沿LLM+3款主流Agent harness的7种组合，在5/6任务上可稳定超越基线，平均相对提升16.1%；其中Claude Code+Claude Opus 4.8、Codex+GPT-5.5的平均提升超过24%。轨迹分析显示91.7%的优化动作属于工程优化，仅8.3%为算法创新，当前Agent平均novelty得分仅2.42/4，停留在使用标准组件的探索级水平。注入外部高质量idea后，Agent平均性能比自主生成创意额外提升13.35%，算法novelty提升0.58分。

最值得记住的一句话：当前RSE-Agent仅能胜任推荐算法的工程调优工作，若要实现突破性性能提升，必须优先解决算法创意生成的瓶颈问题。
