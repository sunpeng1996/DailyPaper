---
title: 'HyperStyler: Low-resource Authorship Style Transfer via Context-aware Style
  Navigation and Hypernetworks'
title_zh: HyperStyler：基于上下文感知风格导航与超网络的低资源作者风格迁移
authors:
- Jongkyung Shin
- Minguk Jeon
- Chanwoo Park
- Chiehyeon Lim
affiliations:
- UNIST
- POSTECH
- POSCO Holdings Inc.
arxiv_id: '2609.02772'
url: https://arxiv.org/abs/2609.02772
pdf_url: https://arxiv.org/pdf/2609.02772
published: '2026-09-02'
collected: '2026-09-04'
category: LLM
direction: 大模型低资源风格迁移 · 超网络优化
tags:
- Style Transfer
- Hypernetwork
- Low-resource Learning
- T5
- Inference Optimization
one_liner: HyperStyler解耦低资源风格迁移的风格选择与实现，兼顾保真度、语义保留与推理效率
practical_value: '- 电商商品文案/品牌话术/客服回复个性化场景，可复用该架构仅用少量参考样例迁移目标风格，大幅降低标注成本

  - 可借鉴风格选择+实现的解耦设计，替代现有直接注入隐向量的风格控制方案，降低风格与语义纠缠，提升生成内容语义一致性

  - 超网络动态参数调制思路可复用在大模型轻量适配场景，仅增加极少量参数即可实现特定能力适配，推理速度远高于ICL/全量微调方案'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
低资源作者风格迁移（LAST）仅需少量参考样例即可将文本改写为目标作者风格，现有方案普遍存在两个核心问题：一是将多份参考压缩为单一静态作者嵌入，抹平上下文相关的风格差异；二是依赖隐表示控制风格，导致风格与语义纠缠，难以同时兼顾风格保真度与语义保留。
### 方法关键点
HyperStyler架构将任务解耦为两个独立阶段：1）Stylo-navigator联合建模源文本上下文与目标作者参考样例，输出动态风格坐标；2）Stylo-hypernet通过动态参数调制而非隐态注入实现风格适配，底座基于T5-large。
### 关键结果
在Reddit、Blog、News三类数据集上全面优于此前包括LLM基在内的SOTA方案，跨域泛化性更强；仅比T5-large增加2.4%参数，推理速度比通用LLM快1.8倍以上
