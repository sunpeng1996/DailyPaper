---
title: 'VibeVideoAgent: Closing the Perceptual Loop for Code-Driven Video Generation'
title_zh: VibeVideoAgent：为代码驱动视频生成闭合感知闭环
authors:
- Xuanyu Zheng
- Luoyuan Zhang
- Yancheng Long
- Haoyang Xu
- Muxi Diao
- Yuzhe Chen
- Kaiyu Jiang
- Bin Wen
- Tingting Gao
affiliations:
- KlingAI Research
arxiv_id: '2611.34237'
url: https://arxiv.org/abs/2611.34237
pdf_url: https://arxiv.org/pdf/2611.34237
published: '2026-11-24'
collected: '2026-11-26'
category: Agent
direction: Agent 多模态生成感知闭环优化
tags:
- LLM Agent
- Multimodal Perception
- Code Generation
- Video Generation
- Perceptual Loop
one_liner: 无训练解耦感知框架，将原始媒体隔离在编码Agent上下文外，提升代码驱动视频生成质量
practical_value: '- 做电商/广告短视频生成类Agent业务时，可复用「解耦感知+结构化反馈」架构，将原始多模态数据隔离在主Agent上下文外，仅返回带时空锚点的紧凑Findings，大幅降低长上下文开销，避免主Agent注意力分散

  - 可复用7种分层感知原语设计，替代通用VLM的大段评注，显著提升多模态生成任务的反馈精准度，减少无效迭代

  - 可复用风险优先的分阶段执行协议，编码前先锁定最高风险需求，用最小预览提前验证，避免后期全量返工，降低生成业务的时延和成本

  - 做代码生成类Agent时，可参考多时钟媒体表示方法，解决不同版本/片段的时间对齐问题，精准定位缺陷对应的代码片段，提升修复效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
代码驱动视频生成可实现精确的排版、数据可视化、音视频同步、多镜头控制，还能留存可编辑项目，但现有编码Agent存在三大痛点：程序运行成功不代表视听效果达标，大量感知类Bug无运行时报错；原始渲染帧、音频传入编码上下文会占用海量token，损害长程编码能力；仅评估最终渲染结果会导致早期错误需全量重写，成本极高。

### 方法关键点
- 解耦感知闭环架构：原始媒体永远不进入主编码Agent上下文，所有感知查询交给独立无状态VLM工作节点或本地分析器，仅返回结构化、带时空锚点的紧凑Findings
- 统一多时钟草稿表示：兼容不同阶段媒体，通过三时钟映射实现时间精准对齐，原生支持裁剪优先缩放、自适应采样、不可变快照缓存
- 7个跨渲染栈感知原语：覆盖粗到细探索、需求校验、双时钟对比、确定性信号探测四大类需求，无需适配特定渲染引擎
- 轻量分阶段生产协议：编码前拆解需求锁定最高风险项，按最小预览→粗剪组装→定向修复→验证交付四阶段执行

### 关键结果
在239个VibeVideoBench任务上，固定感知模型为Gemini 3.8 Flash，相同运行时长下：Claude Opus 5.5的整体视听质量L3从4.03升至4.43，L2规则符合率从98.87%升至99.35%；GPT-6 Astra的L3从4.03升至4.27；Claude Sonnet 5.5的L3从3.97升至4.10；音视频同步指标最高提升0.56。

### 核心结论
把多模态感知能力从主Agent的长上下文剥离，用结构化紧凑反馈替代原始媒体输入，是兼顾Agent生成质量和上下文效率的核心路径
