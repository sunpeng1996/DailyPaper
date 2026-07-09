---
title: 'HoloCount: A Holistic Visual Counting Benchmark for MLLMs'
title_zh: HoloCount：面向多模态大模型的全局视觉计数基准
authors:
- Jinhong Deng
- Limeng Qiao
- Guanglu Wan
affiliations:
- Meituan
arxiv_id: '2607.06420'
url: https://arxiv.org/abs/2607.06420
pdf_url: https://arxiv.org/pdf/2607.06420
published: '2026-07-07'
collected: '2026-07-09'
category: Eval
direction: 多模态大模型计数能力评测
tags:
- MLLM
- Visual Counting
- Benchmark
- Multimodal Evaluation
- Numerical Hallucination
one_liner: 构建三层分类的视觉计数基准HoloCount，评测20+SOTA MLLM计数能力，揭示推理与鲁棒性短板
practical_value: '- 电商多模态导购Agent研发中，可复用HoloCount的三层测试范式，验证MLLM在商品计数、货架SKU盘点场景的数值准确性，减少计数类幻觉

  - 多模态推荐的商品属性量化任务，可参考基准的鲁棒性测试思路，构造高密度、属性混淆的对抗样本，提前校验模型可靠性

  - 涉及多模态数值推理的业务（如库存识别、直播商品计数），可优先选用HoloCount评测排名靠前的MLLM底座，降低落地误差'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有MLLM定性场景理解表现优异，但定量计数精度不足、数值幻觉问题突出，已有计数基准仅覆盖简化场景的基础感知，无法捕捉逻辑约束、对抗条件下的失效模式，无法支撑零售、物流等高容错要求的业务落地。
### 方法关键点
提出三层层级分类的HoloCount全局视觉计数基准，覆盖三类评测维度：
1. 语义计数：原子、属性级枚举能力
2. 分析计数：空间、集合推理的逻辑组合能力
3. 鲁棒性测试：高密度场景、语言偏见等对抗场景下的模型稳定性
### 关键结果
完成20+ SOTA MLLM的全量评测，发现顶级模型在从基础感知任务转向复杂分析推理、对抗场景时，性能出现显著下降，明确了当前MLLM计数能力的系统性短板。
