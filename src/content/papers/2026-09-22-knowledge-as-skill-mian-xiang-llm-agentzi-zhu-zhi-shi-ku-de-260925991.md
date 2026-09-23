---
title: 'Knowledge-as-Skill: A Structural Design for Autonomous Knowledge-Base Use
  by LLM Agents'
title_zh: Knowledge-as-Skill：面向LLM Agent自主知识库调用的结构化设计
authors:
- Jiangxu Wu
affiliations:
- 中山大学
arxiv_id: '2609.25991'
url: https://arxiv.org/abs/2609.25991
pdf_url: https://arxiv.org/pdf/2609.25991
published: '2026-09-22'
collected: '2026-09-23'
category: Agent
direction: Agent 知识库自主调用架构设计
tags:
- LLM Agent
- RAG
- Knowledge Base
- Skill Protocol
- Agentic Retrieval
one_liner: 提出三层结构化知识库组织方案，让LLM Agent可自主发现、导航、调用外部知识替代固定RAG流程
practical_value: '- 电商客服/商品/活动规则知识库可复用三层结构：加SKILL.md入口标注适用场景、每层目录配带语义描述的index.md、每个知识点加来源/有效期元数据，减少无效RAG召回的无关内容干扰

  - 可复用异构知识转结构化pipeline：自动将商品说明书、售后规则、活动通知等PDF/Word/网页内容转成带元数据的Markdown结构，降低Agent调用知识库的开发成本

  - 事实性要求高的场景（如客服应答、活动规则咨询）优先采用该分层导航方案，实测Factuality提升12.2pct、Context Recall提升10.8pct，大幅降低回答错误率

  - 可与现有RAG混合部署：高频简单问题用传统RAG快速返回，复杂多跳问题用分层导航结构，平衡latency和准确率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统固定RAG的「检索-拼接-生成」流程由系统强制触发检索，不管问题是否需要外部知识，也不允许LLM自主决定检索内容；当Agent工具调用能力成熟后，新的瓶颈是Agent不知道知识库包含什么内容，传统知识库返回的是无上下文的匿名文本块，缺乏范围、来源、关联信息，Agent无法自主判断内容价值，也无法分层探索。
### 方法关键点
- 三层分层曝光架构：①发现层：根目录放置SKILL.md，元数据标注知识库适用范围、触发条件、边界、导航规则、停止条件，Agent仅在任务匹配时才读取完整内容；②导航层：每个目录配index.md，每条条目是带一句话语义描述的文件链接，Agent可逐层缩小检索范围，替代单一的关键词/向量检索入口；③知识层：每个文档开头带YAML frontmatter，标注类型、标题、描述、标签、来源、生成/校验时间、过期时间，Agent可先读元数据判断相关性，再决定是否读全文。
- 配套自动化构建pipeline：支持将PDF、Word、网页、笔记等异构内容自动转换为符合OKF规范和Skill协议的上述结构，支持增量更新。
### 关键实验
在WixQA企业客服基准的200条专家标注测试集上，和同期的Corpus2Skill方案做方向性对比：Factuality 0.889（相对提升12.2个百分点），Context Recall 0.816（相对提升10.8个百分点），Hallucination Rate均为4.5%；但平均交互轮次达4.015（比Corpus2Skill多1.635轮），Context Precision、Faithfulness略低。
### 核心结论
当Agent负责自主决定读取什么知识时，知识库应该暴露结构、标识、来源信息，而不是只提供匿名的可检索块。
