---
title: Feeling of Knowing in Large Language Models
title_zh: 大语言模型功能型知晓感（FoK）：知识更新后自判断能力对齐方法
authors:
- Zichuan Fu
- Xian Wu
- Jingtong Gao
- Wenlin Zhang
- Jiaxuan Li
- Binhao Wang
- Yimin Deng
- Guojing Li
- Xiaopeng Li
- Derong Xu
affiliations:
- City University of Hong Kong
- Tencent Jarvis Lab
- Xi'an Jiaotong University
- Renmin University of China
- Westlake University
arxiv_id: '2611.04834'
url: https://arxiv.org/abs/2611.04834
pdf_url: https://arxiv.org/pdf/2611.04834
published: '2026-11-03'
collected: '2026-11-04'
category: LLM
direction: 大语言模型 · 元认知自判断对齐
tags:
- FoK
- LLM Alignment
- Knowledge Editing
- Metacognition
- LoRA
one_liner: 提出双通道三阶段训练框架，解决LLM知识更新后回答能力自判断与实际能力不同步问题
practical_value: '- 电商/广告垂类LLM做领域知识SFT/编辑后，可复用K∆-FT方法单独训练FoK LoRA通道，避免知识更新后模型幻觉/漏答，降低错误输出率

  - 搭建Agent的检索触发/模型路由逻辑时，可借鉴先生成短推理链再做FoK判断的设计，比直接基于query判断的AUROC提升15%+，减少不必要的RAG开销

  - 垂类LLM微调时可复用OP-SFT技巧：仅对错误答案片段做梯度回传，保留模型原生生成上下文，降低知识更新对原有能力的扰动'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM的回答能力自判断（FoK）方法均基于静态参数校准，当模型通过SFT/LoRA/知识编辑更新知识后，实际回答能力发生变化，但自判断边界无法同步调整，要么出现幻觉（不会的问题强行回答）要么漏答（已掌握的问题拒答），现有方案无法适配动态知识迭代场景。
### 方法关键点
- 双通道设计：知识通道负责更新回答能力，FoK通道负责判断当前知识状态下的回答可行性，两个通道均以LoRA实现，互不干扰
- 三阶段训练流程：
  1. OP-SFT：仅对采样回答中的错误答案片段做监督训练，保留模型原生生成的上下文，减少对原有FoK能力的扰动，同时保存训练全流程的知识checkpoint
  2. K∆-FT：基于OP-SFT的checkpoint轨迹训练FoK通道，让判断能力跟随知识状态动态迭代，而非绑定静态知识边界
  3. FGPO：用强化学习让模型先生成推理链、再做FoK判断、最后输出回答或拒答解释，端到端优化判断+响应的整体效果
### 关键结果
在Qwen2.5-7B上做TriviaQA知识更新实验，对比10种现有FoK baseline：1）知识更新后FoK AUROC从vanilla K-SFT的0.519提升到0.809，接近静态模型最优水平0.810；2）跨3次连续知识更新，FoK AUROC稳定在0.797以上，比不更新FoK通道的方案高4.3个百分点；3）MMLU/ARC-Easy通用能力保留率达99%以上。
**最值得记住的一句话**：LLM的知识更新不会自动同步自我判断能力，每做一次知识迭代都要单独对齐FoK通道，才能保证输出可靠性。
