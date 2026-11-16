---
title: Folding Language Models into Themselves
title_zh: Concertina：自折叠式大语言模型低数据量蒸馏压缩方法
authors:
- Ziyang Zhang
- Yubin Jing
- Yuyao Li
- Haofan Wang
- Yichen Gong
affiliations:
- Peking University
- Georgia Institute of Technology
- Tsinghua University
- Lovart AI
arxiv_id: '2611.18113'
url: https://arxiv.org/abs/2611.18113
pdf_url: https://arxiv.org/pdf/2611.18113
published: '2026-11-13'
collected: '2026-11-16'
category: LLM
direction: 大语言模型压缩 · 知识蒸馏
tags:
- Knowledge Distillation
- LLM Compression
- LoRA
- Layer Sharing
- SVD Initialization
one_liner: 通过相邻层折叠+逐token门控LoRA校正，仅用22B token蒸馏出保留原模型84%能力的轻量LLM
practical_value: '- 端侧/轻量Agent基座压缩：电商导购、推荐场景的端侧小模型可直接复用该折叠方案从现有大基座压缩，仅需几十B token蒸馏就能拿到接近原生小模型的效果，省掉万亿级预训练成本

  - 蒸馏数据优化：无需盲目堆通用蒸馏数据，针对性补充业务领域结构化数据（如选品推理、优惠计算QA数据），能以更低数据量恢复目标能力，适配推荐系统特定推理需求

  - 小模型结构设计：做生成式推荐自定义小基座时，优先选择相邻层共享而非跨层共享结构，配合逐token门控校正，可在低参数量下更好保留生成、推理能力

  - 压缩方案选型：若业务需要小模型的生成/推理能力（如商品文案生成、智能答疑），优先选择保留全深度的折叠压缩方案，不要直接剪层，避免生成质量大幅下降'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统知识蒸馏需从零初始化学生模型，依赖万亿级训练token成本极高；直接剪层压缩会大幅丢失模型生成与推理能力，现有层共享方案绑定差异较大的跨距层、使用静态校正，效果上限低，亟需低数据成本、高能力保留的LLM压缩方案。
### 方法关键点
- 层折叠架构：将预训练LLM每N个相邻层分为一组，替换为1个共享块循环执行N次，仅存储1份层权重，RMSNorm按原层单独保留不共享
- SVD初始化Step-LoRA：每个循环步骤的低秩校正通过SVD分解原层与共享权重的差值初始化，学生初始状态接近教师，大幅降低蒸馏数据需求
- 逐token门控机制：根据当前token隐状态动态混合不同步骤的LoRA校正，支持每个token自主适配共享块的行为模式
- 蒸馏数据配方：按35%数学内容、55%知识类内容、10%通用文本配比，加入多学科选择题与合成QA数据，同时恢复常识、推理、知识能力
### 关键结果
基于Qwen3-4B教师模型折叠得到的2.27B参数Concertina，仅用22B蒸馏token，8项基准平均保留教师84%能力，其中常识、数学推理分别保留92%、90%，效果优于用36T token预训练的同尺寸级原生模型Qwen3-1.7B；对比同参数剪层稠密模型，GSM8K得分高41倍、MATH得分高11倍；对比RRT、FoldGPT等现有折叠方案，197M token训练效果就超过两者用10倍数据训练的效果。
### 核心结论
对于从大模型蒸馏的小模型，蒸馏数据的覆盖范围比数据量更重要，保留模型全深度比单纯保留更多层权重更利于生成与推理能力留存
