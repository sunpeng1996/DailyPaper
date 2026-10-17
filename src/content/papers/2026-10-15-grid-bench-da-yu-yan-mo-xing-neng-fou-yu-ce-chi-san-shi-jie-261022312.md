---
title: 'Grid-Bench: Can LLMs Predict How Discrete Worlds Change?'
title_zh: Grid-Bench：大语言模型能否预测离散世界的变化
authors:
- Zixiang Xu
- Zirui Song
- Wanrong Zheng
- Chiyu Zhang
- Yue Huang
- Yuyang Peng
- Kexin Zhang
- Jinkun Chen
- Xiuying Chen
- Xiangliang Zhang
affiliations:
- University of Southern California
- Mohamed bin Zayed University of Artificial Intelligence
- Meta
- University of Notre Dame
- University of California, Los Angeles
arxiv_id: '2610.22312'
url: https://arxiv.org/abs/2610.22312
pdf_url: https://arxiv.org/pdf/2610.22312
published: '2026-10-15'
collected: '2026-10-17'
category: Eval
direction: LLM评测 · 空间序列推理
tags:
- LLM Benchmark
- Spatial Reasoning
- Sequence Reasoning
- State Prediction
- Discrete World
one_liner: 提出面向LLM空间序列操作推理的可执行基准Grid-Bench，量化长序列下性能差异
practical_value: '- 做电商虚拟货架动态调整、线下门店动线规划等空间操作类Agent时，可优先选用Grid-Bench测评中长序列状态预测准确率高的LLM，降低多步操作累计误差

  - 涉及多步规则叠加的推荐业务（比如组合满减、分层权益叠加后的商品排序），可参考Grid-Bench的可执行真值校验框架，实现模型输出的自动化校验，降低业务错误率

  - 长序列决策类Agent的效果评估，可复用Grid-Bench的「完整状态准确率+单错误单元统计」双指标体系，替代单一Exact Match指标，更细粒度区分模型性能差异'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM处理多步空间操作序列时的状态预测能力缺乏统一可量化的评测基准，无法准确衡量长序列操作下的累计误差与模型间真实性能差异。
### 方法关键点
1. 构建Grid-Bench可执行基准，覆盖2/3/4维离散网格、8类空间操作，输入为初始网格、操作规则、文本化操作历史，输出为完整最终网格，所有预测值均可通过参考执行自动校验。
2. 从操作类型、历史长度、工作负载三个维度做横向对比，同时采用完整状态准确率、错误单元数双指标细粒度评估模型性能。
### 关键结果数字
评测6款主流LLM发现：操作历史长度增加时，完整状态准确率最高下降超80%；单步性能接近的模型在长序列下性能差异可达50%以上；部分模型长序列下的正确预测比例仍比直接复制初始状态高30%以上。
