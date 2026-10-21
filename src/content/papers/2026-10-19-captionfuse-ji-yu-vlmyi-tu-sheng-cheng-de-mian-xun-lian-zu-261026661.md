---
title: 'CaptionFuse: Training-Free Composed Product Retrieval Via VLM Intent Captioning
  and Weighted Embedding Fusion'
title_zh: CaptionFuse：基于VLM意图生成的免训练组合商品检索方法
authors:
- Zhao Gao
- Mina Metias
- Mohamed Noordeen Alaudeen
- Bassel Saleh
affiliations:
- AWS GenAI Innovation Center
arxiv_id: '2610.26661'
url: https://arxiv.org/abs/2610.26661
pdf_url: https://arxiv.org/pdf/2610.26661
published: '2026-10-19'
collected: '2026-10-21'
category: RecSys
direction: 组合商品检索 · 免训练多模态融合
tags:
- Composed Image Retrieval
- VLM
- Training-Free
- E-commerce Search
- Embedding Fusion
one_liner: 将组合商品检索的融合从嵌入空间迁移到语言空间，免训练即可显著提升属性稀疏查询的检索效果
practical_value: '- 组合检索场景优先做语言空间融合而非嵌入空间算术融合：对用户属性稀疏的修改指令，用VLM生成补全全属性的类商品标题文案，能大幅提升查询与目标的嵌入对齐度，比调嵌入融合权重收益高5倍以上

  - 可复用prompt设计规则：强制VLM输出8-15字短商品标题格式，禁止对比类表述（如“代替原来的XX”），要求覆盖颜色/材质/版型等核心属性，比verbose长caption提升R@10
  5.2个点

  - 降本trick可直接复用：用规则-based的描述性打分路由，对已经包含>3个具体属性的查询直接走原文本编码，可节省26% VLM调用量，仅损失<1.1 R@10；搭配caption缓存可进一步降低调用成本

  - 架构上优先做组件解耦：CaptionFuse的VLM、embedding encoder、向量索引完全独立，可无缝升级各组件，比如从CLIP换为Titan
  backbone无需修改其他逻辑，即可获得+7.6 FashionIQ Avg R@10的提升'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
组合商品检索（给定参考图+文本修改指令找目标商品）是电商搜索核心能力，训练式方案依赖稀缺的三元组标注难落地，现有免训练方案多在嵌入空间做算术融合，但用户修改文本普遍属性稀疏（仅说明修改属性，未提及需保留的属性），且祈使类修改指令和CLIP预训练的描述性Alt-text分布差异大，导致文本嵌入和目标商品嵌入相似度存在36%的gap，线性融合无法弥补，效果受限。

### 方法关键点
- 提出语言空间融合范式：用VLM同时理解参考图与修改文本，生成补全所有保留+修改属性的短商品标题式caption，填补用户未提及的属性缺口
- 加权嵌入融合：caption编码后与参考图嵌入按固定权重融合，最优全局权重α=0.15（仅保留15%参考图信号，其余依赖caption）
- 规则式混合路由：通过属性匹配打分判断文本修改的描述性，对属性充足的查询直接走原文本编码，减少不必要的VLM调用

### 关键结果
在3个标准基准测试，统一使用CLIP ViT-L/14 backbone：FashionIQ数据集Avg R@10达27.2%，和当前最优免训练baseline WeiMoCIR仅差1个点；123K库的CIRCO数据集上mAP达22.4%，较WeiMoCIR提升8.5个点，R@10提升11.5个点；升级为Titan backbone后CIRCO mAP进一步提升至31.7%。失败分析显示仅5%错误来自VLM幻觉，68%来自embedding backbone的细粒度属性区分能力不足。

最值得记住的一句话：检索效果由查询的属性丰富度而非语言风格决定，prompt工程的收益远高于更换VLM或调整融合权重。
