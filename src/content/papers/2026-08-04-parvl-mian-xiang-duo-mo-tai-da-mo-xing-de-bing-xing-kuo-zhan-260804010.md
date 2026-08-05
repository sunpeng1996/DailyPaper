---
title: 'ParVL: Parallel Scaling and Expandable Compute Allocation for Multimodal LLMs'
title_zh: ParVL：面向多模态大模型的并行扩展与弹性算力分配框架
authors:
- Yang Yang
- Qinyu Zhao
- Mouxiang Chen
- Xiaohui Li
- Lixin Gu
- Wenhai Wang
- Hongjie Zhang
- Wenwei Zhang
affiliations:
- The Australian National University
- Shanghai AI Laboratory
- Zhejiang University
- Shanghai Jiao Tong University
- Nanjing University
arxiv_id: '2608.04010'
url: https://arxiv.org/abs/2608.04010
pdf_url: https://arxiv.org/pdf/2608.04010
published: '2026-08-04'
collected: '2026-08-05'
category: Multimodal
direction: 多模态大模型 · 并行算力分配与参数复用
tags:
- MLLM
- Parameter Reuse
- Parallel Scaling
- KV Prefix
- Compute Allocation
one_liner: 通过参数复用的并行分支结构，在低参数增量下提升MLLM性能，可灵活分配视觉与语言侧算力
practical_value: '- 做多模态商品理解/直播内容理解的MLLM优化时，可复用KV前缀分支+参数共享方案，仅增加<4%参数量就能提升推理性能，避免全量扩参带来的部署成本飙升

  - 针对不同业务场景灵活分配ViT/LLM分支数：商品OCR/小票识别等视觉依赖场景多配ViT分支，商品文案生成/多轮导购推理等语言依赖场景多配LLM分支，性价比最优

  - 部署时可复用稀疏路由技巧，训练多分支模型后推理阶段单样本仅激活1对分支，性能损失仅0.3%，但算力成本降到与单分支一致，适合高并发线上场景

  - KV cache优化可参考Shared KV方案，合并多分支普通token的KV缓存，batch size=8时内存占用降低30%，适合多分支MLLM的线上部署降本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多模态大模型（MLLM）扩容通常要么提升参数量，带来极高存储与内存成本，要么增加串行推理步骤抬高响应 latency，且ViT视觉编码器与LLM解码器之间的算力分配固定，无法针对不同任务特性做定制化优化，很难平衡业务场景的性能与成本要求。

### 方法关键点
- 基于参数复用设计并行分支架构：ViT与LLM分别支持独立配置分支数Pv/Pl，所有分支共享主干权重，仅通过分支特有的KV前缀做区分，整体参数量增量最高仅4%
- 模态内分层聚合：视觉分支输出经token级MLP聚合后输入跨模态连接器，复制分发到所有LLM分支，LLM分支输出再经聚合后输入共享LM头
- 部署侧支持灵活降本：训练后可通过稀疏路由单样本仅激活1对ViT-LLM分支，也可通过Shared KV方案合并多分支普通token的KV缓存，降低内存开销

### 关键结果
- 基于13B tokens的采样SFT数据训练，在1B、2B、8B三个尺度对比同配置单分支基线：1B尺度最优4:4配置9个基准平均得分从49.6提升至50.5，数学推理提升2.0，OCR理解提升0.3；2B、8B尺度的2:2配置分别提升0.3、0.5个百分点
- 稀疏路由单分支激活模式下，性能仅比全分支激活低0.3，算力成本与单分支持平；batch size=8时Shared KV可降低内存占用30%

> 最值得记住的结论：固定参数预算下，并行参数复用扩容的性价比远高于盲目扩参，且不存在通用最优的ViT/LLM算力分配比例，需匹配任务的模态依赖特性做适配
