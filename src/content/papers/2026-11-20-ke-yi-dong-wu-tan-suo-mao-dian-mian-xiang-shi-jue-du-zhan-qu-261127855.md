---
title: 'Anchors That Move Without Collapsing: Exclusive-Region Anchor Routing for
  Vision Transformers'
title_zh: 可移动无坍缩锚点：面向视觉Transformer的独占区域锚点路由
authors:
- Aadi Gupta
affiliations:
- Scaler School of Technology, Bengaluru, India
arxiv_id: '2611.27855'
url: https://arxiv.org/abs/2611.27855
pdf_url: https://arxiv.org/pdf/2611.27855
published: '2026-11-20'
collected: '2026-11-23'
category: Other
direction: 视觉Transformer · 锚点路由架构优化
tags:
- Vision Transformer
- Anchor Routing
- Attention Optimization
- FLOPs Reduction
- High Resolution Inference
one_liner: 提出独占区域锚点路由机制解决ViT锚点坍缩冗余问题，大幅降低高分辨率场景算力开销
practical_value: '- 多模态推荐的高分辨率商品图特征抽取场景，可复用独占区域锚点机制替换直接下采样输入，避免精度损失同时降低FLOPs

  - 长序列（用户行为/长query）语义压缩聚合场景，可参考硬独占分配策略，相比softmax/Gumbel-softmax更稳定精度更高

  - 高分辨率输入（商品长图、直播帧）特征抽取场景，分辨率≥1536x1536时用锚点路由替换FlashAttention可获训练加速收益'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
ViT中通过少量锚点token交换全局信息的优化方案普遍存在锚点表征冗余问题，现有Perceiver/AnchorFormer等方案的锚点池化映射相似度最高达0.99，几乎完全坍缩为单一表征，存在严重算力浪费。
### 方法关键点
1. 基于Voronoi划分的独占区域锚点路由从构造上避免锚点坍缩
2. 新增聚焦锚点变体，将多数锚点分配到学习到的重要性图峰值位置，适配杂乱输入场景
3. 验证硬独占分配是唯一稳定且高精度的区域分配方案，softmax/Sinkhorn松弛方案会发散，Gumbel-softmax精度更低
### 关键结果
CIFAR-100上精度比Representative Attention高2.4~3.6个点；杂乱画布场景聚焦锚点比固定分区高1.5个点；1080P交通标志识别场景仅用1/5 FLOPs即可匹配稠密局部窗口注意力精度，固定分区单步训练速度比FlashAttention快1.5倍；仅分辨率≥1536x1536时锚点路由速度优于FlashAttention。
