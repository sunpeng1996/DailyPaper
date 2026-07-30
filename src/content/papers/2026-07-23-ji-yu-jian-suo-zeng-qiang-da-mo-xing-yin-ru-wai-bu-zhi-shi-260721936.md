---
title: Leveraging External Knowledge for Historical Document Restoration via Retrieval-Augmented
  Large Language Models
title_zh: 基于检索增强大模型引入外部知识的历史文档修复方法
authors:
- Gabeen Kim
- Kyeongpil Kang
affiliations:
- Kangwon National University
arxiv_id: '2607.21936'
url: https://arxiv.org/abs/2607.21936
pdf_url: https://arxiv.org/pdf/2607.21936
published: '2026-07-23'
collected: '2026-07-30'
category: RAG
direction: RAG增强大模型 · 垂直领域知识补全
tags:
- RAG
- LLM
- Knowledge Retrieval
- Domain Application
- Text Restoration
one_liner: 提出融合RAG与LLM的历史文档修复框架ARI，大幅提升普通字符与专有命名实体修复精度
practical_value: '- 电商商品标题纠错、残缺用户评论补全等垂直领域文本处理场景，可复用「LLM隐式知识+RAG外部显式领域知识」框架，解决小众商品名、专业术语等专有名词识别补全难题

  - 可迁移该思路优化QueryRec场景下的残缺query补全、拼写纠错能力，引入商品库/历史高转化query库的检索结果提升改写准确率

  - 涉及专有名词生成的GenRec场景，可参考该方法补充外部检索模块，有效降低LLM生成商品名、品牌名等专有名词的幻觉率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
历史文档因物理损毁常出现内容模糊难以识别的问题，传统基于掩码语言模型的修复方法仅能利用局部上下文，无法解决需要外部历史知识支撑的命名实体修复难题。

### 方法关键点
提出名为ARI的历史文档修复框架，基于RAG架构融合预训练LLM的内部隐式知识与检索得到的外部历史领域显式上下文，针对性解决上下文依赖专有名词的推断问题。

### 关键结果
在韩语历史文档数据集上显著优于所有基线，普通字符、命名实体两类修复任务均实现大幅性能提升，经专家评估确认可作为实用工具提升历史记录分析效率。
