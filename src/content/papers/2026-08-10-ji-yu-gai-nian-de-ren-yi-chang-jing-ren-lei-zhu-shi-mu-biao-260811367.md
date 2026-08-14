---
title: Gaze Target Estimation Anywhere with Concepts
title_zh: 基于概念的任意场景人类注视目标估计方法
authors:
- Xu Cao
- Houze Yang
- Vipin Gunda
- Zhongyi Zhou
- Tianyu Xu
- Adarsh Kowdle
- Inki Kim
- James M. Rehg
affiliations:
- University of Illinois Urbana-Champaign
- Google
arxiv_id: '2608.11367'
url: https://arxiv.org/abs/2608.11367
pdf_url: https://arxiv.org/pdf/2608.11367
published: '2026-08-10'
collected: '2026-08-14'
category: Other
direction: 多模态 · 可提示注视目标估计
tags:
- Gaze Estimation
- Promptable Paradigm
- Multimodal Fusion
- Transformer
- Benchmark Dataset
one_liner: 提出可提示注视目标估计新范式PGE，配套120K标注数据集与首个SOTA开源模型
practical_value: '- 仅当业务涉及线下零售用户行为分析、直播内容用户注意力分析时，可直接复用GazeAnywhere识别用户注视的商品/内容对象，辅助业务优化

  - prompt驱动端到端多任务融合的设计思路，可迁移至多模态交互系统，避免多阶段pipeline的级联误差问题

  - 自动化数据引擎生成大规模标注数据集的方案，可复用至多模态小样本任务的训练数据构造'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有野生场景注视估计依赖多阶段pipeline，需显式输入头部框、人体姿态等中间结果，检测误差会级联传递，且不支持自然语言提示灵活指定分析对象，灵活性和扩展性差。

### 方法关键点
1. 定义可提示注视目标估计（PGE）新范式，支持文本/视觉提示指定分析主体，端到端融合主体定位与注视估计，消除对中间步骤的刚性依赖
2. 搭建可扩展数据引擎，生成含120K高质量带提示标注的Gaze-Co基准数据集
3. 提出首个PGE模型GazeAnywhere，基于Transformer检测器融合冻结编码器特征，同时完成主体定位、是否在帧内判断、注视目标热图估计

### 关键结果
在多个PGE基准上达到SOTA，在域外真实临床数据集上也取得领先效果，模型已完全开源
