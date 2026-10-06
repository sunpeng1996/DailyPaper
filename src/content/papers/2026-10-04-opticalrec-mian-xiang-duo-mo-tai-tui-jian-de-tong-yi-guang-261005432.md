---
title: 'OpticalRec: Unified Optical Vision-Language Representation for Multimodal
  Recommendation'
title_zh: OpticalRec：面向多模态推荐的统一光学视觉语言表示框架
authors:
- Yueqi Wang
- Zitian Guo
- Yupeng Hou
- Yifei Wang
- Kibum Kim
- Zhenrui Yue
- Shuo Xing
- Haodong Li
- Heming Xia
- Renrui Zhang
affiliations:
- University of California, San Diego
- Alibaba Group
- University of Illinois Urbana-Champaign
- The Hong Kong Polytechnic University
- Texas A&M University
arxiv_id: '2610.05432'
url: https://arxiv.org/abs/2610.05432
pdf_url: https://arxiv.org/pdf/2610.05432
published: '2026-10-04'
collected: '2026-10-06'
category: RecSys
direction: 多模态推荐 · 跨模态统一编码
tags:
- Multimodal Recommendation
- Vision-Language Model
- Cross-Modal Fusion
- Collaborative Filtering
- Item Representation
one_liner: 将商品文本元数据渲染为视觉 glyph 合并图像输入VLM，免 late fusion 提升多模态推荐效果
practical_value: '- 多模态特征融合可直接复用渲染思路：把商品标题/价格/品牌等元数据渲染到商品图空白区域，用现成VLM（如Qwen-VL、InternVL）直接输出统一item
  embedding，省去独立编码+late fusion的复杂流程，迁移成本极低

  - 渲染操作可离线批量执行，对布局、字体、颜色鲁棒性强，无需精细调参，544×544分辨率性价比最高，7万级商品仅需不到1小时预处理，适合电商大规模商品库落地

  - 现有多模态协同过滤召回/排序模型可直接替换原有item embedding为OpticalRec输出，无需修改模型结构就能获得1.5%~3%的NDCG@20提升，图结构推荐模型收益更明显'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前多模态推荐主流方案是视觉、文本模态独立编码后通过拼接、求和或图结构做late fusion，既缺失原生跨模态交互，又会引入语义失真，成为多模态item表征和用户-物品匹配的核心瓶颈。

### 方法关键点
- 提出像素空间统一编码范式，离线将商品图像、文本元数据（标题/品牌/品类/价格）按照电商商品页布局渲染为统一卡片图像，无需额外训练VLM
- 统一卡片直接输入冻结的多模态VLM，同时利用VLM视觉编码器的感知层跨注意力、语言解码器的语义层跨注意力完成图像与文本的原生交互，输出统一item embedding，完全省去late fusion步骤
- 通过互信息分析和矩阵有效秩从理论上证明该方案比late fusion保留更多跨模态信息，表征丰富度更高

### 关键实验
在Amazon Baby、Pets、Clothing三个电商数据集上，对比VBPR、LATTICE、FREEDOM等5个主流多模态推荐基线，平均NDCG@20提升2.41%，Pets数据集最大提升5.82%，对图结构推荐模型的平均收益达2.5%左右；渲染操作对布局、字体、颜色鲁棒，性能波动在±1%以内，7.5万商品仅需57分钟离线预处理。

最值得记住的结论：让模型像用户一样同时感知商品图和文本介绍的统一编码范式，比人为拆分模态再融合的方案效果更优、落地更简单。
