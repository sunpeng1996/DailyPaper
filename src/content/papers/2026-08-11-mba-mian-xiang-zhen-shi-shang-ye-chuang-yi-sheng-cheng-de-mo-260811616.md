---
title: 'MBA: Multimodal Benchmark and Agents for Real-World Business Ideation'
title_zh: MBA：面向真实商业创意生成的多模态基准与智能体框架
authors:
- Hojun Choi
- Jaeyo Shin
- Suin Lee
- Hyunjung Shim
affiliations:
- KAIST AI, Republic of Korea
arxiv_id: '2608.11616'
url: https://arxiv.org/abs/2608.11616
pdf_url: https://arxiv.org/pdf/2608.11616
published: '2026-08-11'
collected: '2026-08-13'
category: Agent
direction: 多模态Agent · 商业创意生成
tags:
- Multimodal Agent
- Benchmark
- LoRA
- GRPO
- MLLM-as-a-Judge
- Business Ideation
one_liner: 提出首个多模态商业创意生成基准及适配两种评估场景的专用智能体
practical_value: '- 多模态开放生成类任务可复用「LoRA SFT + GRPO 定制奖励」两阶段训练范式，有效规避通用MLLM输出同质化问题

  - 生成内容的可行性校验可参考方案：构建领域知识库+FAISS检索匹配市场相关性+FActScore校验事实性，大幅降低幻觉

  - 针对评估指标已知/未知两类部署场景设置差异化奖励权重的思路，可迁移到电商素材生成、个性化文案生成等业务

  - MLLM-as-a-Judge适配多模态生成任务的评估框架，可直接复用在商品图生成、短视频创意生成的自动评测环节'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有商业创意生成方法完全依赖文本输入，无法捕捉真实场景中难以被文字完整描述的视觉细节，通用多模态大模型零样本生成的创意同质化严重、缺乏落地可行性，同时没有专用的多模态基准支撑相关任务的训练与评估。
### 方法关键点
- 构建MBA-Bench多模态基准：覆盖6个视觉信息难以被文字完全表达的领域，筛选2K图像对，通过「视觉查询提取→DuckDuckGo检索市场证据→证据增强生成」三阶段流程生产30K标注样本，配套6个商业维度的MLLM-as-a-Judge自动评估框架
- 设计两款适配不同部署场景的智能体：MBA-b适配评估指标未知的盲测场景，仅优化创意性、可行性两个通用奖励；MBA-k适配评估指标已知场景，额外优化6个公开评估维度，合计8个奖励
- 训练采用两阶段范式：先基于Qwen2.5-VL-7B做LoRA监督微调，再用分组相对策略优化（GRPO）做强化学习微调，其中可行性奖励基于自建的网络知识库（MBA-Library）做事实校验，避免法官模型幻觉
### 关键结果
在MBA-Bench测试集上，MBA-b相比纯文本caption基线性能提升63.9%，相比通用多模态基线提升25.6%；MBA-k相比caption基线提升77.1%，相比多模态基线提升35.8%，7B参数规模即可达到与闭源MLLM相当的创意生成效果。

**最值得记住的一句话**：仅靠文本无法完整覆盖真实场景的有效信息，多模态输入+定制奖励的GRPO微调，是开放生成类任务平衡创意性与落地可行性的高性价比路径。
