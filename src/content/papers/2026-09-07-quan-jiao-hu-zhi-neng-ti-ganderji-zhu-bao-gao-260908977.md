---
title: Omni Interaction Agent Technical Report
title_zh: 全交互智能体Gander技术报告
authors:
- Orantqing
- Shengpeng Ji
- Junlong Tong
- Jialong Zuo
- Dongjie Fu
- Di Cao
- Yangzhuo Li
- Shangda Wu
- Franz
- Evan
affiliations:
- Hunyuan Speech Team, Tencent
- Zhejiang University
- Shanghai Jiao Tong University
- The Chinese University of Hong Kong
- Nanyang Technological University
arxiv_id: '2609.08977'
url: https://arxiv.org/abs/2609.08977
pdf_url: https://arxiv.org/pdf/2609.08977
published: '2026-09-07'
collected: '2026-09-09'
category: Agent
direction: Agent 多模态全双工实时交互
tags:
- MultiModal Agent
- Full Duplex Interaction
- Realtime Agent
- Brain-Cerebellum Architecture
- Streaming Processing
one_liner: 提出小脑-大脑分层架构的多模态全双工交互Agent，兼顾低延迟实时对话与长周期复杂任务执行
practical_value: '- 架构上可复用小脑-大脑分层设计，前端轻量模型负责电商实时客服/导购的低延迟语音/多模态交互，后端大模型处理复杂订单查询、售后纠纷推理等长周期任务，兼顾响应速度与推理能力

  - 流式分块平铺（chunk flattening）的交互机制可直接迁移到直播场景AI助手，按1s滑动窗口处理实时音视频流，动态判断是否响应用户弹幕/语音提问，无需依赖VAD模块降低交互延迟

  - 可复用其全双工交互数据构造流水线，合成包含用户打断、背景噪音、多用户插话的场景训练数据，提升电商语音客服、直播导购Agent在真实复杂场景的鲁棒性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent多采用轮次式交互范式，与人类自然流畅的多模态交流存在明显差距，既无法支持用户随时打断、主动反馈等全双工交互能力，也难以同时满足实时对话低延迟要求与复杂任务长周期推理需求，限制了Agent在客服、办公协作、导购等真实场景的落地效果。

### 方法关键点
- 采用小脑-大脑解耦架构：前端小脑为基于Thinker-Talker的实时多模态模型，负责流式音视频输入处理、低延迟交互控制；后端大脑为训练即可插拔的通用推理Agent，负责长周期任务执行、工具调用与复杂推理；中间Agent编排运行时负责两层的任务调度、状态管理与上下文同步
- 前端小脑引入流式分块平铺机制：将所有模态输入、模型输出按1s时间窗口切分为对齐的分块，每个分块预测控制token（监听/发言/打断），通过128块滑动窗口维护2分钟上下文，无需外部VAD模块即可实现全双工交互
- 训练数据总规模2.7M，覆盖语音交互、音视频交互、Agent交互、鲁棒性负样本四类，专门合成包含打断、多轮插话、背景噪音的场景数据，提升真实环境适配性

### 关键结果
内部人工评估显示，Gander自然对话能力对齐SOTA开源模型，背景噪音、多用户交互、插话反馈等复杂场景鲁棒性表现优异，端到端交互延迟控制在百毫秒级，音视频编码分别实现5x、16x压缩保证实时处理效率，可对接Codex等后端大模型实现代码编写、文档处理等复杂任务。

### 核心结论
实时交互能力不应作为Agent的外部编排层能力，而应作为模型的原生内置能力，通过分层架构可以同时兼顾交互的低延迟与任务推理的深度。
