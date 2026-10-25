---
title: Self-Distilling Future Video Representations for World Action Models
title_zh: 面向世界动作模型的自蒸馏未来视频表示学习方法
authors:
- Huiwon Jang
- Suhyeok Jang
- Hyeonmo Kang
- Seungku Kim
- Jinwoo Shin
- Sihyun Yu
affiliations:
- KAIST
- RLWRLD
arxiv_id: '2610.30320'
url: https://arxiv.org/abs/2610.30320
pdf_url: https://arxiv.org/pdf/2610.30320
published: '2026-10-20'
collected: '2026-10-25'
category: Other
direction: 世界动作模型 · 自蒸馏视频表示学习
tags:
- World Action Model
- Self-Distillation
- Video Representation
- Diffusion Model
- Zero-shot Generalization
one_liner: 提出带时序上下文的自蒸馏框架FRED，提升世界动作模型泛化与技能迁移能力
practical_value: '- 自蒸馏以真值特征为监督目标优化单步生成表示的思路，可迁移到GenRec中单步生成Semantic ID的质量提升，避免多步迭代的推理成本

  - 引入历史时序上下文作为生成条件的设计，可复用到时序用户行为建模的召回/排序模块，优化长序列行为的表征效果

  - 零样本跨域泛化的蒸馏优化思路，可借鉴到跨域推荐、新场景冷启动的模型适配任务，降低跨域数据标注成本'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有基于预训练视频扩散模型的World Action Models（WAM）为提升推理效率，采用单步去噪提取未来视频表征输入动作解码器，跳过高成本的多步迭代视频生成流程，但动作预测效果高度依赖单步生成的未来表征质量，现有方案表征精度不足。

### 方法关键点
提出FRED框架：
1. 采用自蒸馏范式，以真值未来观测提取的表征为监督目标，训练模型从噪声中直接预测高质量未来表征
2. 给视频扩散模型增加历史观测作为输入条件，引入时序上下文提升未来表征的预测准确率

### 关键结果
多类真实机器人操作场景下性能全面优于现有SOTA WAM；零样本跨域长周期任务提升显著，仅用人类演示视频的零样本人机技能迁移任务成功率达50.0%，远超SOTA的19.4%
