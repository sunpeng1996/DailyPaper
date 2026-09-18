---
title: 'Video DeltaNet: A Video-Native Hybrid Attention for Livestream Video Generation'
title_zh: Video DeltaNet：面向直播视频生成的原生混合注意力架构
authors:
- Haocheng Xi
- Yiming Xie
- Hexu Zhao
- Yiwen Zhang
- Michael Liu
- Thomas Creavin
- Kurt Keutzer
- Xiuyu Li
- Zhaoyang Lv
- Chenfeng Xu
affiliations:
- University of California, Berkeley
- Impossible, Inc.
- University of Texas at Austin
arxiv_id: '2609.20744'
url: https://arxiv.org/abs/2609.20744
pdf_url: https://arxiv.org/pdf/2609.20744
published: '2026-09-16'
collected: '2026-09-18'
category: Multimodal
direction: 多模态生成 · 视频注意力效率优化
tags:
- Hybrid Attention
- Linear Attention
- Video Generation
- Delta Rule
- Knowledge Distillation
- Inference Acceleration
one_liner: 提出混合帧级delta注意力架构，在视频生成质量无损前提下实现14.5倍推理提速
practical_value: '- 注意力拆分思路可迁移到长序列用户行为建模：局部滑动窗口Softmax捕捉短期细粒度交互，线性内存压缩长期行为，平衡推荐精度与计算效率

  - 预训练大模型的三阶段对齐+LoRA改造方案可复用：先单模块对齐、再全链路适配、最后低秩微调，避免破坏预训练能力，大幅降低大模型定制改造成本

  - 帧级批量delta更新逻辑可借鉴到多token批处理场景：同一时间窗的特征联合更新而非逐token独立处理，降低写入冲突同时提升计算效率

  - 少步蒸馏+分布式推理的加速组合可直接用于AIGC电商素材生成链路：将视频/图像生成的推理延迟降低到可交互水平，适配直播素材实时生成需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
视频扩散模型的Dense Softmax注意力随序列长度呈平方级增长，占去噪阶段85%以上运行时间；直接替换为线性注意力会丢失细粒度交互信息，导致生成质量明显下降，现有方案无法兼顾长视频生成的效率与画质。
### 方法关键点
- 混合注意力拆分：局部滑动窗口Softmax负责相邻帧细粒度交互，新增首尾帧锚点作为全局参考，剩余长距离上下文由双向线性记忆分支处理
- 视频原生Delta Attention(VDA)：按帧为单位联合更新线性记忆状态，而非逐token独立更新，通过联合优化目标解决同帧patch写入冲突，天然适配视频扩散的帧级批处理模式
- 三阶段预训练模型适配：先单线性层对齐预训练输出，再全链路组装适配，最后加QKVO LoRA联合微调，全程冻结主干避免预训练能力退化
- 端到端优化链：融合VDA专用Triton内核、chunk级序列扫描、小矩阵逆算子优化，配合8步少步蒸馏、多卡分布式并行进一步压缩延迟
### 关键结果
在1万条14.3秒768p直播视频数据集上训练，对比50步Dense H3、4步FastH3基线：
1. 8步VDN-H3在所有无参考画质指标上匹配甚至超过50步Dense H3，运动幅度、首尾帧保真度无明显下降，显著优于4步FastH3
2. 单B200上仅混合注意力改造就实现2.6倍提速，加8步蒸馏后单卡16.2倍提速，8卡B200下仅需6.7秒完成14.3秒768p视频去噪，相对同配置50步Dense H3提速14.5倍，单H200下最高提速19.8倍

> 最值得记住的一句话：长序列生成类任务的注意力优化，核心是拆分「需要细粒度交互的局部/关键节点」和「可压缩的全局上下文」，配合场景适配的更新规则与增量改造流程，就能实现效率与质量的双赢。
