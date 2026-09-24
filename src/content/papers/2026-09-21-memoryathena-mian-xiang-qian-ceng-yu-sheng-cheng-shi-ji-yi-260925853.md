---
title: 'MemoryAthena: Adaptive Routing over Latent and Generated Memories'
title_zh: MemoryAthena：面向潜层与生成式记忆的自适应路由框架
authors:
- Mingyuan Li
- Guangsheng Yu
- Juyuan Zhang
- Xu Wang
- Zhibo Man
- Haonan Zhang
- Shaoxiong Ji
affiliations:
- ELLIS Institute of Finland
- University of Turku
- University of Technology Sydney
- University of Science and Technology of China
- Shanghai Jiao Tong University
arxiv_id: '2609.25853'
url: https://arxiv.org/abs/2609.25853
pdf_url: https://arxiv.org/pdf/2609.25853
published: '2026-09-21'
collected: '2026-09-24'
category: LLM
direction: LLM记忆增强 · 自适应无监督路由
tags:
- Memory-Augmented-LLM
- Adaptive-Routing
- Memory-Generation
- Counterfactual-Distillation
- Unsupervised-Learning
one_liner: 提出锚定直接记忆检索的三通路自适应路由框架，无需下游标签训练即可提升多类NLP任务效果
practical_value: '- 推荐系统记忆模块可复用三通路设计：既有直接检索用户/物品记忆（对应E通路），也可基于检索 cue 生成适配上下文的记忆表征（对应GE），还可直接基于当前会话上下文生成记忆（对应GH），覆盖不同场景的记忆需求

  - 多通路召回/排序融合可复用锚定路由策略：以现有成熟基线（如现有排序模型输出）为锚点，仅当其他通路预测增益超过阈值时做加权修正，保证效果下限，避免新通路引入bad
  case

  - 轻量路由头的无监督训练方法可直接迁移：无需下游业务标注，通过未来token似然差构造监督信号训练路由头，大幅降低落地标注成本，适合冷启动场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有记忆增强LLM仅依赖存储的记忆表征做检索读取，忽略了记忆也可基于上下文或检索 cue 生成；而生成记忆并非在所有场景都优于直接检索，无条件替换会引入效果波动，亟需自适应机制判断何时使用哪种记忆通路。

### 方法关键点
- 三通路记忆架构：1）E通路：直接读取Engram存储的记忆表征；2）GE通路：基于检索到的Engram cue生成适配当前上下文的潜层记忆；3）GH通路：不访问外部记忆表，直接基于LLM当前因果隐状态生成记忆
- E锚定非对称路由：以E通路为稳定基线，仅当GE/GH的预测相对优势与置信度超过阈值时，通过[0,1]区间的加权插值修正E的输出，无符合条件的候选则直接fallback到E通路，保证效果下限
- 无监督路由训练：冻结主干、记忆模块、生成器与读取器，仅训练53万参数量的轻量路由头，通过不同通路未来token似然的反事实差值构造监督信号，推理时仅依赖当前状态特征，符合因果要求

### 关键实验
在5个QA任务、6个通用NLP任务上验证，主干采用Mistral-7B-v0.3，对比同checkpoint仅用E通路的基线：QA平均得分从37.65提升至39.28，6个NLP任务平均准确率从76.73提升至79.13，额外计算开销极低。

### 最值得记住的一句话
生成式记忆是直接检索记忆的选择性补充而非通用替代，路由的核心挑战是判断何时干预、选择哪条通路、以及控制干预强度。
