---
title: Do LLM-Generated Skills Make Better AI Data Scientists? A Component Ablation
  Across Data-Science Workflows
title_zh: LLM生成技能能否优化AI数据科学Agent？工作流全组件消融研究
authors:
- Wei-Jung Huang
affiliations:
- Independent Researcher
arxiv_id: '2607.07504'
url: https://arxiv.org/abs/2607.07504
pdf_url: https://arxiv.org/pdf/2607.07504
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: Agent技能生成 提示策略消融评估
tags:
- LLM Agent
- Prompt Engineering
- Skill Generation
- Ablation Study
- Data Science Agent
one_liner: 通过9种模型配置、超9000次实验验证单样本生成的LLM技能对数据科学Agent无显著性能增益
practical_value: '- 搭建Agent复用技能库时，不要默认采用LLM单次生成的单份技能文件，优先选择专家编写或多轮迭代校验的技能模板，避免无效投入

  - 验证技能收益时需设置token匹配的无关内容对照组，排除prompt长度、格式本身对结果的干扰，避免误判技能有效性

  - 电商/推荐场景的SQL生成、数据清洗等重复性Agent任务，若验证生成技能无增益，可直接用任务原生prompt简化链路，降低维护成本'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
专家编写数据科学Agent的复用技能文件成本高、跨任务维护负担重，行业尝试用LLM生成技能降低人工成本，但缺少系统性的有效性验证。

### 方法关键点
覆盖数据准备、抽取、统计分析、报表4个数据科学工作流阶段，在56个任务、9种模型配置、3家LLM服务商上做全组件消融，累计完成7560次主实验+1512次token匹配对照实验，对比全生成技能、消融组件版技能、无技能prompt、无关格式内容的效果差异。

### 关键结果数字
所有生成技能（含消融变体）相对原生任务prompt均无显著性能提升，p值均≥0.396，不同变体间性能差仅1.2pp；完整生成技能效果与无关的同格式内容基本一致，单份单次生成的技能无法作为默认提示策略。
