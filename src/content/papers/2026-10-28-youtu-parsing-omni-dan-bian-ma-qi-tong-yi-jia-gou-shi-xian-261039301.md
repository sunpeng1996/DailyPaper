---
title: 'Youtu-Parsing-Omni: One Encoder, One Schema, All Modalities'
title_zh: Youtu-Parsing-Omni：单编码器统一架构实现全模态结构化解析
authors:
- Yunhang Shen
- Zhangquan Chen
- Xiaotian Li
- Zhongpeng Cai
- Qing Zhou
- Zekai Zhang
- Kun Zhang
- Zezhong Wu
- Jian Hu
- Haihan Gao
affiliations:
- Tencent Youtu Lab
- Tencent Cloud ADP
arxiv_id: '2610.39301'
url: https://arxiv.org/abs/2610.39301
pdf_url: https://arxiv.org/pdf/2610.39301
published: '2026-10-28'
collected: '2026-10-30'
category: Multimodal
direction: 多模态感知 · 全模态结构化解析
tags:
- Multimodal Parsing
- Omni-modal Encoder
- Unified Schema
- Agent Perception
- Open Source
one_liner: 单编码器+统一Schema架构的全模态结构化解析开源模型，性能领先多数开源方案
practical_value: '- 可复用全模态编码器架构：用LLM初始化的单共享编码器替代多模态双塔，仅保留轻量模态专属stem与投影层，大幅降低多模态感知模块参数量与部署成本，适配电商场景下商品图/短视频/直播音频的统一结构化解析需求

  - 统一Schema+OSAD训练范式可迁移至多任务结构化生成场景：将不同模态/任务输出格式归一化后，用带参考条件的自蒸馏做token级角色适配（结构token用KL散度、内容token用JS散度），无需额外训练教师模型，可直接用于商品多模态信息抽取、直播内容结构化等任务

  - 电商多模态内容召回/推荐场景可直接集成该开源模型作为预解析层：将商品图、短视频、直播音频预先解析为带时空锚点的结构化文本，降低下游推荐/检索模型的输入长度与计算开销，同时支持证据溯源，适配监管要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent处理文档、图像、音视频等非文本输入时，直接逐次重编码成本极高，且输出结果无法溯源至原始输入的对应时空区域；现有多模态解析工具仅覆盖部分模态，不同任务输出格式不统一，需要单独维护多套模型，部署成本高。

### 方法关键点
- 架构层：用预训练LLM初始化单共享Transformer作为Youtu-Omni-Encoder核心，仅保留轻量模态专属输入stem与输出投影层，所有模态共享统一时空位置编码，新增少量融合层实现音视频时序对齐与跨模态交互
- 输出层：定义OmniSchema统一10类跨模态解析任务的输出格式，所有解析元素自带空间（图像）/时间（音视频）锚点，天然支持结果溯源
- 训练层：后训练阶段提出OSAD自蒸馏范式，基于输出token的角色（结构/内容）匹配不同损失函数，无需额外训练教师模型，每轮迭代后学生模型升级为新教师，实现监督信号与模型共同进化

### 关键结果
单5B参数checkpoint覆盖所有模态与任务：OmniDocBench v1.6得分96.96，达到SOTA；OmniParsingBench平均得分75.08，为当前最强开源模型，较第二名Logics-Parsing-Omni高出2.82个点，其中音频、自然视频、文本富视频任务分别领先2.5、6.8、10.3个点；乐谱识别CER 22.73，与专用模型LEGATO（23.30）性能相当。

### 核心结论
单共享编码器+统一Schema的架构可在不牺牲单任务精度的前提下实现全模态解析能力覆盖，大幅降低多模态感知系统的部署与维护成本
