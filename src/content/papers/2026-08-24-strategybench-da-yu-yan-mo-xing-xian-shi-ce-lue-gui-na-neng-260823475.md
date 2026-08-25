---
title: 'StrategyBench: Evaluating Explicit Strategy Induction in Large Language Models'
title_zh: 《StrategyBench：大语言模型显式策略归纳能力评估基准》
authors:
- Jinghan Tan
- Yuanzheng Wang
- Lu Chen
- Zijun Chen
- Yuqian Wang
- Maosong Sun
arxiv_id: '2608.23475'
url: https://arxiv.org/abs/2608.23475
pdf_url: https://arxiv.org/pdf/2608.23475
published: '2026-08-24'
collected: '2026-08-25'
category: Eval
direction: LLM能力评估 · 显式策略归纳
tags:
- Strategy Induction
- In-context Learning
- LLM Evaluation
- Benchmark
- Few-shot Learning
one_liner: 构建评估LLM显式策略归纳能力的基准StrategyBench，开展多维度影响因素分析
practical_value: '- 做Agent任务适配时可加入显式策略归纳步骤，先从少量样本抽取规则再执行，降低ICL对示例构造的敏感性

  - 冷启动少样本场景下可参考generator-executor分离的策略归纳架构，提升优惠券规则适配、用户意图判定等复杂任务准确率

  - 优化少样本prompt时可优先引导LLM先输出任务规则再作答，提升推荐/广告场景下的推理结果稳定性'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
直接few-shot ICL仅利用样本表面特征，未抽象稳定任务规则，对示例构造高度敏感，难以适配数据稀缺、动态迭代的业务场景，而LLM类人的「先归纳规则再应用」的显式策略归纳能力缺乏统一评估基准。

### 方法关键点
从BIG-Bench筛选支持策略归纳的任务集合，标注参考策略，定义「策略质量」「下游效用」两个维度的核心评估指标；从任务差异、模型配置、适配设置三个维度开展分析，覆盖任务类别差异、generator-executor选型、演示样本设计、SFT适配效果等核心变量。

### 关键结果
不同任务类别下显式策略的效用差异极大，最终任务效果同时取决于策略生成质量与执行环节的适配效果。
