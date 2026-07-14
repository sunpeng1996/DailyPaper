---
title: 'LightMem-Ego: Your AI Memory for Everyday Life'
title_zh: LightMem-Ego：面向日常生活的轻量化多模态个人记忆系统
authors:
- Yijun Chen
- Boyi Xiao
- Yixian Zhao
- Haoting Xia
- Buqiang Xu
- Jizhan Fang
- Yanya Li
- Yaqi Zheng
- Xuehai Wang
- Zirui Xue
affiliations:
- Zhejiang University
- South China University of Technology
- Central China Normal University
- Lenovo Group Limited
arxiv_id: '2607.11487'
url: https://arxiv.org/abs/2607.11487
pdf_url: https://arxiv.org/pdf/2607.11487
published: '2026-07-13'
collected: '2026-07-14'
category: Agent
direction: 个人智能体 · 多模态分层记忆
tags:
- Multimodal Memory
- Hierarchical Memory
- Egocentric Perception
- Personal Agent
- Wearable AI
one_liner: 提出可部署于手机、AI眼镜的三级分层多模态流记忆系统，支持多场景日常记忆查询
practical_value: '- 个人助理类Agent可直接复用三级分层记忆架构：当前/短期/长期记忆拆分+查询动态路由，降低检索延迟、提升响应效率，适配移动端/可穿戴设备的低算力场景

  - 多模态流处理的事件分段方案可迁移到用户行为序列建模：基于时序连续性+跨帧变化信号做轻量分段，无需逐帧语义解析，降低长序列处理开销

  - 电商全渠道用户行为记忆可参考该框架：将浏览、下单、线下到店等多模态行为按时间线对齐分层存储，支持跨时段行为召回、消费习惯挖掘，提升个性化推荐精准度

  - 记忆路由逻辑可复用在RAG系统中：根据查询的时间范围、语义意图自动选择检索源，避免全量检索的冗余开销，提升RAG响应速度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前移动端、可穿戴设备的个人AI助理仅能处理单轮即时查询，无法对用户日常产生的连续视觉、音频多模态流做长期记忆管理，无法支撑物品查找、对话回忆、生活总结、规律挖掘等跨时间维度的记忆类查询，现有系统要么仅支持文本记忆、要么仅能处理即时感知，缺乏统一的分层多模态记忆架构适配端侧部署。

### 方法关键点
- 多模态流捕获层：端侧仅做轻量采样、压缩、时间戳对齐，将视觉帧、音频chunk同步上传后端，统一对齐到共享时间线
- 事件分段：基于时序连续性和跨帧变化信号对连续流做增量微事件拆分，异步补充ASR、图像描述等语义信息，作为记忆基本单元
- 三级分层记忆架构：分为当前记忆（滚动缓存实时上下文，支持即时查询）、短期记忆（存储近期微事件完整信息）、长期记忆（固化为episodic事件记忆和semantic规律/偏好记忆两类）
- 查询路由：根据查询的时间范围、语义意图自动选择对应的记忆层检索，融合证据后生成可溯源的回答

### 关键结果
在物品查找、对话回忆、生活总结三类日常场景测试，对比无分层多模态记忆的基线：整体检索Recall@3达74.1%，MRR达0.627；整体QA LLM评估准确率51.9%，人工评估准确率55.6%，生活总结场景准确率最高达77.8%；短期记忆查询P50端到端延迟手机端5.86s、眼镜端7.01s，可满足近实时交互需求。

### 核心结论
个人AI助手的核心能力正在从单轮语言理解转向长期生活经验的捕获、组织与召回，分层多模态记忆是端侧个人Agent落地的核心基础组件。
