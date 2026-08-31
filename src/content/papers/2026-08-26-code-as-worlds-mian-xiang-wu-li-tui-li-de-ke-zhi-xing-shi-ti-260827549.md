---
title: 'Code as Worlds: Agentic Discovery of Executable World Representations for
  Physical Reasoning'
title_zh: Code as Worlds：面向物理推理的可执行世界表示智能体发现框架
authors:
- Hanyang Wang
- Yimo Cai
- Weiliang Chen
- Jiawei Chi
- Haowen Sun
- Qiyu Dai
- Yi-Hsin Hung
- Xingzhuo Guo
- Jinshan Ren
- Runmao Yao
affiliations:
- MirroS
- Tsinghua University
- Peking University
- Nanyang Technological University
arxiv_id: '2608.27549'
url: https://arxiv.org/abs/2608.27549
pdf_url: https://arxiv.org/pdf/2608.27549
published: '2026-08-26'
collected: '2026-08-31'
category: Agent
direction: Agent 物理世界可执行表示构建
tags:
- Agent
- Physical Reasoning
- Code as Representation
- Vision Language Model
- World Model
one_liner: 提出将物理世界编码为可执行代码的范式，搭配智能体迭代环路提升VLM定量物理推理性能
practical_value: '- 可复用「提出-实例化-执行-渲染-验证」的迭代闭环架构，用于电商场景下的用户行为仿真、商品组合效果模拟，如虚拟试搭、促销规则效果预判

  - 基于可执行代码生成带精准标注训练数据的思路，可迁移到电商多模态内容生成、定量属性理解任务，大幅降低真实数据标注成本

  - 两阶段训练范式（先像素级测量接地、再世界级物理校准）可复用在多模态推荐模型的细粒度属性识别、视频内容语义理解任务中'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态模型能描述物理现象，但缺乏对物体状态、物理参数、动力学规律等底层机制的显式表示，无法可靠推理世界演化与干预响应；同时真实物理推理任务的定量标注成本极高，缺乏可泛化的世界表示范式支撑相关任务落地。

### 方法关键点
- 提出Code-as-World范式，将物理世界的静态组成（物体、物理属性）、动态演化（初始状态、事件、模拟规则）、视觉外观（相机、光照、渲染配置）编码为可执行代码，兼顾语义性、结构性与可执行性
- 设计智能体迭代发现环路：针对文本/视频输入分别提取语义/视觉证据，通过「提出世界假设-实例化模拟参数-物理引擎执行-渲染生成结果-多维度验证对比」的流程持续修正表示，直到匹配输入证据
- 两阶段训练VLM：第一阶段用现有视觉数据集构造像素级测量监督，训练模型定位、跟踪、测量物体的基础能力；第二阶段用可执行世界生成的带精准物理标注的VQA数据，通过GRPO优化定量物理推理能力

### 关键结果
在QuantiPhy定量物理推理基准上，Code-as-World-VL-9B平均MRA达55.4%，超过Gemini-3.1 Flash的54.8%；27B推理版平均MRA达58.6%，大幅领先所有开源及闭源基线；5轮迭代的智能体环路相比Best-of-5采样，在轨迹预测误差、物体IoU等指标上均有10%以上的提升。

**最值得记住的一句话**：可执行代码是连接多模态观测与机制化推理的高价值中间表示，智能体迭代优化比单次独立采样能更高效利用计算资源，获得更可靠的结果。
