---
title: Automatic Model Card Generation Using an LLM
title_zh: 基于大语言模型的模型卡片自动生成方法
authors:
- Tajkia Rahman Toma
- Balreet Grewal
- Cor-Paul Bezemer
affiliations:
- University of Alberta, Canada
arxiv_id: '2608.24807'
url: https://arxiv.org/abs/2608.24807
pdf_url: https://arxiv.org/pdf/2608.24807
published: '2026-08-25'
collected: '2026-08-26'
category: LLM
direction: LLM自动化结构化文档生成
tags:
- LLM
- Model Card
- Automatic Documentation
- Information Extraction
- Standardization
one_liner: MCTidy与MCGenie两款LLM工具，实现模型卡自动规整与从仓库数据自动生成
practical_value: '- 团队内部算法模型文档标准化可复用MCTidy思路，用LLM将零散的模型说明自动对齐统一模板，降低跨团队沟通成本

  - 算法资产库建设可参考MCGenie框架，直接从Git仓库、实验报告、关联论文等多源数据自动生成模型卡片，减少人工录入成本

  - 结构化文档自动生成场景可复用其评估维度：信息留存率、语义相似度、事实正确性、幻觉发生率，快速验证生成效果'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前ML模型配套模型卡普遍结构不统一，大量模型无公开模型卡，导致模型对比、解读难度高，人工编写标准化模型卡成本高，无法规模化落地
### 方法关键点
1. MCTidy：基于LLM将现有非标准化模型卡自动重组为统一模板，提升可读性与跨模型可比性
2. MCGenie：基于LLM直接从模型仓库多源数据自动生成标准化模型卡
### 关键结果
MCTidy在48个Hugging Face模型卡测试中信息留存率高、章节对齐准确、幻觉极少，多轮运行稳定性强；MCGenie生成的模型卡平均语义相似度达0.9，超50%完全正确，剩余错误多为微小失误，生成质量高度依赖配套资源尤其是关联论文
