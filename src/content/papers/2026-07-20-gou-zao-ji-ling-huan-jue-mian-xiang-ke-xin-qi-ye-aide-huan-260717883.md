---
title: 'Zero Hallucination, by Construction: Hallucination-Aware Layered Oversight
  for Trustworthy Enterprise AI'
title_zh: 构造级零幻觉：面向可信企业AI的幻觉感知分层监督架构HALO
authors:
- Bogdan Raduta
- Horia Velicu
- Alexandru Preda
- Serban Chiricescu
affiliations:
- FlowX.AI
arxiv_id: '2607.17883'
url: https://arxiv.org/abs/2607.17883
pdf_url: https://arxiv.org/pdf/2607.17883
published: '2026-07-20'
collected: '2026-07-21'
category: LLM
direction: LLM可信治理 · 分层幻觉遏制架构
tags:
- Hallucination Containment
- RAG
- LLM-as-Judge
- Drift Detection
- Agent Trustworthy
one_liner: 提出六层防御的HALO架构，将幻觉视为可遏制故障，实现企业级AI零幻觉输出保障
practical_value: '- 落地电商客服、商品属性抽取、广告文案合规类Agent/RAG系统时，放弃单一层幻觉检测思路，采用纵深防御架构，将幻觉逃逸率降低为各层漏检率乘积，大幅降低资损/合规风险

  - 替换LLM自报告置信度为证据锚定校验：对抽取的结构化字段（如商品价格、订单金额）做原文精确/模糊匹配、跨字段逻辑校验，可大幅降低高置信度幻觉漏判

  - 上线后的Agent需配置持续监控闭环：基于多维度质量指标做漂移检测，触发阈值后自动生成候选修复方案，经离线golden数据集验证、线上灰度放量后全量上线，规避大模型迭代/输入分布偏移风险'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前企业级AI落地核心障碍是LLM幻觉，单靠模型迭代、RAG+单层幻觉法官的方案无法根除幻觉：95%准确率的检测器在企业级吞吐量下每月仍会产生数千漏检，且LLM自报告置信度校准度极低，高置信度输出也可能是幻觉，极易引发合规、资损等严重事故。
### 方法关键点
提出HALO六层纵深防御架构：
1. **Grounded Generation**：混合BM25+稠密向量检索+交叉编码器重排的两级检索，仅从核准知识库生成答案；
2. **Constrained Execution**：Agent工作流运行在确定性状态机上，限制工具/模型调用次数、做PII脱敏，缩小故障爆炸半径；
3. **多信号校验**：融合LLM-as-judge接地性打分+非LLM的证据校验（原文匹配、跨字段逻辑校验如金额求和、日期先后校验等），打破生成器与法官的偏差相关性；
4. **校准弃权**：证据不足时直接拒绝回答或转人工，而非强行生成；
5. **全链路可追溯**：基于OpenTelemetry记录所有检索、工具调用、生成步骤，满足合规审计要求；
6. **持续监督**：9维质量指标漂移检测，触发阈值后自动启动修复闭环，经离线验证、线上灰度后上线。
### 关键结果
在保险理赔抽取场景验证：初始版本幻觉率0.28、正确率0.72，经HALO修复后幻觉率降至0.08，正确率提升至0.88，所有未通过校验的幻觉输出100%被拦截，未流入下游系统。
### 核心结论
零幻觉不是模型的固有属性，而是系统层面可强制执行的保障能力
