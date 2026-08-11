---
title: 'MMOOC: A Comprehensive Benchmark for Out-of-Context Evaluation in Multimodal
  Large Language Models'
title_zh: 多模态大模型上下文偏离评估综合基准MMOOC
authors:
- Wenjie Zhu
- Yabin Zhang
- Wenjun Zeng
- Lei Zhang
affiliations:
- The Hong Kong Polytechnic University
- Eastern Institute of Technology, Ningbo
- Harbin Institute of Technology (Shenzhen)
arxiv_id: '2607.27637'
url: https://arxiv.org/abs/2607.27637
pdf_url: https://arxiv.org/pdf/2607.27637
published: '2026-07-31'
collected: '2026-08-11'
category: Eval
direction: 多模态大模型鲁棒性评估基准
tags:
- MLLM
- Benchmark
- Out-of-Context
- Robustness
- LLM-as-a-Judge
one_liner: 构建包含41K+图文对的多模态基准，覆盖可答/不可答上下文偏移场景，评估MLLM回答与拒答平衡能力
practical_value: '- 搭建多模态商品导购Agent时，可复用MMOOC的8种上下文偏移类型设计测试用例，降低模型回答商品不存在属性的hallucination风险

  - 评估多模态理解模型鲁棒性时，可直接采用「Accuracy+Refusal Rate+LLM-as-a-Judge」三维指标体系，平衡幻觉率和服务可用性

  - 针对多模态模型在上下文偏移下的失效模式，可参考论文结论通过post-training做针对性微调，提升模型鲁棒性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前MLLM在上下文偏移场景下极易出现两种问题：对真正不可答的OOC（主体级上下文偏移）问题 hallucination 回答，或对仍可答的Shifted IC（非主体上下文偏移）问题过度拒答，现有评估基准仅覆盖不可答OOC场景，忽略可答偏移场景，偏移类型覆盖有限。
### 方法关键点
构建41K+规模的图文对基准MMOOC，包含可答Shifted IC、不可答OOC两类样本，覆盖3种问题格式、8种偏移类型、6种视觉场景，通过MLLM自动过滤+人工校验双重保障数据质量；评估维度除准确率、拒答率外，新增LLM-as-a-Judge指标判断模型推理逻辑正确性。
### 关键结果
实验验证当前主流MLLM均无法很好平衡回答与拒答能力；针对性post-training可有效提升模型在上下文偏移场景下的鲁棒性。
