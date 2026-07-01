---
title: 'DEEPMED Search: An Open-Source Agentic Platform for Medical Deep Research
  with Introspective Verification'
title_zh: DEEPMED Search：带自省验证的开源医疗深度研究智能体平台
authors:
- Maolin Liu
- Fanyu Xu
- Ruoqing Xu
- Jiahang Zhang
- Hao Wang
- Rui Wang
affiliations:
- School of Computer Science and Software Engineering, Shanghai University
- Department of Computer Science and Engineering, Shanghai Jiao Tong University
arxiv_id: '2606.29746'
url: https://arxiv.org/abs/2606.29746
pdf_url: https://arxiv.org/pdf/2606.29746
published: '2026-06-29'
collected: '2026-06-30'
category: Agent
direction: Agent 医疗检索智能体平台构建
tags:
- Agent
- RAG
- MultiAgent
- Verification
- Information Retrieval
- Open Source
one_liner: 开源面向医疗深度研究的智能体平台，融合多源路由与多智能体自省验证解决RAG推理漂移问题
practical_value: '- 多源自适应路由设计可直接复用：电商搜索/推荐场景中，可根据query属性自适应分发到商品库、用户行为库、公域资讯库等不同数据源，降低无效召回，提升检索效率

  - 多智能体自省验证框架可迁移：生成式推荐的商品文案生成、营销内容合规校验场景，通过多智能体辩论对齐业务规则，大幅减少生成内容的错误漂移

  - 异构数据结构化输出逻辑可借鉴：电商用户画像构建、行业研报自动生成场景，可复用其多源数据整合+溯源能力，输出可解释的结构化结果'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
异构医疗数据（学术文献、临床指南、私域知识库）的检索整合是循证医学落地的核心瓶颈，现有商用黑盒检索工具透明度不足，通用开源RAG方案处理复杂长尾query时普遍存在推理漂移问题。
### 方法关键点
1. 基于高性能Next.js架构搭建全开源智能体检索平台；
2. 搭载源自适应路由器，根据信息密度自动将拆解后的子query分发到PubMed、公域网页搜索、本地图知识库三类适配数据源；
3. 集成因果一致的多智能体辩论驱动的自省验证模块，结果合成前先校验检索证据与诊断逻辑的一致性。
### 关键结果
可自主拆解高难度罕见病query，过滤干扰噪声，数分钟内生成带引用支撑的结构化研究报告，平台完全开源开放。
