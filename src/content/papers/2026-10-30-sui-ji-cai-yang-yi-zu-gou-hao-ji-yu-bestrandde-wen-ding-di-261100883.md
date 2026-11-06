---
title: Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand
title_zh: 随机采样已足够好？基于BestRand的稳定低成本基准压缩方法
authors:
- George Ling
- Shanshan Zhong
- Lijin Yang
- Hao Yang
- Nanxiang Li
- Zhongzhan Huang
affiliations:
- Bosch Research
- Carnegie Mellon University
arxiv_id: '2611.00883'
url: https://arxiv.org/abs/2611.00883
pdf_url: https://arxiv.org/pdf/2611.00883
published: '2026-10-30'
collected: '2026-11-06'
category: Eval
direction: 模型评估 · 基准数据集压缩
tags:
- BenchmarkCompression
- ModelEvaluation
- LLM
- VLM
- AgentEvaluation
one_liner: 提出BestRand基准压缩方法，在70+多模态、Agent等基准上实现更低误差、更高稳定性与更低构建成本
practical_value: '- 做LLM4Rec、智能导购Agent等业务的模型迭代评测时，可直接复用BestRand压缩现有评测集，降50%+评测成本同时保障结果稳定性

  - 线上A/B测试的小流量切片选型可参考其长尾误差抑制思路，避免小样本带来的效果评估偏差

  - 跨版本、跨场景的OOD效果评估可复用其误差分布建模方法，提升估计准确性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
LLM、VLM、Agent等大模型全量基准评测时间与算力成本极高，现有随机采样压缩方案存在长尾大误差问题，且该不稳定性是大模型固有属性，无法通过增加评测模型数量解决。
### 方法关键点
推导了子集估计全基准得分的误差分布解析近似，证实误差呈长尾分布；提出BestRand方法，保留随机采样高效性的同时针对性裁剪高误差长尾，大幅提升压缩后评测的稳定性。
### 关键结果
在70+文本、多模态、Agent基准上验证，对比SOTA方法：平均高误差风险降低50.2%、估计误差降低16.4%，构建成本仅为前者的51.3%；跨得分区间、模型家族、时间偏移场景下OOD估计误差平均降低21.8%
