---
title: Understanding Mamba-3 Through Oscillatory Dynamics
title_zh: 基于振荡动力学视角解读Mamba-3的长序列建模机制
authors:
- Shutian Liang
- Yue Song
affiliations:
- Tsinghua University
arxiv_id: '2610.13341'
url: https://arxiv.org/abs/2610.13341
pdf_url: https://arxiv.org/pdf/2610.13341
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: 大语言模型 · Mamba长序列建模机制
tags:
- Mamba-3
- State-Space Model
- Oscillatory Dynamics
- Long-context Modeling
- Dynamical System
one_liner: 将Mamba-3的输入依赖旋转解释为欠阻尼二阶动力学，揭示振荡对长序列建模的增益机制
practical_value: '- 业务中若用Mamba建模长用户行为序列（如电商半年浏览历史、Agent长对话记忆），优先选带输入依赖旋转的Mamba-3，参数量>400M时长上下文增益更显著

  - 做长序列召回/排序的序列模块时，可借鉴欠阻尼振荡设计，给状态更新加可学习的输入依赖旋转，调节历史与新输入的对齐度，避免状态范数爆炸导致的长度外推退化

  - 基于SSM搭建Agent轻量化记忆模块时，需保证状态写入和读出的相位一致性，否则会大幅降低长上下文信息的读取准确率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Mamba-3引入输入依赖旋转的状态更新机制，相比前序版本长上下文性能显著提升，但旋转的具体作用原理尚未明确，缺乏统一框架解释其超越状态保留的额外贡献。
### 方法关键点
- 将Mamba-3的衰减-旋转状态转移等价为欠阻尼二阶动力学系统：衰减系数对应阻尼包络，输入依赖的旋转角度对应振荡相位，可统一对比欠阻尼、临界阻尼、过阻尼三种模式的差异
- 设计控制变量实验，保持二阶状态结构完全一致，仅调整模态参数区分振荡/非振荡变体，排除结构差异的干扰
- 通过相位擦除、反转、打乱等干预实验，分析相位对状态积累、写入读出一致性的作用
### 关键结果
- 状态跟踪任务上，欠阻尼变体（原生Mamba-3）准确率达100%，远超过阻尼的3.27%、临界阻尼的3.22%
- 444M参数的带振荡Mamba-3在LongBench-E上得分13.22，较无振荡变体提升24.6%，64K上下文下PG-19困惑度降低约15%
- 相位擦除会导致64K上下文下SISO版Mamba-3的PG-19困惑度飙升41倍，验证相位对长上下文建模的核心作用
### 核心结论
SSM的有效记忆不仅取决于信息保留的比例，还取决于新输入到达时保留信息的变换方式，振荡通过调节历史与新信息的积累模式提升长上下文性能
