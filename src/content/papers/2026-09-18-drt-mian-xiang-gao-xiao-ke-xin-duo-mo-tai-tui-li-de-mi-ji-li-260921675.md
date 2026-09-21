---
title: 'DRT: Dense Reasoning Trace for Efficient and Grounded Multimodal Reasoning'
title_zh: DRT：面向高效可信多模态推理的密集推理轨迹范式
authors:
- Wan Xu
- Yuanfan Guo
- Kevin Han
- LaLa Chen
- Wangmeng Zuo
affiliations:
- Harbin Institute of Technology
- ByteDance Inc
- Facebook
- University of California, Irvine
arxiv_id: '2609.21675'
url: https://arxiv.org/abs/2609.21675
pdf_url: https://arxiv.org/pdf/2609.21675
published: '2026-09-18'
collected: '2026-09-21'
category: Reasoning
direction: 多模态大模型 · 高效推理范式优化
tags:
- Multimodal Reasoning
- Chain-of-Thought
- GRPO
- Reinforcement Learning
- MLLM
one_liner: 提出结构化密集推理轨迹替代自然语言CoT，实现多模态推理效率与准确率双提升
practical_value: '- 电商多模态导购Agent、商品理解场景可复用DRT的<visual>/<think>/<answer>三段式结构化推理格式，解耦视觉感知与逻辑推理，减少冗余token生成的同时降低幻觉，提升商品属性识别、搭配推荐等任务准确率。

  - 大模型推理优化可复用「三视角验证+Trace-Grounded GRPO」训练范式，针对业务特定推理任务构造紧凑轨迹SFT数据集，结合过程奖励RL优化，可在低token预算下保留推理能力，适配高QPS的搜索推荐实时场景。

  - 长链路推理场景（如复杂用户query语义理解、多步商品归因）可借鉴DRT的符号化连接器设计，用→等符号替代冗余自然语言描述，提升KV cache利用率，推理吞吐量可提升数倍。'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有多模态大模型的CoT推理完全依赖自然语言表达空间，存在严重语言冗余，既导致推理token效率低、计算成本高，还会因信息稀释让模型更关注生成文本而非原始视觉证据，加剧多模态幻觉。现有高效推理优化方案仍未跳出自然语言表达空间的限制，无法从根源解决效率与效果的平衡问题。

### 方法关键点
- 提出DRT结构化推理范式，将推理轨迹拆解为<visual>视觉证据、<think>符号化紧凑推导（显式声明[Priors]先验规则）、<answer>结论三个模块，解耦感知与推理，用符号连接器替代冗余自然语言描述，大幅提升信息密度。
- 两阶段训练框架：第一阶段密集轨迹初始化，构造200K DRT-SFT数据集，通过「解构-压缩-锚定」三步将原始长CoT改写为紧凑格式做SFT，让模型习得DRT推理模式。
- 第二阶段轨迹锚定RL优化，先通过「答案正确、逻辑一致、视觉忠实」三视角验证pipeline构造高质量DRT-RL数据集，再用带过程奖励+探索激励的Trace-Grounded GRPO优化，减少幻觉同时保证推理完整性。

### 关键结果
在MathVista、MathVerse、LogicVista等5个多模态/文本推理基准上，对比Qwen3-VL不同推理范式、CoD、ThinkLess等高效推理基线，DRT-RL相对Qwen3-VL官方CoT baseline实现**5.5× token效率提升**，推理准确率提升1.3个百分点，吞吐量提升4.6倍，推理时延降低80%。

最值得记住的结论：复杂多模态推理不需要冗长的自然语言推理轨迹，通过重构推理表达空间即可实现效率与效果的双重提升。
