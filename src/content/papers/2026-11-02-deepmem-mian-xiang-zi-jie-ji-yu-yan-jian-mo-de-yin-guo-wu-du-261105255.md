---
title: Going Deeper With Memories
title_zh: DEEPMEM：面向字节级语言建模的因果无损多尺度记忆架构
authors:
- Afshin Khadangi
affiliations:
- University of Luxembourg
arxiv_id: '2611.05255'
url: https://arxiv.org/abs/2611.05255
pdf_url: https://arxiv.org/pdf/2611.05255
published: '2026-11-02'
collected: '2026-11-04'
category: LLM
direction: 字节级语言模型 · 多尺度无损编码
tags:
- Byte-level-LLM
- Multiscale-Architecture
- FastWeight
- Lossless-Encoding
- Causal-Modeling
one_liner: 提出分离语义压缩与字节无损保留的多尺度架构，显著提升字节级语言模型性能与推理效率
practical_value: '- 可借鉴「语义压缩+无损细节旁路」的分层架构优化长序列推荐的用户行为序列建模，降低长序列计算开销的同时保留细粒度交互特征

  - 多语种商品标题/query理解场景可尝试字节级建模替代子词tokenizer，避免小语种/稀有词/特殊符号的切分错误，提升跨语种泛化性

  - 长文本生成类Agent可复用因果超分辨率解码的延迟分配规则，避免未来信息泄露的同时降低长序列生成的KV cache占用

  - FastWeight+共享瓶颈迭代优化的设计可复用到大模型推理优化，在低分辨率语义空间做多轮推理，大幅降低FLOPs开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
字节级语言模型可彻底避免子词tokenizer引入的切分错误、语种偏见、噪声鲁棒性差等问题，但全分辨率逐字节计算开销极高，现有分层压缩方案存在压缩效率与字节信息保真度的矛盾，难以兼顾效果与效率。

### 方法关键点
- 双路并行架构：分离语义流（渐进压缩做长程语义建模）与无损载波流（固定8维比特编码+可学习可逆小波变换，逐层级保留字节细节，可精确还原原始字节）
- 编码器用FastWeight记忆块做分层语义计算，最深层仅16个语义token，支持多轮共享参数的瓶颈迭代优化，推理FLOPs较全分辨率降低7600×
- 因果超分辨率解码器：采用延迟父节点分配规则避免未来信息泄露，融合编码器旁路特征、载波特征恢复高分辨率语义表示

### 关键结果
100M参数量下，对比同参数的字节Transformer基线：FineWeb-Edu BPB低3.1%，PG19 BPB低1.6%，8语种FLORES平均BPB低1.9%，推理吞吐量达Transformer的81.4%，HellaSwag零样本准确率高1.5个百分点。

### 核心结论
分层架构中将语义抽象与细粒度信息保留拆分为独立路径，可在大幅降低计算开销的同时，甚至提升模型的泛化性与鲁棒性。
