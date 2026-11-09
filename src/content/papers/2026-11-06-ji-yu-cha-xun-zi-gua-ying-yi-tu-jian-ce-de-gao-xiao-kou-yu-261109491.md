---
title: An Effective Spoken Language Understanding Approach Leveraging Query-Adaptive
  Intent Detection
title_zh: 基于查询自适应意图检测的高效口语理解方法
authors:
- Bing-Long Kuo
- Yu-Hsuan Fang
- Tien-Hong Lo
- Hsueh-Wei Liao
- Berlin Chen
affiliations:
- National Taiwan Normal University
- Realtek Semiconductor Corp.
arxiv_id: '2611.09491'
url: https://arxiv.org/abs/2611.09491
pdf_url: https://arxiv.org/pdf/2611.09491
published: '2026-11-06'
collected: '2026-11-09'
category: QueryRec
direction: 查询意图理解 · 检索增强ICL
tags:
- Intent Detection
- Spoken Language Understanding
- In-Context Learning
- Retrieval Augmented
- Prototype Learning
one_liner: 提出两阶段原型引导检索框架APEX，免微调提升LLM口语理解的上下文学习效果
practical_value: '- 做搜索/语音助手query意图识别时，可复用两阶段检索思路：先匹配query与各意图的原型embedding筛选Top-K候选意图，再在限定范围内检索ICL示例，避免语义相似但意图不符的示例干扰效果

  - 意图原型可直接用类别下所有训练样本的embedding均值构造，无需额外训练，轻量化易落地，适合无法频繁SFT的业务场景

  - 针对低置信度（高PPL）的模糊query、ASR转写错误多的语音query场景，该方法收益远高于普通全局检索，可优先落地

  - ICL选示例时，优先保证正确意图的覆盖率，比单纯选语义最相似的示例对提升任务准确率更有效'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
免微调的LLM上下文学习（ICL）是降低口语理解（SLU）、搜索query意图识别等场景迭代成本的核心方案，但传统基于query语义相似度的示例检索，容易选到语义接近但意图完全不符的示例，严重干扰ICL预测效果，尤其在ASR转写错误多、query语义模糊的场景下问题更突出。
### 方法关键点
- 两阶段检索框架APEX无额外训练参数：第一阶段做原型引导的候选意图筛选，第二阶段在候选意图范围内检索上下文示例
- 意图原型直接取对应类别所有训练样本的embedding均值，一次性预计算后固化使用，轻量化易实现
- 先通过query与意图原型的余弦相似度筛选Top-K候选意图，缩小检索范围后再在候选池内检索最相似的样本构造ICL prompt
### 关键实验
在SLURP口语理解基准数据集上测试，对比传统全局query检索基线：Qwen3-4B、Gemma-3-4B的Exact Match Accuracy（EMA）分别提升4.34、3.97个百分点；在高PPL（语义模糊）query子集上，Qwen3-4B的EMA提升可达7.66个百分点；所有输入场景下APEX的正确意图覆盖率均显著高于传统检索方法。
### 核心结论
ICL示例检索时引入类别级先验做粗筛，比单纯依赖样本级语义相似度的收益更高，且实现成本极低。
