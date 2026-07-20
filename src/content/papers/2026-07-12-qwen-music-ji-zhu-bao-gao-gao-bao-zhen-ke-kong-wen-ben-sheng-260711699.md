---
title: Qwen-Music Technical Report
title_zh: Qwen-Music 技术报告：高保真可控文本生成与翻唱音乐系统
authors:
- Jin Xu
- Kangdi Wang
- Ruibin Yuan
- Shun Lei
- Xiong Wang
- Xize Cheng
- Xueyao Zhang
- Yang Zhang
- Yiheng Chen
- Yongqi Wang
affiliations:
- Qwen Team
arxiv_id: '2607.11699'
url: https://arxiv.org/abs/2607.11699
pdf_url: https://arxiv.org/pdf/2607.11699
published: '2026-07-12'
collected: '2026-07-20'
category: Other
direction: 生成式音乐 · 可控多模态生成
tags:
- Music Generation
- Chain-of-Thought
- Tokenizer
- Diffusion Model
- Preference Alignment
one_liner: 采用分层架构的可控音乐生成系统，文本生成与翻唱效果匹敌商用SOTA
practical_value: '- 做电商短视频/直播/广告的配乐生成业务，可复用Melody-CoT显式规划思路，生成前先锁定适配商品风格的旋律走向，大幅降低不符合调性的Badcase

  - 多模态离散tokenizer开发可复用四阶段训练策略：自监督预训练→因果适配→多任务SFT→VQ插入，平衡语义保留度和生成效率，适配长序列生成场景

  - 生成类任务的偏好对齐可复用三阶段流程：SFT冷启动→离线DPO迭代→在线GSPO优化，在稳定生成质量的前提下提升用户偏好匹配度

  - 音视频素材库质检可复用论文中的音频质量检测流水线，自动过滤低质量转码、假立体声、削波的劣质素材，提升素材库整体质量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有音乐生成模型难以同时满足长序列结构连贯、语义匹配用户意图、高保真音质三大要求，翻唱任务也难以平衡参考旋律保留和风格可控性，性能领先的商用系统大多闭源，缺乏可复现的开源高性能方案。
### 方法关键点
- 三阶段分层架构：Tokenizer将音频压缩为25Hz单码本Music Semantic Tokens，保留核心语义与旋律信息；LLM基于Qwen3.5-Omni 3B模型，新增Melody-CoT机制，生成全曲前先规划旋律，同时支持文本生成和参考音频条件的翻唱任务；Render采用DiT+Spec-VAE+Band-Mode Refiner的生成式渲染流程，输出48kHz高保真立体声。
- 训练策略：Tokenizer采用四阶段训练流程，逐步引入因果约束、多任务监督和VQ量化，保证token语义有效性；LLM采用质量分级预训练课程，从低质量到高质量数据渐进训练，再经过SFT→离线DPO→在线GSPO三阶段偏好对齐，提升音乐性和指令遵循能力。
- 翻唱任务提供两种Melody-CoT模式：段落级模式保留全部旋律实现精准克隆，唯一段落级模式仅保留重复段落的代表性旋律，提升风格适配自由度。
### 关键结果
训练数据覆盖超500万小时多语言音乐，在600条中英prompt测试集上，16项客观音乐性与音质指标中13项达到SOTA；专业盲测中对Suno V5胜率55.4%，对MiniMax 2.6胜率66.7%，仅以50.3%的微弱优势领先Suno V5.5，整体效果匹敌商用SOTA；翻唱任务段落级模式Melody MAE低至1.48，显著优于Suno V5.5的2.00，在真实流行歌翻唱集上全面优于MiniMax Cover。

**最值得记住的一句话**：复杂多模态生成任务可通过「语义层显式规划+独立渲染层还原细节」的分层架构，同时兼顾生成可控性、长序列一致性和高保真输出
