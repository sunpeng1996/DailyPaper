---
title: A Cost-Efficient Routing Pipeline for Multilingual Short-Text Classification
  Using Small Language Models
title_zh: 面向多语言短文本分类的低成本小语言模型路由管线
authors:
- Wajdi Ben Saad
- Safa Madiouni
affiliations:
- Carthago Labs
- Université Paris Dauphine-PSL
arxiv_id: '2608.10939'
url: https://arxiv.org/abs/2608.10939
pdf_url: https://arxiv.org/pdf/2608.10939
published: '2026-08-11'
collected: '2026-08-12'
category: LLM
direction: 多语言短文本分类 · 低资源性能优化
tags:
- Multilingual-Classification
- Low-Resource-Language
- Routing-Pipeline
- Small-Language-Model
- Zero-Shot-Classification
one_liner: 提出按语言资源分层的分类路由策略，仅对低资源语言转英语后分类，无微调即可大幅提升低资源场景效果
practical_value: '- 多语言电商客服/搜索意图识别场景可直接复用分层路由思路：高/中资源语言走原生多语言分类通路，仅低资源语言翻译为英语后分类，在不损伤高资源语言效果的前提下大幅提升低资源表现，同时控制算力成本

  - 中小团队可直接复用无需微调的全自托管管线：仅需预训练轻量化句子编码器即可搭建，无需任务级标注数据做fine-tuning，大幅降低多语言分类模块的落地成本

  - 评估路由策略时避免只看全局指标，可按语言资源分层统计效果+延迟，根据业务优先级灵活选择路由边界：效果优先场景可选择全量翻译，成本优先场景仅处理低资源语言即可'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
多语言短文本分类是内容审核、客服路由、意图识别的核心支撑模块，现有统一推理策略忽略高低资源语言的效果差异，低资源语言表现极差，全量翻译为pivot语言的方案又会大幅拉高算力成本。
### 方法关键点
提出固定分层路由策略，按语言资源丰富度分为高/中/低三层，高/中层直接走原生多语言分类通路，仅低资源语言先翻译为英语再做zero-shot分类；全管线自托管，采用预训练轻量化句子编码器，无需任务特定fine-tuning。
### 关键结果
- 15语言SIB-200主题分类数据集：仅翻译低资源语言的配置下，低资源层Macro-F1从0.4632提升至0.6828，高/中层效果无损失
- 15地区MASSIVE意图分类数据集：同策略将低资源层Macro-F1从0.2143提升至0.4417，全量翻译配置可达到全局最优Macro-F1 0.4647
- 最优路由边界可根据任务特性选择，推荐按分层效果+分层延迟评估路由策略而非单一全局指标
