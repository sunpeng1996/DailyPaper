---
title: 'Ask Self, Ask Others: Relation Is All You Need'
title_zh: 问自身、问全局：基于显式关系建模的全新Token混合原语
authors:
- Yuting Ge
- Pengju Yang
- Mingkai Nie
affiliations:
- City University of Hong Kong
- Jilin University
- National University of Singapore
arxiv_id: '2608.20172'
url: https://arxiv.org/abs/2608.20172
pdf_url: https://arxiv.org/pdf/2608.20172
published: '2026-08-20'
collected: '2026-08-21'
category: LLM
direction: LLM基础架构 · Token混合原语优化
tags:
- Token Mixing
- Attention Alternative
- FlashRelation
- Relation Cache
- Decoder LLM
one_liner: 提出显式拆分Self/Exchange关系的Token混合原语，效果优于同规模MHA且支持高效部署
practical_value: '- 小参数LLM落地场景（如Agent意图理解、推荐prompt生成、电商文案生成）可尝试用Relation替换MHA，同参数下NLL更低，生成质量更优

  - 长序列用户行为建模可借鉴Hybrid Relation架构：75%线性层+25%全量层的组合，平衡长序列建模效率和效果，降低计算成本

  - 推理侧优化可参考FlashRelation、Relation Cache设计，在不损失效果的前提下提升3.6~4.4倍推理速度，降低缓存显存占用

  - 序列建模可复用Self/Exchange拆分思路：显式控制当前token自身信息和历史信息的权重分配，适配用户实时兴趣建模、query理解等场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统多头注意力（MHA）将token间关系建模和信息流分配压缩为单步计算，单个标量得分无法承载语言场景中异构的token交互关系，且长序列下计算、显存瓶颈明显，亟需更结构化、高效的Token混合原语。
### 方法关键点
- 核心拆分两类显式关系：Self描述token与自身的关系，Exchange描述token与历史其他token的关系，先构造关系矩阵$R$再计算归一化信息流，践行「Flow follows Relation」的设计理念
- 衍生多场景实现族：Full Relation保留全量token级交互，FlashRelation通过分块扫描实现无全矩阵物化的高效执行，Linear Relation用循环状态压缩历史信息，Hybrid Relation混合线性层与全量层平衡效率效果，Relation Cache替代KV Cache支持自回归解码
- 新增对数长度校准项适配不同序列长度，引入Givens正交旋转实现相邻注意力头的信息交互
### 关键结果
- 数据集采用TinyStories、SmolLM corpus，基线为同结构、同训练配置的MHA decoder模型
- 10M/30M/100M三个参数规模下，Full Relation的验证NLL比MHA分别低0.0412/0.0151/0.0310
- FlashRelation比物化Full Relation实现快3.60~4.41倍，吞吐量达PyTorch FlashAttention的76.4%~84.9%
- 75% Linear+25% Full的Hybrid Relation在30M级模型上NLL达1.278，效果优于纯Full Relation
> 最值得记住的结论：Token混合无需直接围绕信息流设计，可先完成显式关系建模再推导信息流
