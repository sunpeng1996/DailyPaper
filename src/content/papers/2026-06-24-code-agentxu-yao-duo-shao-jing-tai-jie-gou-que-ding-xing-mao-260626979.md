---
title: How Much Static Structure Do Code Agents Need? A Study of Deterministic Anchoring
title_zh: Code Agent需要多少静态结构？确定性锚定研究
authors:
- Zhihao Lin
- Mingyi Zhou
- Yizhuo Yang
- Li Li
affiliations:
- Beihang University
arxiv_id: '2606.26979'
url: https://arxiv.org/abs/2606.26979
pdf_url: https://arxiv.org/pdf/2606.26979
published: '2026-06-24'
collected: '2026-06-30'
category: Agent
direction: Code Agent 静态结构性能优化
tags:
- Code Agents
- static analysis
- LLM agents
- deterministic anchoring
- reproducibility
one_liner: 研究静态结构对grep-first代码Agent的影响，提出确定性锚定并给出实用部署指南
practical_value: '- 对检索增强型Agent，可将离线提取的确定性结构以inline注释方式注入检索上下文，无需修改原有Agent控制流，低侵入提升效果与稳定性

  - 可针对知识库规模适配结构粒度：中小规模用全量双向结构，大规模hub-heavy场景仅保留反向依赖，减少冗余token和检索偏差

  - 确定性锚定可大幅降低Agent run-to-run方差，减少生产环境best-of-N重复运行的总成本

  - LLM可将不完整的结构信息作为软提示使用，轻量不完备的静态分析已经足够带来收益，降低工程落地门槛'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：当前主流grep-first代码Agent依赖关键词检索，无法暴露代码库固有结构关系（调用、继承、配置依赖等），导致LLM导航随机性强、运行可复现性差，跨文件依赖任务容易出错；已有图架构Agent性能反而低于纯grep强基线，需要低侵入方式给现有基线注入结构信息。

**方法关键点**：
- 提出CodeAnchor框架，离线做轻量静态分析，提取各类结构关系，转换成plain-text注释标签（确定性锚点）注入到对应代码实体旁；
- 无需修改原有Agent的检索-推理循环，Agent通过原有关键词检索就能同时获得代码和结构标签，实现检索短路，减少多轮探索搜索；
- 支持多种配置：轻量拓扑（仅调用/继承/导入/包含）、全量稠密标签（增加数据流/配置依赖）、反向仅链接（仅保留「谁调用我」，去掉前向链接）。

**关键结果**：在SWE-bench Lite/Verified基准，基于Codex基线测试：轻量拓扑相比基线提升Func@5 +2.2pp（Lite）/+1.2pp（Verified），减少交互轮次-1.6轮，Pass@1提升+3.4pp；稠密标签边际收益递减，仅挽救少数隐式依赖任务，额外增加18%+token开销；中等规模Repo适合双向链接，大规模hub-heavy Repo适合反向仅链接；确定性锚定将run-to-run方差降低约一半，链接跟随率从0.15-0.18提升到0.21-0.24。

最值得记住的结论：静态结构更多是让Agent导航更规范可复现，而非让Agent更聪明，轻量确定性锚定就足够。
