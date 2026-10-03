---
title: 'Ego2Act: Evaluating Goal-Directed Manipulation in Egocentric Video Generation'
title_zh: Ego2Act：第一人称视频生成的目标导向操作能力评估基准
authors:
- Patrick Amadeus Irawan
- Iskandar Muda Rizky Parlambang
- Rava Maulana
- Qinrong Cui
- Erland Hilman Fuadi
- Zayd M. K. Zuhri
- Nanda Ryaas Absar
- Ahmed Elshabrawy
- Wilfried Ariel Mulyawan
- Shoubin Yu
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Independent Researcher
- Nanyang Technological University
- University of North Carolina at Chapel Hill
arxiv_id: '2610.01092'
url: https://arxiv.org/abs/2610.01092
pdf_url: https://arxiv.org/pdf/2610.01092
published: '2026-09-30'
collected: '2026-10-03'
category: Eval
direction: 视频生成评测 · 具身Agent模拟
tags:
- Egocentric Video
- Video Generation
- Evaluation Benchmark
- Embodied Agent
- Goal-directed Planning
one_liner: 推出含2640条真实任务视频的Ego2Act基准与无参考评估管线，测评视频生成模型的目标导向模拟能力
practical_value: '- 做电商AR试穿、家居布置等具身场景的生成式内容评测时，可复用无参考评估管线的设计思路，对齐人类对任务完成度的判断标准

  - 规划Agent多步任务执行逻辑时，可参考基准的多步复杂度分级设计，规避步骤跳过、依赖状态缺失的问题

  - 做交互类内容生成（如虚拟导购操作演示视频）时，可借鉴基准的真实场景任务设计逻辑，提升生成内容的物理合理性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频生成模型被广泛探索作为具身Agent的世界模拟器，需具备目标导向动作下的环境动态演化预测能力，但现有评测基准仅聚焦单步短动作或逐步骤指令，缺失多步物理推理、第一人称视角下的高层目标导向复杂操作测评能力。
### 方法关键点
1. 构建Ego2Act评测基准，覆盖110种日常真实操作任务、共2640条第一人称视角操作视频，支持给定初始场景图像+高层目标的生成效果测评
2. 推出Ego2ActJudge无参考评估管线，无需匹配参考视频即可自动评估任务完成度与物理合理性
### 关键结果
- Ego2ActJudge的任务完成度、物理合理性评估结果与人类共识的对齐度优于所有相关基线
- 现有模型生成的模拟视频普遍存在步骤跳过、依赖状态缺失问题，复杂操作场景下普遍出现细粒度物理动态错误、全局世界建模不一致问题，最终导致目标未完成
