---
title: A Quantized Native Runtime for On-Device Semantic Audio Generation
title_zh: 面向端侧语义音频生成的量化原生运行时
authors:
- Matteo Spanio
- Antonio Rodà
affiliations:
- Centro di Sonologia Computazionale (CSC), University of Padova
- Dept. of Information Engineering, University of Padova
arxiv_id: '2607.08526'
url: https://arxiv.org/abs/2607.08526
pdf_url: https://arxiv.org/pdf/2607.08526
published: '2026-07-08'
collected: '2026-07-10'
category: Other
direction: 端侧生成 · 量化推理运行时
tags:
- quantization
- on-device inference
- native runtime
- audio generation
- activation steering
one_liner: 提出无依赖原生运行时aria，支持端侧低比特量化运行Stable Audio 3，大幅降内存、提启动与生成速度
practical_value: '- 电商端侧智能导购、商品定制化音效生成等场景可直接复用8bit量化无精度损失的结论，优先采用8bit量化降低端侧内存占用、提升推理速度

  - 端侧生成类模型部署可参考无依赖原生运行时的设计思路，砍掉Python/通用DL框架依赖，最高可降低7倍冷启动延迟，适配端侧低时延交互需求

  - 激活steering的低成本生成控制思路可迁移到端侧推荐/Agent场景，无需重跑模型即可通过调整内部张量实现生成内容的属性管控，适配个性化需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
语义音频生成正从云端Demo向端侧交互式工具、嵌入式设备场景迁移，现有依赖Python/深度学习框架的部署方案内存占用高、冷启动慢，无法适配消费级硬件、嵌入式设备的严格资源约束。
### 方法关键点
1. 自研无依赖原生运行时aria，无需底层Python或通用DL框架支持，可直接在GPU、CPU、树莓派5上运行完整Stable Audio 3文本转音乐管线；
2. 实现原位内存优化的低比特量化方案，直接降低模型运行内存，无额外内存开销；
3. 内置激活steering接口，可低成本控制生成内容的属性特征。
### 关键结果
8bit量化无任何可测质量损失，是GPU上最快的运行模式；4bit量化仅带来小幅可控质量损失，可将1.2B参数模型运行在8GB内存的树莓派5上；对比官方实现，生成速度持平或更优，启动速度快7倍。
