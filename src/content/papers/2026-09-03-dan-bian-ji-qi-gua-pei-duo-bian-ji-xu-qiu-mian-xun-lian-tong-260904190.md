---
title: 'One Editor, Many Edits: A Unified Training-Free Framework for Diverse Video
  Editing'
title_zh: 单编辑器适配多编辑需求：免训练统一多样化视频编辑框架
authors:
- Adheesh Sunil Juvekar
- Onkar Kishor Susladkar
- Kiet A. Nguyen
- Muntasir Wahed
- Nabeel Bashir
- Xiaona Zhou
- Tianjiao Yu
- Vedant Shah
- Ismini Lourentzou
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2609.04190'
url: https://arxiv.org/abs/2609.04190
pdf_url: https://arxiv.org/pdf/2609.04190
published: '2026-09-03'
collected: '2026-09-05'
category: Multimodal
direction: 多模态内容生成 · 免训练视频编辑
tags:
- Video Editing
- Training-Free
- Diffusion Model
- Temporal Consistency
- Multimodal Generation
one_liner: 免训练视频编辑框架EditVid，融合三类时序优化机制覆盖多范式视频编辑需求
practical_value: '- 电商短视频素材生产场景可直接复用EditVid免训练能力，零微调实现商品属性修改、风格迁移、背景替换等操作，大幅降低素材制作成本

  - 三个时序一致性优化trick（稀疏因果记忆保局部连贯、对应关系token注入保身份一致、软隐空间混合保编辑局部性）可迁移到AI生成短视频的一致性优化模块

  - 多方案对比的用户偏好评估实验设计可复用在生成类内容工具的效果验收环节，量化用户对不同生成方案的接受度'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有视频编辑方案存在两类核心问题：单帧独立编辑缺失时序耦合，易出现闪烁、主体身份漂移、背景异常修改；专项训练的视频编辑模型成本高，单一框架无法同时覆盖指令引导、参考引导等多类编辑范式。
### 方法关键点
免训练框架EditVid融合三大核心机制：1）稀疏因果记忆保障帧间局部时序连贯性；2）基于对应关系的注意力后token注入，实现长视频编辑中的主体身份一致性保留；3）软隐空间混合保证编辑区域局部性，不干扰无关内容。统一支持风格迁移、属性修改、物体插入、部件级编辑、主体替换等多类任务。
### 关键结果
FiVE数据集上FiVE-Acc达78.16，较最强免训练基线高出19.21个百分点；IVEBench上效果具备竞争力；用户调研显示相对7个竞品的整体用户偏好率达51.8%
