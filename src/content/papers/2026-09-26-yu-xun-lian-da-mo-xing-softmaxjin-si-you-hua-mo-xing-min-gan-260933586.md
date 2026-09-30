---
title: 'Approximating Softmax in Pretrained LLMs: Model Sensitivity and Kernel Acceleration'
title_zh: 预训练大模型Softmax近似优化：模型敏感度分析与内核加速
authors:
- Shangzhen Zhu
- Muyan Hu
- Tomasz Kozlowski
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2609.33586'
url: https://arxiv.org/abs/2609.33586
pdf_url: https://arxiv.org/pdf/2609.33586
published: '2026-09-26'
collected: '2026-09-30'
category: LLM
direction: LLM推理优化 · 注意力内核加速
tags:
- Softmax Approximation
- FlashAttention
- Kernel Acceleration
- LLM Inference
- Blackwell B200
one_liner: 提出无需重训的Softmax近似方案，嵌入FlashAttention-4后B200上推理提速12.4%，PPL上升不足0.5%
practical_value: '- 部署LLM驱动的生成式推荐/Agent服务时，可直接复用Rowmax-H15优化FlashAttention内核，在效果损失可忽略的前提下降低推理延迟、减少GPU算力成本，尤其适合长上下文（8K+）的商品文案生成、多轮导购对话场景

  - 做LLM4Rec相关的自定义注意力优化时，可优先把分辨率分配给注意力行最大值附近的权重，不要对保留的注意力得分做均匀加权，能以最小精度损失换最大提速

  - 评估注意力近似算法的精度损失时，不要只看JSD等逐点误差指标，要直接测下游任务（比如推荐召回/排序的NDCG、文案生成的BLEU）的效果，相同JSD的扰动对不同模型的效果影响可能相反'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前NVIDIA Blackwell B200 GPU的tensor core吞吐量比特殊函数单元的指数运算吞吐量高两个数量级，fused attention内核中的softmax指数计算已成为新的性能瓶颈。现有softmax近似方案要么需要模型重训，要么精度损失不可控，无法直接在冻结的预训练LLM推理场景落地。
### 方法关键点
- 对10个参数量0.5B~72B的冻结Decoder-only模型做控制变量实验，明确softmax近似的可优化边界：可大幅裁剪注意力行的低权重位置、降低权重分辨率，但对保留位置做均匀加权会显著提升NLL；固定分辨率预算下，将更细的分辨率分配到注意力行最大值附近，可大幅降低精度损失
- 提出Rowmax-PoT近似方案：以每行注意力最大值为锚点，对权重的以2为底对数取整，实现无重训的指数运算近似
- 基于FlashAttention-4做硬件定制得到Rowmax-H15，仅用整数位运算实现{1, 1.5}×2^k的权重表示，替换原softmax的高精度指数计算
### 关键结果
- 精度验证：在WikiText-103数据集测试，BF16内核2K上下文下，5款不同架构模型的PPL上升仅为0.091%~0.492%，远低于1%的可接受阈值
- 性能测试：B200上FP8精度8K上下文下，因果注意力前向推理提速12.4%，非因果注意力提速25.8%；16K因果注意力单步能耗降低8.4%

最值得记住的结论：注意力近似优化不能只看逐点误差指标，要结合模型端到端效果评估，优先保障高权重位置的精度，可实现极小效果损失下的显著性能提升。
