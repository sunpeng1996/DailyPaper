---
title: 'Finding Change in Satellite Archives from Text: How to Combine Before-and-After
  Images Efficiently'
title_zh: 基于文本的卫星档案变化检索：时序前后图像高效融合方案对比
authors:
- Simon Roy
- Mark Bong
- Giovanni Beltrame
affiliations:
- Polytechnique Montréal
arxiv_id: '2607.28571'
url: https://arxiv.org/abs/2607.28571
pdf_url: https://arxiv.org/pdf/2607.28571
published: '2026-07-30'
collected: '2026-08-02'
category: Other
direction: 多模态时序检索 · 高效融合架构评估
tags:
- CLIP
- Mamba
- Multimodal Retrieval
- Efficient Architecture
- Bi-temporal Vision
one_liner: 对比8种双时序卫星图像融合模块，提出两阶段检索方案，给出Mamba等架构实测结论
practical_value: '- 两阶段「低成本粗筛+高精度重排」的检索链路设计可迁移到搜索/推荐召回排序链路，实现降本提效

  - 短序列（长度~200）场景下无需优先选型Mamba，Attention在并行硬件上的实测速度更优

  - 表征压缩方案不能仅看聚合指标，需额外验证细粒度关键信息的保留率，避免业务效果隐性下降'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
卫星时序档案的文本变化检索需求快速增长，查询时需运行大量前后图像对的融合模块，速度直接决定搜索成本，现有融合方案的性能对比缺乏统一控制变量的实测验证。
### 方法关键点
固定采用冻结CLIP作为图像编码器、统一训练流程，对比三类共8种融合模块设计：注意力类、状态空间模型（Mamba）类、自研时序瓶颈融合（TBF）压缩类，在2个基准数据集上用10个随机种子开展统计显著的测试。
### 关键结果数字
1. 无训练两阶段检索（低成本差值模型粗筛+注意力融合重排）在LEVIR-CC上召回率持平或超过全量融合，查询成本降低10-15×，Dubai-CC上R@1/R@5相当；
2. 序列长度196的典型ViT patch场景下，Mamba无速度优势，受内存带宽限制，Attention并行效率更高；
3. TBF压缩使参数量降2.3×、延迟降1.6×，BLEU-1仅损失0.007，但过度压缩会丢失聚合指标无法检测的变化相关细节。
