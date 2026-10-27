---
title: 'Octen-WebGR: Scaling Generative Retrieval to 200 Million Web Pages'
title_zh: Octen-WebGR：支持2亿网页规模的生成式检索框架
authors:
- Guangwei Xu
- Wenkai Zhang
- Yawen Liu
- Dongxu Zhang
- Xijie Xu
- Kuan Zou
affiliations:
- Octen.ai
arxiv_id: '2610.35256'
url: https://arxiv.org/abs/2610.35256
pdf_url: https://arxiv.org/pdf/2610.35256
published: '2026-10-26'
collected: '2026-10-27'
category: GenRec
direction: 生成式检索 · 亿级规模语义ID索引
tags:
- Generative Retrieval
- Semantic ID
- Navigational Search
- Scalable IR
- LLM4Rec
one_liner: 首次实现2亿网页规模生成式检索，导航搜索性能超稠密检索与前沿LLM且成本更低
practical_value: '- 双token语义ID设计可直接复用：给电商商品/广告分配2个16位语义ID，既保证ID唯一，又通过前缀关联相似item，降低生成式检索解码复杂度，适配亿级SKU规模

  - 训练调度trick可落地：高流量query-item对放在训练后期衰减窗口阶段，减少模型遗忘，提升头部流量准确率；冷启动item优先加索引样本（item文本→ID），降低训练样本需求

  - 混合检索架构参考：生成式检索和稠密检索路由搭配，高曝光item走GR提升query泛化能力，低曝光冷启动item走稠密检索提升召回率，整体效果比单一路径提升1pp以上

  - 成本优化经验：4B参数GR仅需10GB显存单卡运行，百万查询成本比闭源LLM低40倍以上，中小规模业务可直接用0.6B版本进一步降本'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
导航类搜索占全网搜索流量的1/5~1/4，现有方案存在明显瓶颈：点击表仅能处理历史见过的query，无法泛化新query表述；稠密检索易将同站点相似页面排序错误，且规模越大准确率衰减越快；闭源LLM闭卷检索准确率低，查询成本是检索系统的数十倍。
### 方法关键点
- 语义ID设计：每个URL分配2个16位语义ID（总容量超42亿），通过残差量化+碰撞规避保证ID唯一，相似URL共享首token前缀，解码仅需2步
- 训练策略：基于点击数据加权采样query-ID对，混合文档索引样本（URL文本+关联高频query映射到ID），高流量样本放在训练后期衰减窗口，减少遗忘
- 推理约束：仅允许生成合法ID词表内的token，输出URL100%存在，beam search宽度20，推理延迟低至2.3ms/query
### 关键结果
- 2亿网页规模下，导航搜索hit@1达59.6%，领先加点击先验的稠密检索13.1pp，领先前沿闭源LLM 22pp以上
- 未见过的新query（目标为高曝光页面）场景下，hit@1达30.9%，是稠密检索的1.8倍
- 仅需10GB显存单GPU即可运行，百万查询成本比稠密检索低40%，比闭源LLM低40倍以上
- 生成式检索性能主要受样本曝光次数限制，而非模型容量，模型规模需求随索引量亚线性增长
### 核心结论
生成式检索与稠密检索能力完全互补，前者对query泛化性更优适配高曝光item，后者对冷启动item效果更好，混合路由架构是亿级规模生成式检索落地的最优方案
