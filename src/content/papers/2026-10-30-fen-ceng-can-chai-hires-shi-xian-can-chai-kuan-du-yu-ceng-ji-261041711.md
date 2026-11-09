---
title: 'Hierarchical Residuals: A Minimalist Decoupling of Residual Width from Compute
  Width'
title_zh: 分层残差(HiRes)：实现残差宽度与层计算宽度的极简解耦
authors:
- Ziteng Wang
- Jianqiao Lu
- Xinyu Ma
- Jintao Zhang
- Jun Zhu
- Yiyuan Ma
- Jianfei Chen
affiliations:
- Tsinghua University
- ByteDance Seed
arxiv_id: '2610.41711'
url: https://arxiv.org/abs/2610.41711
pdf_url: https://arxiv.org/pdf/2610.41711
published: '2026-10-30'
collected: '2026-11-09'
category: LLM
direction: LLM架构优化 · 残差连接改进
tags:
- Transformer
- Residual Connection
- Model Efficiency
- MoE
- Scaling Law
one_liner: 提出分层残差架构HiRes，解耦残差与计算宽度，FLOPs效率提升30%无需特殊算子
practical_value: '- 垂域LLM（如电商导购LLM、RecSys侧LLM）预训练可直接复用HiRes默认配置（n=2、B=4），仅修改不到10行代码即可获得1.3倍FLOPs效率提升，无额外算子依赖

  - 深层Transformer排序/召回模型可借鉴分层残差设计，将层分组后加边界PostNorm，解决深层残差尺度爆炸、梯度衰减问题，提升深模型训练稳定性和效果

  - MoE架构的广告/推荐大模型预训练可直接集成HiRes，仅增加1.2%总参数即可获得下游任务1.14精度提升，内存开销仅增加3%左右，吞吐损失可忽略

  - 跨空间投影的门控恒等初始化trick可迁移到任意多空间交互的模型设计中，避免训练初期表示震荡，减少调参成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统Transformer残差连接隐含绑定跨层传递的残差宽度和每层内部的计算宽度，要提升残差容量只能同步加宽所有层的计算维度，算力成本陡增；现有残差扩展方案需要每层新增复杂混合算子，激活I/O和内存开销高，依赖定制内核优化，落地门槛高。
### 方法关键点
- 双层残差结构：将Transformer层划分为多个连续块，块内保留原d维PreNorm残差结构完全不变，块间维护更宽的D维PostNorm外层残差（D>d），独立控制残差容量
- 仅在块边界增加可学习的读（D→d）、写（d→D）投影，开销被块内层数摊销，投影采用门控恒等初始化，避免训练初期表示震荡
- 全流程使用标准算子实现，无需修改原生Transformer层代码，也不依赖定制内核优化
### 关键实验结果
- 跨不同模型尺度拟合scaling law显示，HiRes比原生残连FLOPs效率提升1.30倍；深度扩展到128层时仍保持线性收益，原生模型出现明显收益递减
- 与VWN、mHC、AttnRes等现有残差扩展方法相比效果相当，激活I/O更低，吞吐保留原生模型的91.7%~93.1%，内存开销仅增加3%左右
- 在OLMoE-1B-7B MoE模型500B token预训练任务上，训练损失比基线低0.0208，下游12个任务平均精度高1.14个点，仅增加1.2%总参数
### 核心结论
残差宽度是独立于层计算宽度的可扩展维度，通过极简的分层设计即可获得显著的效率收益，无需复杂定制化优化
