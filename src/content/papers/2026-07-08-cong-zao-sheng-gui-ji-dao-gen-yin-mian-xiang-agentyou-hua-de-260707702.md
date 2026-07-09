---
title: 'From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal
  Extraction for Agent Optimization'
title_zh: 从噪声轨迹到根因：面向Agent优化的结构化轨迹分析与因果提取
authors:
- Ying Chang
- Jiahang Xu
- Xuan Feng
- Chenyuan Yang
- Peng Cheng
- Yuqing Yang
affiliations:
- University of Chinese Academy of Sciences
- Microsoft Research
arxiv_id: '2607.07702'
url: https://arxiv.org/abs/2607.07702
pdf_url: https://arxiv.org/pdf/2607.07702
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: Agent长序列轨迹优化 · 根因定位
tags:
- Agent Optimization
- Causal Localization
- Trajectory Analysis
- Reflexive Optimization
- Long-horizon Agent
one_liner: 提出STRACE框架，通过因果轨迹切片与根因定位提升长序列Agent反射优化的效率与效果
practical_value: '- 针对电商导购Agent、推荐系统链路故障排查场景，可复用STRACE的执行依赖图（EDG）构建逻辑，先梳理模块间data/control
  dependency，再做根因定位，避免只修复表面错误

  - 处理海量用户行为轨迹、Agent交互日志时，可复用「统计严重性+结构路径模式」的聚类筛选逻辑，仅保留高价值代表性故障样本，大幅降低优化算力成本

  - 针对长链路生成式推荐、多阶段搜索排序系统的bad case诊断，可复用反向因果切片逻辑，沿依赖链回溯定位根因模块，避免截断或滑动窗口丢弃关键因果证据

  - 优化Agent prompt/策略时，可复用将故障样本归纳为通用启发式规则、仅注入根因模块的做法，避免全链路修改带来的过拟合和不可控性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前长horizon Agent反射优化依赖全量轨迹输入，面临双重困境：批量轨迹冗余异构，全量优化效率低、易过拟合低价值故障；单条轨迹包含大量无关步骤，截断/滑动窗口等压缩方法易丢失因果证据，导致优化仅修复表面症状而非根因，亟需高信噪比的优化上下文构建方案。

### 方法关键点
- 结构化建模：从Agent代码/配置中提取执行依赖图（EDG），记录模块间data dependency和control dependency作为结构先验
- 故障模式挖掘与轨迹过滤：统计各模块错误关联全局失败的条件概率（统计严重性），聚类模块调用序列的结构路径模式，筛选覆盖所有故障模式的最小代表性轨迹集
- 因果定位：从故障显式发生的节点沿EDG反向回溯，裁剪无依赖的无关步骤，提取最小因果切片，定位故障的根因模块而非表象节点
- 归纳式策略优化：将同类根因的故障切片归纳为通用启发式规则，仅注入根因模块的prompt中，无需修改代码即可完成优化

### 关键实验
在HotpotQA、WebArena、VeruSAGE-Bench三个基准上对比Base Agent、Naive Few-shot、Failure-aware RAG、TextGrad、GEPA等基线：HotpotQA EM达68.5%，WebArena整体成功率较Base Agent提升12.9pp；VeruSAGE-Bench整体成功率从42.5%提升至58.5%，较最强基线GEPA高11.3pp；相同训练规模下优化成本仅为全轨迹优化方法的1/2左右。

**最值得记住的一句话**：Agent优化的核心是定位根因而非修复表象，基于结构依赖的因果切片是解决长序列上下文噪声trade-off的有效路径。
