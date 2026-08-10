---
title: 'The Optimizer Is the Agent: Reasoning-Driven Search across Prompts, Programs,
  and ML Workflows'
title_zh: 优化器即Agent：跨提示、程序与ML工作流的推理驱动搜索
authors:
- Junbo Li
- Boyi Liu
- Canwen Xu
- Yite Wang
- Yuxiong He
- Zhangyang Wang
- Qiang Liu
- Zhewei Yao
affiliations:
- The University of Texas at Austin
- Snowflake
arxiv_id: '2608.06714'
url: https://arxiv.org/abs/2608.06714
pdf_url: https://arxiv.org/pdf/2608.06714
published: '2026-08-06'
collected: '2026-08-10'
category: Agent
direction: Agent优化 · 跨域推理驱动搜索
tags:
- Agentic Optimization
- Prompt Optimization
- Code Agent
- Hyperparameter Tuning
- Reasoning Search
one_liner: 提出无外部控制器的ReASearch统一Agent框架，跨域优化提示/程序/ML工作流性能超SOTA基线
practical_value: '- 优化推荐/广告场景的系统prompt时，可复用ReASearch的无硬编码控制器架构，替代传统贝叶斯优化、进化算法等外置搜索策略，省掉手动编写启发式规则的成本，同预算下提示效果可提升2%~26%

  - 做推荐模型超参调优、召回/排序链路工作流优化时，借鉴其持久化`lessons.md`+Python执行诊断的设计，自动沉淀调优经验，避免重复踩坑，效率优于黑盒调参工具

  - 优化广告文案、推荐理由等生成类任务时，可复用其「小批量验证效果→确认提升逻辑→高成本验证」的流程，减少不必要的A/B测试开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有提示、程序、ML工作流的优化方案普遍依赖人工设计的外置搜索控制器（如进化算法、贝叶斯优化、多臂老虎机），LLM仅作为局部修改生成器，搜索逻辑与语义推理能力割裂，跨场景适配成本高，且难以基于历史经验做长周期复杂优化。

### 方法关键点
- 无硬编码外层搜索逻辑：所有优化操作（评估、诊断、编辑、验证、回退）均封装为工具，由单个工具调用Agent自主决策全流程，仅需替换领域工具集和系统prompt即可适配不同任务
- 长周期优化支撑：配套上下文压缩机制+持久化`lessons.md`内存，自动记录成败经验、规律与待尝试方向，避免历史信息丢失
- 分场景工具设计：提示优化场景提供批量样本采样、学生模型调用、验证集评估工具；程序/ML工作流优化场景提供代码编辑、实验运行、Python分析工具

### 关键实验
覆盖14个跨域任务，对比GEPA、AdaEvolve、Claude Code等领域SOTA基线，同预算下效果领先2%~40%；Circle Packing任务部分场景结果超过此前人类已知最优值；ML工作流优化中Kaggle加密货币预测任务排名从36位提升至第6位。

### 核心结论
推理不仅可用于解决具体任务，本身就能成为开放式搜索的强大引擎。
