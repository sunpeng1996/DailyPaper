---
title: 'RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement'
title_zh: RSIGame：具备递归自提升能力的自主智能体游戏开发框架
authors:
- Wenyi Wu
- Minghao Fu
- Jieyu You
- Kun Zhou
- Siqi Liu
- Aayush Salvi
- Yiheng Lin
- Ce Zhang
- Xiaohan Lan
- Jiahui Zhu
affiliations:
- University of California San Diego
- ByteDance Inc.
- Carnegie Mellon University
arxiv_id: '2609.39045'
url: https://arxiv.org/abs/2609.39045
pdf_url: https://arxiv.org/pdf/2609.39045
published: '2026-09-29'
collected: '2026-10-01'
category: Agent
direction: Agent 递归自提升 长周期任务优化
tags:
- Autonomous Agent
- Recursive Self-Improvement
- LLM Generation
- Multi-Agent Collaboration
- SFT
one_liner: 提出双循环递归自提升Agent架构，大幅提升自动生成游戏的质量与开发效率
practical_value: '- 局部探索-诊断-改进+全局最优checkpoint保留+饱和检测的双循环架构，可直接迁移到生成式推荐的Prompt迭代、商品文案/落地页自动优化场景，避免迭代过程效果回退，比普通Self-Refine稳定性更强

  - 自适应任务调度+动态checklist的设计，可复用在推荐系统badcase自动挖掘修复流程中，自动根据当前系统短板分配算力优先级，无需人工固定迭代顺序

  - 迭代过程中成功轨迹回灌SFT的思路，可用于优化垂直场景LLM4Rec模型，大幅降低推理token消耗，提升小模型生成质量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM驱动的自动游戏生成已经能产出基础可玩版本，但简单迭代优化极易过拟合少量测试用例，生成的游戏存在大量未发现的bug、功能缺失，泛化性差，无法支撑长周期质量提升需求，同类迭代方法还容易出现效果饱和甚至回退问题。

### 方法关键点
- 双循环递归自提升架构：局部为探索-诊断-改进循环，由Controller、Explorer、Editor、Verifier四个角色Agent协作，维护动态更新的Checklist积累问题与优化方向，每次迭代基于已验证进展推进；全局循环负责监控整体质量，保留最优checkpoint，检测迭代饱和/效果回退，避免盲目浪费算力
- 经验内化机制：将迭代过程中验证通过的生成、规划、改进轨迹整理为SFT数据集，微调基座生成模型，把自提升能力沉淀到模型参数中，从上下文优化延伸到参数优化

### 关键实验
在140个GameCraft-Bench任务、2个游戏引擎、5个生成器上验证效果：Qwen3.8-27B经过经验内化+RSIGame迭代后，Godot引擎得分达61.38，超过GPT-5.5单次生成的50.26分，生成token消耗降低11倍；Phaser引擎得分达58.53，超过GPT-5.5单次生成的49.44分；同预算下比同类迭代方法Play2Code整体得分高7.2~13.8分。

### 核心结论
长周期复杂Agent任务的迭代优化，不能只依赖局部单次改进，必须配合全局进度监控+最优版本保留+能力沉淀，才能持续稳定获得质量收益，避免迭代饱和或回退。
