---
title: Bigger Model or Bigger Table? How Much Backbone a Chorus N-gram Module Replaces
title_zh: 更大模型还是更大表？Chorus N-gram模块可替代多少Transformer骨干参数
authors:
- Szymon Kocur
affiliations:
- Independent Researcher, Warsaw, Poland
arxiv_id: '2611.34725'
url: https://arxiv.org/abs/2611.34725
pdf_url: https://arxiv.org/pdf/2611.34725
published: '2026-11-25'
collected: '2026-11-26'
category: LLM
direction: LLM结构优化 · N-gram模块替代率量化
tags:
- Chorus
- N-gram
- Transformer
- Lookup Memory
- Scaling Law
one_liner: 量化16M~349M规模下Chorus N-gram模块对Transformer骨干的等效替代倍率
practical_value: '- 端侧生成推荐文案、搜索Query补全场景下，可引入Chorus N-gram模块，16M骨干加1倍参数量的表即可达到21M纯模型效果，降低端侧推理延迟

  - 训练小尺寸垂域LLM（如电商导购Agent专用模型）时，优先加N-gram查表内存而非扩大骨干参数，同等效果下训练速度提升3%~11%，降低训练成本

  - Chorus的N-gram表可量化到4bit几乎无损，适合部署在内存受限的端侧电商导购Agent，可节省75%的表存储开销

  - 垂域推荐场景下的高频N-gram模式（如用户搜索词搭配、商品标题常见组合）可直接复用Chorus的跨层共享查表架构，无需扩大LLM骨干规模'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有查表式内存模块（如Chorus、Engram）可在几乎不增加单token计算量的前提下扩充LLM参数量，但行业缺乏不同骨干规模下的等效替代量化数据，从业者无法判断扩大骨干参数还是加N-gram表的性价比更高，且过往对比多采用统一学习率，对两类模型的公平性不足，结论存在偏差。

### 方法关键点
- 实验覆盖16M~550M共6种尺寸的Decoder-only Transformer骨干，Chorus模块包含跨层共享的bigram、trigram哈希表，参数增量与骨干的比值覆盖0.275~21.7
- 为纯骨干模型和加Chorus的模型单独搜索最优学习率，消除学习率设置带来的评估偏差
- 定义「等效规模」：达到相同held-out损失时，纯骨干模型参数量与加Chorus的骨干参数量的比值为替代倍率

### 关键结果
在13.4亿token的古波兰语语料上训练，对比纯Transformer基线：
- 加与骨干参数量相当的Chorus表时，16M骨干等效倍率1.34，47M为1.29，107M~349M区间稳定在1.16~1.20
- 每新增1个Chorus参数最多可替代0.31个骨干参数，同等总参数量下纯骨干模型损失更低但推理计算量更高
- 加Chorus的模型训练速度比同等损失的纯骨干快3%~11%，N-gram表量化到4bit仅损失0.002 nat，效果几乎无损

小尺寸LLM（16M~100M）加N-gram表的性价比远高于扩大骨干参数，大尺寸模型加表的收益快速衰减。
