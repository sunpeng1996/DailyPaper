---
title: The Lattice of Transition Laws
title_zh: 过渡律格：统一扩散与自回归模型的解码调度分析框架
authors:
- T. Y. Tsui
- Jiatao Gu
- Lingjie Liu
affiliations:
- University of Pennsylvania
arxiv_id: '2610.11216'
url: https://arxiv.org/abs/2610.11216
pdf_url: https://arxiv.org/pdf/2610.11216
published: '2026-10-07'
collected: '2026-10-10'
category: LLM
direction: 生成模型解码调度优化
tags:
- Diffusion Model
- Autoregressive Model
- Decoding Schedule
- Generative Model
- Lattice Theory
one_liner: 将扩散、自回归及混合生成模型统一映射到corruption格，实现解码调度性能的预解码预测
practical_value: '- 生成式推荐场景下的商品文案、营销素材生成任务，可参考该框架优化解码调度，在保障生成质量的前提下压缩推理步数，提升线上QPS

  - 针对序列型生成任务（如用户个性化query推荐、评论自动生成），可基于数据的图树深确定零成本解码最小步数，平衡推理 latency 与生成效果

  - 大模型微调落地时，可通过预训练权重提取的pairwise依赖核提前预判不同解码调度的性能排名，大幅减少线下调优的试错成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
扩散与自回归生成模型长期被视为两类独立范式，现有混合模型的解码调度均为人工固定设计，无法在解码前预判固定步数下的调度性能，缺乏统一的设计指导准则。
### 方法关键点
1. 将扩散、自回归及介于两者之间的混合模型统一映射为corruption格上的路径，定义调度成本为并行解码步骤丢弃的token/维度依赖度
2. 零成本调度的最小步数由数据的几何结构决定：对于图上的马尔可夫数据，最小步数等于图的树深，序列场景下为序列长度的对数，网格场景下为边长的线性值
3. 解码前可通过预训练权重估计的pairwise依赖核，直接预测不同调度的成本排名
### 关键结果
在文本、图像、视频三类生成任务的多基准、多指标验证中，调度性能排名的预测结果与实际解码结果基本一致，验证了框架的通用性。
