---
title: 'SPLATIFY: Reproduce, Discover, Innovate! From Papers and Ideas to Trainable
  3DGS Code'
title_zh: SPLATIFY：可将3DGS论文/想法转换为可训练代码的多智能体框架
authors:
- Seemandhar Jain
- Keshav Gupta
- Manmohan Chandraker
affiliations:
- University of California, San Diego
arxiv_id: '2610.09116'
url: https://arxiv.org/abs/2610.09116
pdf_url: https://arxiv.org/pdf/2610.09116
published: '2026-10-05'
collected: '2026-10-13'
category: Agent
direction: Agent 特定领域论文到可执行代码生成
tags:
- MultiAgent
- CodeGeneration
- RAG
- Graph-of-Thought
- 3DGS
one_liner: 提出针对3DGS领域的多智能体论文转代码框架，实现高效复现、性能优化与跨领域方法创新
practical_value: '- 做特定领域代码生成类Agent时，可优先定义领域上下文无关文法+模块化模板约束输出，从生成逻辑上避免违反领域架构不变性，大幅减少无效输出

  - 多组件代码生成任务可引入按拓扑依赖顺序的Graph-of-Thought调度，结合RAG召回同领域已验证实现做In-Context样例，显著提升生成准确率

  - 生成结果核验环节可引入多维度反馈（指标校验、结构检查、多模态判优）驱动迭代修复，替代纯人工核验，大幅降低特定领域开发成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
3DGS领域研究迭代快，通用论文转代码方案无法满足需求，研究者需花费数周复现论文才能开展后续工作，落地门槛高。
### 方法关键点
1. 定义gsplat领域上下文无关文法与模块化模板，预置损失、稠密化、渲染等扩展点，强制生成代码满足3DGS架构不变性；
2. 引入分支感知引用恢复、按拓扑依赖排序的Graph-of-Thought代码合成、RAG召回20+已验证实现做In-Context样例，搭配PSNR引导再生、高斯结构检查、VLM驱动修复的反馈链路保障复现准确率；
3. 支持自主诊断算法缺陷并组合互补策略优化效果，可跨领域检索外部物理先验生成未覆盖场景的全新方法；
4. 配套覆盖30篇3DGS论文的评测基准SPLATIFY-Bench。
### 关键结果
对无公开代码的3DGS论文，生成效果匹配专家实现，开发耗时从数周压缩至分钟级，通过组合优化可将PSNR最高提升2.4dB，还可自主生成星云渲染等跨领域新3DGS方法。
