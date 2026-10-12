---
title: 'zip2zip++: Towards Inference-Time Token Compression with Minimal Quality Loss'
title_zh: zip2zip++：实现推理阶段几乎无质量损失的动态Token压缩
authors:
- Saibo Geng
- Andrea Gentilini
- Xinxian Ma
- Nathan Ranchin
- Yunzhen Yao
- Robert West
affiliations:
- EPFL
- Technical University of Munich
- Zuse School ELIZA
- ETH Zürich
arxiv_id: '2610.13605'
url: https://arxiv.org/abs/2610.13605
pdf_url: https://arxiv.org/pdf/2610.13605
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: LLM推理优化 · 动态Token压缩
tags:
- Dynamic Tokenization
- LZW Compression
- Inference Acceleration
- RoPE
- LoRA
- KV Cache
one_liner: 针对LZW动态Token压缩的质量损失问题提出4项优化，不改动预训练LLM即可缩小一半与无压缩基线的性能差
practical_value: '- 推理侧成本优化：电商推荐文案生成、Agent对话、搜索Query改写等大流量LLM场景可直接复用该压缩方案，在保证生成质量的前提下降低KV
  cache占用30%+，减少推理 latency，显著降低服务成本

  - 自定义Embedding设计：做动态Token、语义块合并类优化时，可复用「输入输出Embedding解耦+残差零初始化」的设计，避免训练初期分布偏移，大幅提升LoRA
  finetune效率

  - 敏感Token防护：对商品ID、订单号、数字类属性等业务敏感Token设置合并白名单，避免动态合并导致的识别错误，可将数值类推理准确率提升70%以上

  - 变长Token位置编码适配：业务中用到长上下文压缩、语义块合并的场景，可复用size-aware RoPE设计，按原Token跨度分配位置编码，避免位置信息失真导致的长上下文召回错误'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM的固定BPE词表对电商商品属性、代码、数值类结构化数据易过度分词，导致序列过长、推理 latency高、KV cache占用大；此前的zip2zip方案通过LZW算法动态合并Token实现约40%的压缩率，但会大幅降低推理质量，尤其是数学推理、长上下文理解能力，质量损失问题阻碍其业务落地。

### 方法关键点
- 解耦输入输出动态Embedding层：针对LZW前缀封闭词典的特性，分别训练输入/输出超编码器，解决共享编码器的几何结构冲突
- 残差零初始化超编码器：将超Token的Embedding初始化为其首个base Token的Embedding，仅学习残差修正，避免训练初期的分布偏移
- Size-aware RoPE：按超Token覆盖的原base Token的最后位置分配RoPE编码，避免合并后位置信息失真
- 容错LZW编解码器：支持数字、特殊符号等敏感Token禁止合并，采用多视角PPL评估聚合所有合法分词的概率，消除评价偏差

### 关键实验
在Phi-3.5-mini（3.8B）、Phi-3-medium（14B）等4个模型上测试，对比原zip2zip和无压缩基线：GSM8K数学推理准确率从原zip2zip的0.36提升到0.68，接近无压缩基线的0.75；所有语料perplexity均优于原zip2zip，与无压缩基线的质量差距缩小约50%；长上下文RULER基准4K准确率从46.6提升到70.7，32K准确率从15.2提升到52.8。

最值得记住的一句话：动态Token压缩的质量损失并非固有代价，通过针对性的嵌入层、位置编码、编解码器优化，可在保留高压缩率的同时几乎对齐无压缩模型的性能。
