---
title: 'REAP: Relation-Aware Elicitation and Parsing for Closed-Book Knowledge Base
  Construction from LLMs'
title_zh: REAP：闭书场景下从大模型提取知识构建KB的关系感知方法
authors:
- Thanh-Dan Bui
- Thanh-Trung Do
- Tuan-Phong Nguyen
affiliations:
- VNU University of Engineering and Technology, Hanoi, Vietnam
arxiv_id: '2608.10963'
url: https://arxiv.org/abs/2608.10963
pdf_url: https://arxiv.org/pdf/2608.10963
published: '2026-08-11'
collected: '2026-08-12'
category: LLM
direction: LLM参数知识提取 · 闭书知识库构建
tags:
- LLM
- Knowledge Base Construction
- Chain-of-Thought
- Closed-book
- Prompt Engineering
one_liner: 无需微调32B以下LLM，结合关系专属策略与结构化CoT实现闭书KB构建
practical_value: '- 针对商品属性、品牌关联等不同关系可设计专属查询Prompt，无需微调LLM即可提升结构化知识抽取准确率

  - 推理驱动的空集门控可直接复用，避免LLM生成不存在的关联关系，适配商品属性补全、电商KG构建场景

  - 结构化CoT+直接输出合法JSON的范式，可降低Agent知识抽取链路的后处理成本，提升落地效率'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
闭书无RAG、无模型微调、最高可用32B参数的约束下，从LLM参数中提取知识构建KB时，同一主体-关系对可能对应空值、单值或多值结果，传统事实探测方法准确率不足，难以直接输出结构化结果。
### 方法关键点
1. 采用结构化Chain-of-Thought推理，搭配关系专属查询策略，适配不同类型关系的知识提取逻辑；
2. 新增推理驱动的空集判断门控，提前识别无对应结果的主体-关系对，减少幻觉输出；
3. 直接引导LLM输出合法JSON数组，省去复杂后处理流程。
### 关键结果
基于Mistral-Small-24B-Instruct-2501实现，测试集macro-F1达0.62，其中国家边界关系F1=0.95、公司上市交易所关系F1=0.73、面积属性F1=0.77。
