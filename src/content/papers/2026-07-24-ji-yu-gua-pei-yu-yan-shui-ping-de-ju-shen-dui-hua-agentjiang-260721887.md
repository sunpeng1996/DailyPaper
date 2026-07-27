---
title: Towards Reducing Foreign Language Anxiety Using Level-Appropriate Embodied
  Conversational Agents
title_zh: 基于适配语言水平的具身对话Agent降低外语学习焦虑研究
authors:
- Krishan Rajaratnam
- Wenbin Gan
- Yuan Sun
affiliations:
- University of Oxford
- National Institute of Information and Communications Technology (Japan)
- National Institute of Informatics (Japan)
arxiv_id: '2607.21887'
url: https://arxiv.org/abs/2607.21887
pdf_url: https://arxiv.org/pdf/2607.21887
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: Agent 对话内容分级适配优化
tags:
- Conversational Agent
- LLM
- CEFR Classification
- Multi-Agent System
- Content Control
one_liner: 提出多Agent生成-评估-重生成闭环，输出匹配CEFR水平的对话，探索缓解外语学习焦虑方案
practical_value: '- 可复用「生成-评估-重生成」多Agent闭环框架，用于生成匹配用户认知水平的商品文案、客服话术，降低用户理解门槛

  - 分级打分机制可迁移：生成内容按等级分类后按规则算分，不达阈值触发重生成，可用于内容合规、用户分层内容生成场景

  - 仅保留最终有效对话、丢弃中间修订过程的上下文管理策略，可降低LLM对话系统的token消耗与上下文窗口占用'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
外语焦虑（FLA）是二语习得的核心障碍，会导致学习者回避口语练习，严重阻碍学习效果。现有LLM驱动的语言学习对话Agent，普遍存在输出内容难度与学习者水平不匹配的问题，反而可能提升用户焦虑；而CEFR等级文本分类技术已被验证准确率超过人类专家，但缺乏将其用于对话生成难度管控的落地框架，也没有明确数据验证难度适配对焦虑的缓解效果。

### 方法关键点
- 用标注好的CEFR对话数据集微调BERT作为等级分类器，可单句判断对话内容的CEFR难度等级
- 设计多Agent闭环：120B参数主对话Agent生成回复→拆分单句用BERT分类，计算达标率（目标等级及以下占比+超1级内容半权重赋分），阈值设为0.66→不达标时由20B参数反馈Agent生成简化提示，引导主Agent重生成，直到达标或达到最大迭代次数，仅保留最终有效回复到上下文
- 采用被试内交叉实验设计，对比分级适配Agent和无分级Agent的用户FLA得分差异

### 关键实验结果
小样本预实验招募3名自评CEFR水平A1-A2的日本大一英语学习者，对比无分级的同架构具身对话Agent；核心结果：分级条件下87.4%的句子落在用户自评水平上下1个CEFR等级内，无分级条件仅为54.1%；2/3被试在分级条件下的FLA得分更低，整体呈现等级适配率越高、焦虑越低的负相关趋势，但受样本量限制未达统计显著性。

### 核心启示
内容可控性优化不能只关注文本本身的属性，场景的文化适配、交互节奏的适配同样会显著影响用户体验与感知
