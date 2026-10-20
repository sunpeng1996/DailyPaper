---
title: 'EvoWeb: A Benchmark for Coding Agents on Evolving Web Applications'
title_zh: EvoWeb：面向演进式Web应用的编码Agent评测基准
authors:
- David Nukrai
- Bar Alon
- Nativ Levy
- Ido Andrew Atad
- Ido Cohen
- Itamar Zimerman
- Lior Wolf
- Eli David
- Ilan Naiman
affiliations:
- Stealth Startup, Tel Aviv
- Tel Aviv University
arxiv_id: '2610.16402'
url: https://arxiv.org/abs/2610.16402
pdf_url: https://arxiv.org/pdf/2610.16402
published: '2026-10-11'
collected: '2026-10-20'
category: Agent
direction: 编码Agent · 长周期迭代场景评测基准
tags:
- Coding Agent
- Benchmark
- Long-Horizon Task
- Multimodal Eval
- Web Agent
one_liner: 发布含32个Web应用320条累积需求的EvoWeb基准，用于长周期多轮迭代编码Agent评测
practical_value: '- 迭代类Agent任务评测可复用「跨轮次依赖校验+多模态动态测试」框架，替代固定静态指标，更贴合业务长周期迭代场景的真实要求

  - 多轮交互Agent的错误防控可参考结论：依赖层级越深的后续任务，需额外加入历史状态校验、运行时错误检测环节，降低连锁故障率

  - 开发面向运营/商家的低代码Agent工具时，可引入用户容忍度阈值的轨迹性能评估方式，匹配不同用户的容错需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有编码Agent评测基准均基于固定开发需求，未覆盖真实Web开发中多轮迭代、功能依赖逐步累积的长周期场景，无法评估多轮修改后的功能兼容性、历史逻辑留存等核心能力。
### 方法关键点
构建EvoWeb基准，覆盖32个真实Web应用、320条带功能依赖关系的累积迭代需求；采用多模态Web Agent在真实浏览器环境测试每轮迭代结果，同时校验新增功能可用性、跨轮集成兼容性、历史功能完好性；评估逻辑采用跨用户容忍度阈值的轨迹性能积分，替代传统固定停止判据。
### 关键结果
基准可有效区分开源/闭源前沿模型性能，跨轮集成是编码Agent核心瓶颈；依赖层级更深/数量更多的后续需求准确率下降超40%，运行时错误率随迭代轮次提升35%以上。
