---
title: 'NS-ST-GraphRAG: Neuro-Symbolic Spatio-Temporal GraphRAG for Literary Knowledge
  Processing'
title_zh: NS-ST-GraphRAG：面向文学知识处理的神经符号时空GraphRAG
authors:
- Zheng Kui Lin
affiliations:
- 大连海洋大学港口大数据与智能应用联合实验室
arxiv_id: '2609.05139'
url: https://arxiv.org/abs/2609.05139
pdf_url: https://arxiv.org/pdf/2609.05139
published: '2026-09-04'
collected: '2026-09-07'
category: RAG
direction: RAG优化 · 时空知识图谱 神经符号推理
tags:
- GraphRAG
- Spatio-Temporal KG
- Neuro-Symbolic Reasoning
- Hallucination Mitigation
- Multi-hop QA
one_liner: 提出融合本体约束、双时间坐标、动态子图检索的神经符号时空GraphRAG，配套首个古典中文文学多跳QA基准
practical_value: '- 做涉及时序/空间约束的RAG系统时，可复用双时间坐标设计：粗粒度索引+细粒度事件区间，解决跨段时序信息对齐问题，适用于电商用户行为时序、商品上下架状态的RAG检索场景

  - LLM抽取结构化信息时，可引入领域本体的神经符号约束层，对抽取三元组做规则校验+有限次局部修复，能显著降低幻觉，适合电商商品属性、用户标签的结构化抽取场景

  - 多跳QA/Agent回答效果评估可复用双轨校验协议：机械答案匹配+独立语义校验+引用忠实度检查，平衡评估的严格性和合理性，可用于电商导购Agent、客服Agent的回答效果评估'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长叙事文本的RAG处理存在三类核心痛点：一是关键证据跨章节分布，普通分块向量检索无法对齐时序、空间约束；二是现有GraphRAG采用静态图谱结构，未存储关系的有效时间区间，无法匹配叙事过程中的状态演变；三是无约束LLM抽取三元组易产生违反领域逻辑的幻觉，且古典中文文学领域缺乏公开的多跳QA基准做效果对齐。
### 方法关键点
- 神经符号约束层：基于领域本体的硬规则（亲属一致性、主仆互斥、头衔性别匹配）+软规则校验抽取三元组，硬规则违规的三元组触发最多R_max次局部重抽取，无法修复的排除出图谱
- 时空图谱建模：采用双时间坐标系统，粗粒度为章节索引，细粒度为叙事时间事件区间，同时给实体/关系标注空间场景属性，按时间版本存储图谱切片
- 动态子图检索：从Query中解析时间、空间约束，直接索引匹配对应图谱切片，保留多跳推理路径后送入LLM生成带溯源证据的答案
- 构建Red-Chamber-QA，是首个公开的古典中文文学多跳QA基准，含104题预发布集+120题留存集，覆盖时间约束、空间约束、通用三类问题
### 关键结果
在Red-Chamber-QA留存集上，NS-ST-GraphRAG的机械答案复现率达0.733，优于固定窗口基线的0.675和闭卷模型的0.083；语义评估准确率达0.866，略优于基线的0.850。
### 核心结论
对于强逻辑、带时序/空间约束的知识处理场景，神经符号约束+结构化时空索引的RAG架构，能在几乎不损失语义准确率的前提下，显著提升答案的可溯源性与幻觉抑制能力。
