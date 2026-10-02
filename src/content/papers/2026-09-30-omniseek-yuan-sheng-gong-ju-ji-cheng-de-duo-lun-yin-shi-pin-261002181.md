---
title: 'OmniSeek: Native Tool Integration for Multi-turn Audio-Visual Reasoning'
title_zh: OmniSeek：原生工具集成的多轮音视频推理Agent框架
authors:
- Haibo Wang
- Jiteng Mu
- Jialu Li
- Jingru Yi
- Yuanjun Xiong
- Jianming Zhang
- Lifu Huang
- Mingze Xu
affiliations:
- University of California, Davis
- Adobe Research
arxiv_id: '2610.02181'
url: https://arxiv.org/abs/2610.02181
pdf_url: https://arxiv.org/pdf/2610.02181
published: '2026-09-30'
collected: '2026-10-02'
category: Agent
direction: 音视频多模态Agent · 多轮工具调用
tags:
- Multi-modal Agent
- Tool Integration
- Reinforcement Learning
- Audio-Visual Reasoning
- Synthetic Corpus
one_liner: 将全模态LLM改造为主动检索跨模态证据的多轮音视频推理Agent
practical_value: '- 多模态检索Agent的<think>→<tool_call>→<observe>三段式交互框架可直接复用在电商短视频/直播内容理解、商品信息检索任务，按需拉取指定时间窗的音频/视频片段，避免长上下文信息稀释

  - 构造合成推理轨迹数据集的三阶段pipeline可迁移到业务小样本标注：先对齐多模态时间戳、再生成带证据链的QA、最后组装工具调用轨迹，大幅降低人工标注成本

  - Audio-Visual Necessity奖励设计思路可复用在跨模态校验场景，通过注意力掩码判断模型是否真的用到不同模态有效信息，避免单模态捷径导致的badcase

  - 三阶段训练策略（SFT冷启动→RL探索→难例优化）可直接套用到业务Agent迭代流程，解决纯SFT的对齐税问题，兼顾泛化性和任务效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前全模态LLM处理长音视频时采用单轮全量编码，细粒度细节易被无关内容稀释，且推理依赖纯文本CoT，只能基于固定全局上下文或转译后的文本证据，无法调用原始多模态信号，容易触发单模态捷径或语言先验，长序列多跳推理效果差。

### 方法关键点
1. 多轮工具协议：采用<think>→<tool_call>→<observe>迭代框架，提供`get_audio_clip`、`get_video_clip`两个原生工具，可动态拉取指定时间窗、分辨率/帧率的原始音视频片段追加到上下文，自主判断证据足够后输出结果
2. 合成数据集OmniTraj-170K：三阶段数据引擎生成，先对齐音视频时间戳生成分场景带时间戳的字幕/ASR，再生成必须同时用到音视频证据的QA和有序证据链，最后组装为带工具调用的完整推理轨迹，共17万条轨迹覆盖3.98万个视频
3. 三阶段训练策略：第一阶段用10%轨迹数据+90%普通QA做SFT冷启动对齐工具调用格式；第二阶段用GSPO强化学习，基于准确率、格式、工具使用三个规则奖励探索；第三阶段用难例+Audio-Visual Necessity奖励，通过模态注意力掩码计算模型对双模态的依赖度，强制模型同时使用音视频证据避免单模态捷径

### 关键结果
在10个音视频推理benchmark上，30B参数的OmniSeek相比基线Qwen3-Omni-Instruct，在长视频任务MMOU、LVOmni上分别提升16.3%、8.4%，在VideoHolmes、OmniVideoTest上分别提升15.5%、15%，效果超过多数开源和部分闭源模型；纯文本CoT相比基线仅提升1.1%，而多轮工具调用方案相比纯文本CoT在OmniVideoTest上提升13.5%。

> 值得记住的一句话：对于复杂多模态长序列推理，主动按需检索原始多模态证据的收益远高于单纯增加纯文本思考链的长度。
