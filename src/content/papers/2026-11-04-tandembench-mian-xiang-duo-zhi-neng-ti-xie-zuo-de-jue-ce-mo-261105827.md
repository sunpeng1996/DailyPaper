---
title: 'TandemBench: Benchmarking Decision Models for Multi-Agent Collaboration'
title_zh: TandemBench：面向多智能体协作的决策模型基准测试
authors:
- Baohang Li
- Xiaocheng Feng
- Bing Qin
affiliations:
- Harbin Institute of Technology
- Peng Cheng Laboratory
arxiv_id: '2611.05827'
url: https://arxiv.org/abs/2611.05827
pdf_url: https://arxiv.org/pdf/2611.05827
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: 多智能体协作 · 决策模型评测
tags:
- Multi-Agent
- Benchmark
- Decision Model
- Planning
- Evaluation
one_liner: 推出含1200道问题的多智能体协作决策基准，同时评估最优计划选择与最优性判断能力
practical_value: '- 多智能体协作场景（电商客服、履约、运营多Agent协同）的决策评测，可复用「配对验证+精确搜索打标最优解」的方法，避免仅测选择准确率漏判系统性误差

  - 多Agent任务调度（直播场控、供应链多角色协同）的决策模型开发，可参考长短目标拆分设计，区分短期阶段效率和长期全局成本的选择偏好

  - 排序/选择类任务的模型评测，可借鉴「选项旋转测试」方法，量化模型对选项顺序的敏感度，评估决策稳定性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多智能体决策基准多聚焦单步选择准确率，忽略判断「给定候选是否包含最优方案」的能力，仅靠选择准确率会掩盖系统性偏差，缺乏针对多角色协同计划全局最优性的标准化评测框架。

### 方法关键点
- 基于Collab-Overcooked烹饪场景构建200个协同场景，共1200道评测题，包含400道最优计划选择题、800道配对最优性验证题（一组保留最优计划、一组移除）
- 所有答案通过实际执行+精确搜索确定全局最优解，区分短期阶段目标、长期全局目标两种评测设置，成本单位为联合执行步数
- 同时评测两个核心指标：决策准确率（DA，选对最优计划的比例）、验证准确率（VA，正确判断是否存在更优方案的比例）

### 关键结果
- 评测40个原生决策模型、10个通用大模型：最优原生决策模型KnowLine DA仅62.50%，VA接近随机水平（51.44%）；最优通用大模型Qwen3.8-27B DA达82.80%，VA为71.88%
- 64%的模型最优性判断接近随机，部分模型无论是否存在最优计划都会虚报更优方案，部分模型无论是否有更优方案都会选择给定候选
- 模型决策准确率对选项顺序敏感度中位数达10.38个百分点，长期目标下DA普遍比短期目标低2-3个百分点

### 核心结论
仅靠多智能体决策的选择准确率，会完全掩盖模型在最优性判断上的系统性误差，实际业务部署时必须补充最优性验证能力的评测
