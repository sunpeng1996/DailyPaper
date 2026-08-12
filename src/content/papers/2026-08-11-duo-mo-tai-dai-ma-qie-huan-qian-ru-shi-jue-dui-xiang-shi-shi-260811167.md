---
title: 'MultiModal Code-Switching: Interleaving Visual Objects into Language for Explicit
  Object-Level Alignment'
title_zh: 多模态代码切换：嵌入视觉对象实现显式对象级模态对齐
authors:
- Changhao Xiang
- Shangyu Xing
- Zhen Wu
- Jianbing Zhang
- Xinyu Dai
affiliations:
- National Key Laboratory for Novel Software Technology, Nanjing University
arxiv_id: '2608.11167'
url: https://arxiv.org/abs/2608.11167
pdf_url: https://arxiv.org/pdf/2608.11167
published: '2026-08-11'
collected: '2026-08-12'
category: Multimodal
direction: 多模态大模型 · 跨模态对齐预训练
tags:
- MLLM
- Multimodal Alignment
- Pre-training
- Visual Grounding
- Code-Switching
one_liner: 提出多模态代码切换预训练范式，通过实体-视觉对象替换实现显式对象级对齐，大幅提升训练数据效率
practical_value: '- 电商多模态内容理解场景可复用MMCS思路，将商品图局部对象（如款式、配件）与文本描述实体显式绑定，提升图文匹配准确率，减少歧义

  - 可复用文中可扩展数据合成pipeline，低成本生成带精准实体-视觉对应关系的训练数据，降低多模态模型预训练的数据采集成本

  - 多模态推荐/导购Agent的基座MLLM微调时，可引入MMCS范式，用远少于常规图文对的数据量达到同等视觉grounding效果，节省训练成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有多模态大模型（MLLM）预训练普遍依赖全局图像-文本对做模态对齐，存在指代歧义问题，无法精准建立多个视觉对象与文本实体的对应关系，导致数据效率低、语义grounding效果差。
### 方法关键点
提出多模态代码切换（MMCS）预训练范式，借鉴语言学代码切换现象，将文本中的实体直接替换为对应的视觉对象嵌入，强制模型学习局部视觉-语言的显式对齐；同时设计可扩展的数据合成pipeline，生成773K带精准对象-实体对应关系的预训练数据集。
### 关键结果数字
仅用50K MMCS格式训练样本，性能即可追平甚至超过用600K常规图文对训练的模型；在不同规模MLLM上验证，均可稳定提升视觉grounding与感知能力。
