---
title: 'N-Gram Memories at Two Bits: Quantizing Lookup Tables in Large Language Models'
title_zh: 《2比特n-gram存储：大语言模型查找表量化方法》
authors:
- Donghoon Han
- Minseop Jung
- Dong Woo Kwak
- SeungJae Lee
- Junhoo Lee
affiliations:
- Dnotitia Inc.
- KAIST
arxiv_id: '2610.21810'
url: https://arxiv.org/abs/2610.21810
pdf_url: https://arxiv.org/pdf/2610.21810
published: '2026-10-15'
collected: '2026-10-20'
category: LLM
direction: LLM推理优化 · 查找表量化
tags:
- Quantization
- Lookup Table
- N-gram Memory
- LLM Inference
- Memory Optimization
one_liner: 提出Conditional Program量化方案，将LLM n-gram查找表压缩4-8倍，效果损失极小且提升推理容量
practical_value: '- 推荐系统大规模用户/物品Embedding表可直接复用CP设计：每行列存短code+本地scale、共享高斯格形解码器，无需重训即可实现4-8倍压缩，大幅节省GPU
  HBM，适配召回/粗排等稀疏查表场景

  - 带外部记忆的Agent/RAG系统可复用独立行存储+按需重建的架构，相比块存储查表延迟降低约40%，尤其适合跨PCIe访问离线记忆库的场景

  - Embedding量化选型可直接复用论文结论：优先保留原始向量的norm比最小化重建MSE更能降低下游任务的输出KL，无需额外开销就能提升量化效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM通过n-gram等条件记忆查表扩容时，无需提升逐token计算量，但上百GB的Embedding查找表会占满GPU显存；现有LLM压缩方案针对稠密权重设计，未适配稀疏查表的独立访问需求，压缩后需读取整块数据才能获取单条记录，查表效率极低。

### 方法关键点
- 提出Conditional Program（CP）压缩范式：每行仅存储短量化code+bf16 scale，共享全局高斯格形解码器，仅按需重建查询到的行，用少量重建计算置换全表存储开销
- 基于中心极限定理假设归一化后的行坐标服从标准高斯分布，采用共享格形量化（TCQ）编码，无需训练专属码本，编码成本极低
- 压缩时直接保留原始行的norm，而非最小化向量重建MSE，避免幅值损失导致的下游效果下降，每行独立存储，无需解码无关行即可完成查询

### 关键结果
测试DeepSeek、Qwen、LongCat三个带n-gram查找表的模型，覆盖40个下游任务，对比RTN、QTIP、NVFP4等主流量化方案：2比特CP将查找表压缩4-8倍，DeepSeek的203GB表降至51GB，输出KL比2比特RTN低41-63%，多数任务得分与原表几乎一致；推理侧4卡H200部署DeepSeek时，2比特CP比FP8表单卡省38GB显存，64k token预填充延迟从OOM降至18.23s，8卡部署时解码batch上限从1024提升至2048，跨PCIe查表延迟从10.78ms降至6.54ms。

### 核心结论
针对稀疏访问的Embedding表，量化时优先保留行的原始范数、用共享通用源模型替代专属码本，能在极低存储开销下同时保障效果和查表效率。
