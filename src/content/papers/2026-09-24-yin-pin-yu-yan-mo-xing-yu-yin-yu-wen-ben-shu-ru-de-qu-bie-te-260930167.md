---
title: Do Audio Language Models Hear and Read Distinctive Features Alike?
title_zh: 音频语言模型语音与文本输入的区别性特征表征一致性研究
authors:
- Yuanhao Chen
- Peter Chin
affiliations:
- Thayer School of Engineering, Dartmouth College
arxiv_id: '2609.30167'
url: https://arxiv.org/abs/2609.30167
pdf_url: https://arxiv.org/pdf/2609.30167
published: '2026-09-24'
collected: '2026-09-25'
category: LLM
direction: 音频大模型 · 跨模态表征对齐研究
tags:
- Audio LLM
- Cross-modal Representation
- Phonological Feature
- Multilingual
- Representation Alignment
one_liner: 对比6款音频大模型跨7类特征15种语言的音系表征一致性，仅Qwen2.5-Omni清浊特征达显著对齐
practical_value: '- 跨模态表征对齐评估方法可复用：采用「最小差异对表征偏移量计算特征方向+随机配对基线校正」的范式，可直接迁移到电商多模态（图文/音视频）推荐的跨模态表征对齐度量化评估

  - 多语言语义对齐验证方法可借鉴：跨语言单特征一致性校验方法，可用于跨境电商多语言搜索、多语言商品推荐的语义对齐效果验证

  - 大模型选型策略参考：特征表征对齐效果由模型家族而非尺寸决定，多模态大模型选型时可优先匹配架构，无需盲目堆叠参数'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有音频语言模型（ALM）共用同一解码器处理语音、文本输入流，但两类输入下同一音系区别性特征的表征是否对齐尚不明确，缺乏跨模态、跨语言的系统性验证框架。

### 方法关键点
针对仅存在单特征差异的音素最小对，计算两类音素平均表征的偏移量，聚合得到语音/文本流各自的特征方向，通过两类方向的余弦相似度衡量一致性；采用随机配对生成的参考基线替代零基准，消除任意音素对天然对齐带来的偏差。实验覆盖6款ALM、7类音系特征、11个语系下的15种语言。

### 关键结果数字
仅两款Qwen2.5-Omni模型的清浊特征一致性显著高于随机基线；6款模型中有3款的清浊特征在14种语言的语音流中方向统一，其中2款所有语言对均完全对齐；模型家族而非模型尺寸是特征表征所属流的核心预测因子。
