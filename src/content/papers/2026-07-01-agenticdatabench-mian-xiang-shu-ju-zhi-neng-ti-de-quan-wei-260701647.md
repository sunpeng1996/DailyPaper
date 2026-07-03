---
title: 'AgenticDataBench: A Comprehensive Benchmark for Data Agents'
title_zh: AgenticDataBench：面向数据智能体的全维度评测基准
authors:
- Zhaoyan Sun
- Shan Zhong
- Daizhou Wen
- Jiaxing Han
- Guoliang Li
- Ying Yan
- Peng Zhang
- Yu Su
- Xiang Qi
- Baolin Sun
affiliations:
- Tsinghua University
- Ant Group
arxiv_id: '2607.01647'
url: https://arxiv.org/abs/2607.01647
pdf_url: https://arxiv.org/pdf/2607.01647
published: '2026-07-01'
collected: '2026-07-03'
category: Agent
direction: Agent评测 · 数据科学场景
tags:
- Data Agent
- Benchmark
- Skill Extraction
- Task Generation
- LLM Evaluation
one_liner: 构建覆盖15个领域、433项数据科学技能的细粒度数据Agent评测基准，配套开源测试框架
practical_value: '- 可复用分层技能抽取方法：从电商/推荐业务历史数分、特征工程、建模任务中抽取高频操作技能，量化Agent在用户标签计算、A/B实验分析、推荐效果归因等场景的短板，针对性优化Prompt或工具链

  - 参考技能驱动的任务生成框架：基于业务真实技能组合自动生成评测任务，大幅降低业务场景下Agent评测的人工标注成本，支撑Agent能力快速迭代

  - 复用双层评估逻辑：采用「输出结果匹配+技能级错误溯源」的评估方法，比单纯Pass@1更精准定位Agent在推荐特征清洗、多源数据对齐等环节的具体缺陷，大幅提升调优效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有数据Agent评测基准普遍覆盖任务类型有限，缺乏真实业务场景的复杂度与数据规模，且仅提供粗粒度聚合打分，无法定位Agent在具体操作环节的能力缺陷，难以支撑工业级数据Agent的研发与迭代优化。

### 方法关键点
- 分层技能抽取：从Stack Overflow 6510个高质量数分任务解决方案中，通过LLM拆解→文本嵌入聚类→LLM语义提纯→专家校验的流程，抽取出7大类共433项可量化的数据科学技能，完整覆盖数据处理、分析、建模全流程
- 任务构建：从蚂蚁集团真实业务中筛选102个高技能多样性的真实任务，再基于技能频率关联图+LLM自动生成242个跨10个公共领域的补充任务，共344个评测实例，覆盖所有433项技能
- 细粒度评估：提供5种输出匹配评分模式（表格/模型/JSON/图表/文本）+ 技能级错误溯源的双层评估逻辑，开源完整测试框架和Docker执行环境

### 关键结果
基准覆盖15个垂直领域（含5个蚂蚁真实B2B业务场景），单任务平均对应493.4MB数据、113.6行解决方案代码、23.5项技能，真实性与复杂度远超现有同类基准。测试4种主流Agent框架搭配3款SOTA LLM，最优组合（CodeX+Kimi-K2.5）整体准确率仅48.8%，电商、营销等复杂业务场景准确率不足37%；单任务平均消耗20+执行步骤，成本0.1~1.6美元。

### 核心结论
当前数据Agent在工业级复杂业务场景的落地能力仍有极大缺口，细粒度技能级评估是针对性优化的核心前提
