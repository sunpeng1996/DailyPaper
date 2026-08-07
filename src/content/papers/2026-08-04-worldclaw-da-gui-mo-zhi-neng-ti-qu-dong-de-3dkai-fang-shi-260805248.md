---
title: 'WorldClaw: Agentic 3D Open-World Generation at Scale'
title_zh: WorldClaw：大规模智能体驱动的3D开放世界生成
authors:
- Chunchao Guo
- Jinpeng Li
- Yang Li
- Zilong Huang
affiliations:
- Tencent Hunyuan
arxiv_id: '2608.05248'
url: https://arxiv.org/abs/2608.05248
pdf_url: https://arxiv.org/pdf/2608.05248
published: '2026-08-04'
collected: '2026-08-07'
category: Agent
direction: Agent 3D开放世界内容生成
tags:
- Agent
- 3D Generation
- Open-World Generation
- Procedural Content Generation
- Scene Editing
one_liner: 提出全Agent驱动的粗到细框架，支持文本生成大规模可编辑连贯3D开放世界
practical_value: '- 粗到细分层Agent规划框架可复用：复杂生成任务（如电商3D数字场景、虚拟直播间搭建）可拆分「全局规划→局部生成→细节迭代」的Agent流水线，降低全局一致性维护成本

  - 结构化布局+可复用资产结合的生成思路：电商虚拟场景生成可先输出语义布局再绑定资产库资源，兼顾生成灵活性和落地效率，减少重复生成开销

  - 渲染反馈的Agent自迭代机制：生成式内容生产链路可接入渲染侧结果做自动修正，无需人工标注即可优化生成内容的贴合度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
文本生成大规模可探索3D开放世界需同时满足全局空间一致性、局部内容丰富度、资产可编辑复用性三大要求，现有方案难以兼顾。
### 方法关键点
1. 采用全Agent驱动的粗到细生成框架，规划Agent先将文本prompt转化为区域、地形、资产、材质、空间关系的结构化规范；
2. 基于语义布局、可复用资产、生成/程序化材质、区域感知高度场搭建全局一致的地形基底；
3. 高细节需求区域先生成地形条件约束的组合内容，重建可编辑带纹理网格并匹配地形位置，再通过渲染驱动Agent进一步优化地形、物体、外观与接触关系。
### 关键结果
跨多样开放世界prompt测试，生成的大规模场景同时满足全局地形结构一致、空间组织连贯、局部内容视觉效果达标，且所有实例级资产均支持下游编辑。
