---
title: 'MM-ContextFold: Context Folding for Multimodal Agentic Retrieval'
title_zh: MM-ContextFold：面向多模态智能体检索的上下文折叠方法
authors:
- Yang Tian
- Fan Liu
- Jingyuan Zhang
- Zhenyang Li
- Yupeng Hu
- Liqiang Nie
affiliations:
- 山东大学
- 东南大学
- 快手
- 香港科技大学
- 哈尔滨工业大学（深圳）
arxiv_id: '2609.23121'
url: https://arxiv.org/abs/2609.23121
pdf_url: https://arxiv.org/pdf/2609.23121
published: '2026-09-19'
collected: '2026-09-22'
category: Agent
direction: 多模态检索Agent · 上下文管理
tags:
- Multimodal Agent
- Context Management
- Agentic Retrieval
- Context Folding
- Multimodal Retrieval
one_liner: 免训练双状态上下文管理框架，解决多模态检索Agent上下文爆炸问题，较ReAct提6.3%准确率降27.5%上下文长度
practical_value: '- 多模态检索Agent工程落地可直接复用双状态架构：主上下文仅存文本，图像按需加载到临时分支，任务结束后分支仅回传文本结果，大幅降低KV
  cache占用和推理成本

  - 电商多模态搜索/商品溯源场景可参考初始化阶段的图像粗描述机制：提前生成商品图的核心文本摘要用于全局规划，避免反复加载高token开销的图像输入

  - 长任务Agent的上下文优化可借鉴该研究结论：冗余多模态信息长期留存会提升输出熵、降低推理准确率，无需全局保留原始高成本模态输入'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多模态智能体检索（MAR）任务普遍采用ReAct类框架，全程留存原始图像与累计交互历史，极易引发上下文爆炸；现有上下文压缩方案仅面向文本优化，未解决高token开销的图像冗余留存问题，且研究发现图像长期留存会提升输出熵、降低推理准确率，此前无针对性解决方案。
### 方法关键点
- 双状态机制：拆分纯文本主状态+临时多模态分支状态，主状态仅存储任务进度、全局策略与蒸馏后文本证据，仅当需要视觉信息时触发分支，按需加载指定原始图像
- 初始化分支：首次触发的分支生成所有输入图像的高置信度粗文本描述，作为主状态全局任务规划的先验信息
- 分支折叠逻辑：分支完成子任务后仅将结构化文本结果回传合并入主上下文，直接丢弃原始图像与分支交互轨迹，框架免训练可适配任意多模态大模型底座
### 关键实验
覆盖7个MAR基准数据集、5个不同量级的多模态大模型底座（Gemini-3-Flash、GPT-5.2、Qwen3.5系列），对比ReAct、AgentFold、ContextFold三类基线；平均准确率较ReAct提升6.3个百分点，工作上下文长度降低27.5%，在长轨迹视觉深度研究任务上增益更为突出。
### 核心结论
多模态智能体对原始图像的依赖仅集中在早期视觉落地阶段，后续推理仅需留存文本化后的视觉证据即可，全局保留原始图像反而会损害推理性能。
