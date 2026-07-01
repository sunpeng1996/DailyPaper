---
title: 'SafePyramid: A Hierarchical Benchmark for In-context Policy Guardrailing'
title_zh: SafePyramid：面向上下文策略护栏的分层评测基准
authors:
- Jiacheng Zhang
- Haoyu He
- Sen Zhang
- Shen Wang
- Xiaolei Xu
- Yuhao Sun
- Meng Shen
- Feng Liu
affiliations:
- ByteDance
- The University of Melbourne
arxiv_id: '2606.29887'
url: https://arxiv.org/abs/2606.29887
pdf_url: https://arxiv.org/pdf/2606.29887
published: '2026-06-28'
collected: '2026-06-30'
category: Eval
direction: LLM安全护栏 · 分层评测基准
tags:
- Guardrail
- LLM Safety
- Benchmark
- In-context Learning
- Policy Evaluation
one_liner: 推出覆盖10个域的三层难度上下文策略护栏评测基准，完成15款前沿模型与护栏的能力摸底
practical_value: '- 电商/广告/推荐Agent的自定义合规护栏上线前，可复用三层难度测试范式，依次验证单规则理解、规则依赖推理、新政策适配能力，提前规避上线安全风险

  - 业务合规规则迭代频繁的场景，可参考上下文注入自定义规则的护栏设计范式，无需重新训练模型，大幅降低规则迭代的研发成本

  - 搭建业务自定义安全护栏时，可直接引入SafePyramid公开数据集做预测试，优先选择L0/L1准确率更高的底座模型，平衡效果与部署成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM安全护栏多依赖预定义风险分类，无法适配电商、广告等业务场景频繁迭代、高度定制化的合规规则需求，缺乏对上下文注入式自定义策略护栏的系统性评测方法。

### 方法关键点
SafePyramid分层基准覆盖10个业务域、1000组多轮对话、3000套业务定制政策、共61699条自然语言规则，设置三层难度评测维度：L0评测单规则理解能力，L1评测规则依赖推理能力，L2评测全新政策框架适配能力，通过多阶段构造校验流水线保证数据质量。

### 关键结果
完成10款前沿LLM、5款可配置政策护栏的评测，最优性能的GPT-5.5在L0/L1/L2难度下的全违规规则准确识别率仅为54.0%、35.3%、12.9%，当前上下文策略护栏能力存在显著短板。
