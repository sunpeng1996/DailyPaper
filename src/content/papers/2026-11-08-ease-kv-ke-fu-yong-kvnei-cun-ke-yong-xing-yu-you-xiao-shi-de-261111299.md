---
title: 'EASE-KV: Diagnosing the Gap Between Memory Availability and Effective Use'
title_zh: EASE-KV：可复用KV内存可用性与有效使用的差距诊断框架
authors:
- Di Lu
- Zechen Li
- Xuanyu Yue
- Jiabo Fan
- Hao Xue
- Flora D. Salim
affiliations:
- University of New South Wales
- Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2611.11299'
url: https://arxiv.org/abs/2611.11299
pdf_url: https://arxiv.org/pdf/2611.11299
published: '2026-11-08'
collected: '2026-11-10'
category: LLM
direction: LLM KV内存复用 性能瓶颈诊断
tags:
- KV cache
- Memory Reuse
- LLM Inference
- Attention Steering
- Reward Engineering
one_liner: 分解KV内存复用的三个影响维度，量化编码、分配、监督各环节的性能增益上限
practical_value: '- 搭建RAG/Agent长时记忆系统时，优先保证KV编码时的上下文可见性，采用因果编码而非块对角/独立编码，可直接提升多跳推理准确率10~25pp，收益远高于推理阶段补充分隔符、锚点等cue的效果

  - 做KV内存权重分配时，不要直接用检索相似度排序作为注意力优先级，证据导向的正负bias（相关内存+2，无关内存-2）可在不重编码的情况下提升LongMemEval准确率7.2pp，更适配多跳推理场景

  - 训练内存分配策略时，不要仅依赖二元正确/错误reward，加入塑形reward可将存在差异反馈的query占比从53%提升到73.6%，大幅降低策略学习难度

  - 针对Agent多轮对话的时序记忆冲突场景，仅在分配侧增加时间衰减bias就能补上93%的文本-latent性能差，无需额外编码或删除历史记忆'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
可复用KV内存能避免重复预填充检索文本，大幅降低LLM长上下文推理时延，但现有系统普遍存在「内存已存入但无法作为有效证据影响输出」的问题，端到端优化无法定位瓶颈是在编码、分配还是监督环节，亟需可拆解的诊断框架定位性能gap。

### 方法关键点
- 提出EASE-KV三阶段诊断框架，固定候选集和冻住LLM backbone，分别隔离三个影响环节：编码（保留了什么信息）、分配（如何控制已有内存的影响力）、监督（能否从反馈中学到最优分配策略）
- 编码侧控制跨内存可见性，对比独立编码、块对角编码、因果编码三种模式的信息保留度
- 分配侧通过给每个内存块的attention logit加可配置正负bias，在不修改存储KV的情况下控制不同内存的相对影响力
- 监督侧通过组内reward方差量化不同reward设计的反馈区分度，验证分配策略的可学习性

### 关键实验
基于Qwen2.5-7B、Llama 8B、Gemma 12B三个模型，在可控多跳推理任务、LongMemEval长时对话记忆基准、时序冲突场景下测试：
- 编码侧：因果编码比块对角编码的组合准确率高25.0pp（Qwen）/10pp（Llama/Gemma），推理阶段加分隔符、锚点等桥接方法完全无法补回独立编码损失的上下文信息
- 分配侧：证据导向的bias分配可将LongMemEval准确率从31.2%提升到38.4%，时序冲突场景下加recency bias可补回93.3%的文本-KV性能差
- 监督侧：二元正确reward仅能给53.0%的query组提供有效反馈，加塑形reward后提升到73.6%，但训练得到的分配策略相比手工bias无明显增益

### 核心结论
KV内存有效复用的优先级是「先保编码时的关系保留，再优化分配权重，最后验证监督信号区分度」，不要把所有内存失效问题都归为召回错误。
