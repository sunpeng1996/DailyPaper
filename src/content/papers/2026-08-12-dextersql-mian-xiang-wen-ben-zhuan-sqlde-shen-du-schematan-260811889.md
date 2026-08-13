---
title: 'DexterSQL: Deep Schema Exploration and Rule-based Correction for Text-to-SQL
  Generation'
title_zh: DexterSQL：面向文本转SQL的深度Schema探索与规则校正
authors:
- Anik Pramanik
- Murat Kantarcioglu
- Vincent Oria
- Shantanu Sharma
affiliations:
- New Jersey Institute of Technology
- Virginia Tech
arxiv_id: '2608.11889'
url: https://arxiv.org/abs/2608.11889
pdf_url: https://arxiv.org/pdf/2608.11889
published: '2026-08-12'
collected: '2026-08-13'
category: LLM
direction: 大模型Text-to-SQL生成优化
tags:
- Text-to-SQL
- Prompt Engineering
- Schema Parsing
- Rule-based Correction
- LLM Application
one_liner: 提出免微调Text-to-SQL框架DexterSQL，通过三大组件提升跨模型SQL生成准确率
practical_value: '- 电商智能导购/运营自助查询场景下，可复用深度Schema探索模块，提前分析库表字段分布区分歧义列，降低SQL生成的字段匹配错误

  - 可借鉴跨库通用校正规则挖掘思路，从历史生成错误中提取与数据源无关的修正规则，无需微调即可降低LLM的重复错误率

  - 处理复杂用户查询转结构化检索的场景（如多条件商品检索转ES查询/SQL），可参考依赖树语义分解方法，先搭查询骨架再补全条件，减少条件遗漏、幻觉问题'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有免微调Text-to-SQL方案存在三大痛点：依赖粗粒度Schema信息无法区分歧义列、未捕获重复出现的SQL生成错误、复杂查询下易出现条件遗漏/幻觉/错位。
### 方法关键点
提出DexterSQL免微调框架，包含三大核心组件：
1. 深度Schema探索器：识别歧义列，分析单字段与联合字段的数据分布，挖掘字段间关联与各自作用
2. 跨库通用规则生成器：仅在训练库上挖掘生成SQL与标注SQL的错配，转化为与库无关的校正规则，捕获LLM重复错误模式
3. 多路径SQL生成：引入基于依赖树的中间表示，根据问句结构拆解为SQL骨架后生成最终语句
### 关键结果
在BIRD-Dev数据集上，开源模型GPT-OSS-120B准确率提升至少2.7%，达67.6%；闭源模型GPT-4o、GPT-5.2准确率分别提升至少0.9%，达71.6%、72.2%，整体效果优于现有SOTA
