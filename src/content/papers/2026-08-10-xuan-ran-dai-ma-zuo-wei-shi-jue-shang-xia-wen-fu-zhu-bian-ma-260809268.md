---
title: Can Coding Agents Solve Repository-Level Issues with Rendered Code? An Exploratory
  Study of Visual Representations
title_zh: 渲染代码作为视觉上下文辅助编码Agent解决仓库级问题的探索研究
authors:
- Weijie Liang
- Yuanfeng Song
- Xing Chen
- Caleb Chen Cao
- Sirui Han
- Yike Guo
affiliations:
- The Hong Kong University of Science and Technology
- ByteDance
arxiv_id: '2608.09268'
url: https://arxiv.org/abs/2608.09268
pdf_url: https://arxiv.org/pdf/2608.09268
published: '2026-08-10'
collected: '2026-08-11'
category: Agent
direction: 编码Agent · 长上下文视觉压缩
tags:
- CodingAgent
- VisualCompression
- LongContext
- LLM
- SWE-bench
one_liner: 系统评估渲染代码在仓库级编码Agent工作流中的降本效果与适用边界
practical_value: '- 长上下文场景可复用结构化文本转视觉输入的降本思路：可将商品详情、用户长行为序列、召回候选集等大段结构化文本渲染为视觉输入降低Prompt
  Token成本，注意避免过度压缩导致可读性下降

  - Agent工作流可参考分阶段解耦设计：将探索定位与执行迭代拆分，前置结构化检索定位环节，减少后期无意义交互的Token消耗

  - 成本优化优先级判断：当任务中试错迭代（如广告创意调优、推荐策略模拟AB测）占比更高时，上下文压缩的边际收益会大幅降低，优先优化迭代链路效率更划算

  - 方案评估注意点：新的上下文表示方案不能仅做静态理解测试，必须嵌入完整Agent交互链路验证，避免静态效果好但实际链路增益弱的问题'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有渲染代码压缩方案仅在静态代码理解场景验证过效果，而编码Agent需要完成仓库导航、代码编辑、测试验证等长交互链路任务，静态场景的结论无法直接迁移，亟需明确渲染代码在真实Agent工作流中的实际收益与适用边界。

### 方法关键点
- 设计三类受控Agent配置：原生mini SWE-agent、带离线预定位的PLB Agent、定位-编辑解耦的LET Agent，逐步拆分仓库探索、代码阅读、编辑测试等环节，精准定位视觉压缩的作用环节
- 控制多组渲染压缩比r∈{1,3,5,7}，对比文本上下文与渲染代码上下文的效果差异，覆盖正常/宽窗口两种代码查看模式
- 评估维度覆盖单轮代码读取成本、全链路Token消耗、端到端任务准确率三个层面

### 关键结果
基于SWE-bench Verified数据集，在Qwen3.5、Kimi-K2.5两个多模态基座上测试得到：
1. 渲染代码可稳定降低Prompt Token成本，最高可达2.81倍，同时基本保留端到端修复准确率，大部分场景下准确率波动在5%以内
2. 压缩收益不与标称压缩比线性相关，小窗口代码很快达到成本地板，过度压缩会导致可读性下降、准确率不稳定
3. 当结构化定位已经降低代码阅读需求时，视觉压缩的边际收益大幅下降，LET Agent中编辑测试环节占总Token消耗的76%以上，压缩对这部分几乎无增益

**最值得记住的结论**：视觉文本压缩是可行的长上下文降本手段，但仅在原始文本阅读是核心瓶颈时收益显著，不能替代对Agent整体工作流的优化。
