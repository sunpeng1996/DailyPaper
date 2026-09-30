---
title: Pretraining Transformers with Quantized Softmax in Attention
title_zh: Transformer预训练中注意力模块的量化Softmax优化方案
authors:
- Shangzhen Zhu
- Muyan Hu
- Tomasz Kozlowski
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2609.33591'
url: https://arxiv.org/abs/2609.33591
pdf_url: https://arxiv.org/pdf/2609.33591
published: '2026-09-26'
collected: '2026-09-30'
category: Training
direction: LLM预训练 · 注意力softmax量化优化
tags:
- Transformer
- Attention Quantization
- Softmax
- Pretraining
- Low Precision
one_liner: 提出K区间注意力算子族，优化量化softmax前后向规则，预训练损失接近原生softmax
practical_value: '- 训练/微调业务侧LLM（比如电商文案生成、召回排序用的小参数模型）时，不要直接detach注意力softmax的行极值梯度，否则即使前向计算完全一致，也会出现训练后期loss飙升的问题

  - 硬量化softmax时优先选择FWM（固定窗口锚定行最大值）校准+Prob-STE（归一化后加直通估计器）的组合，K=4时损失仅比原生softmax高0.019
  nats，K=16时仅高0.004 nats，精度损失可忽略的前提下大幅降低算力和显存开销

  - 推荐/搜索场景的推理端LLM优化，可直接复用K区间注意力的量化方案，在QPS提升30%~50%的前提下，下游排序、生成任务的性能下降幅度可控'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前低精度Transformer训练已完成线性层、注意力矩阵乘的量化落地，但softmax算子仍需保持FP16/FP32高精度，成为算力优化的瓶颈；现有量化softmax方案多适配推理场景，预训练时因梯度规则不合理会出现训练不稳定、效果暴跌的问题，且业界对量化softmax的前后向设计如何影响预训练效果缺乏系统性研究。
### 方法关键点
- 提出K区间注意力算子族，沿三个可控维度设计：校准策略（MinMax行极值动态校准 / FWM固定窗口锚定行最大值校准）、指数函数重建方式（LERP线性插值 / Nearest硬舍入到网格值）、STE（直通估计器）放置位置（Weight-STE归一化前添加 / Prob-STE归一化后添加）
- 推导完整的反向传播规则，显式保留行极值的校准梯度，保证梯度满足shift invariance的零和约束
- 所有对比算子前向计算逻辑严格对齐，仅反向梯度规则不同，排除前向差异对实验结果的干扰
### 关键实验
基于GPT-2结构（124M/1B参数）在FineWebEdu、WikiText-103语料上训练，对比原生softmax基线：
- detach行极值梯度的方案前向与全梯度方案完全一致，但训练到25~30M tokens后损失飙升，最终比全梯度方案高0.65~3.07 nats
- K=4硬舍入场景下，MinMax+Weight-STE组合损失比基线高0.89 nats，替换为FWM+Prob-STE后差距缩小到0.019 nats；K=16时FWM+Weight-STE的损失差距仅为0.004 nats
- 训练域损失差距<0.01 nats的量化方案，下游任务性能与原生softmax无统计显著差异
### 核心结论
量化softmax的预训练效果不仅取决于前向近似精度，更取决于反向梯度规则的完整性，仅对齐前向逻辑而忽略梯度约束必然会出现训练故障。
