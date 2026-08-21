---
title: 'Daedalus-150M: A Convolution-Attention Hybrid Designed for CPU Inference'
title_zh: Daedalus-150M：面向CPU推理的卷积-注意力混合小语言模型
authors:
- Christos Koutsiaris
arxiv_id: '2608.20210'
url: https://arxiv.org/abs/2608.20210
pdf_url: https://arxiv.org/pdf/2608.20210
published: '2026-08-20'
collected: '2026-08-21'
category: LLM
direction: 小语言模型 · CPU端高效推理优化
tags:
- Small LLM
- CPU Inference
- Hybrid Architecture
- Quantization
- KV Cache
one_liner: 150M参数量卷积-注意力混合小模型，单用户CPU推理速度随上下文提升，效果超同规模全注意力基线
practical_value: '- 端侧/离线Agent推理架构参考：可复用「多数固定状态卷积层+少量注意力层」的混合设计，大幅降低长上下文下KV cache开销，适配客户端/CPU部署的轻量Agent需求

  - 小模型训练优化：低参数量模型可采用「学习率线性衰减到0+高质量小 corpus 多轮训练」的策略，用1/10级别的训练数据量达到同参数级大训练量模型效果

  - 4-bit量化落地技巧：CPU部署优先选择Q4_0量化格式，其点积 kernel 优化成熟，在小模型上即使无量化感知训练，精度损失也可接受，吞吐量收益显著

  - 长上下文推理成本控制：面向会话式推荐、长文档RAG的CPU部署场景，可通过调整注意力层占比、搭配GQA，在不损失召回能力的前提下压低推理延迟'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
小语言模型通常照搬大模型架构后压缩适配CPU，未考虑单用户CPU推理的特有约束：batch size=1无批量摊销、内存带宽优先于计算、KV cache随上下文线性增长成为延迟瓶颈，长会话/长文档场景下性能衰减严重。

### 方法关键点
- 架构：18层混合堆叠，仅6层用搭配GQA的注意力层，12层用核长3的深度可分离短卷积层，卷积层仅保留2个时间步的固定状态，不受上下文长度影响，层交错分布保证长程检索能力
- 训练：用16.9B高质量教育/代码/对话混合语料训练59.9B token，每个语源最多重复4轮避免过拟合；拆分参数用Muon优化二维权重、AdamW优化嵌入与归一化层，学习率采用线性衰减到0的调度提升样本效率
- 部署：绑定输入输出嵌入减少参数量，FFN内层维度设为2.67×d_model降低带宽开销，直接适配llama.cpp的Q4_0量化格式，无需自定义kernel即可跑在通用CPU上

### 关键结果
对比同参数量全注意力基线，4-bit量化下2048上下文推理速度快1.76×，模型体积小6.3%，验证集bits-per-byte优0.81%，下游5任务效果持平；对比训练数据量1T的MobileLLM-125M，5任务得分47.31更高，2048上下文推理速度快2.08×，训练数据量仅为后者的6%。

> 最值得记住：单用户CPU推理场景下，架构优化核心是降低KV cache增长开销而非单纯减参，混合设计的速度优势随上下文扩大，天然适配长会话、长文档RAG场景
