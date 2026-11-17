---
title: 'Grounding Language Models in Speech Does Not Fix "AI Flavor": Calibrated LLM
  Judges, Goodhart Traps, and a Preference-Tuning Fix'
title_zh: 语音接地无法消除大模型中文AI味：校准裁判、优化陷阱与偏好调优方案
authors:
- Dongwu Qian
affiliations:
- Independent Researcher
arxiv_id: '2611.19840'
url: https://arxiv.org/abs/2611.19840
pdf_url: https://arxiv.org/pdf/2611.19840
published: '2026-11-15'
collected: '2026-11-17'
category: LLM
direction: LLM生成风格优化 · LLM-as-Judge
tags:
- LLM-as-Judge
- DPO
- Preference-Tuning
- Goodhart-Trap
- AI-Flavor
one_liner: 验证语音接地消除中文AI味无效，提出校准LLM裁判框架与带锚定的DPO调优方案
practical_value: '- 电商营销文案、商品详情、客服回复等生成场景去AI味时，无需投入成本做语音模态注入，直接用纯文本偏好调优即可达到目标

  - 落地LLM-as-Judge做生成质量/风格评估时，必须先做校准catch trial，再采用双独立裁判+A/B swap+分歧算平局的协议，大幅降低评估偏差

  - 用DPO做风格/偏好调优时，可加入RPO风格的SFT锚定项，通过调整权重w平衡偏好对齐效果与模型原始能力保留，还可解决裁判偏好带来的长度坍缩等Goodhart陷阱

  - 小参数模型做垂直场景风格调优时，百级高质量偏好对即可接近效果饱和，无需堆砌海量标注数据'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
中文大模型生成内容普遍存在可感知的「AI味」：公式化句式、书面连接词堆砌、重复、排版泄露等问题，行业主流假设认为该问题源于纯文本训练缺少人类写作的内语音层，注入语音/韵律信号即可改善，但该假设从未经过严格对照验证；同时AI味评估存在自动指标与人类感知脱节、人工盲评统计效力不足的痛点。

### 方法关键点
- 提出RA-Eval三层评估框架：包含经人类验证的AI味客观特征库、人工盲评协议、校准LLM裁判流程（裁判需先通过已知答案catch trial，再采用双独立裁判+A/B swap标注，分歧判定为平局）
- 直接将校准裁判的一致标注作为DPO正负样本，无需训练额外奖励模型
- 针对DPO训练中裁判偏好传导导致的Goodhart陷阱（如长度坍缩），加入RPO风格的SFT锚定损失项，通过权重w平衡偏好对齐与原始能力保留

### 关键实验
- 在0.6B Qwen3模型上的三组语音接地对照实验全部失败：音素interleaved续训无口语增益且重复率提升0.13，韵律条件生成的规则adherence仅0.257，规则韵律奖励在双盲评估中胜率仅50%，与人类感知完全脱节
- 仅用89对校准裁判标注的偏好对做DPO训练，held-out盲胜率达0.833，重复率从0.114降至0，MMLU基本无下降
- 加入w=0.1的SFT锚定项后，既修复了输出长度坍缩问题，又保留了风格增益，盲胜率达0.771，240对偏好对即接近效果饱和

### 核心结论
AI味源于训练语料的分布特性而非模态缺失，校准LLM裁判是低成本优化生成风格的可行路径，但必须防范其偏好通过优化pipeline放大的Goodhart陷阱。
