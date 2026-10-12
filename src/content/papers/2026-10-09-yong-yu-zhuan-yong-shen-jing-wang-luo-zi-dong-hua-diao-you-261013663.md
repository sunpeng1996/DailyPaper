---
title: A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network
  Models
title_zh: 用于专用神经网络自动化调优的多智能体LLM系统
authors:
- Ivan Moloshnikov
- Dmitry Kunitsyn
- Alexander Sboev
- Maksim Skorokhodov
- Roman Rybka
- Yuanchao Liu
affiliations:
- National Research Centre “Kurchatov Institute”
- National Research Nuclear University MEPhI
- Moscow Institute of Physics and Technology
- Harbin Institute of Technology
arxiv_id: '2610.13663'
url: https://arxiv.org/abs/2610.13663
pdf_url: https://arxiv.org/pdf/2610.13663
published: '2026-10-09'
collected: '2026-10-12'
category: MultiAgent
direction: 多智能体 · 神经网络自动化调优
tags:
- MultiAgent
- AutomatedML
- LLM
- NeuralNetworkTuning
- PINN
- SNN
one_liner: 提出三角色多Agent框架，无需改动架构即可跨不同类型神经网络任务自动调优核心模块
practical_value: '- 可复用三角色（分析师/编码员/记录员）的Agent分工架构，用于推荐系统核心模块（如排序模型loss、召回层特征转换）的自动调优，仅需定义可修改模块的接口契约、目标指标即可快速落地

  - 详细prompt+方法分类覆盖地图的设计可大幅提升弱LLM的任务完成效果，在业务Agent开发中可优先把领域知识拆分为结构化分类+动态探索进度提示，降低对大参数量LLM的依赖

  - 沙箱执行+迭代实验日志的闭环设计可直接迁移到推荐模型AB测试自动化流程，自动记录有效方案、过滤错误代码，减少算法工程师重复劳动'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
专用神经网络（如脉冲神经网络SNN、物理 informed 神经网络PINN）的核心模块（解码层、输入输出特征转换、损失项权重）通常依赖人工调优，效率低且可复现性差；现有LLM Agent调优方案要么修改整段ML代码稳定性差，要么做固定空间的神经网络架构搜索（NAS）通用性弱，缺乏可跨任务复用、仅修改指定模块的通用调优框架。

### 方法关键点
- 三角色分工：Analyst基于历史实验日志生成调优方案的结构化技术规范，Coder按照预定义的接口契约生成仅修改指定模块的Python代码，Recorder自动将方案、代码、评测指标写入结构化实验日志作为外部记忆
- 闭环迭代流程：生成代码在Docker沙箱中执行，运行错误直接返回Coder重写，评测通过则更新日志进入下一轮迭代，全程仅开放指定模块的修改权限，其余网络结构、训练流程完全固定
- 支持双prompt模式：标准模式仅给定任务约束，详细模式新增领域方法分类+动态覆盖地图，引导Agent优先探索未尝试的方法类，避免无效重复试错

### 关键实验结果
跨5类异质任务验证：2个SNN分类任务（MNIST、sklearn digits）、3个PINN物理方程求解任务。对比基线包括人工调优基线、TPOT遗传算法、随机采样。核心效果：MNIST分类准确率较基线提升13pp，sklearn digits提升6pp；GNLSE单孤子求解误差降低2491倍，高斯扰动GNLSE守恒误差降低325倍，KS方程质量漂移降低14倍；详细prompt可将弱LLM（如Qwen3-30B）的调优效果从完全无法超过基线提升到接近强LLM水平。

### 核心结论
Agent做自动化调优时，限制修改范围+明确接口契约的效果远好于让Agent自由生成整段代码，可大幅提升落地成功率
