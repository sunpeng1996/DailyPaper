---
title: 'MegaParts: Scaling Part-Aware 3D Object Generation to 300 Parts via Token-Efficient
  Autoregressive Modeling'
title_zh: MegaParts：基于Token高效自回归建模支持300部件级3D物体生成
authors:
- Manwen Liao
- Xinyu Lian
- Jian Mao
- Kaixu Chen
- Li Luo
- Jinghao Yan
- Wanshui Gan
- Qiao Yu
- Weitian Zhang
- Chunhua Shen
affiliations:
- Shanghai Artificial Intelligence Laboratory
- The University of Hong Kong
- Fudan University
- Tongji University
- University of Science and Technology of China
arxiv_id: '2608.14783'
url: https://arxiv.org/abs/2608.14783
pdf_url: https://arxiv.org/pdf/2608.14783
published: '2026-08-13'
collected: '2026-08-18'
category: Other
direction: 3D物体生成 · Token高效自回归建模
tags:
- Autoregressive Modeling
- Token Efficiency
- 3D Generation
- VQ Tokenizer
- Long Context Training
one_liner: 提出Token高效自回归3D生成框架，支持最多300个部件的复杂物体生成，效果优于现有基线
practical_value: '- 可复用「按内容复杂度动态分配Token」的自适应压缩思路，在长文本广告生成、多轮对话Agent等场景下降低长序列生成的显存与耗时开销，同时保障生成质量

  - 参考异构信息统一结构化序列建模方法，可将推荐场景下的用户行为、商品属性、上下文信息编码为统一序列输入LLM做生成式召回/排序

  - 可借鉴「Token压缩+长上下文训练」的组合策略，支撑十万级长度的超长用户行为序列建模，提升生成式推荐的长序列表征能力'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有部件感知3D生成方法无法适配高复杂度物体，随部件数量上升，Token长度、显存开销急剧膨胀，难以同时兼顾生成规模和几何精度。
### 方法关键点
1. 设计Token高效的向量量化形状Tokenizer，在保障高保真重建的前提下最小化Token用量，实现基于几何复杂度的自适应长度Token化；
2. 基于紧凑离散表示，用LLM在统一结构化序列中生成物体边界框、部件边界框、部件形状Token；
3. 搭配高效长上下文训练策略，降低超大规模序列的训练开销。
### 关键结果
可支持最多300个部件的3D物体生成，序列长度最高可达256k；生成网格质量优于基线自回归、扩散模型，压缩离散部件Token同时提升了生成保真度，验证了LLM原生的Token高效自回归建模在大规模部件级3D生成场景优于扩散范式。
