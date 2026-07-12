---
title: 'Simulating the Resident: Generating Executable Smart Home Schedules via LLM
  Personas'
title_zh: 基于LLM用户画像生成可执行的智能家居交互日程
authors:
- Victor Jüttner
- Xenia Wagner
- Christoph Jahn
- Erik Buchmann
affiliations:
- Leipzig University
- ScaDS.AI Dresden/Leipzig
- ipoque GmbH (Rohde & Schwarz)
arxiv_id: '2607.08231'
url: https://arxiv.org/abs/2607.08231
pdf_url: https://arxiv.org/pdf/2607.08231
published: '2026-07-09'
collected: '2026-07-12'
category: LLM
direction: LLM用户画像 · 行为序列生成
tags:
- LLM
- Persona
- Smart Home
- Behavior Simulation
- Synthetic Data Generation
one_liner: 通过多维度家庭配置框架与多阶段LLM pipeline生成可执行智能家居交互日程，规避真实数据采集的隐私与成本问题
practical_value: '- 多维度用户画像配置框架可复用：在生成电商/推荐场景虚拟用户行为数据时，可参考其社会技术维度拆分用户属性，生成更贴合真实分布的虚拟用户

  - 多阶段LLM生成结构化可执行序列的pipeline可迁移：生成虚拟用户浏览、加购、下单行为序列时，可分阶段约束输出格式，解决直接生成结构化程度低、不符合业务逻辑的问题

  - 隐私合规场景下模拟数据生成思路可参考：无法采集真实用户行为数据时，可通过LLM persona生成模拟数据用于模型训练、AB测试前置验证，规避隐私风险'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
智能家居HCI、安全隐私研究依赖真实家庭的设备交互、网络流量、日常行为数据集，但真实采集需长期监测用户私密空间，周期长、成本高，且存在严重隐私风险，难以规模化落地。
### 方法关键点
1. 提出覆盖5个社会技术维度的模拟家庭配置框架，支持生成多样化、差异化的居民与家庭画像
2. 设计多阶段LLM生成pipeline，输出结构化、可直接在物理测试床执行的设备交互日程
3. 完成可行性验证POC，验证方案落地可能性
### 关键结果
当前为在研项目，可实现无侵入式数据采集的可扩展、隐私友好的智能家居实验支撑，完全无需依赖真实用户数据采集，解决了领域数据获取的核心痛点。
