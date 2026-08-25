---
title: 'Block3D: Efficient Text-to-3D Generation via Block-Wise Diffusion'
title_zh: Block3D：基于分块扩散的高效文本转3D生成方法
authors:
- Bowen Cui
- Weijie Wang
- Zeyu Zhang
- Yefei He
- Mingda Lin
- Haoyu Zhao
- Yuanyu He
- Donny Y. Chen
- Feng Chen
- Bohan Zhuang
affiliations:
- ZIP Lab, Zhejiang University
- Monash University
- University of Adelaide
arxiv_id: '2608.19567'
url: https://arxiv.org/abs/2608.19567
pdf_url: https://arxiv.org/pdf/2608.19567
published: '2026-08-19'
collected: '2026-08-25'
category: Multimodal
direction: 多模态生成 · 文本转3D高效推理
tags:
- Text-to-3D
- Diffusion Model
- Efficient Inference
- Block-wise Processing
- Token Correction
one_liner: 提出分块扩散框架与置信度块内校正策略，文本转3D推理提速5倍且不损失几何保真度
practical_value: '- 分块生成+块内校正的思路可迁移到长序列生成类GenRec/商品文案生成任务，缓解自回归生成的误差累积问题，同时提升生成速度

  - 置信度引导的局部修正策略可复用在生成式推荐的候选Token后处理阶段，比如Semantic ID序列生成时低置信度ID的校正，提升生成准确率

  - 分块自回归+局部并行去噪的架构可优化生成式推荐推理延迟，适合高并发场景下的商品推荐、商品文案生成等业务的提速改造'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文本转3D生成方案存在两大核心瓶颈：自回归解码逐Token生成速度慢、生成误差无法回溯修正；全局扩散/流匹配模型需重复处理全量表征，高保真生成算力成本极高，无法适配高并发落地场景。
### 方法关键点
1. 采用分块扩散架构，将离散形状Token序列切分为连续块，块间按自回归顺序生成、块内所有Token联合并行去噪，兼顾生成语义连贯性与推理效率
2. 新增置信度引导的块内校正机制，每个块生成完成前先修正低置信度Token，缓解自回归模式固有的误差累积问题
### 关键结果
在TRELLIS-500K测试集上，端到端平均生成时间从25.71s降至4.99s，相比微调后的自回归基线实现5.15倍提速，同时几何保真度无损失。
