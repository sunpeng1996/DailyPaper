---
title: 'GS-Agent: Creating 4D Physical Worlds With Generative Simulation'
title_zh: GS-Agent：基于生成式仿真构建4D物理世界
authors:
- Hongxin Zhang
- Chunru Lin
- Junyan Li
- Zhou Xian
- Tsun-Hsuan Wang
- Chuang Gan
affiliations:
- University of Massachusetts Amherst
- Genesis AI
arxiv_id: '2607.21522'
url: https://arxiv.org/abs/2607.21522
pdf_url: https://arxiv.org/pdf/2607.21522
published: '2026-07-23'
collected: '2026-07-25'
category: MultiAgent
direction: 多智体协作 · 文本生成4D物理场景
tags:
- MultiAgent
- Generative Simulation
- Text-to-4D
- Physics Engine
- Content Generation
one_liner: 提出融合物理引擎的多Agent框架GS-Agent，实现文本到可控物理可信4D世界的端到端生成
practical_value: '- 多Agent分专业协作的架构可直接复用，电商商品3D/短视频营销素材生成可拆为选品、场景配置、渲染等子Agent，降低复杂任务实现难度

  - 工具调用+反馈迭代的流程可借鉴，在生成类任务中接入领域引擎（如渲染引擎、合规规则引擎）的输出做迭代优化，提升结果真实性与合规性

  - 复杂生成任务的分层拆解思路可迁移，例如虚拟直播间搭建、商品动态展示任务，可参考拆为实体管理、渲染配置两大模块并行优化'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统4D物理世界依赖人工制作，需耗费大量精力调优材质、动作、视觉效果，效率极低；现有大模型生成方案无法保证物理合理性与可控性，输出效果难以落地。
### 方法关键点
端到端多Agent框架GS-Agent模拟人类制作4D世界的流程，将任务拆分为两大模块：1）实体管理，覆盖3D资产筛选、材质调优、摆放、运动控制；2）渲染配置，包含相机、灯光设置。多个具备专业能力的Agent通过代码调用物理引擎，获取多模态反馈后迭代协作，输出对齐文本描述的结果。
### 关键结果
可稳定生成包含液体、可变形物体、刚体间丰富交互的物理可信4D场景，同时实现电影级相机与灯光控制，覆盖多类文本输入需求
