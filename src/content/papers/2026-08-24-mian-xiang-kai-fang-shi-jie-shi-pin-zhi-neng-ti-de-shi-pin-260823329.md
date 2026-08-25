---
title: 'Thinking Beyond Videos: Unifying Video Reasoning and Deep Research for Open-World
  Video Agents'
title_zh: 面向开放世界视频智能体的视频推理与深度研究统一框架
authors:
- Wenqi Liu
- Shijie Ma
- Yunxiao Wang
- Meng Liu
- Qile Su
- Han Liu
- Bohan Hou
- Xuanyu Zheng
- Changyi Liu
- Tianke Zhang
affiliations:
- Shandong University
- Institute of Automation CAS
- Kuaishou Technology
- Beihang University
- Southern University of Science and Technology
arxiv_id: '2608.23329'
url: https://arxiv.org/abs/2608.23329
pdf_url: https://arxiv.org/pdf/2608.23329
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: 多模态Agent · 视频深度推理
tags:
- Video Agent
- Multimodal Reasoning
- Tool Use
- RL
- RAG
- Video Understanding
one_liner: 提出VideoRover统一框架，融合视频主动感知与多模态深度检索实现开放世界长视频推理
practical_value: '- 短视频种草/商品识别类Agent可复用工具协同逻辑：视频裁剪定位关键片段→图像搜索验证实体→文本搜索补全信息，解决视频商品识别不准、信息不足的问题

  - 多步交互Agent训练流程可直接复用：先用自动合成的SFT轨迹冷启动工具使用能力，再用困难样本做RL优化长时序决策，小参数模型也能超过开通同等工具权限的大模型

  - 多模态RAG的误差修正逻辑可迁移：用视频感知结果锚定检索query，检索返回的外部证据反过来指导重新感知视频片段，避免早期感知误差向下游传播'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有视频推理与深度研究能力割裂：视频感知类Agent仅能完成视频内时序定位与推理，无法调用外部知识补全视频缺失信息；深度研究类Agent仅支持静态图像/文本检索，无法处理长视频中稀疏分布的视觉证据，两者结合时易出现早期感知误差传播、检索结果无视觉锚点的问题，无法满足开放世界长视频推理需求。

### 方法关键点
- **框架设计**：迭代协调4种工具：视频裁剪定位关键片段、图像搜索验证视觉实体、文本搜索获取外部知识、网页浏览提取详细证据，每步工具输出更新共享研究状态，动态决策下一步动作
- **数据构建**：自动化生成26K经过验证的SFT交互轨迹，覆盖视频定位、多模态检索、证据融合全流程；筛选3K长时序困难样本作为RL训练集，强化长周期决策能力
- **训练流程**：先通过SFT学习基础工具调用逻辑，再用Group Sequence Policy Optimization（GSPO）做RL优化，基于最终回答正确性给予奖励

### 关键实验
在公开数据集VideoDR和自建分层评测基准VideoRover-Bench（共300个样本，按视频长度、推理难度分为6个层级）上测试：VideoRover-8B-RL平均准确率达57.71%，超过所有开通同等工具权限的开源大模型（如35B参数的Qwen3.6-35B-A3B仅53.14%），性能与闭源专有模型直接回答水平相当。

### 核心结论
仅给模型开通工具权限远远不够，让模型学会根据证据状态动态组合工具，才能真正提升开放域多模态推理能力。
