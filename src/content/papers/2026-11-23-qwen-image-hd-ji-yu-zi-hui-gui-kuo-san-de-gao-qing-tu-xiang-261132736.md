---
title: 'Qwen-Image-HD: Autoregressive Diffusion for High Definition Image Generation'
title_zh: Qwen-Image-HD：基于自回归扩散的高清图像生成方法
authors:
- Zihao Liu
- Zekai Zhang
- Shengming Yin
- Zikai Zhou
- Donghao Zhou
- Chenyang Zhu
- Lihan Jiang
- Ningyuan Tang
- Bingxuan Zhao
- Yanran Zhang
arxiv_id: '2611.32736'
url: https://arxiv.org/abs/2611.32736
pdf_url: https://arxiv.org/pdf/2611.32736
published: '2026-11-23'
collected: '2026-11-25'
category: Multimodal
direction: 多模态文生图 · 高清高效生成
tags:
- Text-to-Image
- High-Resolution Generation
- Autoregressive Diffusion
- Parallel Inference
- Efficient Fine-tuning
one_liner: 基于分块自回归与波前并行推理实现低算力成本的4K/16K高清文生图
practical_value: '- 分块生成+双尺度上下文的设计可直接迁移到电商4K商品图、长详情页生成场景，无需全图训练即可大幅降低高清素材生成的算力成本

  - Wavefront多GPU并行调度思路可复用在所有生成类服务的推理优化，无需额外训练就能降低单请求延迟，提升线上服务并发能力

  - NSE无参考纹理评估指标可直接用于电商生成素材的自动化质量校验，快速识别重复条纹、纹理异常等badcase，减少人工审核成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统全图高清文生图训练需处理超长图像序列，算力成本极高，且资源受限场景下易出现局部重复纹理；现有分块生成方案存在上下文缓存随画布扩张无限增长、全局结构连贯性差的问题，亟需兼顾效率、全局布局与局部细节的高清生成路径。
### 方法关键点
- 分块自回归训练：将4K画布拆分为4×4个1K tile，每个tile预测仅依赖上/左邻居的256像素边界细节、全局压缩历史缩略图，上下文token长度固定为10240，仅为全图4K生成的1/6.4，不随画布扩大增长
- 统一画布坐标对齐：将缩略图、邻居、目标tile映射到全局坐标系，通过RoPE编码保留空间位置与尺度差异，解决分块生成的边界不连贯问题
- Wavefront并行推理：将同一反对角线的tile分配到多GPU并行生成，结合CFG分支并行、序列并行优化，无需额外训练即可降低延迟
### 关键实验结果
在Qwen-Image-Bench 4K数据集上，对比同骨干全图SFT：训练FLOPs降低68%，Q-Judger Overall得分提升1.17分，重复纹理指标NSE降低60.85%；对比FLUX-3-Image-Klein，Overall得分高1.75分；4GPU优化Wavefront推理单图延迟仅139s，比同GPU串行生成降低16%。
### 核心结论
固定边界上下文+全局缩略图的分块生成范式，能够以远低于全图训练的成本实现更高质量的高清生成，是大分辨率生成任务降本提效的核心可行路径
