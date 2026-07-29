---
title: 'ReDesign: Recovering Editable Design Structures from Images via Agentic Decomposition'
title_zh: ReDesign：基于智能体分层分解的光栅图像可编辑设计结构恢复方法
authors:
- Jooyeol Yun
- Jintae Park
- Hyesu Lim
- Junha Hyung
- Hyungjin Chung
- Jaegul Choo
affiliations:
- KAIST AI
- Helmholtz Munich
- Korea University
- EverEx
arxiv_id: '2607.25565'
url: https://arxiv.org/abs/2607.25565
pdf_url: https://arxiv.org/pdf/2607.25565
published: '2026-07-27'
collected: '2026-07-29'
category: Agent
direction: Agent 工具调用 · 结构化分层任务执行
tags:
- Agent
- VLM
- Tool Use
- Hierarchical Reasoning
- Verification
one_liner: 提出树状扩展+每步优雅校验的VLM智能体框架，从光栅图像恢复高可编辑性分层设计结构
practical_value: '- 做工具调用Agent时可借鉴「结构化树状扩展+每节点局部校验」架构，替代单链路串行工具调用，避免错误累积，减少整体重试成本，可直接复用在电商素材自动化解析/修改类Agent场景

  - 工程优化可复用无依赖节点并行执行思路：树状扩展中每个子节点仅依赖父节点状态，无跨子节点依赖，文中实测最高7.1倍加速，可直接用于优化大流量Agent服务的吞吐量

  - 效果评估可借鉴「操作回放Benchmark」设计：不局限于最终输出相似度，用真实业务操作（如改文案、调色、调布局）的执行成功率衡量系统实际可用性，适合电商素材生成/修改类系统的效果验收'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有从光栅图恢复可编辑设计文件的方案，要么单工具能力存在局限，要么串行工具调用容易出现错误累积，最终输出可编辑性差，设计师仍需大量手动重构，效率极低，且行业缺乏统一的可编辑性评估标准。

### 方法关键点
- 任务建模为分层树扩展问题：从根节点（整图）开始，逐步扩展子节点，最终得到原子级可编辑元素（文本、矢量形状、图层等）的分层结构
- VLM控制器做动态动作选择：支持文本提取、图层拆分、连通域分割、目标检测分割、矢量化5类工具链的自适应选择，支持并行扩展多个无依赖的叶子节点
- 每步优雅校验机制：对每个节点扩展结果做局部校验，判断子节点是否覆盖父节点内容、是否存在冗余/幻觉，输出接受、剪枝、重试三种反馈，从源头阻断错误传递
- 单节点线性内存设计：每个节点仅存储自身扩展历史，无需记录兄弟节点状态，避免内存爆炸和并发冲突

### 关键实验
- 自建Figma Edit Replay Benchmark：包含909个真实Figma文件、14796条控制编辑指令，覆盖布局、颜色、文本三类编辑场景
- 对比LayerD、Qwen-Image-Layered、串行工具Agent、VTracer等基线，编辑回放SSIM全面领先，文本编辑召回率显著高于串行Agent；Crello数据集上布局F1达0.587，比基线最高值高0.06
- 工程效率上，并行执行最高7.1倍提速，局部校验比终态校验更快、准确率更高、运行方差更小

**最值得记住的一句话**：给Agent任务加上结构化约束，把长链路任务拆分为分层局部决策+局部校验，能同时提升可控性、准确率和执行效率。
