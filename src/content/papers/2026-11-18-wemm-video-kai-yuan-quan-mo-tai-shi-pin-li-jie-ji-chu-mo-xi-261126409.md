---
title: 'WeMM-Video: Pushing the Frontiers of Open-Source Omni-Modal Video Understanding'
title_zh: WeMM-Video：开源全模态视频理解基础模型系列
authors:
- Changli Tang
- Jie Yang
- Tianyi Wang
- Lei Li
- Daoze Zhang
- Zijie Xin
- Zhan Liu
- Li Li
- Jinchang Xu
- Fengyun Rao
affiliations:
- Tencent Inc. WeChat Vision
- Tsinghua University
arxiv_id: '2611.26409'
url: https://arxiv.org/abs/2611.26409
pdf_url: https://arxiv.org/pdf/2611.26409
published: '2026-11-18'
collected: '2026-11-20'
category: Multimodal
direction: 全模态视频理解 · 多模态大模型
tags:
- Multimodal-LLM
- Video-Understanding
- Audio-Visual-Perception
- Foundation-Model
- Open-Source
one_liner: 推出2B-35B参数中英双语全模态视频理解开源模型系列，性能超越主流开源/闭源竞品
practical_value: '- 短视频电商/直播推荐场景可直接复用9B参数版本做商品视频卖点提取、违规内容检测，效果优于更大参数的Qwen3-Omni-30B模型，推理成本更低

  - 多模态推荐系统的内容特征抽取环节可借鉴其视听联合感知训练范式，提升视频类内容的特征表征质量

  - 多模态Agent开发可按需选择不同参数版本，利用其双模式切换能力适配低延迟应答/高复杂度推理两类场景'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前多模态智能领域带音频的视频理解仍是核心瓶颈，短视频电商、直播推荐、多模态Agent等场景对视听联合感知推理能力的需求快速增长。
### 方法关键点
推出2B/4B/9B/35B-A3B四个参数规格的中英双语全模态大模型系列WeMM-Video，采用混合思维范式统一处理文本、图像、音频、视频数据，支持无思维快速响应指令模式与有思维分步推理模式；基于1.2万亿token多模态语料，通过渐进式预训练+多阶段后训练（多教师OPD、抗重复MrDPO、专家RL）完成训练。
### 关键结果
在120+基准测试中性能领先，35B旗舰版成为开源全模态视频理解SOTA，性能优于Qwen3.5-Omni-Flash等闭源模型，缩小与Gemini-3.0-Flash的差距；9B小参数版性能超越更大的Qwen3-Omni-30B-A3B-Instruct
