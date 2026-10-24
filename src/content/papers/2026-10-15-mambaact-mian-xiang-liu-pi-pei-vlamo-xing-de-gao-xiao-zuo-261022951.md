---
title: 'MambaAct: Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action
  Models'
title_zh: MambaAct：面向流匹配VLA模型的高效Mamba动作专家
authors:
- Khuyen Pham
- Tran Nguyen Le
- Edoardo Fazzari
- Cesare Stefanini
arxiv_id: '2610.22951'
url: https://arxiv.org/abs/2610.22951
pdf_url: https://arxiv.org/pdf/2610.22951
published: '2026-10-15'
collected: '2026-10-24'
category: Multimodal
direction: 多模态大模型 · 推理效率优化
tags:
- Mamba
- VLA
- Flow Matching
- Inference Optimization
- Multimodal
one_liner: 设计基于Mamba的轻量动作专家，替换流匹配VLA的Transformer模块，降延迟且提精度
practical_value: '- 生成式推荐等需多步迭代采样的任务，可将迭代调用的Transformer序列生成模块替换为Mamba结构，在精度无损前提下大幅降参、降低推理延迟

  - 多模态/多条件的迭代生成任务，可引入轻量Context Compressor将上游条件token压缩为门控信号，避免每步迭代重复执行跨注意力计算，减少冗余开销

  - 模型轻量化优化可优先针对迭代调用的高频模块做结构替换，保留预训练主干不动，性价比远高于全模型压缩/剪枝'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
流匹配类视觉-语言-动作（VLA）模型需迭代调用动作专家完成去噪，Transformer动作专家的高推理延迟是实时落地的核心瓶颈，现有优化多聚焦在减少采样步数或压缩视觉语言通路，未针对高频调用的动作专家做结构级优化。
### 方法关键点
1. 保留预训练VLM前缀编码器不变，将原Transformer动作专家替换为紧凑型Mamba结构，用Mamba作为动作混合器建模连续动作序列的依赖关系；
2. 新增轻量Context Compressor将VLM前缀token压缩为紧凑条件信号，直接门控调制每个Mamba动作块，避免每步迭代重复执行跨注意力计算。
### 关键结果
动作专家参数量缩小10×，LIBERO数据集去噪延迟降低64.8%，真实场景部署延迟降低58.8%，同时LIBERO平均任务成功率提升1.08pp，在LIBERO-Plus和真实场景基准上均保持收益。
