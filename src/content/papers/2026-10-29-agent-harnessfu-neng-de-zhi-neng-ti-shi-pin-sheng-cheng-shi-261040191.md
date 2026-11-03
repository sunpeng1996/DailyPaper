---
title: 'Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World
  Modeling and Recursive Self-Improvement'
title_zh: Agent Harness赋能的智能体视频生成、世界建模与递归自优化
authors:
- Liaoyuan Fan
- Yuhao Zheng
- Dongxing Mao
- Hangyu Ran
- Siyuan Hu
- Weijia Mao
- Rui Zhao
- Weijia Wu
- Guian Fang
- Yanzhe Chen
affiliations:
- Video Rebirth
- National University of Singapore
- Nanyang Technological University
- Hong Kong University of Science and Technology
- University of Science and Technology of China
arxiv_id: '2610.40191'
url: https://arxiv.org/abs/2610.40191
pdf_url: https://arxiv.org/pdf/2610.40191
published: '2026-10-29'
collected: '2026-11-03'
category: Agent
direction: Agent 架构设计 · 智能体视频生成
tags:
- Agent Harness
- Video Generation
- World Modeling
- Recursive Self-Improvement
- MultiAgent
one_liner: 以Agent Harness为核心的统一框架，系统梳理智能体视频生成三大核心方向的技术路径与挑战
practical_value: '- Agent Harness分层设计可直接复用到电商短视频生成Agent的工作流编排中，拆分规划、素材管理、生成、剪辑四个独立模块，用统一状态层管理跨模块依赖，大幅降低多轮生成的商品外观、场景一致性问题

  - 资产分层管理思路可迁移到营销物料库建设，将物料的固定属性（如商品外观）、动态状态（如使用场景）、上下文约束（如营销节点要求）分开存储，减少生成营销内容时的属性冲突

  - 多层级反馈路由机制可复用到自迭代Agent系统中，区分当前输出修正、状态更新、模型参数更新、全局流程更新四个反馈层级，避免单次任务的错误反馈改动全局逻辑，提升系统稳定性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视频生成仅能完成单片段合成，无法统筹多镜头规划、资产一致性、反馈迭代等复杂视频生产需求；同时视频世界模型的交互控制、视频生成系统的自迭代也缺乏统一的执行层框架，难以落地复杂的商业视频生产、交互仿真等场景。
### 方法关键点
- 定义Agent Harness为智能体的可执行运行时，核心能力覆盖上下文构造、工具暴露、状态维护、反馈路由、预算管控，是串联智能体决策与视频生成能力的核心执行载体
- 统一框架覆盖三大研究方向：1）智能体视频生成：Harness统筹脚本/镜头规划、资产管理、镜头生成、剪辑全流程，保障跨镜头一致性与生产效率；2）智能体世界建模：Harness作为交互中间层，可对接游戏引擎/代码生成的显式世界状态，由视频模型负责渲染，实现高保真持续交互；3）递归自改进（RSI）：区分当前输出修正、Harness状态更新、生成器参数更新、开发流程更新四个迭代层级，明确能力迭代的有效反馈通道
- 梳理视频场景下智能体需具备的核心能力：视听感知、长时序规划、记忆、代码/工具交互、反馈引导控制、技能复用、多智能体协作
### 关键结果
本研究为综述类工作，系统性梳理了近3年70+相关工作的技术演进路径，明确当前尚无完整实现递归自改进闭环的商用视频生成系统。
### 核心结论
智能体性由生成器外层的决策与执行流程决定，而非生成器本身的采样架构，Harness是实现复杂生成任务可靠落地的核心载体。
