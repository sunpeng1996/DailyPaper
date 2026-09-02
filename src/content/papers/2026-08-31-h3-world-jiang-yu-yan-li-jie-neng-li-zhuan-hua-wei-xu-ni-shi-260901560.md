---
title: 'H3-World: Turning Language Understanding into World Control'
title_zh: H3-World：将语言理解能力转化为虚拟世界控制能力
authors:
- Danze Chen
- Zeqing Wang
- Ziyue Lin
- Xingyi Yang
- Yeying Jin
affiliations:
- Tencent
- National University of Singapore
- The Hong Kong Polytechnic University
arxiv_id: '2609.01560'
url: https://arxiv.org/abs/2609.01560
pdf_url: https://arxiv.org/pdf/2609.01560
published: '2026-08-31'
collected: '2026-09-02'
category: Agent
direction: Agent 世界模型 · 语言指令时序可控生成
tags:
- Interactive World Model
- LoRA
- Temporal Attention
- Video Generation
- Language Control
one_liner: 基于33B视频生成模型通过轻量LoRA微调实现精准时序可控的交互式虚拟世界控制框架
practical_value: '- 大预训练模型下游适配可参考仅用0.2%左右参数的LoRA微调方案，用万级以内少量样本即可实现自定义能力对齐，大幅降低落地成本

  - 时序类生成任务（如电商短视频生成、直播虚拟主播动作控制）可复用时序注意力路由机制，限制指令作用区间避免控制信号泄露，提升时序精准度

  - 交互类应用（如虚拟试穿、数字人导购）可参考结构化指令+预训练语义复用的思路，无需新增专用动作模块即可实现可控生成，降低架构复杂度'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
大参数视频生成模型已具备零样本语言控制角色行为、相机运动的能力，但天然控制粒度较粗、时序对齐精度差，实现交互式世界控制通常需要新增专用动作模块，落地成本高。
### 方法关键点
1. 将动作抽象为角色指令+相机指令的结构化组合，与对应时段的视频隐变量做对齐；
2. 新增时序注意力路由机制，限制每条指令仅作用于目标时间区间，降低跨动作的控制信号泄露；
3. 完全复用预训练阶段学习的语义表示，仅通过轻量LoRA做适配，无需新增专用动作模块。
### 关键结果
仅用8000个游戏样本、10000步LoRA优化、占比仅0.199%的可训练参数，即可实现精准的角色与相机控制，同时保留原模型的高质量生成能力，且可泛化到未见过的场景。
