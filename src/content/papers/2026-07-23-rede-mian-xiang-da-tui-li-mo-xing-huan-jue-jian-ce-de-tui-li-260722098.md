---
title: 'Reasoning Denoiser: Denoising Reasoning Traces for Hallucination Detection
  in Large Reasoning Models'
title_zh: REDE：面向大推理模型幻觉检测的推理轨迹去噪框架
authors:
- Junlin Fang
- Do Nguyen-Thanh
- Xiaogang Xu
- Zhen Fang
- Sean Du
affiliations:
- Nanyang Technological University
- Zhejiang University
- University of Technology Sydney
arxiv_id: '2607.22098'
url: https://arxiv.org/abs/2607.22098
pdf_url: https://arxiv.org/pdf/2607.22098
published: '2026-07-23'
collected: '2026-07-28'
category: Reasoning
direction: 大推理模型 · 幻觉检测 · 推理轨迹去噪
tags:
- Hallucination Detection
- Reasoning Model
- Chain-of-Thought
- Denoising
- Attention
one_liner: 利用无标注最终答案注意力信号训练轻量投影层，过滤推理轨迹噪声，提升各类幻觉检测器性能
practical_value: '- 电商导购、商品推理类Agent的幻觉检测可复用REDE思路：以最终答案对思考步骤的注意力为无标注监督，过滤CoT冗余/无关步骤，无需额外标注即可提升检测准确率

  - 针对LLM生成推荐理由、商品文案的幻觉校验场景，可将REDE作为前置轻量插件，仅需训练MLP投影层（冻结主干LLM），即可适配现有各类幻觉检测器，获得稳定增益

  - 长推理链的LLM推理提速场景可借鉴REDE的噪声步骤识别方法，剪枝冗余思考步骤，降低KV cache占用，同时不影响下游推理结果的可靠性校验

  - REDE的跨场景迁移能力强，训练好的投影层可跨推理任务复用，适合搭建电商多场景（问答、选品、文案生成）统一幻觉校验pipeline'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大推理模型（如o1、DeepSeek R1）生成的长推理轨迹中存在大量无关、重复的噪声步骤，会掩盖幻觉检测的有效信号，现有基于置信度、原始嵌入的过滤方法无法有效区分噪声和有效步骤，导致检测性能大幅下降。

### 方法关键点
- 无需人工标注，利用最终答案token对每个推理步骤的注意力得分作为监督信号，得分低的步骤对应无关/重复噪声
- 采用困惑度加权聚合token embedding得到步骤级表示，训练轻量投影层，通过三类损失优化表示空间：拉近有效步骤间距、推开噪声步骤间距、增大两类步骤的间隔
- 推理时仅需对步骤embedding做投影，用kNN距离识别过滤噪声步骤，过滤后的轨迹可直接接入任意下游幻觉检测器

### 关键结果
在TruthfulQA、MATH、CodeElo、MultiHopQA四个基准，Qwen3-8B、DeepSeek-R1等模型上测试：
- 相比原始轨迹，REDE接入CCS检测器在TruthfulQA上AUROC从68.63%提升至87.32%，涨幅达18.69%
- 接入有监督探测检测器在MATH上AUROC从81.05%提升至87.06%，全面领先10+现有SOTA基线
- 跨数据集迁移性能优异：MultiHopQA上训练的投影层在CodeElo上测试达到88.04% AUROC，略优于域内训练结果

### 核心结论
推理轨迹中的噪声步骤是幻觉检测性能的重要瓶颈，利用模型自身的最终答案注意力信号做无监督表示空间塑造，可低成本实现通用推理轨迹去噪
