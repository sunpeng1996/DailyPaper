---
title: 'HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition
  for Multimodal Agents'
title_zh: HiVe-Mem：面向多模态Agent的横向记忆扩展与纵向证据组合框架
authors:
- Haozhen Zhang
- Bohan Liu
- Jianzhu Bao
- Qingyuan Liu
- Haodong Yue
- Xiao Li
- Zi Pong Lim
- Wenya Wang
affiliations:
- Nanyang Technological University
- Tsinghua University
- Sun Yat-sen University
- Aumovio Singapore Pte. Ltd.
arxiv_id: '2611.12872'
url: https://arxiv.org/abs/2611.12872
pdf_url: https://arxiv.org/pdf/2611.12872
published: '2026-11-09'
collected: '2026-11-10'
category: Agent
direction: 多模态Agent · 长时记忆优化
tags:
- Multimodal Agent
- Long-term Memory
- Reinforcement Learning
- Token Efficiency
- Cross-modal Retrieval
one_liner: 提出横纵二维多模态Agent记忆框架，提升任务效果同时降低约90%token消耗
practical_value: '- 电商多模态召回/Agent客服场景可复用「语义检索种子+跨模态关联图扩展」架构：将用户交互历史（含商品文本、图片）切分episode，提取文本/视觉锚点构建关联图，检索时补充种子的关联邻居，大幅提升召回覆盖率，避免语义匹配漏检相关内容。

  - 多粒度证据存储+RL自适应选择设计可直接落地：为每个记忆单元存储摘要、详情、原图、裁剪图等多粒度内容，用轻量RL选择器根据query动态选择返回内容，通过λ参数灵活调控不同算力预算下的回答质量与token成本平衡，实测可降本90%左右。

  - 跨模态锚点+IDF加权的关联度计算可优化用户行为序列建模：将用户行为中的文本特征（商品标题、评价）和视觉特征（商品主图、晒图）作为锚点，加权计算不同行为的关联度，提升序列推荐、用户画像建模的效果。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多模态Agent长时交互场景下，现有记忆系统普遍采用压缩记忆语义检索+固定表征返回的逻辑，存在两个核心问题：一是仅依赖单记忆语义匹配，容易漏检分布在不同交互片段中、仅靠弱跨模态cue关联的相关内容；二是所有检索结果都返回固定粒度表征，要么粒度太粗信息不足，要么太细冗余度高，导致任务效果差、token消耗高，无法适配不同query的异质性信息需求。
### 方法关键点
- **横向记忆扩展**：将长交互历史切分episode作为记忆基本单元，每个episode提取文本锚点（实体、事件、话题）和视觉锚点（物体、场景、属性），基于锚点重叠度+IDF加权计算跨episode关联度，构建稀疏关联图；检索时先通过query与episode摘要的语义匹配得到种子记忆，再扩展种子的关联邻居，补全分布式的互补信息。
- **纵向证据组合**：每个episode存储5种不同粒度的证据：原始交互文本、紧凑摘要、图片caption、原始图片、上下文相关的裁剪图；用3层轻量MLP作为选择器，通过PPO强化学习训练，根据query和episode摘要独立决策每个证据是否需要返回，奖励函数同时兼顾回答质量和token消耗，可通过λ参数调整质量与成本的平衡。
### 关键实验
在Mem-Gallery、WorldMemArena、H2HMem三个多模态记忆基准上测试，对比M2A、MIRIX、MemVerse等SOTA多模态记忆方案，分别以Qwen3-VL-4B-Instruct、GPT-5-mini为基座：平均F1/LLM-Judge分数分别提升3.9/14.07、3.0/3.98，同时token消耗相比最优多模态基线降低约90%；选择器跨基座直接迁移仍能保持效果，单query Time to First Token仅1.03s，runtime overhead极低。
### 最值得记住的一句话
多模态记忆系统优化不要局限于固定检索逻辑和单粒度表征，从「召回哪些记忆」和「返回什么粒度的内容」两个维度同时优化，可在提升效果的同时大幅降低推理成本。
