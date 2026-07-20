---
title: An Exam for Active Observers
title_zh: 主动观察者测试：多模态大模型主动视觉观测能力评测基准
authors:
- Jiarui Zhang
- Muzi Tao
- Shangshang Wang
- Ollie Liu
- Xuezhe Ma
- Willie Neiswanger
affiliations:
- University of Southern California
arxiv_id: '2607.16165'
url: https://arxiv.org/abs/2607.16165
pdf_url: https://arxiv.org/pdf/2607.16165
published: '2026-07-17'
collected: '2026-07-20'
category: Eval
direction: 多模态大模型 · 视觉能力评测
tags:
- MLLM
- Evaluation Benchmark
- Active Vision
- Visual Reasoning
- Perception-Reasoning Loop
one_liner: 提出ActiveVision基准量化多模态大模型主动视觉观测能力，揭示当前模型与人类的显著差距
practical_value: '- 多模态商品理解、直播内容理解类Agent评测，可引入ActiveVision的动态任务范式，避免单帧静态评测高估模型实际表现

  - 搭建多模态搜索推荐的感知-推理闭环Agent时，可参考基准的3类任务设计训练数据，强化模型注意力调度、跨区域特征比对能力

  - 当前通用MLLM主动视觉能力不足，复杂商品质检、多目标识别类业务不要直接复用通用MLLM，需搭配专用CV模型做分层处理'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有多模态基准多为单帧静态视觉理解任务，无法衡量MLLM是否具备人类式的感知-推理闭环主动观测能力，而该能力是复杂视觉任务的核心支撑。
### 方法关键点
提出ActiveVision基准，覆盖分布式扫描、序列遍历、视觉属性迁移3大类共17个任务，强制模型完成多次动态视觉感知而非单次静态描述，实现主动观测能力的可量化评估。
### 关键结果数字
前沿MLLM表现极差：最高分为GPT-5.5最高推理档位的10.6%，且在17个任务中的11个得0分；Claude Fable 5仅得3.5%，远低于人类平均96.1%的得分；即使允许模型自行编写运行视觉代码，差距仍显著，因代码鲁棒性差且故障排查本身也需要主动感知能力。
