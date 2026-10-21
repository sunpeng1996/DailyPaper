---
title: 'S-Agent 2.0: Spatial Reasoning with a General Coding Agent'
title_zh: S-Agent 2.0：基于通用编码Agent的空间推理框架
authors:
- Rui Gong
- Ruoyu Wang
- Yalun Dai
- Hao Li
- Sidi Yang
- Qihao Zhao
- Hongyu Li
- Zeyang Guan
- Fangzhou Hong
- Zhaoxi Chen
affiliations:
- Nanyang Technological University
- University of Hong Kong
arxiv_id: '2610.28354'
url: https://arxiv.org/abs/2610.28354
pdf_url: https://arxiv.org/pdf/2610.28354
published: '2026-10-19'
collected: '2026-10-21'
category: Agent
direction: 空间推理Agent · 证据闭环设计
tags:
- Spatial Reasoning
- Coding Agent
- Tool Use
- Scene Memory
- VLM
one_liner: 搭配命令行感知工具包构建空间推理证据闭环，性能超越现有SOTA Agent系统
practical_value: '- 可复用「工具返回结果自带业务语义解释」的设计：比如在导购Agent、商品召回场景中，工具返回的商品不仅输出ID，同时附带「凑单满减」「用户常购同品类」「符合本次搜索需求」等语义标签，大幅降低LLM理解和整合信息的误差

  - 持久化场景内存的设计可迁移至多轮会话推荐系统：将用户历史交互、偏好、上下文实体存储在独立的内存模块，按实体名查询调用，无需每次都从上下文窗口提取信息，既减少Token消耗，也避免长上下文下的信息丢失

  - 「语义决策+精确测量」的分工感知思路可迁移至多模态导购场景：LLM负责理解用户需求的语义，确定需要检索/识别的商品属性，调用专用的图像检索、属性识别工具获取精确结果，再组合生成回答，兼顾语义理解的灵活性和测量的准确性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有工具增强型空间推理Agent仅聚焦感知工具的丰富度，缺失证据存储、语义解释环节的系统设计，即使工具返回正确测量结果，模型仍易出现读错坐标系、丢弃有效证据、回归自身幻觉感知等错误，最终输出错误结论。
### 方法关键点
- 基于通用编码Agent（兼容OpenHands、Codex、Claude Code等多种主流harness）构建，无需微调VLM backbone，额外扩展CLI感知工具包+逐轮持久化场景内存两大模块
- 感知能力按分工拆分：LLM负责语义决策（确定要测量的实体、关系），专用模型负责精确测量（重建、分割、几何计算）；同时支持LLM向场景内存注入自定义实体（如问题要求的虚拟观察者）、删除工具识别错误的实例，两种感知结果共享同一几何坐标系
- 工具返回结果同时输出数值与自然语言语义解释，直接匹配问题使用的空间描述词汇，避免模型理解数值时出现偏差
- 场景内存由环境维护，存储场景点云、实体属性、6DoF位姿等信息，后续查询直接通过实体名调用，无需重复感知或在上下文窗口中携带中间结果，降低Token消耗与信息丢失风险
### 关键结果
在MMSI-Bench、ReVSI等5个空间推理基准测试：
1. Qwen3.8-27B backbone下，MMSI-Bench准确率达66.5%，较SOTA SpatialClaw高3.9pp；ReVSI得分82.3%，较SpatialClaw高7.8pp
2. Gemini-3.8-Flash backbone下，MMSI-Bench准确率达74.1%，较SpatialClaw高7.1pp；ReVSI得分90.5%，较SpatialClaw高10.8pp
3. 工具增益在强backbone下仍保持稳定，而SpatialClaw的工具增益随backbone能力提升大幅衰减

> 最值得记住的一句话：工具增强Agent的核心不是堆砌工具数量，而是要构建从证据采集、存储到语义解释的全链路闭环，减少模型在中间环节的信息损耗与幻觉。
