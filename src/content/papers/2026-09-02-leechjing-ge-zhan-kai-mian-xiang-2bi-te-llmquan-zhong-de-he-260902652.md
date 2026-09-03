---
title: 'Unfolding the Leech Lattice: Fused Multi-Shell Decoding and VRAM Layouts for
  2-Bit LLM Weights'
title_zh: Leech晶格展开：面向2比特LLM权重的融合多壳层解码与VRAM布局优化
authors:
- Pier-Jean Malandrino
affiliations:
- Scub, France
arxiv_id: '2609.02652'
url: https://arxiv.org/abs/2609.02652
pdf_url: https://arxiv.org/pdf/2609.02652
published: '2026-09-02'
collected: '2026-09-03'
category: LLM
direction: 大模型低比特量化 · 推理内核优化
tags:
- 2-bit-quantization
- Leech-lattice
- CUDA-kernel
- VRAM-optimization
- LLM-inference
one_liner: 首个实现Leech晶格全301类2比特LLM量化融合解码，L40S上较FP16提速2.15倍，4B模型显存仅2.6GB
practical_value: '- 低比特LLM部署可复用「离线展开+融合解码」设计思路，把复杂索引解码逻辑移到加载阶段，避免推理时warp divergence，用可控的显存开销换推理速度，适合边缘/端侧Agent部署场景

  - VRAM布局优化可直接复用二进制位平面代替独热掩码的trick，相同带宽下可同时降低存储开销、提升推理速度，适合大流量推荐系统中LLM排序模块的降本

  - 推理内核调优可参考launch geometry优化方法：融合q/k/v、gate/up等矩阵运算减少启动次数，实测可无精度损失拿回11.7%的内核耗时收益

  - 低比特量化选型参考：2比特量化的精度损失随模型参数量增大显著降低，14B模型MMLU损失仅6.85分，可根据业务精度/成本需求选择7B/14B级模型做2比特部署'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
2比特LLM量化可将70B模型显存占用从140GB压缩至20GB，是大模型私有化部署的核心降本路径；现有Leech晶格2比特量化精度为同级别最优，但仅支持单壳层解码，无公开可用的多壳层高效实现，推理性能瓶颈突出，无法落地。
### 方法关键点
- 离线展开设计：加载阶段将47位Leech晶格索引预展开为解码字段，推理时无需解码索引，实现无warp divergence的统一指令流
- 4种VRAM布局对比：验证独热掩码、二进制位平面等4种无损布局，其中Planes14布局用3个二进制位平面代替独热掩码，无额外旁路开销
- 融合解码内核：将dequantize与GEMV融合，类表存入L1缓存，使用谓词树查表代替动态索引，无本地内存开销
- 性能归因框架：引入无权重基线内核，准确定位launch geometry、数据读写、解码逻辑等各环节的耗时占比
### 关键结果
- 单batch推理场景下，L40S上Planes14布局较FP16提速2.15倍，每权重仅占4.8bit；4B模型端到端吞吐87.0 tok/s，显存仅2.60GB
- 对比已部署的2-bit QTIP内核，本方案读取字节数为其2.4倍，速度慢2.27倍，差异主要来自晶格索引展开的显存开销
- 精度方面：4B模型perplexity较FP16高1.38倍，MMLU降14.7分；14B模型精度损失显著收窄，MMLU仅降6.85分
- 跨硬件测试：A100上所有晶格解码内核速度均低于FP16，优化收益仅在GDDR6类显存带宽受限的硬件上成立

> 最值得记住：低比特量化的推理优化不能只看磁盘存储率，VRAM读取率、解码开销、硬件带宽特性三者的匹配度才是决定落地性能的核心
