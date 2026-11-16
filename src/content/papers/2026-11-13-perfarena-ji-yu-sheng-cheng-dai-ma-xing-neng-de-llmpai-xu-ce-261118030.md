---
title: 'PerfArena: Ranking LLMs by Code Performance'
title_zh: PerfArena：基于生成代码性能的LLM排序评测框架
authors:
- Rui Rua
- Hailemariam Mersha
- Joao Paulo Fernandes
- Karim Ali
arxiv_id: '2611.18030'
url: https://arxiv.org/abs/2611.18030
pdf_url: https://arxiv.org/pdf/2611.18030
published: '2026-11-13'
collected: '2026-11-16'
category: Eval
direction: LLM评测 · 代码生成性能
tags:
- LLM_Evaluation
- Code_Generation
- Performance_Benchmark
- Open_Source
- Energy_Efficiency
one_liner: 开源可插拔代码生成LLM评测框架，跨7种语言从正确性时延内存能耗维度排序模型
practical_value: '- 团队做代码生成类Agent（如推荐系统特征工程代码生成、数仓SQL生成工具）选型LLM时，可直接参考PerfArena公开的leaderboard，优先选生成代码能耗/时延更低的模型，降低线上运行成本

  - 可复用PerfArena的可插拔评测框架逻辑，搭建业务专属的LLM生成代码评测流水线，支持自定义正确性/性能判题器，不需要修改主流程即可新增评测维度

  - 做内部代码生成LLM微调时，可将生成代码的时延、内存占用、能耗加入RLHF奖励项，优化生成代码的运行效率，而非只关注正确性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前工业界大量使用LLM生成生产代码，但现有代码生成基准大多仅评测正确性，少数性能导向基准覆盖语种少，几乎不衡量能耗，无法满足生产级代码对运行成本的要求。
### 方法关键点
提出开源可复现的评测框架PerfArena，在Unix主机上执行LLM生成的代码，同时输出正确性、时延、峰值内存、能耗4类指标；框架采用可插拔设计，正确性/性能判题器、性能分析工具、代码生成工作流均可独立替换，无需修改主流程，支持跨7种编程语言统一协议评测。
### 关键结果
已覆盖13个SOTA LLM、2类评测集（10个计算密集型基准、99道LeetCode题），累计9455条可复现的正确解；gpt-6-astra性能最优，LeetCode题正确率99.7%、计算密集基准正确率100%，其他LLM生成代码平均时延是其1.1~3.6倍，最高运行成本是其9.3倍
