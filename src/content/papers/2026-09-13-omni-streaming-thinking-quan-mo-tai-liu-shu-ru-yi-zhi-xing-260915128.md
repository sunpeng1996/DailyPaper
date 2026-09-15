---
title: Omni-Streaming Thinking
title_zh: Omni-Streaming Thinking：全模态流输入一致性推理框架
authors:
- Enjun Du
- Siyi Liu
- Ziyu Zheng
- Jingyu Li
- Yiwen Guo
- Yongqi Zhang
- Difan Zou
affiliations:
- The University of Hong Kong
- The Hong Kong University of Science and Technology (Guangzhou)
- LIGHTSPEED
- University of Sussex
- Independent Researcher
arxiv_id: '2609.15128'
url: https://arxiv.org/abs/2609.15128
pdf_url: https://arxiv.org/pdf/2609.15128
published: '2026-09-13'
collected: '2026-09-15'
category: Reasoning
direction: 全模态流推理 · 跨模态一致性校验
tags:
- Streaming Reasoning
- Cross-modal Consistency
- Multimodal LLM
- Hallucination Mitigation
- LoRA
one_liner: 提出带待验证声明、依赖传播修正的全模态流推理框架，解决过早跨模态承诺偏差
practical_value: '- 直播/短视频实时理解场景（如直播带货口播信息提取、实时内容标签生成）可复用「待验证声明+指定模态到期校验」机制，避免提前将画面信息固化为事实导致的错误，比如画面显示原价但口播已改优惠价的冲突场景

  - 多模态内容理解业务可借鉴「分模态独立存储+依赖谱系传播修正」方案，当后续证据推翻早期假设时，自动衰减所有关联推理结果的权重，大幅降低多模态幻觉

  - 基于冻结基座的轻量适配方案可直接复用，仅用LoRA训练声明生成、校验、门控模块，无需全量微调，适合业务快速迭代落地'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
全模态流推理场景下，视觉证据的确认速度通常远快于音频，现有模型会提前将早期视觉判断固化为记忆事实，即便后续音频证据出现矛盾也无法有效修正，导致「过早跨模态承诺」问题，产生持续的视觉偏置幻觉，比如航班信息屏显示Gate6但后续口播已改到Gate12时，模型依然输出错误的Gate6结果。

### 方法关键点
- 核心采用声明-校验-修正三段式推理流程：将未确认的判断定义为待验证声明，记录其验证所需模态、到期时间、依赖谱系，到期后仅使用指定模态的证据完成校验
- 采用分模态独立存储预算：音频、视觉证据分别分配存储额度，避免高密视觉token挤占音频证据空间，待验证声明对应的证据窗口会被锁定直到校验完成
- 依赖谱系传播修正机制：声明被证伪后，自动衰减该声明及所有依赖它的推理结果的注意力权重，再通过判决条件引导解码修正当前状态
- 答案门控机制：仅当所有支撑答案的声明都完成校验后才输出结果，否则继续等待，避免输出未验证的错误信息

### 关键实验
基于冻结的Qwen3-Omni-30B backbone加LoRA轻量适配，在5个流处理、音视频基准测试上比最强开源基线相对提升10%以上；自研OST-DiagBench（固定视频修改音频测试跨模态一致性）上d'达到2.95，远高于基线最高的1.38，视觉诱发的听觉幻觉大幅降低。

### 核心启示
多模态流推理中，不要将未完备验证的早期判断固化为事实，绑定声明的校验条件与依赖关系才能让新证据有效修正之前的错误推理。
