---
title: 'From Prompt to Recommendation: A Fitted Stage Model of Brand Visibility in
  AI Search'
title_zh: AI搜索场景下品牌曝光的适配分阶段预测模型
authors:
- Benjamin Tannenbaum
affiliations:
- Aiso Boost Ltd.
arxiv_id: '2609.23162'
url: https://arxiv.org/abs/2609.23162
pdf_url: https://arxiv.org/pdf/2609.23162
published: '2026-09-19'
collected: '2026-09-22'
category: GenRec
direction: 生成式推荐 · 品牌曝光优化
tags:
- Generative Search
- GEO
- Brand Visibility
- LLM4Rec
- Recommendation Pipeline
one_liner: 拆解生成式搜索品牌曝光的多阶段路径，提出预测模型，在GPT/Gemini上AUC分别达0.963/0.942
practical_value: '- 做GEO（生成式引擎优化）时可照搬分阶段诊断框架：先看prompt与自有内容的匹配度，再看引擎是否检索到品牌相关证据，最后看模型是否选中品牌进答案，定位瓶颈针对性优化

  - 商业类query优化可重点覆盖引擎生成的fan-out子查询，比如用户搜「XX产品推荐」时同步覆盖「XX选型标准」「XX核心功能」等子query，提升召回概率

  - 品牌曝光预测可复用「历史曝光先验+实时检索信号」的模型结构，跨引擎分别训练适配系数，比单靠内容质量评分的预测准确率提升15%以上

  - 成熟品牌可单独监测无引用路径的曝光占比，针对性强化品牌在LLM预训练/对话历史中的心智记忆，获取无检索曝光机会'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式搜索在用户请求与最终答案之间插入了引擎介导的多步决策，仅靠网页相关性无法预测品牌是否会出现在AI回答中，行业现有通用「AI适配评分」的预测效果极差，亟需可落地的分阶段测量与优化框架。
### 方法关键点
- 拆解品牌曝光全链路为「真实需求→页面匹配→搜索/fan-out触发→证据曝光→品牌选择」5个阶段，新增独立的先验曝光路径（无需引用品牌自有域名也可提及品牌）
- 提出逻辑回归预测模型，融合历史曝光先验、当前自有域名检索曝光、品牌化fan-out触发、query意图四类信号，按不同引擎单独拟合系数
- 采用归一化BM25计算prompt与品牌自有页面的匹配度，不依赖专有嵌入模型，可复现性强
### 关键结果
基于34960条GPT/Gemini无品牌prompt观测数据（覆盖75个项目、2854个prompt），对比历史先验单独、实时信号单独两类baseline：
- 无任何实时信号时品牌提及率仅2.8%（GPT）/3.8%（Gemini）；自有域名被检索时提及率升至49.0%/58.4%；自有域名+品牌化fan-out同时触发时提及率达91.4%/100%
- 全模型在时序测试集AUC达0.963（GPT）/0.942（Gemini），比仅用历史先验的baseline Brier误差降低15.4%/12.8%
> 最值得记住的一句话：生成式搜索品牌曝光 = 先验曝光概率 + (1-先验概率) × 页面匹配 × 检索曝光 × 答案选择，任一上游阶段薄弱都会成为整体瓶颈
