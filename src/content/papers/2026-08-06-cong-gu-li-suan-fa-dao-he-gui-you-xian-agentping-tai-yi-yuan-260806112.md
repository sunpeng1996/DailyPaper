---
title: 'From Siloed Algorithms to Compliance-First Agentic Platforms: A Multi-Layered
  Architecture for Hospital AI Systems'
title_zh: 从孤立算法到合规优先Agent平台：医院AI系统多层架构
authors:
- Manideep Dhar
- Ritwik Singh
- Sharat Chandra Kumar Manikonda
affiliations:
- Instil-IT, Hyderabad, Telangana
arxiv_id: '2608.06112'
url: https://arxiv.org/abs/2608.06112
pdf_url: https://arxiv.org/pdf/2608.06112
published: '2026-08-06'
collected: '2026-08-09'
category: Agent
direction: Agent 医疗场景合规架构设计
tags:
- Multi-Agent System
- Agent Orchestration
- Compliance-first AI
- Privacy Preserving
- Policy-as-code
one_liner: 提出面向医院的合规优先多Agent三层可互操作架构，破解医疗AI试点落地率低痛点
practical_value: '- 可复用「合规层+编排层+数据层」的三层Agent平台架构，适配电商跨部门业务Agent协同、用户数据合规管控需求

  - policy-as-code集中管控思路可直接迁移到电商推荐的广告合规、用户隐私保护、内容审核等规则落地场景

  - 隐私计算技术对接现有业务系统的落地方案，可复用在跨域用户特征共享、跨商家联合建模等业务场景'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
医疗场景AI部署多为部门级孤立点方案，70%-80%医疗AI试点无法规模化落地，核心痛点为治理缺失、数据碎片化、无统一集成蓝图。
### 方法关键点
设计三层可互操作的医院专属合规优先Agent架构：
1. Agent Orchestration Layer：支持跨临床、运营、财务域的多Agent工作流调度
2. Compliance and Policy Layer：集中式policy-as-code落地HIPAA、GDPR、欧盟AI法案等全球主流监管标准
3. Privacy-Preserving Data Fabric：将federated learning、differential privacy、secure enclaves能力直接接入现有医院信息管理系统流程
### 关键结果
基于结构真实的合成医院数据集验证，可实现任务周转时间、人工文档工作量的显著下降，全程满足政策管控的数据访问要求，适配本地、混合、云原生多种部署模式
