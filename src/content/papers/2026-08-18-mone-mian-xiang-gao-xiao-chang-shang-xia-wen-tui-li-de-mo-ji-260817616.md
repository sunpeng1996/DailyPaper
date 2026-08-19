---
title: 'MoNe: Modular Neural Memory for Efficient Long Context Inference'
title_zh: MoNe：面向高效长上下文推理的模块化神经记忆插件
authors:
- Wonguk Cho
- Kyubyung Chae
- Tribhuvanesh Orekondy
- Sunghyun Park
- Hyoungwoo Park
- Jeongho Kim
- Arash Behboodi
- Kyuwoong Hwang
- Sungrack Yun
affiliations:
- Qualcomm AI Research
arxiv_id: '2608.17616'
url: https://arxiv.org/abs/2608.17616
pdf_url: https://arxiv.org/pdf/2608.17616
published: '2026-08-18'
collected: '2026-08-19'
category: LLM
direction: LLM长上下文推理 · 即插即用神经记忆
tags:
- Long-Context-Inference
- Neural-Memory
- Test-Time-Learning
- Efficient-Inference
- Transformer
one_liner: 为冻结预训练Transformer提供无重训长上下文推理能力，128K场景显存算力较ICL降80%
practical_value: '- 端侧电商Agent/个性化推荐场景可直接复用MoNe插件，将用户数月的长行为历史编码为固定大小神经记忆，无需每次拼接全量历史到prompt，端侧显存可降80%，推理成本不随历史长度增长，还能支持超过LLM原生窗口的超长行为序列建模

  - 解决现有RAG在跨多段分散信息推理的痛点：例如用户查询“近半年买过的单价超过300的户外装备清单”这类需要聚合多段信息的需求，可将全量用户订单/浏览历史先用MoNe编码为记忆，推理时结合记忆输出，准确率较纯RAG提升20%+

  - 工程改造成本极低：MoNe仅附加6.4%参数，测试阶段仅做层内局部梯度更新，完全不修改原有LLM backbone权重，可直接适配已上线的LLM服务，无需重新训练和部署大模型

  - 多查询复用优化：同一个用户的多轮查询可复用预编码的记忆状态，新增行为仅需做增量更新，无需重处理全量历史，大幅降低高并发个性化推荐/用户咨询场景的推理成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有长上下文推理方案存在显著短板：ICL自attention成本随序列长度平方增长，KV cache显存随长度线性上升，超过原生窗口后性能暴跌；RAG依赖嵌入检索，无法处理需要整合多段分散关联信息的任务；Mamba等新架构需全量重训，无法复用成熟预训练Transformer。端侧电商Agent、个性化推荐等场景亟需低成本、无重训的长上下文处理能力。
### 方法关键点
- 即插即用架构：为每一层冻结Transformer decoder附加SwiGLU结构的fast-weight神经记忆模块，总参数仅增加6.4%，完全不修改backbone权重
- 两阶段处理：测试阶段学习时将长上下文切为512 token固定段，逐层用关联记忆损失做层内局部梯度更新，仅更新记忆模块参数，预处理复杂度O(N)；推理时仅用查询token读取记忆生成固定大小KV，推理成本O(1)，显存不随上下文长度增长
- 段内RoPE编码：位置索引始终落在[0,512)区间，无需位置插值即可泛化到远超原生窗口的长度，记忆状态支持多查询复用、增量更新
### 关键实验
以Qwen2.5-0.5B为backbone，在RULER基准的S-NIAH、MK-NIAH、高频词提取任务上对比ICL、RAG：128K上下文下，MoNe较ICL降低80%显存和算力，三类任务准确率分别达0.96、0.94、0.96，远高于ICL的0.28、0.00、0.23，也优于RAG的0.89、0.71、0.60；仅在4K长度下训练即可泛化到128K长度。
### 核心结论
仅增加6.4%参数的即插即用神经记忆模块，就能让冻结Transformer获得超32倍训练时长度的长上下文推理能力，同时降低80%显存与算力开销。
