---
title: 'Stress-Testing Efficient Responsible-AI Evaluation: When Compute Savings Change
  Benchmark Conclusions'
title_zh: 高效负责任AI评估压力测试：算力优化对基准结论的影响
authors:
- Ahmed El Kady
- Aravind Narayanan
- Rehana Noorani
- Yani Ioannou
- Shaina Raza
affiliations:
- Vector Institute
- Independent researcher
- University of Calgary
arxiv_id: '2608.31108'
url: https://arxiv.org/abs/2608.31108
pdf_url: https://arxiv.org/pdf/2608.31108
published: '2026-08-31'
collected: '2026-09-02'
category: Eval
direction: 负责任AI基准评估 · 效率优化
tags:
- ResponsibleAI
- Evaluation
- Quantization
- MoE
- Benchmark
- Efficiency
one_liner: 量化batch、量化、基准裁剪等高效评估策略对负责任AI基准结论稳定性的影响，给出实践参考
practical_value: '- 做LLM/GenRec离线效果评估时，优先选择大batch策略，精度损失控制在0.35pp以内，还可降低GPU能耗，性价比优于INT8量化

  - 裁剪评估数据集降本时，避免使用极小子集，尤其是涉及公平性、子群效果的专项评估，需保留足够样本量降低结果波动

  - 校验推荐系统的用户群体bias等负责任AI指标时，不要仅验证整体精度，需同步校验子群指标、bias严重度等核心结论的稳定性，避免用INT4量化导致结论偏差'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前业界普遍采用批处理、量化、基准数据集裁剪等手段压缩AI评估算力成本，但很少验证这些优化是否会导致评估结论失真，尤其是负责任AI相关的公平性、偏差等核心结论的稳定性缺乏系统性校验。
### 方法关键点
针对3个稠密模型与MoE模型，在BBQ、BBQ-V两个负责任AI基准上，测试7种高效评估方案（批处理、INT8/INT4量化、基准裁剪及组合策略），对比BF16全量基准的精度、偏差严重度、子群表现、GPU能耗等多维度指标。
### 关键结果数字
大batch策略精度损失<0.35pp，子群指标波动小，6组模型-数据设置中有5组能耗下降；INT8精度保留较好，但能耗是基线的1.79~4.26倍；INT4会导致模型/场景依赖的显著指标偏差；裁剪基准降本效果最稳定，但极小子集的评估结果对样本选择高度敏感。
