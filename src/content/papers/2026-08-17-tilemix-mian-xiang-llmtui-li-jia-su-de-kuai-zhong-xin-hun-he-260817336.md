---
title: 'TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration'
title_zh: TileMix：面向LLM推理加速的块中心混合精度注意力
authors:
- Hanzhi Zhang
- Qiao Zhang
- Qinglei Cao
- Heng Fan
- Yan Huang
- Kewei Sha
- Yunhe Feng
affiliations:
- University of North Texas
- Saint Louis University
arxiv_id: '2608.17336'
url: https://arxiv.org/abs/2608.17336
pdf_url: https://arxiv.org/pdf/2608.17336
published: '2026-08-17'
collected: '2026-08-25'
category: LLM
direction: LLM推理优化 · 混合精度注意力内核
tags:
- Mixed-Precision
- Attention Kernel
- LLM Inference
- Prefill Acceleration
- INT8 Quantization
one_liner: 无需训练的块级混合精度注意力内核，大幅提升长上下文LLM的prefill吞吐量
practical_value: '- 长上下文RAG系统的LLM推理部署可直接复用TileMix内核，在精度损失极小的前提下提升prefill吞吐量，降低长商品/用户行为文档的处理时延

  - 无需模型重训，仅通过配置INT8 tile覆盖比例和路由模板即可适配业务的精度-效率权衡：搜索query理解、广告文案生成等高精度场景调低INT8比例，对话Agent、个性化内容摘要等场景可调高比例

  - 原生支持INT8 KV cache，解码阶段也可复用这套混合精度逻辑，适合高并发的推荐服务、用户意图理解等在线场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文LLM的prefill阶段自Attention存在O(L²)计算开销，是推理核心瓶颈；现有方法要么采用统一低精度损失长上下文任务效果，要么做稀疏Attention破坏完整token连接，无法兼顾精度、效率和全连接特性。

### 方法关键点
- 将注意力矩阵按硬件对齐的tile块划分，每个tile组通过紧凑位掩码路由到FP16或INT8计算路径，两个路径共享同一online-softmax状态，完整保留所有合法token交互
- 支持key tile分组，单个路由位可控制多个相邻key tile，长上下文下依然保持元数据紧凑，全程无需训练
- 原生支持Grouped-Query Attention、变长batch、INT8 KV cache，兼容主流LLM结构

### 关键实验
在LongEval、LV-Eval长上下文数据集上测试LLaMA 3.2、Qwen、Vicuna三类模型，A100 40GB显卡下4k序列长度prefill吞吐量达31.8K tokens/s，是FP16 FlashAttention的2.22倍，精度仅下降<2%；相比统一INT8方法，长上下文QA精度提升15%以上，比SageAttention吞吐量高60%。

**最值得记住的结论**：无需训练的硬件对齐块级混合精度路由，是平衡长上下文LLM推理精度与效率的高性价比落地方案。
