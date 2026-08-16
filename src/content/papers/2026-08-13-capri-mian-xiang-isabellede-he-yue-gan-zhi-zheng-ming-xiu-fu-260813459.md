---
title: 'CAPRI: Contract-Aware Proof Repair for Isabelle'
title_zh: CAPRI：面向Isabelle的合约感知证明修复系统
authors:
- Jim Woodcock
- Gabriel Leite
- Augusto Sampaio
- Ran Wei
affiliations:
- Southwest University, China
- Aarhus University, Denmark
- University of York, UK
- Universidade Federal de Pernambuco (UFPE), Brazil
- University of Lancaster, UK
arxiv_id: '2608.13459'
url: https://arxiv.org/abs/2608.13459
pdf_url: https://arxiv.org/pdf/2608.13459
published: '2026-08-13'
collected: '2026-08-16'
category: LLM
direction: LLM辅助形式化证明安全修复
tags:
- LLM
- Formal Proof
- Contract Enforcement
- Repair Workflow
- Audit Trail
one_liner: 提出带编辑合约校验的LLM辅助Isabelle证明修复工作流，避免非授权修改且留存全链路审计轨迹
practical_value: '- LLM生成内容后叠加独立权限校验层的架构可复用在营销文案、商品标题生成场景，禁止修改预设合规保护字段

  - 全链路留存prompt、生成结果、校验日志、哈希值的方案可迁移到大模型生成内容的合规追溯链路

  - 限制LLM仅可编辑指定区域的设计可降低生成内容违规率，可复用在Agent调用工具的权限管控场景'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM辅助Isabelle证明生成流程仅验证证明正确性，无法约束LLM仅修改开发者授权范围的内容，存在非预期篡改风险，且缺乏全链路审计能力。
### 方法关键点
1. 设计CAPRI双层校验工作流：先由Isabelle验证证明正确性，再由独立校验器执行机器可读的编辑合约，确保仅允许修改指定区域；
2. 全流程留存prompt、生成候选、诊断信息、校验结果、哈希值，支持完整审计追溯；
3. 对比5种不同配置的修复工作流，包括单轮生成、迭代全理论编辑、仅允许修改证明体、带匹配示例prompt等。
### 关键结果数字
180次实验共得到138次有效修复；仅允许修改证明体的方案实现29/36的有效修复率且0合约违规，带匹配示例的Sol配置修复率达33/36，仅比全理论编辑方案低2pp且无违规；迭代修复方案修复率最高达32/36，显著高于单轮修复的22/36。
