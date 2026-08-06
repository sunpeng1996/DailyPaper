---
title: 'CoCo-IR: Contextual Composed Image Retrieval'
title_zh: CoCo-IR：上下文感知组合式图像检索
authors:
- Shengcao Cao
- Tanmaya Shekhar Dabral
- Zhongli Ding
- Madhuri Shanbhogue
- Kaifeng Chen
- Zhe Li
- Mojtaba Seyedhosseini
- Yu-Xiong Wang
- Liang-Yan Gui
affiliations:
- University of Illinois Urbana-Champaign
- Google DeepMind
- OpenAI
arxiv_id: '2608.05149'
url: https://arxiv.org/abs/2608.05149
pdf_url: https://arxiv.org/pdf/2608.05149
published: '2026-08-05'
collected: '2026-08-06'
category: Multimodal
direction: 多模态检索 · 多轮交互搜索
tags:
- Composed Image Retrieval
- Multimodal LLM
- Multi-turn Interaction
- Image Embedding
- Data Engine
one_liner: 提出多轮上下文组合图像检索任务及TIE模型，搭配自动数据引擎大幅超越现有基线
practical_value: '- 电商多模态搜商品场景可复用TIE动态图像嵌入方案，支持用户多轮交互 refine 搜索需求，降低导购路径转化损耗

  - 可直接复用其无标注数据生成方案，用LMM自动生成多轮交互检索训练数据+hard negative挖掘，大幅压缩标注成本

  - 对话式购物Agent的图像理解模块可借鉴原生上下文感知思路，避免多轮上下文压缩导致的指代信息丢失'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有指令驱动的图像检索仅支持单轮交互，无法适配真实场景中用户逐步迭代细化搜索需求的使用习惯，外部上下文摘要拼接的方案易丢失关键指代信息，检索准确率低。
### 方法关键点
1. 定义全新CoCo-IR多轮上下文组合图像检索任务，支持用户通过多轮交互迭代优化检索结果
2. 基于LMM搭建上下文感知推理模型，生成随交互轮次动态演化的Transformable Image Embeddings（TIE），原生支持跨轮上下文与指代理解
3. 搭建全自动可扩展数据引擎，基于LMM生成高质量上下文检索训练数据，搭配模型引导的验证机制挖掘难负样本，无需人工标注即可完成模型训练
### 关键结果
单轮基准CIRCO上mAP@5达39.4，刷新SOTA；4轮交互的CoCo-IR基准上R@1达44.1，远超现有基线方法的28.2
