---
title: 'Dory1.0-4B: A Looped Normalized-GPT'
title_zh: Dory1.0-4B：4B参数循环归一化GPT弹性深度大模型
authors:
- Maxim Fishman
- Simeng Sun
- Shantanu Acharya
- Faisal Ladhak
- Brian Chmiel
- Santiago Akle Serano
- Ron Banner
- Boris Ginsburg
- Krishna C. Puvvada
affiliations:
- NVIDIA
arxiv_id: '2611.03998'
url: https://arxiv.org/abs/2611.03998
pdf_url: https://arxiv.org/pdf/2611.03998
published: '2026-11-02'
collected: '2026-11-04'
category: LLM
direction: 大模型 · 弹性深度循环架构
tags:
- Looped-LLM
- nGPT
- Elastic-Depth
- KV-Cache
- Quantization
- Agentic-LLM
one_liner: 4B参数循环归一化GPT单checkpoint可调节推理深度，性能超9B/12B/26B同类模型
practical_value: '- 可复用弹性深度架构思路，为业务LLM提供精度-延迟动态调节能力：电商Agent复杂工具调用/多步骤导购场景增加循环提升准确率，简单查询/推荐文案生成用单循环降本

  - last-loop KV cache优化可直接落地，多轮循环推理时KV缓存不随循环数线性增长，显著降低长上下文用户导购、商品属性理解场景的内存开销

  - 难度感知循环训练课程可迁移到业务LLM微调，难例（如复杂query理解、多轮推荐规划）分配更深循环，提升整体效果同时控制训练成本

  - 同checkpoint自投机解码思路可复用，用浅循环作为draft模型、深循环作为verify模型，无需额外训练小模型即可提升推理吞吐量1.11~1.53×'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM测试时计算大多消耗在token生成侧，推理成本、KV缓存开销随生成长度线性增长，无法灵活适配不同业务的精度-成本需求；循环（隐状态递归）LLM可在隐空间增加计算量不增加参数量，但此前缺乏成熟的工业级开源实现。

### 方法关键点
- 架构基于nGPT backbone，72层拆分为16层输入块、40层共享循环块、16层输出块，3:1比例交替滑动窗口注意力与全注意力，支持256K上下文
- 训练分三阶段：4.5T tokens NVFP4预训练，1.5T tokens BF16循环训练（采样1~4次循环，截断反向传播），300B tokens长上下文扩展；后训练采用SFT+难度感知RLVR，难例优先分配更深循环
- 推理优化：last-loop KV缓存仅保留最后一轮循环的KV，内存开销与单循环一致；同checkpoint自投机解码，浅循环draft、深循环verify，无需额外小模型
- 量化方案：MXFP8 PTQ精度接近BF16，NVFP4/Q5_K_M经量化感知蒸馏后保留98%以上能力，推理速度最高提升2.44×

### 关键结果
4B参数下，2次循环即可超过Qwen3.5-9B、Gemma4 12B、Gemma4 26B-A4B的12个基准平均得分；4次循环下Agent任务输出token减少1.3~2.5×，KV缓存开销与单循环持平，仅损失最多2.1分精度；量化后推理速度最高较BF16提升2.44×，自投机解码吞吐量提升1.37~1.71×。

### 最值得记住的一句话
弹性循环架构用同一checkpoint实现精度与成本的动态tradeoff，小参数模型也可通过增加隐空间计算匹敌数倍参数量的大模型。
