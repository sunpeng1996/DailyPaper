---
title: 'T-DIG: Text-Conditioned Diversity for Image Generation'
title_zh: T-DIG：面向图像生成的文本条件控制多样性框架
authors:
- Simran Khanuja
- Rohit Gandikota
- Gaurav Parmar
- Graham Neubig
affiliations:
- Carnegie Mellon University
- Northeastern University
arxiv_id: '2610.29003'
url: https://arxiv.org/abs/2610.29003
pdf_url: https://arxiv.org/pdf/2610.29003
published: '2026-10-20'
collected: '2026-10-29'
category: Multimodal
direction: 多模态可控生成 · LLM策略驱动
tags:
- Text-to-Image
- LLM Policy
- GRPO
- Controllable Generation
- Reward Modeling
one_liner: 无需修改T2I模型权重，通过LLM策略实现用户指定维度的图像生成多样性增强
practical_value: '- 电商商品图、广告素材生成场景可直接复用该架构，无需微调T2I模型，仅通过上层LLM生成指定维度（如背景、风格、角度）的变体prompt，低成本产出多版本素材，满足主图、种草笔记、信息流投放等不同业务需求

  - 可借鉴GRPO训练LLM策略的双奖励设计思路，用多样性奖励+对齐惩罚优化生成类任务的控制效果，适配广告文案生成、推荐理由生成等需要可控多样性的业务场景

  - 对接闭源生成类API（如Midjourney、商用多模态生成服务）时，可通过外层LLM代理的方式增加自定义控制逻辑，无需获取模型权重即可扩展可控生成能力，大幅降低业务接入成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有Text-to-Image（T2I）模型普遍优化单图生成质量，多图生成多样性不足，且无法按需指定变化维度（如背景、风格、拍摄角度），无法满足用户个性化探索需求。
### 方法关键点
提出T-DIG迭代式文本条件多样性框架，核心为采用GRPO训练的LLM策略，基于用户输入的变化需求生成K个指定维度的变体prompt/编辑指令，无需改动底层冻结的图像生成/编辑模型权重，适配开源、蒸馏、专有各类T2I模型；同时开源首个文本条件prompt多样性数据集，包含人工标注训练验证集与真实用户交互测试集。
### 关键结果
各项指标及人工评估显示，T-DIG在保留基础prompt对齐度的前提下，文本条件控制的多样性表现远超所有基线模型
