---
title: Bridging the Gap Between Semantics and Reconstruction:Unifying Sign Language
  Translation and Production
title_zh: 弥合语义与重构鸿沟：统一手语翻译与生成框架
authors:
- Xiao Liu
- Shiwei Gan
- Yafeng Yin
- Jiaxin Yin
- Bowen Guo
- Yaqi Sun
- Zhiwei Jiang
- Lei Xie
affiliations:
- State Key Laboratory of Novel Software Technology, Nanjing University
arxiv_id: '2608.09045'
url: https://arxiv.org/abs/2608.09045
pdf_url: https://arxiv.org/pdf/2608.09045
published: '2026-08-10'
collected: '2026-08-16'
category: Other
direction: 多模态双向映射 · 统一生成框架
tags:
- Multimodal
- Unified Framework
- Autoregressive Generation
- Tokenizer
- Modality Alignment
one_liner: 提出Uni-SLTP双向统一框架，同时支持手语翻译与生成任务，效果优于现有基线
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
当前手语理解类子任务已实现单框架下的统一优化，性能提升显著，但手语翻译（手语→文本）与手语生成（文本→手语）属于方向相反的跨模态映射任务，尚无方案能在同一框架下支持两类任务，核心难点在于连续手语动作与离散文本的模态鸿沟、双向生成逻辑难以统一。
### 方法关键点
1. 设计共享手语tokenizer，将连续手语序列转换为离散token与隐表示，同时保留语义抽象信息与动作重构所需的细节；
2. 构建统一条件自回归生成模型，将两类双向任务统一为条件序列生成任务，支持输入任意模态自动生成对应反向模态的目标序列。
### 关键结果
在公开基准数据集上，手语生成任务的动作精度达到SOTA，同时手语翻译性能保持业内竞争力。
