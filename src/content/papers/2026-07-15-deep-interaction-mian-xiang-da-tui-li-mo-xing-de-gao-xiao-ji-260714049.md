---
title: 'Deep Interaction: An Efficient Human-AI Interaction Method for Large Reasoning
  Models'
title_zh: Deep Interaction：面向大推理模型的高效人机交互方法
authors:
- Hefeng Zhou
- Jinxuan Zhang
- Jiong Lou
- Yuxin Liu
- Chaochao Lu
- Jingjing Qu
- Jie Li
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Shanghai Jiao Tong University
arxiv_id: '2607.14049'
url: https://arxiv.org/abs/2607.14049
pdf_url: https://arxiv.org/pdf/2607.14049
published: '2026-07-15'
collected: '2026-07-16'
category: Reasoning
direction: 大模型推理 · 人机交互纠错
tags:
- Chain-of-Thought
- Human-AI Interaction
- LLM Reasoning
- Error Correction
- Token Efficiency
one_liner: 提出支持直接编辑CoT的人机交互框架，推理纠错成功率升25%、token消耗降40%
practical_value: '- 开发Agent类应用（如电商营销方案生成、选品决策）时，可复用「直接编辑中间推理轨迹+高亮修改段+截断错误后续内容」的范式，替代传统多轮对话纠错，降低token消耗同时提升干预成功率

  - 做推荐理由、广告文案的人工审核修正场景时，可借鉴Myers Diff修改追踪+语义去重+数字掩码的轻量化处理流程，减少人工输入成本

  - 当LLM出现路径依赖、重复输出相同错误时，可引入轻量CoT Reprompter对修改后的内容做语义蒸馏，规避模型记忆历史错误的问题

  - 该方法对7B及以上规模LLM均有效，无需修改基座模型，可快速接入现有推理类应用的人机交互模块'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前基于CoT的大推理模型出错后，传统对话式纠错存在两大痛点：一是用户需要繁琐描述错误位置，模型即使口头承认错误也容易重复同类问题；二是多轮对话会累积大量历史token，成本高且容易出现上下文干扰。此外模型还存在训练数据记忆、路径依赖、KV Cache导致的重复错误输出问题，人工干预效率极低，亟需更高效的人机纠错范式。
### 方法关键点
- 采用类文档修订的直接编辑模式，用户可直接修改CoT中的错误步骤，无需额外对话描述错误信息，仅保留正确的前置推理段
- 基于Myers Diff算法实现细粒度修改追踪，将编辑后的CoT拆分为编辑前、编辑段、编辑后三部分，分别做语义剪枝、**高亮修改内容**、删除错误后续内容、数字掩码处理，降低冗余同时突出修改信号
- 可选CoT Reprompter模块，通过小样本学习或7B级轻量模型微调，对编辑后的CoT做语义蒸馏，消除冗余表述，避免模型重复记忆历史错误路径
### 关键实验
在ScienceQA、STEM20K、Gaokao-MM、LogicQA等推理基准上对比传统对话式纠错：
1. 纠错成功率平均提升25%以上，STEM20K数据集1轮纠错后通过率从65.18%提升至74.89%，专家干预模式下可达82.36%
2. 平均token消耗降低约40%，多轮交互下成本优势进一步扩大
3. 适配7B/32B/72B不同规模的开源/闭源LLM，模型能力越强收益越显著

> 最值得记住的一句话：针对LLM推理错误的人工干预，直接修改中间推理链的效率和成功率远高于传统多轮对话反馈
