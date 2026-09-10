---
title: 'Measuring GEO Visibility: Prompt Corpora Define the Answer Market'
title_zh: GEO可见度度量：提示语语料定义生成式搜索答案市场
authors:
- Olivier Martinez
affiliations:
- Sciences Po
arxiv_id: '2609.06811'
url: https://arxiv.org/abs/2609.06811
pdf_url: https://arxiv.org/pdf/2609.06811
published: '2026-09-06'
collected: '2026-09-10'
category: Eval
direction: GEO评估 · 生成式搜索可见度度量
tags:
- GEO
- Visibility Measurement
- Prompt Corpus
- Generative Search
- Evaluation Framework
one_liner: 提出GEO可见度度量框架，明确提示语、权重、评分规则对评估结果的影响
practical_value: '- 开展GEO品牌投放效果评估时，需固定prompt语料库、权重规则、LLM评分prompt，避免规则变动引发的结果误判

  - 生成式搜索场景下的品牌排名对比可复用部分识别方法，区分数据兼容的有效分数区间与权重带来的偏差，避免单一权重下的错误排序

  - 度量品牌/内容来源对生成回答的贡献时，可采用控制变量法：对比同一上下文下有无该来源的生成回答差异，排除竞争来源干扰'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有GEO可见度评分依赖人工选择的prompt语料与权重，无法真实匹配用户需求，且prompt措辞、LLM评分规则都会干扰最终得分，缺乏标准化的可信评估框架。
### 方法关键点
1. 引入总调查误差、信息检索评估领域的成熟研究，构建GEO可见度度量框架，明确覆盖场景标注、prompt构造、执行条件、权重、评分规则五大核心变量；
2. 提出部分识别方法，区分数据兼容的可接受分数区间与权重规则带来的规范性敏感性差异；
3. 采用控制变量法对比有无指定来源的生成回答，准确度量单来源对生成结果的贡献。
### 关键结果数字
基于公开数据集验证，仅调整prompt子语料权重，生成回答激活率可从39.7%变动至70.5%，极端情况下可直接反转两个评估对象的排名。
